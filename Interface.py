if __name__ == "__main__":
    import sys,os
    # Regarde si le programme est lancé avec streamlit, et le lance avec ce dernier si ce n'est pas le cas
    if any("streamlit" in arg for arg in sys.argv):
        os.system(f"cd {str(os.path.abspath(__file__))[:-12]} & streamlit run Interface.py")
        quit()

#Importation des librairies internes
from Player import Music
from session_state_init import init
#Importation def librairies externes
import streamlit as st

from Projet_streamlit import recherche

init()

try:
    st.session_state['music'].test()
except:
    st.session_state['music'] = Music()
finally:
    player = st.session_state['music']

st.title("Bienvenue sur le projet SoundCloud!")

with st.sidebar:
    st.subheader("Le lecteur streamlit")
    st.image("Data/music.jpg")
    st.info("Réalisé par Arlind, Sacha et Lysandre")

st.divider()

search_entry = st.text_input("Rechercher sur YouTube : ")
st.session_state["search"] = search_button = st.button("Lancer la recherche")

if st.session_state["search"]:
    bar = st.progress(0,"Recherche de la requête...")
    import time
    #Obtenir les données
    name,author,duration,link = recherche(search_entry)
    bar.progress(20,"Obtention des donnés")
    minute,seconds = duration.split(":")
    minute,seconds = (int(minute),int(seconds))
    seconds += minute*60
    bar.progress(60,"Convertion")
    bar.progress(80,"Convertion")
    st.session_state["name"] = name
    st.session_state["author"] = author
    st.session_state["duration"] = seconds
    time.sleep(1)
    bar.progress(100,"Fini!")

    col1_,col2_,col3_ = st.columns(3)
    col1_.metric("Titre",name)
    col2_.metric("Auteur",author)
    col3_.metric("Durée",duration)

    with st.spinner("Chargement..."):
        play_button = st.button("Ecouter",on_click=player.play,args=(link,))
        st.toast("Succès!",icon="✅")
        time.sleep(1)

@st.dialog("Settings")
def settings():
    st.session_state["volume"] = st.slider("Volume",0,100,st.session_state["volume"])

if player.state == "playing" or player.state == "paused":
    st.divider()
    st.info(f"Lecture : '{st.session_state['name']}' par {st.session_state['author']}")
    col1,col2,col3 = st.columns(3)
    col1.button("⏯️",on_click=player.pause_unpause)
    col2.button("⏹️",on_click=player.stop)
    col3.button("⚙️",on_click=settings)