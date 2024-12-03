# Nombre: Elena Jaramillo Rosado

'''
    Módulo para pre-procesamiento
'''


# Importar las librerías necesarias

from emoji import demojize
import re
from deep_translator import GoogleTranslator

class Preprocessing():

    def lowercase(self, text):
        return str(text).lower()
    
    def duplicates(self,text):
        return re.sub(r'(.)\1{2,}', r'\1\1', text)
    
    def remove_numbers(self,text):
        return re.sub(r'\d+', '', text)
    
    def replace_abbreviations(self,text):
        abbreviations = [('d','de'), ('[qk]','que'), ('xo','pero'), ('xa', 'para'), ('[xp]q','porque'),('es[qk]', 'es que'),
              ('fvr','favor'),('(xfi|xfa|xf|pf|plis|pls|porfa)', 'por favor'), ('dnd','donde'), ('tb|tmbn|tmb', 'también'),
              ('(tq|tk)', 'te quiero'), ('(tqm|tkm)', 'te quiero mucho'), ('x','por'), ('\+','mas'), ('cn', 'con'), ('xd|lol', 'risa')]
        
        for s,t in abbreviations:
            text = re.sub(r'\b{0}\b'.format(s), t, text)
        
        return text
    def remove_vertical_bars(self,text):
        return text.replace("|", " ")

    def translate_emojis(self,text):
        return demojize(text)
    
    def translate_to_english(self, text):
        try:
            translated_text = GoogleTranslator(source='auto', target='en').translate(text)
            return translated_text
        except Exception as e:
            print(f"Error during translation: {e}")
            return text  # Devuelve el texto original si hay error




    
