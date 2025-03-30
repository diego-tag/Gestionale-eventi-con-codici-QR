import tkinter as tk

# Esempio di una semplice applicazione con GUI che mostra "Ciao, mondo!" a schermo
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Applicazione")
        self.configura_finestra()
        self.crea_widgets()

    def configura_finestra(self):
        """Imposta la configurazione della finestra (GUI dell'applicazione)"""
        self.root.geometry("300x200")
        self.root.resizable(True, True)  # Permetti il ridimensionamento
        self.root.configure(padx=20, pady=20)

    def crea_widgets(self):
        """Crea e posiziona widget nella finestra."""
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        hello_label = tk.Label(
            main_frame,
            text="Ciao, mondo!",
            font=('Arial', 24, 'bold'),
            wraplength=250
        )
        hello_label.pack(pady=50)

    def avvia(self):
        """Inizializza Tkinter loop."""
        self.root.mainloop()

def main():
    """Crea ed esegui l'applicazione."""
    gui = App()
    gui.avvia()

if __name__ == "__main__":
    main()