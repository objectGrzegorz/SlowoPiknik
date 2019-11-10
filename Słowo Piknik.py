import random,copy

#Tworzenie listy liter
def listaliter():
    litery=[]
    lit=input("Podaj litery"+"\n")
    while lit!="":
        litery.append(lit)
        lit = input("Podaj litery"+"\n")
    return litery

#Funkcja tworzenia jednego słowa
def losuj(litery2,ileliter):
    slowo=""
    for i in range(ileliter):
        litera = random.choice(litery2)
        slowo += litera
        litery2.remove(litera)
    return slowo

#Pętla programu
czyszukac=input("Jeśli chcesz szukać wyrazu wpisz 't'")
litery=listaliter()

while czyszukac == "t".lower():
    listaslow = []
    ileliter=int(input("Ilu literowego słowa szukasz?"+"\n"))
    litery2=copy.copy(litery)
    flaga=True
    licznik=0
    while flaga:
        wyraz=losuj(litery2, ileliter)
        litery2 = copy.copy(litery)
        if wyraz not in listaslow:
            listaslow.append(wyraz)
        else:
            licznik+=1
        if licznik==500:
            flaga=False
    with open("slowa.txt","r",encoding="utf-8") as plik:
        for i in plik:
            linia=plik.readline().strip()
            if linia in listaslow:
                print(linia)

    czyszukac = input("Jeśli chcesz szukać wyrazu kliknij 't'")




