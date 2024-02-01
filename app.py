from functions import *
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="NLP Language", page_icon="🧊", layout="wide")

# Title
st.title("Deep Learning NLP")

# sidebar
st.sidebar.title('Language Identification')
st.sidebar.write('Projet Deep Learning, NLP, votre application devra contenir une page analytique et une page permettant d’utiliser le ou les modèles entraînés')
st.sidebar.link_button('📄 Lien vers le dataset utilisé', 'https://huggingface.co/datasets/papluca/language-identification')

# Input
sentence_identification = st.text_input("Your sentence")

if sentence_identification != "":
    st.write("Your sentence is in: ", '**'+model_prediction(sentence_identification)+'**')
   

if st.checkbox("Do you want to know the translated sentence?"):
    json_file = open('lang_code.json')
    language = json.load(json_file)
    language_selected = st.selectbox("Choose the output language", language.keys())
    
    if sentence_identification != "" and language_selected != "":
        st.write("You want to know what does mean: ", '**'+sentence_identification+'**' , " in",'**'+language_selected+'**')

        if st.button('Translate'):
            translated_sentence = translate(sentence_identification, language[language_selected])
            st.write(translated_sentence)
    else:
        st.write("")
