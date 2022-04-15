import sys
#globalne varjiable
global sva_stanja, abeceda, prih_stanja, pocetno_stanje, tablica_prijelaza

def velicina_bez_dupl(a):
    vel=list()
    for index in a:
        if(index not in vel):
            vel.append(index)
    return len(vel)


def ispis():
    string =",".join(sva_stanja)
    print(string)
    string = ",".join(abeceda)
    print(string)
    string = ",".join(prih_stanja)
    print(string)
    print(pocetno_stanje)
    pomoc=0
    for stanje in range(len(tablica_prijelaza)):
        for slovo in range(len(tablica_prijelaza[stanje])):
            print(sva_stanja[pomoc] + "," + abeceda[slovo] + "->"+ tablica_prijelaza[stanje][slovo])
        pomoc+=1


def brisi_nedohvatljiva():
    global sva_stanja, abeceda, prih_stanja, pocetno_stanje, tablica_prijelaza
    lista = list()
    lista.append(pocetno_stanje)
    velicina = len(lista)
    xx=0
    while(xx<velicina):
        for j in range(len(abeceda)):
            var=tablica_prijelaza[sva_stanja.index(lista[xx])][j]
            if(var not in lista):
                lista.append(var)
                velicina+=1
        xx+=1

    lista=sorted(lista)

    lista2=list()
    pomocna_lista = list()
    for el in sva_stanja:
        if(el not in lista):
            lista2.append(sva_stanja.index(el))

    for el in range(len(tablica_prijelaza)):
        if(el not in lista2):
            pomocna_lista.append(tablica_prijelaza[el])

    tablica_prijelaza=pomocna_lista
    sva_stanja=lista

    prih_stanja=[value for value in prih_stanja if value in sva_stanja]


def brisi_istovjetna():
    global sva_stanja, abeceda, prih_stanja, pocetno_stanje, tablica_prijelaza
    neprih_stanja = list()
    skupina = list()
    nova_skupina = list()

    for stanje in sva_stanja:
        if(stanje not in prih_stanja):
            neprih_stanja.append(stanje)

    skupina.append(prih_stanja)
    skupina.append(neprih_stanja)
    prijelazi_skupine = list()
    prijelaz_jednog = list()
    promjena = list()
    promjena2 = list()
    promjena3 = list()
    zavrsi=1

    while(zavrsi==1):
        zavrsi=0
        nova_skupina.clear()
        for skup in skupina:
            prijelazi_skupine.clear()
            for element in skup:
                prijelaz_jednog.clear()
                for slovo in abeceda:
                    var1=tablica_prijelaza[sva_stanja.index(element)][abeceda.index(slovo)]
                    var=-1
                    for indexx in range(len(skupina)):
                        if(var1 in skupina[indexx]):
                            var=indexx
                    prijelaz_jednog.append(var)


                prijelazi_skupine.append(prijelaz_jednog.copy())

            if(velicina_bez_dupl(prijelazi_skupine)!=1):
                promjena.clear()
                promjena3.clear()
                zavrsi=1
                for el1 in range(len(prijelazi_skupine)):
                    promjena2.clear()
                    if(prijelazi_skupine[el1] in promjena):
                        promjena3[promjena.index(prijelazi_skupine[el1])].append(skup[el1])
                    else:
                        promjena.append(prijelazi_skupine[el1])
                        promjena2.append(skup[el1])
                        promjena3.append(promjena2.copy())
                for el2 in promjena3:

                    nova_skupina.append(el2)
            else:
                nova_skupina.append(skup)

        skupina=nova_skupina.copy()
        skupina.sort()

    nova_stanja= list()
    for el in skupina:
        nova_stanja.append(el[0])

    neka_nova_tablica = list()
    for prijel_jedn in range(len(tablica_prijelaza)):
        for slj_stanje in range(len(tablica_prijelaza[prijel_jedn])):
            if(tablica_prijelaza[prijel_jedn][slj_stanje] not in nova_stanja):
                for el in skupina:
                    if(tablica_prijelaza[prijel_jedn][slj_stanje] in el):
                        tablica_prijelaza[prijel_jedn][slj_stanje]=el[0]
        if(sva_stanja[prijel_jedn] in nova_stanja):
            neka_nova_tablica.append(tablica_prijelaza[prijel_jedn].copy())

    sva_stanja = nova_stanja
    prih_stanja = [value for value in prih_stanja if value in sva_stanja]
    tablica_prijelaza=neka_nova_tablica
    if(pocetno_stanje not in sva_stanja):
        for el in skupina:
            if(pocetno_stanje in el):
                pocetno_stanje=el[0]


if __name__ == '__main__':

    # MANIPULACIJA ULAZNOG TEKSTA
    string1 = sys.stdin.read().splitlines()
    #f = open("src.txt", "r")
    #string1 = f.read().splitlines()

    sva_stanja = string1[0].split(",")
    abeceda = string1[1].split(",")
    prih_stanja = string1[2].split(",")
    pocetno_stanje = string1[3]

    tablica_prijelaza = [[0 for x in range(len(abeceda))] for y in range(len(sva_stanja))]

    for i in range(4,len(string1),1):
        pomocna_var = string1[i].split("->")
        st = pomocna_var[0].split(",")[0]
        sl = pomocna_var[0].split(",")[1]
        tablica_prijelaza[sva_stanja.index(st)][abeceda.index(sl)]=pomocna_var[1]




    brisi_nedohvatljiva()
    brisi_istovjetna()
    ispis()




