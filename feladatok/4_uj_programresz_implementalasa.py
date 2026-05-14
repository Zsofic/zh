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
    with open(fajlnev, "r", encoding="utf-8") as f:
        adatok = json.load(f)
    return adatok


def validalt_ertekeles(ertek):
    if not isinstance(ertek, int):
        raise ValueError("Egész számnak kell lennie.")

    if ertek < 1 or ertek > 5:
        raise ValueError("1 és 5 között kell lennie.")
    return True


def termek_atlag(rekord):
    ertekelesek = rekord["ertekelesek"]
    osszeg = 0
    db = 0
    for ertek in ertekelesek:
        validalt_ertekeles(ertek)
        osszeg += ertek
        db += 1
    if db == 0:
        return 0
    return osszeg / db


def kategoriak_atlagai(rekordok):
    kategoriak = {}
    for r in rekordok:
        kat = r["kategoria"]
        atlag = termek_atlag(r)

        if kat not in kategoriak:
            kategoriak[kat] = []
        kategoriak[kat].append(atlag)

    return {
        kat: sum(lista) / len(lista)
        for kat, lista in kategoriak.items()
    }

def mentes_osszefoglalo_json(rekordok, fajlnev):
    termek_atlagok = {}
    kategoriak = {}

    for r in rekordok:
        termek_atlagok[r["termek"]] = termek_atlag(r)
        kat = r["kategoria"]
        if kat not in kategoriak:
            kategoriak[kat] = []
        kategoriak[kat].append(termek_atlag(r))

    kategoriak_atlag = {
        k: sum(v) / len(v) for k, v in kategoriak.items()
    }
    legjobb = max(termek_atlagok, key=termek_atlagok.get)

    osszegzes = {
        "termekek_szama": len(rekordok),
        "termek_atlagok": termek_atlagok,
        "kategoriak_atlagai": kategoriak_atlag,
        "legjobb_termek": legjobb
    }
    with open(fajlnev, "w", encoding="utf-8") as f:
        json.dump(osszegzes, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    minta_rekordok = [
        {"termek": "Laptop A", "kategoria": "elektronika", "ertekelesek": [5, 4, 5]},
        {"termek": "Eger X",   "kategoria": "elektronika", "ertekelesek": [4, 4, 3]},
        {"termek": "Konyv Z",  "kategoria": "konyv",       "ertekelesek": [5, 5, 4]},
        {"termek": "Tablet B", "kategoria": "elektronika", "ertekelesek": [3, 4, 4]},
    ]
    # A TODO-k megoldasa utan ezek hasznalhatok tesztelesre:
    print("Laptop A atlaga:", termek_atlag(minta_rekordok[0]))
    print("Kategoriak atlagai:", kategoriak_atlagai(minta_rekordok))
    mentes_osszefoglalo_json(minta_rekordok, "termek_osszefoglalo.json")
