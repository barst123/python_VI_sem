def zamowienie_produktu(nazwa_produktu:'str', *, cena:'int', ilosc:'int'=1)->str:
    return f'Nazwa produktu: {nazwa_produktu}, łączna cena: {cena*ilosc}, ilość: {ilosc}', cena*ilosc