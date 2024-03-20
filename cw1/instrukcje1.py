def instrukcja1(imiona):
    for count, imie in enumerate(imiona):
        print(count, imie)

imionka=["Bartek", "Szymon", "Wiktor"]
instrukcja1(imionka)

def instrukcja2(liczba):
    if(liczba%2==0 and liczba>=0):
        print("Liczba jest dodatnia i parzysta")
    else:
        print("Liczba nie jest dodatnia lub parzysta")

instrukcja2(6)

def instrukcja3(zero):
    if(zero!=0):
        print("Liczba jest różna od zera")
    else:
        print("Liczba jest równa zero")

instrukcja3(1)

def instrukcja4(owoc):
    if(owoc in ["jabłko", "banan", "pomarańcza"]):
        print("Owoc jest dostępny")
    else:
        print("Kup se batona")

instrukcja4(input())
instrukcja4("truskawka")

i=0
while i<100:
    print("Podaj liczbe: ")
    a=input()
    i=i+int(a)
print(i)

