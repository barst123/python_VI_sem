def licznik_funcatr():
    licznik_atr=getattr(licznik_funcatr, 'atr', 0)
    licznik_funcatr.atr=licznik_atr+1
    return licznik_funcatr.atr