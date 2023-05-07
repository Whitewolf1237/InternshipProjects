from translate import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(text)
    return translation


source_text = str(input("Enter the sentence in english that you want to translate to Frence\n"))
source_lang = 'en'
target_lang = 'fr'

translated_text = translate_text(source_text, source_lang, target_lang)
print(translated_text)
