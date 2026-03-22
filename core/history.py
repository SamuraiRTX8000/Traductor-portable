"""
Módulo encargado del historial de traducciones.
Ahora guarda el historial en un archivo JSON.
"""

import json
import os
from datetime import datetime


class TranslationHistory:
    def __init__(self, filename="history.json"):
        """
        Inicializa el historial.
        Si el archivo existe, lo carga.
        Si no, crea uno nuevo.
        """
        self.filename = filename
        self.records = []

        if os.path.exists(self.filename):
            self._load()
        else:
            self._save()

    def add(self, original, translated, lang):
        """
        Agrega una traducción al historial y la guarda en disco.
        """
        self.records.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "original": original,
            "translated": translated,
            "lang": lang
        })
        self._save()

    def get_all(self):
        """
        Devuelve todo el historial.
        """
        return self.records

    def _save(self):
        """
        Guarda el historial en el archivo JSON.
        """
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.records, f, indent=4, ensure_ascii=False)

    def _load(self):
        """
        Carga el historial desde el archivo JSON.
        """
        with open(self.filename, "r", encoding="utf-8") as f:
            self.records = json.load(f)

