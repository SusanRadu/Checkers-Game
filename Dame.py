import time
import sys
from copy import copy, deepcopy

ADANCIME_MAX = 6

def jucator_opus(jucator):#functie care returneaza opusul jucatorului
    if jucator == 'n':
        return 'a'
    return 'n'

def matrice_inv(matrice):#functie care intoarece o matrice cu susul in jos
    for i in range(4):
        for j in range(8):
            aux = matrice[i+1][j+1]
            matrice[i+1][j+1] = matrice[8-i][j+1]
            matrice[8-i][j+1]= aux
    return matrice

class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    JMIN = None
    JMAX = None
    GOL = '#'

    def __init__(self, tabla=None):
        if tabla is not None:
            self.matr = tabla
        else:
            self.matr = [['0','1','2','3','4','5','6','7','8','0'],
                         ['1','#','a','#','a','#','a','#','a','0'],
                         ['2','a','#','a','#','a','#','a','#','0'],
                         ['3','#','a','#','a','#','a','#','a','0'],
                         ['4','#','#','#','#','#','#','#','#','0'],
                         ['5','#','#','#','#','#','#','#','#','0'],
                         ['6','n','#','n','#','n','#','n','#','0'],
                         ['7','#','n','#','n','#','n','#','n','0'],
                         ['8','n','#','n','#','n','#','n','#','0'],
                         ['0','0','0','0','0','0','0','0','0','0']]

    def mutari(self, jucator):
        l_mutari = []
        j_opus = jucator_opus(jucator)
        if jucator == 'a':#daca jucatorul este cel alb, rasturnam tabla
            self.matr=matrice_inv(self.matr)
        for i in range(9):#parcurgem toata tabla
            for j in range(9):
                if self.matr[i][j]!='0':#daca sunt pe tabla
                    if self.matr[i][j] == jucator:#daca avem o dama pe i j
                        if self.matr[i-1][j+1] == '#':# daca este un spatiu liber pe diagonala dreapta
                            if i-1 == 1:#daca a ajuns la capat
                                matr_tabla_noua = deepcopy(self.matr)#facem o copie la tabla curenta
                                matr_tabla_noua[i - 1][j + 1] = jucator.capitalize()#facem dama rege, si o mutam
                                matr_tabla_noua[i][j] = '#'#lasam spatiu gol de unde era dama
                                if jucator == 'a':#daca jucatorul este cel alb, rasturnam tabla (o aducem la pozitia initiala)
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))#adaugam configuratia curenta a tablei la lista de mutari posibile
                            else:#daca nu a ajuns la capat
                                matr_tabla_noua = deepcopy(self.matr)
                                matr_tabla_noua[i - 1][j + 1] = jucator
                                matr_tabla_noua[i][j] = '#'
                                if jucator == 'a':
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))

                        if self.matr[i-1][j-1] == '#':#daca este un spatiu liber pe diagonala stanga
                            if i-1 == 1:
                                matr_tabla_noua = deepcopy(self.matr)
                                matr_tabla_noua[i - 1][j - 1] = jucator.capitalize()
                                matr_tabla_noua[i][j] = '#'
                                if jucator == 'a':
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))
                            else:
                                matr_tabla_noua = deepcopy(self.matr)
                                matr_tabla_noua[i - 1][j - 1] = jucator
                                matr_tabla_noua[i][j] = '#'
                                if jucator == 'a':
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))

                        if self.matr[i-1][j+1] == j_opus or self.matr[i-1][j+1] == j_opus.capitalize():#daca este o dama adversa pe diagonala din dreapta
                             if i-2 == 1:
                                if self.matr[i - 2][j + 2] == '#':#daca este un loc liber dupa dama
                                     matr_tabla_noua = deepcopy(self.matr)
                                     matr_tabla_noua[i - 2][j + 2] = jucator.capitalize()
                                     matr_tabla_noua[i][j] = '#'
                                     matr_tabla_noua[i - 1][j + 1] = '#'
                                     if jucator == 'a':
                                         matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                     l_mutari.append(Joc(matr_tabla_noua))
                             else:
                                if self.matr[i - 2][j + 2] == '#':
                                     matr_tabla_noua = deepcopy(self.matr)
                                     matr_tabla_noua[i - 2][j + 2] = jucator
                                     matr_tabla_noua[i][j] = '#'
                                     matr_tabla_noua[i - 1][j + 1] = '#'
                                     if jucator == 'a':
                                         matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                     l_mutari.append(Joc(matr_tabla_noua))

                        if self.matr[i-1][j-1] == j_opus or self.matr[i-1][j-1] == j_opus.capitalize():#daca este o dama adversa pe diagonala din stanga

                            if i-2 == 1:
                                if self.matr[i - 2][j - 2] == '#':
                                    matr_tabla_noua = deepcopy(self.matr)
                                    matr_tabla_noua[i - 2][j - 2] = jucator.capitalize()
                                    matr_tabla_noua[i][j] = '#'
                                    matr_tabla_noua[i - 1][j - 1] = '#'
                                    if jucator == 'a':
                                        matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                    l_mutari.append(Joc(matr_tabla_noua))
                            else:
                                if self.matr[i - 2][j - 2] == '#':
                                    matr_tabla_noua = deepcopy(self.matr)
                                    matr_tabla_noua[i - 2][j - 2] = jucator
                                    matr_tabla_noua[i][j] = '#'
                                    matr_tabla_noua[i - 1][j - 1] = '#'
                                    if jucator == 'a':
                                        matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                    l_mutari.append(Joc(matr_tabla_noua))

                    elif self.matr[i][j]==(jucator.capitalize()):#daca avem un rege
                        if self.matr[i-1][j+1] == '#':# daca este un spatiu liber pe diagonala dreapta
                            matr_tabla_noua = deepcopy(self.matr)#facem o copie la tabla curenta
                            matr_tabla_noua[i - 1][j + 1] = jucator.capitalize()#facem dama rege, si o mutam
                            matr_tabla_noua[i][j] = '#'#lasam spatiu gol de unde era dama
                            if jucator == 'a':#daca jucatorul este cel alb, rasturnam tabla (o aducem la pozitia initiala)
                                matr_tabla_noua = matrice_inv(matr_tabla_noua)
                            l_mutari.append(Joc(matr_tabla_noua))#adaugam configuratia curenta a tablei la lista de mutari posibile

                        if self.matr[i-1][j-1] == '#':#daca este un spatiu liber pe diagonala stanga
                            matr_tabla_noua = deepcopy(self.matr)
                            matr_tabla_noua[i - 1][j - 1] = jucator.capitalize()
                            matr_tabla_noua[i][j] = '#'
                            if jucator == 'a':
                                matr_tabla_noua = matrice_inv(matr_tabla_noua)
                            l_mutari.append(Joc(matr_tabla_noua))

                        if self.matr[i-1][j+1] == j_opus or self.matr[i-1][j+1] == j_opus.capitalize():#daca este o dama adversa pe diagonala din dreapta
                            if self.matr[i - 2][j + 2] == '#':#daca este un loc liber dupa dama
                                matr_tabla_noua = deepcopy(self.matr)
                                matr_tabla_noua[i - 2][j + 2] = jucator.capitalize()
                                matr_tabla_noua[i][j] = '#'
                                matr_tabla_noua[i - 1][j + 1] = '#'
                                if jucator == 'a':
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))

                        if self.matr[i-1][j-1] == j_opus or self.matr[i-1][j-1] == j_opus.capitalize():#daca este o dama adversa pe diagonala din stanga
                            if self.matr[i - 2][j - 2] == '#':
                                matr_tabla_noua = deepcopy(self.matr)
                                matr_tabla_noua[i - 2][j - 2] = jucator.capitalize()
                                matr_tabla_noua[i][j] = '#'
                                matr_tabla_noua[i - 1][j - 1] = '#'
                                if jucator == 'a':
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))

                        if self.matr[i+1][j-1] == '#':# daca este un spatiu liber pe diagonala stanga in spate
                            matr_tabla_noua = deepcopy(self.matr)
                            matr_tabla_noua[i + 1][j - 1] = jucator.capitalize()
                            matr_tabla_noua[i][j] = '#'
                            if jucator == 'a':
                                matr_tabla_noua = matrice_inv(matr_tabla_noua)
                            l_mutari.append(Joc(matr_tabla_noua))
                        if self.matr[i+1][j+1] == '#':# daca este un spatiu liber pe diagonala dreapta in spate
                            matr_tabla_noua = deepcopy(self.matr)
                            matr_tabla_noua[i + 1][j + 1] = jucator.capitalize()
                            matr_tabla_noua[i][j] = '#'
                            if jucator == 'a':
                                matr_tabla_noua = matrice_inv(matr_tabla_noua)
                            l_mutari.append(Joc(matr_tabla_noua))
                        if self.matr[i+1][j-1] == j_opus or self.matr[i+1][j-1] == j_opus.capitalize():#daca e o dama opusa in spate stanga
                            if self.matr[i + 2][j - 2] == '#':
                                matr_tabla_noua = deepcopy(self.matr)
                                matr_tabla_noua[i + 2][j - 2] = jucator.capitalize()
                                matr_tabla_noua[i][j] = '#'
                                matr_tabla_noua[i + 1][j - 1] = '#'
                                if jucator == 'a':
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))
                        if self.matr[i+1][j+1] == j_opus or self.matr[i+1][j+1] == j_opus.capitalize():#daca e o dama opusa in spate dreapta
                            if self.matr[i + 2][j + 2] == '#':
                                matr_tabla_noua = deepcopy(self.matr)
                                matr_tabla_noua[i + 2][j + 2] = jucator.capitalize()
                                matr_tabla_noua[i][j] = '#'
                                matr_tabla_noua[i + 1][j + 1] = '#'
                                if jucator == 'a':
                                    matr_tabla_noua = matrice_inv(matr_tabla_noua)
                                l_mutari.append(Joc(matr_tabla_noua))

        if jucator == 'a':
            self.matr=matrice_inv(self.matr)
        return l_mutari

    def final(self):
        a = 0
        n = 0
        for i in range(10):
            for j in range(10):
                if self.matr[i][j] == 'a':
                    a=a+1
                if self.matr[i][j] == 'n':
                    n=n+1
        if n==0 or not(self.mutari('n')):
            return 'a'
        if a==0 or not(self.mutari('a')):
            return 'n'

        return 0

    def estimeaza_scor(self):  # estimeaza scorul in functie de numarul de dame de pe tabla
        scor = 0
        for i in range(10):
            for j in range(10):
                if self.matr[i][j] == self.JMIN:
                    scor = scor + 1
                if self.matr[i][j] == self.JMIN.capitalize():
                    scor = scor + 3

                if self.matr[i][j] == self.JMAX:
                    scor = scor - 1
                if self.matr[i][j] == self.JMAX.capitalize():
                    scor = scor - 3

        return scor

    """
        def estimeaza_scor1(self):#estimeaza scorul in functie de numarul de dame de pe tabla
            scor = 0
            for i in range(10):
                for j in range(10):
                    if self.matr[i][j] == self.JMAX or self.matr[i][j] == self.JMAX.capitalize():
                        scor=scor+1
                    if self.matr[i][j] == self.JMAX or self.matr[i][j] == self.JMAX.capitalize():
                        scor=scor-1

            return scor
    """


    def __str__(self):#afisare
        sir = (" ".join([str(x) for x in self.matr[0][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[1][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[2][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[3][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[4][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[5][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[6][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[7][0:9]]) + "\n" +
               " ".join([str(x) for x in self.matr[8][0:9]]) + "\n"
               )

        return sir

class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
    """

    def __init__(self, tabla_joc, j_curent, adancime, scor=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari(self):
        l_mutari = self.tabla_joc.mutari(self.j_curent)
        juc_opus = self.jucator_opus()
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):#afisare
        sir = str(self.tabla_joc) + "(Juc curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor()
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor()
        return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if (alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:

            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if (beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if final!= 0:
        if final == "a":
            print("Au castigat albele ")
        else:
            print("Au castigat negrele ")

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    # initializare jucatori
    raspuns_valid = False

    print("Nivel de dificultate?")
    print("1.Incepator")
    print("2.Mediu")
    print("3.Avansat")
    x = int(input())
    if x == 1:
        ADANCIME_MAX = 2
    elif x == 2:
        ADANCIME_MAX = 4
    elif x == 3:
        ADANCIME_MAX = 6

    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu albe sau cu negre? ").lower()
        if (Joc.JMIN in ['a', 'n']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie a sau n.")
    Joc.JMAX = 'a' if Joc.JMIN == 'n' else 'n'

    # initializare tabla
    tabla_curenta = Joc();

    print("Tabla initiala")
    if Joc.JMIN == 'a':
        matrice_inv(tabla_curenta.matr)
    print(str(tabla_curenta))
    if Joc.JMIN == 'a':
        matrice_inv(tabla_curenta.matr)

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'n', ADANCIME_MAX)

    while True:

        if stare_curenta.j_curent == Joc.JMIN:#mutare jucator
            start_time = time.time()
            if Joc.JMIN == 'a':
                matrice_inv(stare_curenta.tabla_joc.matr)
            print("Tura Jucator")
            print("Ce piesa doriti sa mutati?")
            print("Randul?")
            choice = input()
            if(choice.upper() == "EXIT"):
                print("scorul este:")
                print(stare_curenta.tabla_joc.estimeaza_scor())
                break
            else: x = int(choice)
            print("Coloana?")
            choice = input()

            if (choice.upper() == "EXIT"):
                print("scorul este:")
                print(stare_curenta.tabla_joc.estimeaza_scor())
                break
            else:
                y = int(choice)


            if stare_curenta.tabla_joc.matr[x][y] == Joc.JMIN:

                print("Unde doriti sa o mutati?")
                print("Stanga sau Dreapta?")

                choice = input()
                if choice.upper() == "STANGA":
                    x1 = x - 1
                    y1 = y - 1
                elif choice.upper() == "DREAPTA":
                    x1 = x - 1
                    y1 = y + 1
                elif choice.upper() == "EXIT":
                    print("scorul este:")
                    print(stare_curenta.tabla_joc.estimeaza_scor())
                    break
                else:
                    if Joc.JMIN == 'a':
                        matrice_inv(stare_curenta.tabla_joc.matr)
                    continue


                if stare_curenta.tabla_joc.matr[x1][y1] == '#':

                    if x1 == 1:
                        stare_curenta.tabla_joc.matr[x1][y1] = Joc.JMIN.capitalize()
                    else:
                        stare_curenta.tabla_joc.matr[x1][y1] = Joc.JMIN

                    stare_curenta.tabla_joc.matr[x][y] = '#'

                    print("\nTabla dupa mutarea jucatorului")
                    print(str(stare_curenta))

                    if (afis_daca_final(stare_curenta)):
                        break
                     # S-a realizat o mutare. Schimb jucatorul cu cel opus
                    if Joc.JMIN == 'a':
                        matrice_inv(stare_curenta.tabla_joc.matr)
                    print("Jucatorul s-a gandit:")
                    print("--- %s seconds ---" % (time.time() - start_time))
                    stare_curenta.j_curent = stare_curenta.jucator_opus()

                elif stare_curenta.tabla_joc.matr[x1][y1] == jucator_opus(Joc.JMIN):
                    x2 = x1 - x
                    y2 = y1 - y
                    if stare_curenta.tabla_joc.matr[x1+x2][y1+y2] == '#':
                        if x1+x2 == 1:
                            stare_curenta.tabla_joc.matr[x1+x2][y1+y2] = Joc.JMIN.capitalize()
                        else:
                            stare_curenta.tabla_joc.matr[x1+x2][y1+y2] = Joc.JMIN
                        stare_curenta.tabla_joc.matr[x1+x2][y1+y2] = Joc.JMIN
                        stare_curenta.tabla_joc.matr[x1][y1] = '#'
                        stare_curenta.tabla_joc.matr[x][y] = '#'

                        print("\nTabla dupa mutarea jucatorului")
                        print(str(stare_curenta))

                        if (afis_daca_final(stare_curenta)):
                            break
                        # S-a realizat o mutare. Schimb jucatorul cu cel opus
                        if Joc.JMIN == 'a':
                            matrice_inv(stare_curenta.tabla_joc.matr)
                        print("Jucatorul s-a gandit:")
                        print("--- %s seconds ---" % (time.time() - start_time))
                        stare_curenta.j_curent = stare_curenta.jucator_opus()

            elif stare_curenta.tabla_joc.matr[x][y] == Joc.JMIN.capitalize():
                print("Unde doriti sa o mutati?")

                print("Sus sau jos?")
                choice = input()
                if choice.upper() == "SUS":
                    print("Stanga sau dreapta?")

                    choice = input()
                    if choice.upper() == "STANGA":
                        x1 = x - 1
                        y1 = y - 1
                    elif choice.upper() == "DREAPTA":
                        x1 = x - 1
                        y1 = y + 1
                    elif choice.upper() == "EXIT":
                        print("scorul este:")
                        print(stare_curenta.tabla_joc.estimeaza_scor())
                        break;
                    else:
                        if Joc.JMIN == 'a':
                            matrice_inv(stare_curenta.tabla_joc.matr)
                        continue
                elif choice.upper() == "JOS":
                    print("Stanga sau Dreapta?")

                    choice = input()
                    if choice.upper() == "STANGA":
                        x1 = x + 1
                        y1 = y - 1
                    elif choice.upper() == "DREAPTA":
                        x1 = x + 1
                        y1 = y + 1
                    elif choice.upper() == "EXIT":
                        print("scorul este:")
                        print(stare_curenta.tabla_joc.estimeaza_scor())
                        break
                    else:
                        if Joc.JMIN == 'a':
                            matrice_inv(stare_curenta.tabla_joc.matr)
                        continue
                elif choice.upper() == "EXIT":
                    print("scorul este:")
                    print(stare_curenta.tabla_joc.estimeaza_scor())
                    break
                else:
                    if Joc.JMIN == 'a':
                        matrice_inv(stare_curenta.tabla_joc.matr)
                    continue



                if stare_curenta.tabla_joc.matr[x1][y1] == '#':

                    stare_curenta.tabla_joc.matr[x1][y1] = Joc.JMIN.capitalize()
                    stare_curenta.tabla_joc.matr[x][y] = '#'

                    print("\nTabla dupa mutarea jucatorului")
                    print(str(stare_curenta))

                    if (afis_daca_final(stare_curenta)):
                        break
                    # S-a realizat o mutare. Schimb jucatorul cu cel opus
                    if Joc.JMIN == 'a':
                        matrice_inv(stare_curenta.tabla_joc.matr)
                    print("Jucatorul s-a gandit:")
                    print("--- %s seconds ---" % (time.time() - start_time))
                    stare_curenta.j_curent = stare_curenta.jucator_opus()

                elif stare_curenta.tabla_joc.matr[x1][y1] == jucator_opus(Joc.JMIN):
                    x2 = x1 - x
                    y2 = y1 - y
                    if stare_curenta.tabla_joc.matr[x1 + x2][y1 + y2] == '#':
                        stare_curenta.tabla_joc.matr[x1 + x2][y1 + y2] = Joc.JMIN.capitalize()
                        stare_curenta.tabla_joc.matr[x1][y1] = '#'
                        stare_curenta.tabla_joc.matr[x][y] = '#'

                        print("\nTabla dupa mutarea jucatorului")
                        print(str(stare_curenta))

                        if (afis_daca_final(stare_curenta)):
                            break
                        # S-a realizat o mutare. Schimb jucatorul cu cel opus
                        if Joc.JMIN == 'a':
                            matrice_inv(stare_curenta.tabla_joc.matr)
                        print("Jucatorul s-a gandit:")
                        print("--- %s seconds ---" % (time.time() - start_time))
                        stare_curenta.j_curent = stare_curenta.jucator_opus()
            else: continue

        # mutare calculator
        else:
            start_time = time.time()
            print("Tura Calculator")
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            if Joc.JMIN == 'a':
                matrice_inv(stare_curenta.tabla_joc.matr)
            print(str(stare_curenta))
            if Joc.JMIN == 'a':
                matrice_inv(stare_curenta.tabla_joc.matr)
            print("Calculator s-a gandit:")
            print("--- %s seconds ---" % (time.time() - start_time))


            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

if __name__ == "__main__":
    main()