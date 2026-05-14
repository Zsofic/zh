"""
3. feladat - Meglevo program kiegeszitese uj funkcionalitassal (5 pont)
TODO:
Egeszitsd ki a tanfolyamkezelo programot az alabbi 5 metodussal (1 metodus = 1 pont):
1. hallgato_keresese_nev_alapjan(nev)
   - Adja vissza a hallgato objektumat, ha talalhato, kulonben None.
2. atlag_teljesitmeny()
   - Adja vissza az osszes hallgato pontszamanak atlagat (float).
   - Ures lista eseten 0-t adjon vissza.
3. inaktiv_hallgatok()
   - Adja vissza az inaktiv hallgatok neveit listaként.
4. torol_hallgato(nev)
   - Tablitsa el a nevnek megfelelo hallgatot a listabol.
   - Ha nem talalhato, ValueError kivetelt dobj.
5. mentes_csv(fajlnev)
   - Mentse el a hallgatokat CSV fajlba.
   - Fejlec: nev,pontszam,aktiv
   - Minden hallgato adatai egy sorban szerepeljenek.
Kovetelmenyek:
- A meglevo kodot ne ird at feleslegesen.
- Hasznalj listat, ciklust, feltetelt es fajlkezelest.
"""
import csv
class Hallgato:
    def __init__(self, nev, pontszam, aktiv=True):
        self.nev = nev
        self.pontszam = pontszam
        self.aktiv = aktiv
    def __repr__(self):
        return f"Hallgato(nev=''{self.nev}'', pontszam={self.pontszam}, aktiv={self.aktiv})"

class Tanfolyam:
    def __init__(self, nev):
        self.nev = nev
        self.hallgatok = []
    def uj_hallgato(self, hallgato):
        self.hallgatok.append(hallgato)
    def aktiv_hallgatok(self):
        return [h.nev for h in self.hallgatok if h.aktiv]
    def hallgato_keresese_nev_alapjan(self, nev):
        # TODO: valositsd meg
        pass
    def atlag_teljesitmeny(self):
        # TODO: valositsd meg
        pass
    def inaktiv_hallgatok(self):
        # TODO: valositsd meg
        pass
    def torol_hallgato(self, nev):
        # TODO: valositsd meg (ValueError, ha nem talalhato)
        pass
    def mentes_csv(self, fajlnev):
        # TODO: valositsd meg
        pass

if __name__ == "__main__":
    tanfolyam = Tanfolyam("Python alapok")
    tanfolyam.uj_hallgato(Hallgato("Anna", 78, True))
    tanfolyam.uj_hallgato(Hallgato("Bence", 52, False))
    tanfolyam.uj_hallgato(Hallgato("Csaba", 88, True))
    tanfolyam.uj_hallgato(Hallgato("Dora", 71, False))
    print("Aktiv hallgatok:", tanfolyam.aktiv_hallgatok())
    # A TODO-k kitoltese utan ezeknek is mukodniuk kell:
    print("Kereses - Csaba:", tanfolyam.hallgato_keresese_nev_alapjan("Csaba"))
    print("Kereses - Nem letezik:", tanfolyam.hallgato_keresese_nev_alapjan("Xénia"))
    print("Atlag teljesitmeny:", tanfolyam.atlag_teljesitmeny())
    print("Inaktiv hallgatok:", tanfolyam.inaktiv_hallgatok())
    tanfolyam.torol_hallgato("Bence")
    print("Torles utan aktiv:", tanfolyam.aktiv_hallgatok())
    # tanfolyam.mentes_csv("tanfolyam_hallgatok.csv")
