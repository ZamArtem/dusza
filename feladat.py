#"Vendég neve";"Foglalas,L vagy F";"Fog.kezd";"Fog.veg";"szekek szama";"Asztal azon"

#bármely napon 6:00 és 22:00 között lehet asztalt foglalni


class Asztalok():
    def __init__(self,sor):
        id, db, hely = sor.strip().split(";")
        self.id     = int(id)
        self.db     = int(db)
        self.hely   = hely

class Foglalasok():
    def __init__(self,sor):
        vendeg, f_l, fog_kezd, fog_vege, szek_szam, id = sor.strip().split(";")
        self.vendeg     = vendeg
        self.f_l        = f_l
        self.fog_kezd   = fog_kezd[6:12]
        self.fog_vege   = fog_vege
        self.szek_szam  = int(szek_szam)
        self.id         = id


bemenet = "asztalok1.txt"
bemenetf = "foglalasok1.txt"

with open(bemenet, encoding="UTF-8")as f:
    aszt = [Asztalok(sor) for sor in f]
with open(bemenetf,encoding="UTF-8")as f:

    fog = [Foglalasok(sor) for sor in f]

# bekeres = input("""Írjon be egy számot 1-4 a menupont kiválasztásához.
# •   Foglalás(1)
# •   Foglalás törlése(2)
# •   Statisztika(3)
# •   Kilépés(4)
# """)

# if bekeres == "1":
#     print("Írjon be egy számot 1-5 a menupont kiválasztásához.")
#     nev         = input("•   Vendég neve(1)")
#     fog_kezd    = input("•   Foglalás kezdete (HÓNAP-NAP ÓRA:PERC formátumban)(2)")
#     fog_vege    = input("•   Foglalás vége (ÓRA:PERC formátumban)(3)")
#     szek_szam   = int(input("•   Foglalt székek száma(4)"))
#     id          = input("•   Beltéri vagy kültéri asztalt szeretnének (B = beltéri, K = kültéri)(5)")

fog_kezd = "20:30"
fog_vege = "22:00"


for sor in fog:
    if fog_kezd >= sor.fog_kezd:
        print("szar vagy")
        print(sor.fog_kezd)
    fog_vege = sor.fog_vege
    o,p = fog_vege.split(":")
    p = int(p)
    p += 10
    fog_vege = o + ":" + str(p)
    if fog_vege <= fog_vege:
        print(fog_vege)
        print("\n")