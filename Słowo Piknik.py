import random,copy

#Tworzenie listy liter, z których będą tworzone słowa
def lista_liter():
    litery=[]
    lit=input("Podaj litery"+"\n")
    while lit!="":
        litery.append(lit)
        lit = input("Podaj literę albo daj 'enter' aby przejść dalej"+"\n")
    return litery

#Funkcja tworzenia jednego słowa
def losuj(litery_kopia,ile_liter):
    slowo=""
    for i in range(ile_liter):
        litera = random.choice(litery_kopia)
        slowo += litera
        litery_kopia.remove(litera)
    return slowo

#Pętla programu
czy_szukac=input("Jeśli chcesz szukać wyrazu wpisz 't'")
litery=lista_liter()

while czy_szukac.lower() == "t":
    lista_slow = []
    ile_liter=int(input("Ilu literowego słowa szukasz?"+"\n"))
    litery_kopia=copy.copy(litery)
    flaga=True
    licznik=0
    while flaga:
        wyraz=losuj(litery_kopia, ile_liter)
        litery_kopia = copy.copy(litery)
        if wyraz not in lista_slow:
            lista_slow.append(wyraz)
        else:
            licznik+=1
        if len(litery)<=10 and licznik==1000 or len(litery)<=16 and licznik==10000 or len(litery)>16 and licznik==100000:
            flaga=False

    with open("slowa.txt","r",encoding="utf-8") as plik:
        for linia in plik:
            linia=linia.rstrip("\n")
            if linia in lista_slow:
                print(linia)


    czyszukac = input("Jeśli chcesz szukać wyrazu kliknij 't'")




