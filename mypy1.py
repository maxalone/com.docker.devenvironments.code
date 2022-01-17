# scopo didattico per home school

def miafunzione(nome):
    if nome=="max":
        print("bentornato " + nome)
        x=0
        while x<len(nome):
            if x==len(nome)-1:
                print(nome[x], end="")
                print(" ")
                break
            else:   
                print(nome[x]+"-", end="")
                x+=1
        
    else:
        print("piacere di conoscerti " + nome)

print ("---- py from idle native windows -------")

nomee = input("il tuo nome? ")

miafunzione(nomee)
