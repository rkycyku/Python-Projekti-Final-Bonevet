# Librarit
from random import randint,choice,shuffle
## Randint perdoret per te zgjedhur nje numer te qfardoshem
## Choice perdoret per te zgjedhur diqka nga lista
## Shuffle perdeoret per te perzier karakteret
from time import sleep, time
## Sleep perdoret per ta vendosur nje komand ne pritje per aq kohe sa i japim 
from tkinter import *
## Tkinter sherben ne Lojen e Pelcitesit i cili mundeson hapjen e nje dritare te re
from math import sqrt
## SQRT sherben per te marr rrenjen katrore


# Emri i perdoruesit
perdoruesi = input("Pershendetje. Si quheni? ")
sleep(.5)
## Ne rast se perdoruesi e shkruan emrin me shkronja te vogla,
## Ky funksion shkronjen e pare e ben gjithmon te madhe
perdoruesi = perdoruesi.capitalize()
# Ky funksion sherben per te numeruar sa shkronja i posedon emri i perdoruesit
perdoruesilen = len(perdoruesi)

## Menyja nese emri i pedoruesit ka 3 Shkronja
if perdoruesilen == 3:
    # Ky mesazh sherben per te pershendetur perdoruesin
    print("\n///////////////////////////////////////////////")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                  Mini Menu                  /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/               Mirësevini,",perdoruesi,"              /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("///////////////////////////////////////////////")
    sleep(.1)
    print('\nShkruani "Po" per te hapur menun,')
    sleep(.1)
    print('Shkruani "Jo" per te mbyllur programin.')
    sleep(.1)
    # Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
    fillimi_i_menys = input("\nA deshironi te hapni menun? ")
    fillimi_i_menys = fillimi_i_menys.lower()

## Menyja nese emri i pedoruesit ka 4 Shkronja
elif perdoruesilen == 4:
    # Ky mesazh sherben per te pershendetur perdoruesin
    print("\n////////////////////////////////////////////////")
    sleep(.1)
    print("/                                              /")
    sleep(.1)
    print("/                                              /")
    sleep(.1)
    print("/                    Mini Menu                 /")
    sleep(.1)
    print("/                                              /")
    sleep(.1)
    print("/               Mirësevini,",perdoruesi,"              /")
    sleep(.1)
    print("/                                              /")
    sleep(.1)
    print("/                                              /")
    sleep(.1)
    print("////////////////////////////////////////////////")
    sleep(.1)
    print('\nShkruani "Po" per te hapur menun,')
    sleep(.1)
    print('Shkruani "Jo" per te mbyllur programin.')
    sleep(.1)
    # Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
    fillimi_i_menys = input("\nA deshironi te hapni menun? ")
    fillimi_i_menys = fillimi_i_menys.lower()

## Menyja nese emri i pedoruesit ka 5 Shkronja
elif perdoruesilen == 5:
    # Ky mesazh sherben per te pershendetur perdoruesin
    print("\n/////////////////////////////////////////////////")
    sleep(.1)
    print("/                                               /")
    sleep(.1)
    print("/                                               /")
    sleep(.1)
    print("/                    Mini Menu                  /")
    sleep(.1)
    print("/                                               /")
    sleep(.1)
    print("/               Mirësevini,",perdoruesi,"              /")
    sleep(.1)
    print("/                                               /")
    sleep(.1)
    print("/                                               /")
    sleep(.1)
    print("/////////////////////////////////////////////////")
    sleep(.1)
    print('\nShkruani "Po" per te hapur menun,')
    sleep(.1)
    print('Shkruani "Jo" per te mbyllur programin.')
    sleep(.1)
    # Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
    fillimi_i_menys = input("\nA deshironi te hapni menun? ")
    fillimi_i_menys = fillimi_i_menys.lower()

## Menyja nese emri i pedoruesit ka 6 Shkronja
elif perdoruesilen == 6:
    # Ky mesazh sherben per te pershendetur perdoruesin
    print("\n//////////////////////////////////////////////////")
    sleep(.1)
    print("/                                                /")
    sleep(.1)
    print("/                                                /")
    sleep(.1)
    print("/                     Mini Menu                  /")
    sleep(.1)
    print("/                                                /")
    sleep(.1)
    print("/                Mirësevini,",perdoruesi,"             /")
    sleep(.1)
    print("/                                                /")
    sleep(.1)
    print("/                                                /")
    sleep(.1)
    print("//////////////////////////////////////////////////")
    sleep(.1)
    print('\nShkruani "Po" per te hapur menun,')
    sleep(.1)
    print('Shkruani "Jo" per te mbyllur programin.')
    sleep(.1)
    # Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
    fillimi_i_menys = input("\nA deshironi te hapni menun? ")
    fillimi_i_menys = fillimi_i_menys.lower()

## Menyja nese emri i pedoruesit ka 7 Shkronja
elif perdoruesilen == 7:
    # Ky mesazh sherben per te pershendetur perdoruesin
    print("\n///////////////////////////////////////////////////")
    sleep(.1)
    print("/                                                 /")
    sleep(.1)
    print("/                                                 /")
    sleep(.1)
    print("/                      Mini Menu                  /")
    sleep(.1)
    print("/                                                 /")
    sleep(.1)
    print("/               Mirësevini,",perdoruesi,"              /")
    sleep(.1)
    print("/                                                 /")
    sleep(.1)
    print("/                                                 /")
    sleep(.1)
    print("///////////////////////////////////////////////////")
    sleep(.1)
    print('\nShkruani "Po" per te hapur menun,')
    sleep(.1)
    print('Shkruani "Jo" per te mbyllur programin.')
    sleep(.1)
    # Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
    fillimi_i_menys = input("\nA deshironi te hapni menun? ")
    fillimi_i_menys = fillimi_i_menys.lower()

## Menyja nese emri i pedoruesit ka 8 Shkronja
elif perdoruesilen == 8:
    # Ky mesazh sherben per te pershendetur perdoruesin
    print("\n////////////////////////////////////////////////////")
    sleep(.1)
    print("/                                                  /")
    sleep(.1)
    print("/                                                  /")
    sleep(.1)
    print("/                      Mini Menu                   /")
    sleep(.1)
    print("/                                                  /")
    sleep(.1)
    print("/                Mirësevini,",perdoruesi,"             /")
    sleep(.1)
    print("/                                                  /")
    sleep(.1)
    print("/                                                  /")
    sleep(.1)
    print("////////////////////////////////////////////////////")
    sleep(.1)
    print('\nShkruani "Po" per te hapur menun,')
    sleep(.1)
    print('Shkruani "Jo" per te mbyllur programin.')
    sleep(.1)

    # Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
    fillimi_i_menys = input("\nA deshironi te hapni menun? ")
    fillimi_i_menys = fillimi_i_menys.lower()

## Menyja nese emri i pedoruesit nuk perbush asnje nga kriteret e mesiperme
else:
    print("\nMirësevini", perdoruesi)
    # Ky mesazh sherben per te pershendetur perdoruesin
    sleep(.5)
    # Keto variabla sherbejne per te pyetur perdoruesin a deshiron te hapi menun apo jo
    print('\nShkruani "Po" per te hapur menun,')
    sleep(.1)
    print('Shkruani "Jo" per te mbyllur programin.')
    sleep(.1)
    fillimi_i_menys = input("\nA deshironi te hapni menun? ")
    fillimi_i_menys = fillimi_i_menys.lower()

# Ne rast se pordoruesi zgjedh nje meny tjeter,
# Ateher ky kod i mundeson te zgjedhi perseri
while fillimi_i_menys != "po" and fillimi_i_menys != "jo":
        print('Keni shkruar menun gabim!')
        fillimi_i_menys = input("\nJu lutemi shkeruani prap se cilen menu deshironi te hapni? ")

# Ky funksion sherben kur perdoruesi nuk deshiron te kthehet ne menu
while fillimi_i_menys == "jo":
    menuja = 0
    loja = 0
    programi = 0
    print("\nMire u pafshim", perdoruesi)
    break

# Ky funksion sherben per te shfaqur menun
while fillimi_i_menys == "po":
    # Mini Menuja per te vendosur cilen nga menut te hapesh
    print("\n///////////////////////////////////////////////")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                  Mini Menu                  /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("/                                             /")
    sleep(.1)
    print("///////////////////////////////////////////////")
    sleep(.1)
    # Menut ne dispozicion
    print("\nVendos numrin 1 per te hapur menun e lojrave")
    sleep(.1)
    print("Vendos numrin 2 per te hapur menun e programeve")
    sleep(.1)
    print("Vendos numrin 3 per te pare informacione rreth programit")
    sleep(.1)
    # Variabla e menys
    menuja = int(input("\nCilen meny deshironi te hapni? "))

    # Ne rast se pordoruesi zgjedh nje numer i cili nuk eshte ne meny,
    # Ateher ky kod i mundeson te zgjedhi perseri
    while menuja != 1 and menuja !=2 and menuja !=3:
        print('Keni shkruar numrin gabim!')
        menuja = int(input("\nJu lutemi shkeruani prap se cilen menu deshironi te hapni? "))

    # Kodimet e Menyve 

    # Menuja e pare
    while menuja == 1:
        # Menuja e Lojrave
        print("\n//////////////////////////////////////////////////////////////")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("/                         Game Menu                          /")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("/                                                            /")
        sleep(.1)
        print("//////////////////////////////////////////////////////////////")
        sleep(.1)
        # Lojrat ne dispozicion
        print('\nVendos numrin 1 per te luajtur lojen e "Lotaris"')
        sleep(.1)
        print('Vendos numrin 2 per te luajtur lojen e "Hedhjes se gureve"')
        sleep(.1)
        print('Vendos numrin 3 per te luajtur lojen e "Gure,Leter & Gershere"')
        sleep(.1)
        print('Vendos numrin 4 per te luajtur lojen e "Fantazmes"')
        sleep(.1)
        print('Vendos numrin 5 per te luajtur lojen e "Pelcitesit"')
        sleep(.1)
        print('Vendos numrin 9 per tu kthyer prapa ne menu')
        sleep(.1)
        # Variabla e lojes
        loja = int(input("\nCilen loje deshironi te luani? "))
        
        # Ne rast se pordoruesi zgjedh nje numer i cili nuk eshte ne meny,
        # Ateher ky kod i mundeson te zgjedhi perseri
        while loja != 1 and loja !=2 and loja !=3 and loja !=4 and loja !=5 and loja !=9:
            print('Keni shkruar numrin gabim!')
            loja = int(input("\nJu lutemi shkeruani prap se cilen loje deshironi te luani? "))

        # Fillimi i kodimit te lojrave
        
        # Loja e lotaris
        while loja == 1:
            # Grafiku i lojes se lotaris
            print("\n///////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("/                         Loja e lotaris                          /")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("/                                                                 /")
            sleep(.1)
            print("///////////////////////////////////////////////////////////////////")

            # False ne kete rast sherben per ti bere variablat si te pasakta 
            i1ne1 = False
            i2ne1 = False
            i3ne1 = False
            i1ne2 = False
            i2ne2 = False
            i3ne2 = False
            i1ne3 = False
            i2ne3 = False
            i3ne3 = False

            # Keto variabla sherbejn per ti bere ato si 0 apo fillestare pastaj ti japin vlere kodet e meposhtme
            sakta = 0
            shumaparave = 0

            # Lista e numrave
            numrat = [1,2,3,4,5,6,7,8,9]

            # Keto variabla sherbejne per te zgjedhur nje numer nga lista 'numrat'
            kompjuteri1 = choice(numrat)
            kompjuteri2 = choice(numrat)
            kompjuteri3 = choice(numrat)

            # Keto variabla sherbejne per te vendosur numrat nga pordoruesi
            numri1 = int(input("\nVendosni nje numer nga 1 deri ne 9: "))
            numri2 = int(input("Vendosni nje numer tjeter nga 1 deri ne 9: "))
            numri3 = int(input("Vendosni per here te fundit nje numer nga 1 deri ne 9: "))

            # Keto sherbejn per te treguar se a eshte numri i 1 i sakt apo pasakt
            if kompjuteri1 == numri1:
                i1ne1 = True
                sakta = sakta + 1
            elif i1ne1 == False and kompjuteri1 == numri2:
                i2ne1 = True
                sakta = sakta + 1
            elif i1ne1 == False and i2ne1 == False and kompjuteri1 == numri3:
                i3ne1 = True
                sakta = sakta + 1 

            # Keto sherbejn per te treguar se a eshte numri i 2 i sakt apo pasakt
            if i1ne1 == False and kompjuteri2 == numri1:
                i1ne2 = True
                sakta = sakta + 1
            elif i1ne2 == False and i2ne1 == False and kompjuteri2 == numri2:
                i2ne2 = True
                sakta = sakta + 1
            elif i1ne2 == False and i2ne2 == False and i3ne1 == False and kompjuteri2 == numri3:
                i3ne2 = True
                sakta = sakta + 1

            # Keto sherbejn per te treguar se a eshte numri i 3 i sakt apo pasakt
            if i1ne1 == False and i1ne2 == False and kompjuteri3 == numri1:
                i1ne3 = True
                sakta = sakta + 1
            elif i1ne3 == False and i2ne1 == False and i2ne2 == False and kompjuteri3 == numri2:
                i2ne3 = True
                sakta = sakta + 1
            elif i1ne3 == False and i2ne3 == False and i3ne1 == False and i3ne2 == False and kompjuteri3 == numri3:
                i3ne3 = True
                sakta = sakta + 1

            # Keto funksione sherbejne per te caktuar shumen e parave te fituara
            if sakta == 1:
                shumaparave = 250
            elif sakta == 2:
                shumaparave = 500
            elif sakta == 3:
                shumaparave = 1000
            else:
                shumaparave = 0

            # Printimi i rezultatit ne qoftese asnje numer nuk eshte i sakte
            if sakta == 0:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3)) 
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3)) 
                sleep(.1)
                print("Na vjen keq por ti nuk ke fituar asgje pasiqe nuk keni asnje numer te sakt!")
                sleep(.1)
            # Printimi i rezultatit ne qoftese vetem nje numer eshte i sakte
            elif sakta == 1:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3))
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3)) 
                sleep(.1)
                print("Dhe ti ke vetem " + str(sakta) + " numer te sakte") 
                sleep(.1)
                print("Dhe ke fituar $" + str(shumaparave))
                sleep(.1)
            # Printimi i rezultatit kur dy numera jane te sakta
            elif sakta == 2:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3))
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3))
                sleep(.1)
                print("Dhe ti ke " + str(sakta) + " numera te sakte")
                sleep(.1)
                print("Dhe ke fituar $" + str(shumaparave))
                sleep(.1)
            # Printimi i rezultatit ne qoftese te gjitha numrat jane te sakta
            elif sakta == 3:
                sleep(.1)
                print("\nKompjuteri ka zgjedhur keto numra: " + str(kompjuteri1) + ", " + str(kompjuteri2) + " & " + str(kompjuteri3)) 
                sleep(.1)
                print("Ndersa ti ke zgjedhur keto numra: " + str(numri1) + ", " + str(numri2) + " & " + str(numri3))
                sleep(.1)
                print("Ju lumte ju keni gjetur " + str(sakta) + " numra te sakte") 
                sleep(.1)
                print("Dhe ju keni fituar $" + str(shumaparave))
                sleep(.1)
            
            # Keto funksione sherbejn per tu kthyer ne menu
            loja = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()
            
        # Loja e hedhjes se gureve
        while loja == 2:
            # Grafiku i lojes se hedhjes se gureve
            print("\n////////////////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("/                         Loja e hedhjes se gureve                         /")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("/                                                                          /")
            sleep(.1)
            print("////////////////////////////////////////////////////////////////////////////")
            # Numrat e gurit
            min = 1
            max = 6

            # Variabla e Gjuaj Guret
            print('\nShkruani "Po" per tu gjuajtur guret,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur lojen.')
            sleep(.1)
            gjuajguret = input("\nA deshironi te filloni me gjuajtjen e gureve? ")
            gjuajguret = gjuajguret.lower()

            # While ne kete rast perdoret per kur Gjuaj Guret eshte Po
            while gjuajguret == "po":
                # Guri i 1
                g1 = randint(min,max)
                # Guri i 2
                g2 = randint(min,max)
                # Guri i 3
                g3 = randint(min,max)
                # Guri i 4
                g4 = randint(min,max)
                # Printimi i Gureve per lojtarin e 1
                print("\nPo Rrotullohen guret per lojtarin e 1...")
                sleep(1)
                print("\nKeni qelluar...")
                sleep(1)
                print("Guri i pare:",g1)
                sleep(.8)
                print("Guri i dyte:",g2)
                # Printimi i Gureve per lojtarin e 2
                print("\nPo rrotullohen guret per lojtarin e 2...")
                sleep(1)
                print("\nKeni qelluar...")
                sleep(1)
                print("Guri i pare:",g3)
                sleep(1)
                print("Guri i dyte:",g4)

                # Guret per lojtarin e 1
                lojtari1 = g1 + g2
                sleep(1)
                print("\nLojtari 1 ne total ka:", lojtari1)
                # Guret per lojtarin e 2
                lojtari2 = g3 + g4
                sleep(1)
                print("Lojtari 2 ne total ka:", lojtari2)

                # Ky funksion sherben kur guret e lojtarit te 1 jane me te madhenj se guret e lojtarit te 2 
                if lojtari1 > lojtari2:
                    sleep(1)
                    print("\nKa fituar lojtari 1")
                # Ky funksion sherben kur guret e lojtarit te 1 jane me te vegjel se guret e lojtarit te 2 
                elif lojtari1 < lojtari2:
                    sleep(1)
                    print("\nKa fituar lojtari 2")
                # Ky funksion sherben kur guret e 2 lojtareve jane barazim
                else:
                    sleep(1)
                    print("\nRezultati eshte barazim")
                    
                sleep(1)
                print('\nShkruani "Po" per tu gjuajtur perseri,')
                sleep(.1)
                print('Shkruani "Jo" per te mbyllur lojen.')
                sleep(.1)
                gjuajguret = input("\nA deshironi te gjuani perseri? ")
                gjuajguret = gjuajguret.lower()
                
            # Keto funksione sherbejn per tu kthyer ne menu
            if gjuajguret == "jo":
                print('\nShkruani "Po" per tu rikthyer,')
                sleep(.1)
                print('Shkruani "Jo" per te mbyllur programin.')
                sleep(.1)
                loja = 0
                fillimi_i_menys = input("\nA deshironi te ktheheni tek menuja? ")
                fillimi_i_menys = fillimi_i_menys.lower()
        
        # Loja e Gure,Leter & Gershere
        while loja == 3:
            # Grafiku i lojes se Gure,Leter & Gershere
            print("\n//////////////////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("/                         Loja e Gure,Leter & Gershere                       /")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("/                                                                            /")
            sleep(.1)
            print("//////////////////////////////////////////////////////////////////////////////")
            # Keto sherbejne per te treguar rregullat e lojes
            print("Rregullat e lojes Gure,Leter & Gershere jane keto: \n"
                                +"Gure vs Leter->Fiton ai qe ka zgjedhur Leter \n"
                                + "Gure vs Gershere->Fiton ai qe ka zgjedhur Gur \n"
                                +"Leter vs Gershere->Fiton ai qe ka zgjedhur Gersher \n") 
            
            # Ne kete liste jane te vendosur opcinet e lojes
            lista = ["gure","leter","gershere"]
            
            # Kjo variabel sherben per ti dhene vlere i-se
            i = 1

            # Ky kod eshte funksional vetem kur i eshte me e vogel apo e njejte me 5
            while i <= 5:
                njeriu = input("\nGure, leter apo gershere: ")
                sleep(.1)
                pc = choice(lista)
                njeriu = njeriu.lower()

                # Ky funksion sherben kur eshte shkruar teksti gabim
                while njeriu not in lista:
                    print("\n*****NUK ESHTE SHENUAR MIRE TEKSTI!*****")
                    sleep(.1)
                    njeriu = input("Gure, leter apo gershere: ")
                    njeriu = njeriu.lower()
                    sleep(.1)

                # Ky funksion sherben kur Kompjuteri dhe Perdoruesi kane zjedhur te njejtin opcion    
                while pc == njeriu:
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****BARAZIM*****")
                    sleep(.1)
                    njeriu = input("\nGure, leter apo gershere: ")
                    njeriu = njeriu.lower()
                    sleep(.1)
                    pc = choice(lista)
                    i+=1

                # Keto funksione sherbejne kur Kompjuteri dhe Perdoruesi kane zgjedhur opsione te ndryshme
                ## Keto funksione gjithashtu sherbejne per te treguar se a keni humbur apo keni fituar
                if pc == "gershere" and njeriu == "gure":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("Fituat pas heres se ", i)
                    sleep(.1)
                    break
                elif pc == "gershere" and njeriu == "leter":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****HUMBE*****")
                    sleep(.1)

                elif pc == "gure" and njeriu == "gershere":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****HUMBE*****")
                    sleep(.1)

                elif pc == "gure" and njeriu == "leter":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("Fituat pas heres se ", i)
                    sleep(.1)
                    break
                elif pc == "leter" and njeriu == "gure":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("*****HUMBE*****")
                    sleep(.1)
                elif pc == "leter" and njeriu == "gershere":
                    print("\nKompjuteri ka zgjedhur: ", pc)
                    sleep(.1)
                    print("Fituat pas heres se ", i)
                    sleep(.1)
                    break
                
                # Ky funksion sherben kur Perodoruesi ka kaluar limitin e mundesive 
                if i >= 5:
                    print("\nKeni kaluar limit e mundesive, keni pasur vetem", i, "raste.")
                    sleep(.1)
                    break
                i+=1
            # Keto funksione sherbejn per tu kthyer ne menu
            loja = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()
        
        # Loja e Fantazmes
        while loja == 4:
            # Grafiku i lojes se lotaris
            print("\n////////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("/                         Loja e Fantazmes                         /")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("////////////////////////////////////////////////////////////////////")

            # Pershendetja e Perdoruesit
            print("\nPershendetje", perdoruesi, 'eshte koha per te luajtur "Loja e Fantazmes"')
            sleep(1)

            # Kodimi i lojes
            ndihem_i_guximshem = True
            piket = 0

            while ndihem_i_guximshem:
                dera_e_fantazmes = randint(1,3)
                print("\nTre dyer perpara...")
                sleep(1)
                print("Nje fantazem pas njeres.")
                sleep(1)
                print("Cilen dere do te hapni?")
                sleep(1)
                dera = input("1,2 apo 3? ")
                sleep(1)
                numri_i_deres = int(dera)

                ## Ky sherben ne rast se numri i zgjedhur eshte i njejte
                ## Me ate ne te cilin eshte fantazma
                if numri_i_deres == dera_e_fantazmes:
                    print("\nFantazem!")
                    sleep(1)
                    ndihem_i_guximshem = False
                ## Ne rast se numri i zgjedhur nuk eshte i njejte me ate te fantazmes
                ## Ky kod muneson vazhdimin e lojes per ne deren tjeter
                else:
                    print("\nNuk ka Fantazem!")
                    sleep(1)
                    print("Ti u fute ne dhomen tjeter.")
                    sleep(1)
                    piket +=1

            print("\nLargohu!")
            sleep(1)
            # Keto funksione sherbejne per te printuar rezultatin
            if piket == 1:
                print("Loja Mbaroi! Ti kalove", piket, "dhomë")
            else:
                print("Loja Mbaroi! Ti kalove", piket, "dhoma")

            # Keto funksione sherbejn per tu kthyer ne menu
            loja = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()

        # Loja e Pelcitesit
        while loja == 5:
            # Grafiku i lojes se lotaris
            print("\n////////////////////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("/                         Loja e Fantazmes                         /")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("/                                                                  /")
            sleep(.1)
            print("////////////////////////////////////////////////////////////////////")

            # Ky print sherben per te njoftuar perdoruesin se loja do hapet ne faqe tjeter
            # Ndersa sleep(5) sherben per te pritur 5 sekonda deri ne fillim te lojes
            print("\n***LOJA DO HAPET NE FAQE TJETER***")
            sleep(5)

            # Fillimi i kodimit te lojes
            HEIGHT = 500
            WIDTH = 800
            window = Tk()
            window.title("Pelcitesi i fluskave")
            c = Canvas (window, width = WIDTH, height = HEIGHT, bg = 'darkblue')
            c.pack()

            ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill = 'red')
            ship_id2 = c.create_oval(0, 0, 30, 30, outline = 'red')
            SHIP_R = 15
            MID_X = WIDTH / 2
            MID_Y = HEIGHT / 2
            c.move(ship_id, MID_X, MID_Y)
            c.move(ship_id2, MID_X, MID_Y)

            SHIP_SPD = 10
            def move_ship(event):
                if event.keysym == "W" or event.keysym == "w" or event.keysym == "Up":
                    c.move(ship_id, 0, -SHIP_SPD)
                    c.move(ship_id2, 0, -SHIP_SPD)
                elif event.keysym == "S" or event.keysym == "s" or event.keysym == "Down":
                    c.move(ship_id, 0, SHIP_SPD)
                    c.move(ship_id2, 0,SHIP_SPD)
                elif event.keysym == "A" or event.keysym == "a" or event.keysym == "Left":
                    c.move(ship_id, -SHIP_SPD, 0)
                    c.move(ship_id2, -SHIP_SPD, 0)
                elif event.keysym == "D" or event.keysym == "d" or event.keysym == "Right":
                    c.move(ship_id, SHIP_SPD, 0)
                    c.move(ship_id2, SHIP_SPD, 0)
            c.bind_all('<Key>', move_ship)

            bub_id = list()
            bub_r = list()
            bub_speed = list()
            MIN_BUB_R = 10
            MAX_BUB_R = 30
            MAX_BUB_SPD = 10
            GAP = 100
            def create_bubble():
                x = WIDTH + GAP
                y = randint(0, HEIGHT)
                r = randint(MIN_BUB_R, MAX_BUB_R)
                id1 = c.create_oval(x - r, y - r, x + r, y + r, outline = "white")
                bub_id.append(id1)
                bub_r.append(r)
                bub_speed.append(randint(1, MAX_BUB_SPD))

            def move_bubbles():
                for i in range(len(bub_id)):
                    c.move(bub_id[i], -bub_speed[i], 0)

            def get_coords(id_num):
                pos = c.coords(id_num)
                x = (pos[0] + pos[2])/2
                y = (pos[1] + pos[3])/2
                return x, y

            def del_bubble(i):
                del bub_r[i]
                del bub_speed[i]
                c.delete(bub_id[i])
                del bub_id[i]

            def clean_up_bubs():
                for i in range(len(bub_id) - 1, -1, -1):
                    x, y = get_coords(bub_id[i])
                    if x < -GAP:
                        del_bubble(i)

            def distance(id1, id2):
                x1, y1 = get_coords(id1)
                x2, y2 = get_coords(id2)
                return sqrt((x2 - x1)**2 + (y2 - y1)**2)

            def collision():
                points = 0
                for bub in range(len(bub_id)-1, -1, -1):
                    if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
                        points += (bub_r[bub] + bub_speed[bub])
                        del_bubble(bub)
                return points

            c.create_text(50, 30, text="KOHA", fill="white")
            c.create_text(150,30, text="PIKET", fill="white")
            time_text = c.create_text(50, 50, fill="white")
            score_text = c.create_text(150, 50, fill="white")

            def show_score(score):
                c.itemconfig(score_text, text=str(score))

            def show_time(time_left):
                c.itemconfig(time_text, text=str(time_left))

            BUB_CHANCE = 10
            TIME_LIMIT = 30
            BONUS_SCORE = 1000
            score = 0
            bonus = 0
            end = time() + TIME_LIMIT
            #MAIN GAME LOOP
            while time() < end:
                if randint(1, BUB_CHANCE) == 1:
                    create_bubble()
                move_bubbles()
                clean_up_bubs()
                score += collision()
                if (int(score / BONUS_SCORE)) > bonus:
                    bonus += 1
                    end += TIME_LIMIT
                show_score(score)
                show_time(int(end - time()))
                window.update()
                sleep(0.01)

            c.create_text(MID_X, MID_Y, \
                        text="LOJA MBAROI", fill="white", font=("Helvetica", 30))
            c.create_text(MID_X, MID_Y + 30, \
                        text="Piket: " + str(score), fill="white")
            c.create_text(MID_X, MID_Y + 45, \
                        text="Koha shperblim: " + str(bonus*TIME_LIMIT) + "sekonda", fill="white")
            c.create_text(MID_X, MID_Y + 60, \
                        text="Ti ke kohe shtese: " + str(bonus) + " here", fill="white")

            # Keto funksione sherbejn per tu kthyer ne menu
            loja = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()

        # Ky kod sherben per tu kthyer prapa ne menu
        while loja == 9:
            loja = 0
            menuja = 0
            fillimi_i_menys == "po"
            
        # Ky funksion sherben kur perdoruesi nuk deshiron te kthehet ne menu
        while fillimi_i_menys == "jo":
            loja = 0
            menuja = 0
            print("\nMire u pafshim", perdoruesi)
            sleep(.1)
            break 
    
    # Menuja e dyte
    while menuja == 2:
        # Menuja e programeve
        print("\n//////////////////////////////////////////////////////////////////////")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("/                            Programs Menu                           /")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("/                                                                    /")
        sleep(.1)
        print("//////////////////////////////////////////////////////////////////////")
        sleep(.1)
        # Programet ne dispozicion
        print('\nVendos numrin 1 per te perdorur programin e "Kovertimit te gradeve"')
        sleep(.1)
        print('Vendos numrin 2 per te perdorur programin e "Gjetjes se perimetrit"')
        sleep(.1)
        print('Vendos numrin 3 per te perdorur programin e "Gjenerimit te Paswordit"')
        sleep(.1)
        print('Vendos numrin 9 per tu kthyer prapa ne menu')
        sleep(.1)
        # Variabla e Programit
        programi = int(input("\nCilin program deshironi te perdorni? "))
        
        # Ne rast se pordoruesi zgjedh nje program i cili nuk eshte ne meny,
        # Ateher ky kod i mundeson te zgjedhi perseri
        while programi != 1 and programi !=2 and programi !=3 and programi !=9:
            print('Keni shkruar numrin gabim!')
            programi = int(input("\nJu lutemi shkeruani prap se cilin programe deshironi te hapni? "))

        # Fillimi i kodimit te Programeve
        
        # Konvertimi i Gradeve
        while programi == 1:
            # Grafiku i Konvertimit te Gradeve
            print("\n/////////////////////////////////////////////////")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/            Konvertimi i Gradeve               /")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/                                               /")
            sleep(.1)
            print("/////////////////////////////////////////////////")
            sleep(.1)
            # Variabla e gradeve
            grada = int(input("\nSa grade eshte: "))
            # Variabla e shkalles
            shkalla = input("Deshironi ta konvertoni ne C apo F: ")
            # Formula per konvertimin e °F
            F = int((grada * 9/5) + 32)
            # Formula per konvertimin e °C
            C = int((grada - 32) * 5/9)
                    
            # Funksioni i °C
            def konvertimi(grada, shkalla):
                        if shkalla == "c" or "C":
                            return C
            # Funksioi i °F
            def konvertimi2(grada,shkalla):
                        if shkalla == "f" or "F":
                            return F
                    
            # Printimi per °C
            if shkalla == "c" or shkalla == "C":
                        print(grada,"°F","eshte e barabart me", konvertimi(grada,shkalla),"°C")
            # Printimi per °F
            elif shkalla == "f" or shkalla == "F":
                        print(grada,"°C","eshte e barabart me", konvertimi2(grada,shkalla),"°F")
            
            # Keto funksione sherbejn per tu kthyer ne menu
            programi = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()

        # Perimetri
        while programi == 2:
            # Grafiku i perimetrit
            print("\n////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("/              Gjetja e Perimetrit                 /")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("/                                                  /")
            sleep(.1)
            print("////////////////////////////////////////////////////")
            sleep(.1)
            
            # Variabla e Gjatesise
            a = float(input("\nGjeresia: "))
            sleep(.5)
            
            # Variabla e Gjeresise
            b = float(input("Gjatesia: "))
            sleep(.25)
            
            # Formula e Perimetrit
            P = 2*(a+b)
            
            # Perimetri 
            print("\nPerimetri i kesaj siperfaqe eshte: ", P, "cm")
            sleep(.25)
            
            # Keto funksione sherbejn per tu kthyer ne menu
            programi = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()
        
        # Gjenerimi i Paswordeve
        while programi == 3:
            # Grafiku i Gjenerimit te paswordeve
            print("\n///////////////////////////////////////////////////////")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("/              Gjenerimi i Paswordeve                 /")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("/                                                     /")
            sleep(.1)
            print("///////////////////////////////////////////////////////")
            sleep(.1)
            
            # Ky funksion sherben per te perzier karakteret
            def perziej(shkronja):
                listaezbrazet = list(shkronja)
                shuffle(listaezbrazet)
                return ''.join(listaezbrazet)

            # Keto shkronja,numra & simbole jane marrur bazuar ne kodin ASCII
            # Keto shkronja,numra & simbole jane marrur nga http://www.asciitable.com/
            ## Shkronja te medha
            shtm1 = chr(randint(65,90)) 
            shtm2 = chr(randint(65,90))
            ## Shkronja te vogla
            shtv1 = chr(randint(97,122))
            shtv2 = chr(randint(97,122))
            ## Numra
            nm1 = chr(randint(48,57))
            nm2 = chr(randint(48,57))
            ## Simbole
            si1 = chr(randint(33,47))
            si2 = chr(randint(58,64))

            # Variabla per te treguar se sa password do te printohen
            a = int(input("\nSa Password ju nevojiten?: "))
            sleep(.1)
            
            # Keto printime perdoren per te treguar Perdoruesit sa Karaktere jane ne dispozicion
            print('\nPer 8 Karaktere vendosni numrin 8')
            sleep(.1)
            print('Per 16 karaktere vendosni numrin 16')
            sleep(.1)
            print('Per 24 karaktere vendosni numrin 24')
            sleep(.1)
            print('Per 32 karaktere vendosni numrin 32')
            sleep(.1)
            print('Per 40 karaktere vendosni numrin 40')
            sleep(.1)
            
            # Variabla per te treguar programit se sa karaktere duhet te gjenerohen
            b = int(input("\nSa karakteresh e deshironi Paswordin?: "))

            # Kjo variabel sherben per te i dhene vlere i-se
            i = 1

            # Ky funksion eshte aktiv per aq here sa password ju nevojiten perdoruesit
            ## Ndersa a+1 sherben qe kur te gjenerohen passwordet printimi i tyre te filloj nga 1 dhe jo nga 0
            while i in range(a+1):
                # Ky kod sherben kur shkruhet numri i karaktereve eshte shkruar gabim
                while b != 8 and b != 16 and b != 24 and b != 32 and b != 40:
                    print("\nE keni shkruar gabim, Ju lutemi shkruani numrin perseri.")
                    b = int(input("\nSa karakteresh e deshironi Paswordin?: "))
                
                # Kodi per 8 Karaktere
                if b == 8:
                    password = shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2 
                    password = perziej(password)
                # Kodi per 16 Karaktere
                elif b == 16:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*2 
                    password = perziej(password)
                # Kodi per 24 Karaktere
                elif b == 24:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*3 
                    password = perziej(password)
                # Kodi per 32 Karaktere
                elif b == 32:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*4 
                    password = perziej(password)
                # Kodi per 40 Karaktere
                elif b == 40:
                    password = (shtm1 + shtm2 + shtv1 + shtv2 + nm1 + nm2 + si1 + si2)*5 
                    password = perziej(password)
                
                # Printimi i Paswordeve
                print("Paswordi i", str(i) + ":", password)
                sleep(.1)
                i+=1
            
            # Keto funksione sherbejn per tu kthyer ne menu
            programi = 0
            print('\nShkruani "Po" per tu rikthyer,')
            sleep(.1)
            print('Shkruani "Jo" per te mbyllur programin.')
            sleep(.1)
            fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
            fillimi_i_menys = fillimi_i_menys.lower()

        # Ky kod sherben per tu kthyer prapa ne menu
        while programi == 9:
            programi = 0
            menuja = 0
            fillimi_i_menys == "po"
    
        # Ky funksion sherben kur perdoruesi nuk deshiron te kthehet ne menu
        while fillimi_i_menys == "jo":
            programi = 0
            menuja = 0
            print("\nMire u pafshim", perdoruesi)
            sleep(.1)
            break 
    
    # Menuja e trete
    while menuja == 3:
        print("\nKy është projekti im final i kursit dy mujor në Bonevet rreth Python.")
        sleep(1)
        print("\nProjekti përmban një Main Menu (Menyn Kryesore) i cili përbëhet nga 4 Lojra & 3 Programe")
        sleep(1.5)
        print("\nKy programë është realizuar në vitin 2019")
        sleep(1)
        print("Zhvilluesi i ketij programi është Rilind Kyçyku")
        sleep(1)
        print("Përditësimi i fundit i këtij programit është bërë në vitin 2021")
        sleep(1.5)
        print("\nLista e Lojrave")
        sleep(1)
        print("* Loja e Lotaris")
        sleep(.50)
        print("* Hedhja e Gurëve - 2 Lojtarë")
        sleep(.50)
        print("* Random Number")
        sleep(.50)
        print("* Loja e Fantazmës")
        sleep(.50)
        print("* Loja e Pelcitesit")
        sleep(.50)
        print("\nLista e Programeve")
        sleep(1)
        print("* Gjenerimi i Password-it")
        sleep(.50)
        print("* Konvertimi i Gradëve °C & °F")
        sleep(.50)
        print("* Gjetja e Perimetrit")
        sleep(.50)

        # Keto funksione sherbejn per tu kthyer ne menu
        menuja = 0
        print('\nShkruani "Po" per tu rikthyer,')
        sleep(.1)
        print('Shkruani "Jo" per te mbyllur programin.')
        sleep(.1)
        fillimi_i_menys = input("A deshironi te ktheheni mbrapa? ")
        fillimi_i_menys = fillimi_i_menys.lower()

        # Ky kod sherben per tu kthyer prapa ne menu
        while menuja == 9:
            menuja = 0
            fillimi_i_menys == "po"
    
        # Ky funksion sherben kur perdoruesi nuk deshiron te kthehet ne menu
        while fillimi_i_menys == "jo":
            menuja = 0
            print("\nMire u pafshim", perdoruesi)
            sleep(.1)
            break 


# Keto inpute sherbejn qe kur programi te hapet ne Comand Prompt te Pythonit mos te mbyllet pas perfundimit
input()
input()
input()
