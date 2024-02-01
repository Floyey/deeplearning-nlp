import streamlit as st
import pandas as pd

# Title
st.title("Deep Learning NLP")

# sidebar
st.sidebar.title('Language Identification')
st.sidebar.write('	Projet Deep Learning, NLP, votre application devra contenir une page analytique et une page permettant d’utiliser le ou les modèles entraînés')
st.sidebar.link_button('📄 Lien vers le dataset utilisé', 'https://huggingface.co/datasets/papluca/language-identification')

