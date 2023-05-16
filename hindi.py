from googletrans import Translator

def translate_english_to_hindi(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

# Example usage
english_text = str(input("Enter the sentence in english that you want to translate to Hindi\n"))
hindi_text = translate_english_to_hindi(english_text)
print(hindi_text)