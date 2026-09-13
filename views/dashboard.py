import tkinter as tk
from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.ram_display import AffichageRAM
from observers.disk_display import AffichageDisque
from observers.logger import LoggerFichier
 
class Dashboard(tk.Tk):
 
    INTERVALLE_MS = 2000
 
    def __init__(self, metriques: MetriquesSysteme):
        super().__init__()
        self.title("Monitoring système")
        self._metriques = metriques
 
        # À compléter :
        # 1. Créez les observateurs (AffichageCPU, AffichageRAM,
        #    AffichageDisque, LoggerFichier)
        # 2. Abonnez-les tous au sujet
        # 3. Démarrez le rafraîchissement
 
    def _creer_observateurs(self) -> None:

        
 
    def _abonner_observateurs(self) -> None:
        # À compléter
 
    def _rafraichir(self) -> None:
        # À compléter :
        # Appelez actualiser_metriques() sur les métriques
        # Planifiez le prochain appel avec self.after()