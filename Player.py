from turtle import st
from pandas import get_dummies
import pygame,threading
import os
import streamlit

class Music:
    def __init__(self):
        # Initialisation du lecteur
        self.mixer = pygame.mixer
        self.mixer.init()

        # Création du fichier temporaire
        self.temp_file = None

        # Etat du lecteur
        self.state = "stopped"

        # Chemin du fichier précedent pour pouvoir le supprimer après
        self.previous_file = None

        # File d'attente
        self.music_queue = []

        # Thread pour le lecteur
        self.player_thread = None

        #Verrou pour gérer les variables sécurisée
        self.lock = threading.Lock()

    def test(self):
        return True

    def del_previous_file(self):
        if self.previous_file is not None:
            os.remove(self.previous_file)

    def play(self, url):
        def play_music():
            from Projet_streamlit import telecharger

            # Récupération et chargement de la musique à partir du lien
            file = telecharger(url)
            self.mixer.music.load("Data/music.mp3")
            print("Lancement de la musique")
            self.previous_file = file

            # Lancement de la musique
            self.mixer.music.play()

        # On joue play_music() dans un thread pour ne pas bloquer l'interface
        with self.lock:
            self.state = "playing"
        self.player_thread = threading.Thread(target=play_music)
        self.player_thread.start()

    def pause_unpause(self):
        # Pause ou reprise de la musique selon l'état du lecteur
        with self.lock:
            if self.state == "playing":
                self.mixer.music.pause()
                self.state = "paused"
            elif self.state == "paused":
                self.mixer.music.unpause()
                self.state = "playing"
            else:
                print(self.state)

    def stop(self):
        # Arrêt du lecteur et déchargement
        with self.lock:
            self.state = "stopped"
        self.mixer.music.stop()

