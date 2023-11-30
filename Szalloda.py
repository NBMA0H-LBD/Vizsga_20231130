# 1. Osztályok Létrehozása


from abc import ABC, abstractmethod

class Szoba(ABC):
    def __int__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    def info(self):
        pass

class egyagyas_szoba(Szoba):
    def info(self):
        return f" Egyágyas szoba {self.szobaszam}, ár : {self.ar}"

class Szalloda:
    def __int__(self, nev):
        self.nev = nev
        self.szobak =[]

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def szobak_listaja(self):
        for szoba in self.szobak:
            print(szoba.info())

class Foglalas:
    def __int__(self,szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def info(self):
        return f"Foglalás az {self.szoba.info()} szobára a {self.datum} napon"

# 2. Foglalások kezelése

class Hotel:
    def __int__(self,nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self,szoba):
        self.szobak.append(szoba)

    def foglalas(self,szobaszam,datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba,datum)
                self.foglalasok.append(foglalas)
                return f"A {szobaszam} szobára lefoglalás történt {datum} napon, fizetendő : {szoba.ar}"



