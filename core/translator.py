"""
Módulo encargado exclusivamente de la traducción.
No conoce UI ni hotkeys.
"""

from deep_translator import GoogleTranslator


class Translator:
    def __init__(self):
        """
        Inicializa el traductor.
        No necesita configuración porque usamos detección automática.
        """
        pass

    def translate(self, text, target_lang):
        """
        Traduce un texto al idioma objetivo.

        :param text: Texto original
        :param target_lang: Idioma destino ('es' o 'en')
        :return: Texto traducido
        """
        return GoogleTranslator(
            source="auto",
            target=target_lang
        ).translate(text)
