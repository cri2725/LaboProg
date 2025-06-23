"""
scrivete una funzione sum_list(my_list)
che sommi tutti gli elementi di una lista.

def sum_list(my_list):
    if my_list == []:
        return None
    somma= 0
    for item in my_list:
        somma+=item
    return somma
my_list=[3,2,1,2]
print("risultato della somma è: {} \n".format(sum_list(my_list)))
"""
"""
1. Stampare l'equivalente di 538 minuti nel formato 12h:32min
"""
"""
h=538//60
nuoviMin = 538%60
print("538 in orario normale {}h:{}min \n".format(h,nuoviMin))

2. Definire una funzione che prende come argomento una parola e una lettera. Ritorna quante volte
quella lettera è contenuta nella parola.
"""
"""
def parlet(parola, lettera):
    c=0
    if lettera not in parola:
        return 0
    else:
        for let in parola:
            if let==lettera:
                c+=1
    return c
parola=input("scrivi una parola \n")
lettera=input("scrivi una lettera \n")
print("la lettera {} è contenuta {} volte nella parola {}".format(lettera,parlet(parola,lettera),parola))
"""
"""
3. Scrivere una funzione che prende in input una stringa e ritorna True se è un palindromo, False
altrimenti.
"""
"""
def palindromo(parola):
    x=1
    for lettera in parola:
        if lettera == parola[-x]:
            x+=1
        else:
            return False
    return True      
parola = "uwu"
print("la parola {} è {}\n".format(parola, palindromo(parola)))
"""
"""
4. Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un
triangolo e se si di che tipo di triangolo
"""

"""
5. Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di A[i] con A[j].
"""

"""
6. Definite la funzione fattoriale
"""

"""
7. Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno almeno un
elemento in comune
"""

"""
8. Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una lista di
stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] ->["uno","zero","sette","nove","otto"]
"""