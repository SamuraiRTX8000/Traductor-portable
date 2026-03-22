"""
Punto de entrada del sistema.
Conecta todos los módulos.
"""

import tkinter as tk
from queue import Queue

from core.translator import Translator
from core.history import TranslationHistory
from ui.popup import TranslatorPopup
from input.hotkeys import HotkeyManager


def main():
    print("🟢 Jarvis Translator activo")
    print("Ctrl+Alt+T → Español | Ctrl+Alt+E → Inglés")

    ui_queue = Queue()

    translator = Translator()
    history = TranslationHistory()

    root = tk.Tk()
    popup = TranslatorPopup(root, ui_queue)

    hotkeys = HotkeyManager(translator, history, ui_queue)
    hotkeys.start()

    root.mainloop()


if __name__ == "__main__":
    main()


