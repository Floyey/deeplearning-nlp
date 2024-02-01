from googletrans import Translator
import pickle

def translate(sentence, orig_language, dest_language):
    translator = Translator()
    translation = translator.translate(sentence, src=orig_language, dest=dest_language)
    return translation.text

def model_prediction(sentence_identification):
    # Récupération des pickle (model, vectoriseur & label)
    model = pickle.load(open("./models/model.pickle", "rb"))
    vectorizer = pickle.load(open("./models/vectorizer.pickle", "rb"))
    le = pickle.load(open("./models/label.pickle",'rb'))

    prediction = model.predict(vectorizer.transform([sentence_identification]))
    return le.inverse_transform(prediction)[0]
