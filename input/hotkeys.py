"""
Gestión de hotkeys.
No conoce UI ni Tkinter.
"""

import keyboard
import pyperclip
import time
import threading


class HotkeyManager:
    def __init__(self, translator, history, ui_queue):
        """
        Inicializa el sistema de hotkeys.

        :param translator: Instancia de Translator
        :param history: Instancia de TranslationHistory
        :param ui_queue: Cola de comunicación con la UI
        """
        self.translator = translator
        self.history = history
        self.queue = ui_queue

    def start(self):
        """
        Registra las combinaciones de teclas.
        """
        keyboard.add_hotkey(
            "ctrl+alt+t",
            lambda: self._run_translation("es")
        )
        keyboard.add_hotkey(
            "ctrl+alt+e",
            lambda: self._run_translation("en")
        )

    def _run_translation(self, target_lang):
        """
        Ejecuta la traducción en un hilo separado.
        """
        threading.Thread(
            target=self._translate,
            args=(target_lang,),
            daemon=True
        ).start()

    def _translate(self, target_lang):
        """
        Lógica completa de copiar, traducir y enviar a la UI.
        """
        keyboard.press_and_release("ctrl+c")
        time.sleep(0.2)

        text = pyperclip.paste().strip()
        if not text:
            return

        translated = self.translator.translate(text, target_lang)

        self.history.add(text, translated, target_lang)
        self.queue.put((text, translated, target_lang))
