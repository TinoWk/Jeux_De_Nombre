import random

CashNumber=random.randint(1,100)
tentative=0
response='a'
print("                      UN JEU DE RECHERCHE D'UN NOMBRE CACHE GENERE PAR L'ORDINATEUR\n")
while response=='a':
    typingNumber=int(input(" Devinez le nombre secret : "))
    if(CashNumber==typingNumber):
        print(" Bravoooo ! Vous avez touvé le nombre caché, ce fut exactement :",CashNumber)
        print(" Vous aviez eu ",tentative +1," tentatives :) ")
        response='v'
    else:
        if(typingNumber>CashNumber):
            print(" le nombre entré est trop grand !")
        if(typingNumber<CashNumber):
            print(" Le nombre entré est trop petit !")
        tentative +=1
