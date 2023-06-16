# Translator-App
 To accomplish this, we'll use the translate module in Python, which utilizes machine translation services such as Google Translate. Here's an outline of the steps we'll follow:

Install the translate module by running pip install translate in your terminal or command prompt.

Import the necessary modules:

python
Copy code
from translate import Translator
Create a function to handle the translation process:
python
Copy code
def translate_text(text, source_language, target_language):
    translator = Translator(from_lang=source_language, to_lang=target_language)
    translation = translator.translate(text)
    return translation
Prompt the user for input:
python
Copy code
source_language = input("Enter the source language: ")
target_language = input("Enter the target language: ")
text = input("Enter the text to translate: ")
Call the translate_text function and display the translation:
python
Copy code
translation = translate_text(text, source_language, target_language)
print("Translation:", translation)
Run the program and test it by entering the source language, target language, and the text you want to translate.
Here's an example implementation of the translator app:

python
Copy code
from translate import Translator

def translate_text(text, source_language, target_language):
    translator = Translator(from_lang=source_language, to_lang=target_language)
    translation = translator.translate(text)
    return translation

source_language = input("Enter the source language: ")
target_language = input("Enter the target language: ")
text = input("Enter the text to translate: ")

translation = translate_text(text, source_language, target_language)
print("Translation:", translation)
This simple translator app allows you to enter the source language, target language, and the text you want to translate. It then utilizes the translate module to perform the translation using an AI-powered machine translation service.
