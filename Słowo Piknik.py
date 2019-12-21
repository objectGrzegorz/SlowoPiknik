file = open("slowa.txt","r",encoding="utf-8")
lista_wszystkich_slow=file.read()
zbior_wszystkich_slow=set(lista_wszystkich_slow.split())
lista_liter=list(input("Podaj litery w jednym ciągu (bez spacji i przecinków): "))

def szukanie(ile_liter):
    for slowo in zbior_wszystkich_slow:
        kopia_listy_liter=lista_liter[:]
        if len(slowo)== ile_liter:
            litery_w_slowie=[]
            for litera in slowo:
                if litera not in kopia_listy_liter:
                    break
                litery_w_slowie.append(litera)
                kopia_listy_liter.remove(litera)
            if len(litery_w_slowie)==ile_liter:
                print(slowo)

pytanie="T"
while pytanie.upper()=="T":
    ile_liter = int(input("Ilu literowego słowa szukasz?" + "\n"))
    szukanie(ile_liter)
    pytanie=input("Jeśli chcesz szukać słowa, wpisz 'T':"+"\n")
