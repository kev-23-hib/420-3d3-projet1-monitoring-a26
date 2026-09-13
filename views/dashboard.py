import tkinter as tk
from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.ram_display import Affichageram
from observers.disk_display import Affichagedisk
from observers.logger import LoggerFichier
 
class Dashboard(tk.Tk):
 
    INTERVALLE_MS = 2000
 
    def __init__(self, metriques: MetriquesSysteme):
        super().__init__()
        self.title("Monitoring système")
        self._metriques = metriques
 
        # À compléter :
        self._creer_observateurs()
        self._abonner_observateurs()
        self._rafraichir()
       
 
    def _creer_observateurs(self) -> None:
        self.cpu = AffichageCPU(self)
        self.ram = Affichageram(self)
        self.disk = Affichagedisk(self)
        self.logger = LoggerFichier()

        
 
    def _abonner_observateurs(self) -> None:
        self._metriques.abonner(self.cpu)
        self._metriques.abonner(self.ram)
        self._metriques.abonner(self.disk)
        self._metriques.abonner(self.logger)
 
    def _rafraichir(self) -> None:
        # À compléter :
        self._metriques.actualiser_metriques()
        self.after(self.INTERVALLE_MS, self._rafraichir)