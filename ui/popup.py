"""
Ventana de Tkinter.
Solo se encarga de mostrar información.
"""

import tkinter as tk


class TranslatorPopup:
    def __init__(self, root, ui_queue):
        """
        Inicializa la ventana principal.

        :param root: Instancia Tk
        :param ui_queue: Cola de comunicación con el main thread
        """
        self.root = root
        self.queue = ui_queue

        self.root.title("Jarvis Translator")
        self.root.geometry("620x320")
        self.root.attributes("-topmost", True)

        self.root.protocol("WM_DELETE_WINDOW", self.hide)

        self._build_ui()
        self.hide()
        self._check_queue()

    def _build_ui(self):
        """
        Construye los elementos visuales.
        """
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Original", font=("Arial", 10, "bold")).pack(anchor="w")
        self.original_msg = tk.Message(frame, width=580)
        self.original_msg.pack(anchor="w", pady=5)

        tk.Label(frame, text="Traducción", font=("Arial", 10, "bold")).pack(anchor="w")
        self.translated_msg = tk.Message(frame, width=580)
        self.translated_msg.pack(anchor="w", pady=5)

        tk.Label(frame, text="ESC para cerrar", fg="gray").pack(anchor="e")

        self.root.bind("<Escape>", lambda e: self.hide())

    def show(self, original, translated, lang):
        """
        Muestra la ventana con el contenido actualizado.
        """
        self.root.title(f"Jarvis Translator → {lang.upper()}")
        self.original_msg.config(text=original)
        self.translated_msg.config(text=translated)
        self.root.deiconify()
        self.root.lift()

    def hide(self):
        """
        Oculta la ventana sin destruirla.
        """
        self.root.withdraw()

    def _check_queue(self):
        """
        Revisa la cola y actualiza la UI si hay nuevos eventos.
        """
        while not self.queue.empty():
            original, translated, lang = self.queue.get()
            self.show(original, translated, lang)

        self.root.after(100, self._check_queue)
