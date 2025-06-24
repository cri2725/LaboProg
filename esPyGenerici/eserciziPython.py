"""
0. Scrivete una funzione sum_list(my_list)
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
def tri(a,b,c):
    if a+b<=c or a+c<=b or b+c<=a:
        return "no triangolo"
    elif a==b or a==c or b==c:
        return "triangolo isoscele"
    elif a**2+b**2==c**2 or c**2+b**2==a**2 or a**2+c**2==b**2:
        return "triangolo rettangolo"
    else:
        return "scaleno"
#lati
a,b,c=3,4,5
print("bob: {}".format(tri(a,b,c))) 
"""
"""
5. Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di A[i] con A[j].
"""
"""
def scambio(a,i,j):
    extra=a[i]
    a[i]=a[j]
    a[j]=extra
    return a
a=[1,2,3,4,5]
i=0
j=4
print("lista scambiata {}".format(scambio(a,i,j)))
"""
"""
6. Definite la funzione fattoriale
"""
"""
def factorial(a):
    tot=1
    while(a>0):
        tot*=a
        a-=1
    return tot
print("il fattoriale di 6 è {}".format(factorial(6)))
"""
"""
7. Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno almeno un
elemento in comun
"""
"""
def elemcom(a,b):
    for elemento in a:
        if elemento in b:
            return True
    return False
a=[1,2,3,4,"due"]
b=["bob","due"]
print("le liste sono {}".format(elemcom(a,b)))
"""
"""
8. Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una lista di
stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] ->["uno","zero","sette","nove","otto"]
"""
"""
def convertitore(a):
    b=[]
    dizionario={1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove"}
    for numero in a:
        b.append(dizionario[numero])
    return b
a=[1,2,4,5,6,2]
print("lista convertita = {}".format(convertitore(a)))
"""