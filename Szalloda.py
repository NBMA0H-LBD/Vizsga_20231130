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

    def informacio(self):
        return f"Foglalás {self.szoba.informacio()} szobára a {self.datum} dátumra. Ár: {self.ar}"

    def feltoltes_uj(szalloda):
        szobak_szama = 3
        foglalasok_szama = 5

        for i in range(1, szobak_szama + 1):
            szalloda.add_szoba(EgyagyasSzoba(szobaszam=i))
            szalloda.add_szoba(KetagyasSzoba(szobaszam=szobak_szama + i))

        for i in range(foglalasok_szama):
                szalloda.foglalas(szobaszam=i % szobak_szama + 1,
                                  datum=(datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'))

    if __name__ == "__main":
        hotel == Hotel(nev="Lábadi Zoltán")
        feltoltes_uj(hotel)

        while True:
            print("\nVálassz műveletet:")
            print("1. Foglalás")
            print("2. Lemondás")
            print("3. Foglalások listázása")
            print("4. Kilépés")

            valasztas = input("Válassz (1-4): ")

            if valasztas == "1":
                szobaszam = input("Add meg a szoba számát: ")
                datum = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")

                try:
                    datetime_obj = datetime.strptime(datum, '%Y-%m-%d')
                    if datetime_obj < datetime.now():
                        print("Érvénytelen dátum, csak jövőbeni foglalás lehetséges.")
                        continue

                    print(hotel.foglalas(szobaszam, datum))
                except ValueError:
                    print("Hibás dátumformátum. Kérlek használd az YYYY-MM-DD formátumot.")

            elif valasztas == "2":
                szobaszam = input("Add meg a szoba számát: ")
                datum = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")

                try:
                    datetime_obj = datetime.strptime(datum, '%Y-%m-%d')
                    if datetime_obj < datetime.now():
                        print("Érvénytelen dátum, csak jövőbeni lemondás lehetséges.")
                        continue

                    print(hotel.lemondas(szobaszam, datum))
                except ValueError:
                    print("Hibás dátumformátum. Kérlek használd az YYYY-MM-DD formátumot.")

            elif valasztas == "3":
                hotel.listaz_foglalasok()

            elif valasztas == "4":
                break

            else:
                print("Érvénytelen választás. Kérlek válassz 1-4 között.")




