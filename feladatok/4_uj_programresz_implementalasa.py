"""
4. feladat - Uj programresz implementalasa (5 pont)
TODO:
Keszits egy termekertekeles-feldolgozo programot JSON bemenettel.
Minden implementalt fuggveny 1 pont.
Feladat:
- Egy JSON fajlbol termekertekeleseket kell beolvasni.
- Minden rekord tartalmazza:
  - termek (str)
  - kategoria (str)
  - ertekelesek (lista, 1-5 kozotti egesz szamok)
Implementaland fuggvenyek:
1. beolvas_ertekelesek(fajlnev)
   - Olvassa be a JSON fajlt, terjen vissza rekordok listajaval.
2. validalt_ertekeles(ertek)
   - Ellenorizze, hogy az ertek 1 es 5 kozotti egesz szam-e.
   - Hibas ertek eseten dobjon ValueError kivetelt.
3. termek_atlag(rekord)
   - Szamolja ki egy rekord ertekeleseinek atlagat.
   - Minden egyes ertekest validaljon a validalt_ertekeles() segitsegevel.
4. kategoriak_atlagai(rekordok)
   - Adja vissza dict-kent, hogy kategorianként mi az atlagok atlaga.
   - Pelda: {"elektronika": 4.17, "konyv": 4.67}
5. mentes_osszefoglalo_json(rekordok, fajlnev)
   - Mentse el JSON-be az osszes rekordhoz:
     - termekek_szama
     - termek_atlagok  (dict: termek neve -> atlaga)
     - kategoriak_atlagai
     - legjobb_termek  (a legnagyobb atlagu termek neve)
"""
import json
def beolvas_ertekelesek(fajlnev):
    # TODO: valositsd meg
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def validalt_ertekeles(ertek):
    # TODO: valositsd meg (dobjon ValueError-t ha nem 1-5 kozotti egesz szam az ertek)
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def termek_atlag(rekord):
    # TODO: valositsd meg, hasznald a validalt_ertekeles()-t
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def kategoriak_atlagai(rekordok):
    # TODO: valositsd meg
    raise NotImplementedError("A fuggveny meg nincs implementalva.")

def mentes_osszefoglalo_json(rekordok, fajlnev):
    # TODO: valositsd meg
    raise NotImplementedError("A fuggveny meg nincs implementalva.")
if __name__ == "__main__":
    minta_rekordok = [
        {"termek": "Laptop A", "kategoria": "elektronika", "ertekelesek": [5, 4, 5]},
        {"termek": "Eger X",   "kategoria": "elektronika", "ertekelesek": [4, 4, 3]},
        {"termek": "Konyv Z",  "kategoria": "konyv",       "ertekelesek": [5, 5, 4]},
        {"termek": "Tablet B", "kategoria": "elektronika", "ertekelesek": [3, 4, 4]},
    ]
    # A TODO-k megoldasa utan ezek hasznalhatok tesztelesre:
    # print("Laptop A atlaga:", termek_atlag(minta_rekordok[0]))
    # print("Kategoriak atlagai:", kategoriak_atlagai(minta_rekordok))
    # mentes_osszefoglalo_json(minta_rekordok, "termek_osszefoglalo.json")
