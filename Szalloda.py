# Szálloda

from datetime import datetime, timedelta

class Szoba:
    def __int__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.elerheto_datumok = set()

    def elerheto(self,datum):
        return datum in self.elerheto_datumok

    def foglalas(self, datum):
        if self.elerheto(datum):
            self.elerheto_datumok.remove(datum)
            return self.ar
        else:
            return None

    def lemondas(self,datum):
        self.elerheto_datumok.add(datum)

    def informacio(self):
        return  f" {self.szobaszam}, {self.ar}"


class egyagyas_szoba(Szoba):
    def __int__(self,szobaszam):
        super().__int__(szobaszam, ar=50000)

class ketagyas_szoba(Szoba):
    def __int__(self,szobaszam):
        super().__int__(szobaszam, ar=100000)


class Hotel:
    def __int__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self,szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):

        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                ar == szoba.foglal(datum)
                if ar is not None:
                    self.foglalasok.append(Foglalas(szoba, datum, ar))
                    return F"{szobaszam} foglalás készült, {datum} napon"
                else:
                    return F" {szobaszam} nem elérhető"

            return F"{szobaszam} nem található"
    def lemondas(self, szobaszam,datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                foglalas.szoba.lemondas(datum)
                self.foglalasok.remove(foglalas)
                return F" {szobaszam} foglalás lemondva"

    def lemondas_listazas(self,szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam ==szobaszam and foglalas.datum == datum:
                foglalas.szoba.lemondas(datum)
                self.foglalasok.remove(foglalas)

    def foglalas_listazas(self):
        for foglalas in self.foglalas():
            print(foglalas.informacio())


class Foglalas:
    def __init__(self, szoba, datum, ar):
        self.szoba = szoba
        self.datum = datum
        self.ar = ar

    def info(self):
        return f"Foglalás {self.szoba.info()} szobára a {self.datum} dátumra. Ár: {self.ar}"

