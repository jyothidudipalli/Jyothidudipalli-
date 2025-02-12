from googletrans import Translator

# Initialize the Translator object
translator = Translator()

# Function to detect the language of input text and translate to other languages
def multi_language_translator(text, target_languages):
    try:
        # Detect the source language
        detected_lang = translator.detect(text).lang
        print(f"Detected language: {detected_lang}")
        
        translations = {}
        
        # Translate the text into multiple target languages
        for lang in target_languages:
            translated = translator.translate(text, src=detected_lang, dest=lang)
            translations[lang] = translated.text
        
        return translations
    
    except Exception as e:
        return f"Error occurred: {e}"

# Example usage
input_text = "Hello, how are you?"
# List of target languages (you can use language codes like 'fr', 'de', 'es', 'ja', 'zh-cn', etc.)
languages = ['es', 'fr', 'de', 'ja', 'zh-cn']

translated_texts = multi_language_translator(input_text, languages)

# Print translated texts
for lang, translation in translated_texts.items():
    print(f"{lang}: {translation}")
