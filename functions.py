from googletrans import Translator

def translate(sentence, language):
    translator = Translator()
    translation = translator.translate(sentence, dest=language)
    return translation.text