from src.liczniki_stanu.licz_a import *
from src.liczniki_stanu.licz_b import *
from src.liczniki_stanu.licz_c import *
from src.liczniki_stanu.licz_d import *
from src.zad15 import *
from src.zad16 import *
from src.zad17 import *
from src.zad17 import *
from src.zad18 import *
from src.zad19 import *
from src.zad23 import *
def run():
    #6
    dane=(2024, 'Python', 3.8)
    rok=dane[0]
    jezyk=dane[1]
    wersja=dane[2]
    print(rok)
    print(jezyk)
    print(wersja)
    #7
    oceny=[4, 3, 5, 2, 5, 4]
    pierwsza, *srodek, ostatnia=oceny
    print(pierwsza)
    print(srodek)
    print(ostatnia)
    #8
    info=('Jan', 'Kowalski', 30, 'Polska', 'programista')
    imie, nazwisko, _, _, zawod=info
    print(imie, nazwisko, zawod)
    #9
    dane=(2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
    rok=dane[0]
    jezyk=dane[1][0]
    wersja=dane[1][1]
    opis=dane[1][2]
    print(rok, jezyk, wersja, opis)
    #10
    a=b=[1, 2, 3]
    b[0]='zmieniono'
    print(a, b)
    #11
    c=a[:]
    c[0]='nowa wartosc'
    print(a, b, c)
    #12
    x=y=10
    y=y+1
    print(x, y)
    #13
    K=[1, 2]
    L=K
    K=K+[3, 4]
    M=[1, 2]
    N=M
    M+=[3, 4]
    print(K, L, M, N)
    #14
    imiona=['Anna', 'Jan', 'Ewa']
    oceny=[5, 4, 3]
    wyniki=zip(imiona, oceny)
    for imie, ocena in wyniki:
        print(imie, ocena)
    #15
    liczby=[1, 2, 3, 4, 5]
    liczby_kwa=map(kwadrat, liczby)
    print(liczby)
    print(list(liczby_kwa))
    #16
    wynik_int=zmien_wartosc(2)
    print(wynik_int)
    wynik_list=zmien_wartosc(['a', 'b'])
    print(wynik_list)
    #17
    #a
    lista_wynikow=[]
    lista_wynikow.append(zamowienie_produktu('woda', cena=3, ilosc=4))
    lista_wynikow.append(zamowienie_produktu('sok', cena=7, ilosc=3))
    lista_wynikow.append(zamowienie_produktu('bułka', ilosc=9, cena=1))
    #b
    for wynik in lista_wynikow:
        print(wynik)
    #d
    laczna_cena=0
    for wynik, cena in lista_wynikow:
        laczna_cena+=cena
    print(laczna_cena)
    #18
    stworz_raport(101, 102, nazwa_101='a', cena_101='23.49', nazwa_102='b', cena_102='23.21')      
    #19
    potega_2=stworz_funkcje_potegujaca(2)
    print(potega_2(3))
    #20
    #a
    licznik_stanu=licznik_nonlocal()
    print(licznik_stanu())
    print(licznik_stanu())
    #b
    print(licznik_global())
    print(licznik_global())
    #c
    licznik=Licznik()
    print(licznik.dodaj())
    print(licznik.dodaj())
    #d
    print(licznik_funcatr())
    print(licznik_funcatr())
    #21
    print(zamowienie_produktu.__annotations__)
    #22
    ksiazka1={'tytul': 'aaaa', 'autor': 'qaz', 'rok_wydania': 2001}
    ksiazka2={'tytul': 'bbbb', 'autor': 'edc', 'rok_wydania': 1999}
    ksiazka3={'tytul': 'cccc', 'autor': 'wsx', 'rok_wydania': 2005}
    ksiazki=[ksiazka1, ksiazka2, ksiazka3]
    #a
    a=sorted(ksiazki, key=lambda k: k['rok_wydania'])
    print(a)
    #b
    b=filter(lambda k: k['rok_wydania']>2000, ksiazki)
    for ksiazka in b:
        print(ksiazka)
    #c
    c=map(lambda k: k['tytul'], ksiazki)
    for ksiazka in c:
        print(ksiazka)
    #23
    for day in week():
        print(day)
    i=0
    for day in week():
        print(day)
        i+=1
        if i>=3:
            break


if __name__=="__main__":
    run()