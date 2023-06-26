#!/usr/bin/env python
# coding: utf-8

# In[5]:


from googletrans import Translator

def translate_text(text, source_language, target_language):
    translator = Translator()
    translation = translator.translate(text, src=source_language, dest=target_language)
    return translation.text

source_language = input("Enter the source language: ")
target_language = input("Enter the target language: ")
text = input("Enter the text to translate: ")

translation = translate_text(text, source_language, target_language)
print("Translation:", translation)

