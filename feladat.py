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
        vendeg, f_l, fog_kezd, fog_vege, szek_szam, *asztalid = sor.strip().split(";")
        self.vendeg     = vendeg
        self.f_l        = f_l
        self.turmix     = fog_kezd
        self.datum      = fog_kezd[0:5]
        self.fog_kezd   = fog_kezd[6:12]
        self.fog_vege   = fog_vege
        self.szek_szam  = int(szek_szam)
        self.asztalid       = asztalid


bemenet = "asztalok3.txt"
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
# bekeres = "1"
# foglalas = True
# szamlalo = 0
# while foglalas:
#     if bekeres == "1":
#         print("Írjon be egy számot 1-5 a menupont kiválasztásához.")
#         nev         = input("•   Vendég neve ")
#         fog_kezd    = input("•   Foglalás kezdete (HÓNAP-NAP ÓRA:PERC formátumban) ")
#         fog_vege    = input("•   Foglalás vége (ÓRA:PERC formátumban) ")
#         szek_szam   = int(input("•   Foglalt székek száma "))
#         belter          = input("•   Beltéri vagy kültéri asztalt szeretnének (B = beltéri, K = kültéri) ")
fog_kezd    = "12-01 06:00"
fog_vege    = "09:00"
szek_szam   = 7
belter      = "K"


if fog_kezd[0:5] > fog_vege:
    print("a kezdet nagyobb mint a vege")
if fog_kezd[0:5] < "06:00":
    print("06:00-tol van nyitva")
if fog_vege > "22:00":
    print("22:00-tol van zarva")
else:
    foglalas = False

fog_kezd = "12-00 08:00"
fog_vege = "20:20"
#A;F;12-02 20:30;22:00;4;1
for sor in fog:
    vege = sor.fog_vege
    o,p = vege.split(":")
    p = int(p)
    p += 10
    vege = o + ":" + str(p)
    if fog_vege < sor.fog_kezd or fog_kezd > vege and fog_kezd and fog_kezd[0:5] == sor.datum:
        print("pozitiv")
        print(fog_kezd,fog_vege)
        print(sor.fog_kezd,vege)
    else:
        print("idopont foglalt")

    