import datetime
class Hianyzasok(object):
    def __init__(self,elv):
        self.Sor = elv[2]
        self.Vezeteknev = elv[0]
        self.Keresztnev = elv[1]
        self.Igazolt = self.Igazolt_szamitas(elv[2])
        self.Igazolatlan = self.Igazolatlan_szamitas(elv[2])
        self.Hianyzas = self.Igazolatlan+self.Igazolt

    def Igazolatlan_szamitas(self,sor):
        szam=0
        for x in sor:
            if x =='I':
                szam+=1
        return szam

    def Igazolt_szamitas(self,sor):
        szam=0
        for x in sor:
            if x =="X":
                szam+=1
        return szam
#4. feladat: pszeudókódból metódus készítés
def hetnapja(honap:int, nap:int)->str: 
    napnev = ('vasarnap', 'hetfo', 'kedd', 'szerda', 'csutortok','pentek', 'szombat')
    napszam= (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1]+nap) % 7
    return str(napnev[napsorszam])



#1. feladat: Beolvasás
lista = []
Beolvas = open("naplo.txt",encoding="ISO-8859-2")
datumok = []
szotar = {}
datum = datetime.datetime(1,1,1)
for x in Beolvas:
    elv = x.strip().split(" ")
    if elv[0]=="#":
        if datum !=datetime.datetime(1,1,1):
            szotar[datum] = lista
            lista = []
        datum =datetime.datetime.strptime(elv[1]+elv[2], "%m%d")  

    else: lista.append(Hianyzasok(elv))
szotar[datum] = lista
rogzitett = 0


#2. feladat: Rögzített bejegyzések
for x,y in szotar.items():
    for i in y:
        rogzitett+=1
print(f"""2. feladat
A naplóban {rogzitett} bejegyzés van.""")



#3. feladat: Igazolt és igazolatlan
igazolt =0
igazolatlan =0
for x,y in szotar.items():
    for i in y:
        igazolt+=i.Igazolt
        igazolatlan +=i.Igazolatlan
print(f"""3. feladat
Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.""")



#5. feladat: bekérés, és a metódus alkalmazása
print("5.feladat")
honap = int(input("A hónap sorszáma="))
nap = int(input("A nap sorszáma="))
elment = hetnapja(honap,nap)
print(f"Azon a napon {elment} volt")


#6. feladat: bekérés, metódus alkalmazása, hiányzások kikeresése
print("6.feladat")
nap_neve = input("A nap neve=")
ora_sorszama = int(input("Az óra sorszáma="))
szamolas =0
for x,y in szotar.items():
    if hetnapja(x.month, x.day)==nap_neve:
        for i in y:
            if i.Sor[ora_sorszama-1]=="X" or i.Sor[ora_sorszama-1]=="I":
                szamolas+=1
tanulok = set()
max =-1000000
tanulo_lista = {}



#7. feladat: Maxkeresés halmazzal
for x,y in szotar.items():
    for i in y:
        tanulok.add(f"{i.Vezeteknev} {i.Keresztnev}")
for z in tanulok:
    hiany =0
    for x,y in szotar.items():
        for i in y:
            if f"{i.Vezeteknev} {i.Keresztnev}" == z:
                hiany+=i.Hianyzas

        tanulo_lista[z] = hiany
for x,y in tanulo_lista.items():
    if y>max: max=y
print(f"Ekkor összesen {szamolas} óra hiányzás történt.")
print("""7. feladat
A legtöbbet hiányzó tanulók: """, end ="")
[print(f"{x}", end =" ") for x,y in tanulo_lista.items() if y==max]
print()