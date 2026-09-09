import tkinter as tk
from observers.observer import Observateur

class AffichageCPU(Observateur):

    def __init__(self, parent: tk.Frame):
        # À compléter: Créez un LabelFrame "CPU", un Label pour le pourcentage et un Canvas pour la barre de progression
        self.frame_cpu = tk.LabelFrame(parent, text="CPU", padx=10, pady=10)
        self.frame_cpu.pack(fill=tk.X, padx=10, pady=5)
        self.label_cpu = tk.Label(self.frame_cpu, text="0%", font=("Arial", 24, "bold"))
        self.label_cpu.pack()
        self.canvas_cpu = tk.Canvas(self.frame_cpu, width=300, height=20, bg="white")
        self.canvas_cpu.pack()

        self.alertes_80 = tk.Label(self.frame_cpu, text="⚠️ Alerte: CPU > 80%", font=("Arial", 12), fg="red")
        self.alertes_80.pack()

    def actualiser(self, sujet) -> None:
        # À compléter: Récupérez la valeur CPU depuis sujet.get_donnees()
        donnees = sujet.get_donnees()
        cpu = donnees.get("cpu", 0)


        # À compléter: Mettez à jour le label et la barre
        self.label_cpu.config(text=f"{cpu:.1f}%")
        self._dessiner_barre(cpu)





    def _dessiner_barre(self, valeur: float) -> None:
        # À compléter: 
        self.label_cpu.config(text=f"{valeur:.1f}%")
        self.canvas_cpu.delete("all")
        largeur_cpu = int(300 * valeur / 100)
        if valeur < 50:
            couleur_cpu = "green"
        elif valeur < 80:
            couleur_cpu = "orange"
        else:
            couleur_cpu = "red"

       


        self.canvas_cpu.create_rectangle(0, 0, largeur_cpu, 20, fill=couleur_cpu, outline="")
        
        # Effacez le canvas

        # Calculez la largeur (300 * valeur / 100)

        # Choisissez la couleur : vert < 50%, orange < 80%, rouge sinon
        # Dessinez le rectangle