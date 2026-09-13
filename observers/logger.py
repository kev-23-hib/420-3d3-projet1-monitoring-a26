from observers.observer import Observateur
from datetime import datetime


class LoggerFichier(Observateur):

    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()

        cpu = donnees["cpu"]
        ram = donnees["ram"]
        disque = donnees["disque"]

        maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("monitoring.log", "a", encoding="utf-8") as fichier:
            fichier.write(
                f"{maintenant} | CPU: {cpu}% | RAM: {ram}% | Disque: {disque}%\n"
            )