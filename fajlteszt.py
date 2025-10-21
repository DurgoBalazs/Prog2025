verseny_adatok=[]
try:
    with open("F1-2024dec.csv", encoding="utf-8") as fajl:
        verseny_adatok=fajl.readlines()
        
except Exception as ex:
    print(f"halihóóó! hiba oka! {ex}")
except FileNotFoundError:
    print(" Hiba a fájl  megnyitsa közben")
print(verseny_adatok)
print("itt a program vége")
"""
1.[] Megszámolás
2.[] Eldöntés 1
  [] Eldöntés 2
3.[] Kiválasztás
4.[] Keresés  
5.[] Sorozatszámitás, összegzés
6.[] Min/max kiválasztás
7.[] Másolás
8.[] Kiválasztás
9.[] Szétválogatás
10.[] Metszett 
11.[] Únió 
12.Rendezés
   [] Egyszerű cserés redezés
   [] Bubórékos
   [] Minimum kiválasztás
"""
# 1. Hány versenyző nem szerzett még pontott?
db=0
for i in range(1,len(verseny_adatok)):
    if(int( verseny_adatok[i].split(',')[1])==0):
        db=db+1
print(f"{db}ennyi versenyző nem szerzett pontott\n")
# 2. Van-e fernando nevü versenyző? 
i = 0
while (i<len(verseny_adatok) and "Fernando" not in verseny_adatok[i]):
    i=i+1
if (i<len(verseny_adatok)):
    print("Van Fernando ")
else:
    print("nincs Fernando")
# 2.B   Mindenki szezett-e már 90 pontott?
"""
i=0
while i<len(verseny_adatok) and int(verseny_adatok[i].split(',')[1])>=90:
    i=i+1
if i==len(verseny_adatok):
    print("van")
else:
    print("nincs")
"""
# 3. Melyik istálló pilotája a Yuki Tsunoda?
i=1
while verseny_adatok[i].split(",")[0]!="Yuki Tsunoda":
    i=i+1
print("Yuki Tsunoda a",verseny_adatok[i].split(",")[2].strip(),"istálobban van")

#Melyik csapatban van Pierre Gasly?
i=1
while i<len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok [i]:
    i=i+1
if i<len(verseny_adatok):
    print("Pierre Gasly", verseny_adatok [i].split(",")[2].strip(),"csapatban van!")
else:
    print("Pierre Gasly nincsen egy csapatban sem ")