from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class InitPeli:
    def init_peli(self, vastaus):
        arvo = True
        if vastaus.endswith("a"):
                    kaksinpeli = KPSPelaajaVsPelaaja()
                    kaksinpeli.pelaa()

        elif vastaus.endswith("b"):
                    yksinpeli = KPSTekoaly()
                    yksinpeli.pelaa()
                    
        elif vastaus.endswith("c"):
                    haastava_yksinpeli = KPSParempiTekoaly()
                    haastava_yksinpeli.pelaa()
                
        else:
            arvo = False
            return arvo
