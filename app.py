import streamlit as st
import pandas as pd

st.set_page_config(page_title="NLP Language", page_icon="🧊", layout="wide")

# Title
st.title("Deep Learning NLP")

# sidebar
st.sidebar.title('Language Identification')
st.sidebar.write('	Projet Deep Learning, NLP, votre application devra contenir une page analytique et une page permettant d’utiliser le ou les modèles entraînés')
st.sidebar.link_button('📄 Lien vers le dataset utilisé', 'https://huggingface.co/datasets/papluca/language-identification')


if st.checkbox("Do you want to know the translated sentence?"):
    language = {'Français': 'fr', 'English': 'en', 'Deush': 'de', 'Español': 'es'}
    language_selected = st.selectbox("Choisissez une thématique", language.keys())

# Input
sentence_identification = st.text_input("Your sentence")

if sentence_identification != "":
    st.write("You want to know what does mean: ", sentence_identification , " in", language_selected)

if st.button('Translate'):
    # Prediction
    st.write("Prediction: ", "French")