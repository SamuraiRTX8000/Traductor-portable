# usage_lookup/lookup_service.py

import requests
from usage_lookup.base import UsageLookupBase


class FreeDictionaryLookup(UsageLookupBase):
    """
    Implementación de UsageLookup usando Free Dictionary API.
    """

    API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def lookup(self, text: str) -> dict:
        """
        Consulta el uso de una palabra en inglés y
        devuelve la información estructurada.
        """

        response = requests.get(self.API_URL + text.lower())

        if response.status_code != 200:
            return self._error_result(text)

        data = response.json()
        return self._parse_response(text, data)

    # -----------------------------
    # Métodos internos (privados)
    # -----------------------------

    def _parse_response(self, query: str, data: list) -> dict:
        """
        Convierte la respuesta cruda del API
        en una estructura limpia para el sistema.
        """

        entries = []

        for meaning in data[0].get("meanings", []):
            part_of_speech = meaning.get("partOfSpeech", "general")

            for definition in meaning.get("definitions", []):
                entry = {
                    "meaning": definition.get("definition", ""),
                    "explanation": self._human_explanation(definition.get("definition", "")),
                    "context": self._map_context(part_of_speech),
                    "examples": []
                }

                example = definition.get("example")
                if example:
                    entry["examples"].append(example)

                entries.append(entry)

        return {
            "query": query,
            "language": "en",
            "entries": entries
        }

    def _map_context(self, part_of_speech: str) -> str:
        """
        Simplifica el contexto gramatical a algo humano.
        """

        mapping = {
            "noun": "uso general",
            "verb": "acción o estado",
            "adjective": "descripción",
            "adverb": "modo o intensidad"
        }

        return mapping.get(part_of_speech, "uso general")

    def _human_explanation(self, definition: str) -> str:
        """
        Explicación sencilla (por ahora básica).
        Aquí luego entra IA sin romper nada.
        """

        return f"Se usa para expresar: {definition}"

    def _error_result(self, query: str) -> dict:
        """
        Resultado en caso de error o palabra no encontrada.
        """

        return {
            "query": query,
            "language": "en",
            "entries": [],
            "error": "No se encontró información para esta palabra."
        }
