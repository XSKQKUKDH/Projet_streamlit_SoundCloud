if __name__ == "__main__":
    import sys,os
    # Regarde si le programme est lancé avec streamlit, et le lance avec ce dernier si ce n'est pas le cas
    if any("streamlit" in arg for arg in sys.argv):
        os.system(f"cd {str(os.path.abspath(__file__))[:-12]} & streamlit run Interface.py")
        quit()

#Importation des librairies internes
from typing import final
from Player import Music
from session_state_init import init
#Importation def librairies externes
import streamlit as st

init()

try:
    st.session_state['music'].test()
except:
    st.session_state['music'] = Music()
finally:
    player = st.session_state['music']

st.title("Bienvenue sur le projet SoundCloud!")
st.subheader("Arlind, Lysandre, Sacha")

st.divider()

search_entry = st.text_input("Rechercher sur SoundCloud : ")
st.session_state["search"] = search_button = st.button("Lancer la recherche")

if st.session_state["search"]:
    import time
    #Obtenir les données
    name = "Blame"
    author = "Calvin Harris"
    duration = "3:32"
    url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    col1_,col2_,col3_ = st.columns(3)
    col1_.metric("Titre",name)
    col2_.metric("Auteur",author)
    col3_.metric("Durée",duration)

    play_button = st.button("Ecouter",on_click=player.play,args=(url,))

if player.state == "playing" or "paused":
    col1,col2,col3,col4 = st.columns(4)
    col1.button("⏯️",on_click=player.pause_unpause)
    col2.button("⏹️",on_click=player.stop)