import tkinter as tk
from observers.observer import Observateur

class Affichagedisk(Observateur):

    def __init__(self, parent: tk.Frame):
        self.frame_disque = tk.LabelFrame(parent, text="Disque", padx=10, pady=10)
        self.frame_disque.pack(fill=tk.X, padx=10, pady=5)
        self.label_disque = tk.Label(self.frame_disque, text="0%", font=("Arial", 24, "bold"))
        self.label_disque.pack()
        self.canvas_disque = tk.Canvas(self.frame_disque, width=300, height=20, bg="white")
        self.canvas_disque.pack()
        

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        disque = donnees.get("disque", 0)
        self.label_cpu.config(text=f"{disque:.1f}%")
        self._dessiner_barre(disque)

    def _dessiner_barre(self, valeur: float) -> None:
        self.label_disque.config(text=f"{valeur:.1f}%")
        self.canvas_disque.delete("all")
        largeur_disque = int(300 * valeur / 100)
        if valeur < 50:
            couleur_disque = "green"
        elif valeur < 80:
                couleur_disque = "orange"
        else:
            couleur_disque = "red"
        self.canvas_disque.create_rectangle(0, 0, largeur_disque, 20, fill=couleur_disque, outline="")
        