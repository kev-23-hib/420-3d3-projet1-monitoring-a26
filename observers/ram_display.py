import tkinter as tk
from observers.observer import Observateur

class Affichageram(Observateur):

    def __init__(self, parent: tk.Frame):
        self.frame_ram = tk.LabelFrame(parent, text="Ram", padx=10, pady=10)
        self.frame_ram.pack(fill=tk.X, padx=10, pady=5)
        self.label_ram = tk.Label(self.frame_ram, text="0%", font=("Arial", 24, "bold"))
        self.label_ram.pack()
        self.canvas_ram = tk.Canvas(self.frame_ram, width=300, height=20, bg="white")
        self.canvas_ram.pack()
        

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        ram = donnees.get("ram", 0)
        self.label_cpu.config(text=f"{ram:.1f}%")
        self._dessiner_barre(ram)

    def _dessiner_barre(self, valeur: float) -> None:
        self.label_ram.config(text=f"{valeur:.1f}%")
        self.canvas_ram.delete("all")
        largeur_ram = int(300 * valeur / 100)
        if valeur < 50:
            couleur_ram = "green"
        elif valeur < 80:
                couleur_ram = "orange"
        else:
            couleur_ram = "red"
        self.canvas_ram.create_rectangle(0, 0, largeur_ram, 20, fill=couleur_ram, outline="")
        