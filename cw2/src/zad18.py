def stworz_raport(*args, **kwargs):
    for id in args:
        nazwa=kwargs.get(f'nazwa_{id}')
        cena=kwargs.get(f'cena_{id}')
        print(f"ID: {id}, Nazwa: {nazwa}, Cena: {cena}")