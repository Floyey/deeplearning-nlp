from googletrans import Translator
import pickle

def translate(sentence, language):
    translator = Translator()
    translation = translator.translate(sentence, dest=language)
    return translation.text

def model_prediction(sentence_identification):
    model_path = "./models/model.pickle"
    vectorizer_path = "./models/vectorizer.pickle"
    le_path = "./models/label.pickle"
    vectorizer = pickle.load(open(vectorizer_path,'rb'))
    model = pickle.load(open(model_path,'rb'))
    le = pickle.load(open(le_path,'rb'))
    return le.inverse_transform(model.predict(vectorizer.transform([sentence_identification])))[0]