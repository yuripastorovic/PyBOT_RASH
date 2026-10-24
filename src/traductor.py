from googletrans import Translator

translator = Translator()

def traduccion(texto_original):
    translated = translator.translate(texto_original, src='en', dest='es')
    print(translated)
    return translated.text