import sys

if __name__ == '__main__':
    # MANIPULACIJA ULAZNOG TEKSTA
    string1 = sys.stdin.read().splitlines()
    #f = open("C:\\Users\\Filip\\PycharmProjects\\pythonProject\\src.txt" , "r")
    #string1 = f.read().splitlines()

    nizovi= string1[0].split("|")
    for i in range (len(nizovi)):
        nizovi[i]=nizovi[i].split(",")
    #2d lista razdjeljena po nizovima i interno svaki od njih po znakovima

    stanja=string1[1].split(",")
    ul_znakovi = string1[2].split(",")
    zn_stoga = string1[3].split(",")
    prih_stanja = string1[4].split(",")
    pocetno_stanje = string1[5]
    poc_stog = string1[6]

    ul_znakovi.append("$")
    stog=poc_stog

    #3D lista koja je definirana za prijelaze vanjska dimenzija -> stanja, srednja -> ul_znakovi, unutarnja -> zn_stoga
    prijelazi=lst = [[ ['#' for i in range(len(zn_stoga))] for j in range(len(ul_znakovi))] for row in range(len(stanja))]

    for i in range(7,len(string1)):
        pomocna = string1[i].split("->")
        for j in range(2):
            pomocna[j]=pomocna[j].split(",")
        prijelazi[stanja.index(pomocna[0][0])][ul_znakovi.index(pomocna[0][1])][zn_stoga.index(pomocna[0][2])]=pomocna[1]

    for i in range(len(nizovi)):
        stog = poc_stog
        stanje= pocetno_stanje
        ulaz=""
        fail=0
        string_ispis=stanje+"#"+stog+"|"
        kontrola=0
        for j in range(len(nizovi[i])):
            pom_str=""
            ulaz=nizovi[i][j]
            znak_st=stog[0]
            stog=stog[1:]
            izlaz= prijelazi[stanja.index(stanje)][ul_znakovi.index(ulaz)][zn_stoga.index(znak_st)]
            while(len(izlaz)<2):
                pom_str1=""
                izlaz1 = prijelazi[stanja.index(stanje)][len(ul_znakovi) - 1][zn_stoga.index(znak_st)]

                if(len(izlaz1)>1):
                    izlaz=izlaz1

                    stanje=izlaz[0]
                    if(izlaz[1]!="$"):
                        stog=izlaz[1]+stog
                    if(len(stog)!=0):
                        pom_str1+=izlaz[0]+"#"+stog+"|"
                    else:
                        pom_str1 += izlaz[0] + "#$|"
                    string_ispis+=pom_str1
                    if (len(stog) == 0):
                        kontrola=1
                        break

                    znak_st=stog[0]
                    stog=stog[1:]
                    izlaz=prijelazi[stanja.index(stanje)][ul_znakovi.index(ulaz)][zn_stoga.index(znak_st)]

                else:
                    break
            if(kontrola==1):
                break

            stanje = izlaz[0]
            pom_str+=stanje+"#"

            if(len(izlaz)>1):
                if(izlaz[1]!="$"):
                    stog=izlaz[1]+stog
                if(len(stog)==0):
                    pom_str += "$|"
                else:
                    pom_str+=stog+"|"
                string_ispis+=pom_str
            else:
                fail=1
                string_ispis+="fail|"
                break

        if(kontrola==1):
            string_ispis+="fail|0"
            print(string_ispis)
        elif(stanje in prih_stanja):
            string_ispis += "1"
            print(string_ispis)
        elif(fail==1):
            string_ispis+="0"
            print(string_ispis)
        else:
            x=0
            if(len(stog)>0):
                x=1
                skroz_dr_pom=""
                skroz_dr_stog=stog
                skr_stanje=stanje
            while(x):
                znak=skroz_dr_stog[0]
                skroz_dr_stog=skroz_dr_stog[1:]
                lista=prijelazi[stanja.index(skr_stanje)][len(ul_znakovi)-1][zn_stoga.index(znak)]
                if (len(lista) < 2):
                    string_ispis += "0"
                    print(string_ispis)
                    break

                skr_stanje=lista[0]

                if(lista[1]=="$" and len(skroz_dr_stog)==0):
                    skroz_dr_pom += lista[0] + "#" + lista[1]+"|"

                elif(lista[1]!="$"):
                    skroz_dr_stog=lista[1]+skroz_dr_stog
                    skroz_dr_pom+=lista[0]+"#"+skroz_dr_stog+"|"

                else:
                    skroz_dr_pom += lista[0] + "#" + skroz_dr_stog + "|"
                xx = prijelazi[stanja.index(skr_stanje)][len(ul_znakovi) - 1][zn_stoga.index(znak)]
                if(skr_stanje in prih_stanja):
                    string_ispis+=skroz_dr_pom+"1"
                    print(string_ispis)
                    break


                elif (xx[0] == skr_stanje and prijelazi[stanja.index(skr_stanje)][len(ul_znakovi) - 1][
                    zn_stoga.index(xx[1][0])] == "#"):

                    string_ispis += skroz_dr_pom + "0"

                    print(string_ispis)

                    break

                if(len(skroz_dr_stog)==0):
                    string_ispis+="0"
                    print(string_ispis)
                    break