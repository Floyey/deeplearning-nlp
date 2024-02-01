from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import streamlit as st

st.title("Analitics") 

Y_test = pickle.load(open("./datas/Y_test.pickle", "rb"))
y_pred = pickle.load(open("./datas/y_pred.pickle", "rb"))
le = pickle.load(open("./models/label.pickle",'rb'))
language = pickle.load(open("./datas/langue_counts.pickle", "rb"))

conf_matrix = confusion_matrix(Y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel("Prédictions")
plt.ylabel("Vraies valeurs")
plt.title("Matrice de Confusion")

st.pyplot(plt)

plt.figure(figsize=(10, 6))
sns.barplot(x=language.values, y=language.index)
plt.xlabel("Langue")
plt.ylabel("Nombre de Phrases")
plt.title("Distribution des Langues")
plt.show()
st.pyplot(plt)