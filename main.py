import streamlit as st
from parse_dataframe import *

st.write("""
# MelodyMatch
Utilisation d'un filtrage collaboratif pour recommander des musiques similaires à une autre.
         
__________________________________
""")

song = st.text_input("Veuillez entrer le nom d'une chanson pour obtenir des recommandations")

# Vérifie si une chanson a été entrée
if song:  
    with st.spinner('Recherche en cours...'):
        try:
            five_songs = search_engine(song)
            if five_songs:
                st.success("Recommandations trouvées :")
                # Affiche chaque chanson recommandée
                for artist, song, d in five_songs:
                    st.write(f"{song} - {artist}")
            else:
                st.error("Aucune recommandation trouvée.")
        except Exception as e:
            st.error(f"Une erreur est survenue: {e}")
