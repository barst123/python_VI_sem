#działania matematyczne
wartosc=100
dodawanie=wartosc+123.15
potega=dodawanie**12
tekst=str(potega)
print(tekst)
import math
wartosc_pi=math.pi
import random
losowa=random.randint(1, 5)
print(losowa)
#lancuchy znakow
tekst=f"Wartosc: {tekst}"
print(tekst)
print(len(tekst))
print(tekst[1:4])
print(dir(tekst))
tekst=tekst.upper()
print(tekst)
#tekst[2]="p"
#listy
lista=list(tekst)
print(lista)
lista=lista[0:8]
print(lista)
lista.insert(8, [1, 2, 3, 4, 5])
print(lista)
lista.remove(":")
print(lista)
lista2=[1, 2, 3, "banan", 100]
print(lista2)
lista3=[x**2 for x in lista2 if type(x)==int]
print(lista3)
lista4=[x for x in range(2, 18, 2)]
print(lista4)
#slowniki
ja={}
ja["imie"]="Bartosz"
ja["nazwisko"]="Staron"
ja["wiek"]=22
ja["rodzice"]=[{"imie": "Waldemar", "wiek": 60}, {"imie": "Mariola", "wiek": 59}]
print(ja["rodzice"])
print(ja["rodzice"][0]["imie"])
print(ja.keys())
if "rodzenstwo" in ja:
    print(True)
else:
    print(False)
#krotki
krotka1=(1, 2, "3", 4, 2, 5)
print(len(krotka1))
print(krotka1[0])
#print(dir(krotka1))
print(krotka1.count(2))
#krotka1[0]=2
#zbiory
X=set("kalarepa")
Y=set("lepy")
print(X)
print(Y)
print(X&Y)