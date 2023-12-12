from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.parempi_tekoaly = TekoalyParannettu()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.parempi_tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.parempi_tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto