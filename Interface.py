#Importation
import sys,os

if __name__ == "__main__":
    # Check if 'streamlit' is in the sys.argv
    if any("streamlit" in arg for arg in sys.argv):
        os.system(f"cd {str(os.path.abspath(__file__))[:-12]} & streamlit run Interface.py")

import streamlit

streamlit.title("Bienvenue sur le projet SoundCloud!")
streamlit.subheader("Arlind, Lysandre, Sacha")