import psutil
from models.subject import Sujet

class MetriquesSysteme(Sujet):

    def __init__(self):
        super().__init__() # Permet d'initialiser la liste des observateurs
        self._cpu = None
        self._ram = None
        self._disque = None

    def actualiser_metriques(self) -> None:
        # À compléter: Lire les métriques avec psutil
        self._cpu = psutil.cpu_percent(interval=None)
        self._ram = psutil.virtual_memory().percent
        self._disque = psutil.disk_usage('/').percent

        # À compléter: Appeler notifier()
        self.notifier() 

    def get_donnees(self) -> dict:
        # À compléter : Retourner un dictionnaire avec cpu, ram, disque
        return {
            "cpu": self._cpu,
            "ram": self._ram,
            "disque": self._disque
        }