# usage_lookup/base.py

from abc import ABC, abstractmethod


class UsageLookupBase(ABC):
    """
    Clase base (contrato).
    Cualquier sistema que busque el uso de una palabra
    debe implementar este método.
    """

    @abstractmethod
    def lookup(self, text: str) -> dict:
        """
        Busca el uso de una palabra o expresión.

        :param text: palabra o frase a buscar
        :return: diccionario con definiciones, contexto y ejemplos
        """
        pass
