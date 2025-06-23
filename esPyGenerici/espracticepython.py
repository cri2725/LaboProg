"""
ex1:
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
-----------------------------------------------------------------------------------------------------------
nome = input( "scrivi il tuo nome: ")
età = input( "scrivi la tua età: ")
età = int(età)
print("{}, arriverai a 100 anni nel {}.".format(nome, 2025+100- età ))


ex2:
Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message to the user. 
Extras:
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
-----------------------------------------------------------------------------------------------------------
numero = input(" dimmi un numero e ti dico se è even o odd: ")
numero = int(numero)
if(numero % 4 == 0): 
    print("{} è even e multiplo di 4 ".format(numero))
elif(numero % 2 == 0): 
    print("{} è even ".format(numero))
else:
    print("{} è odd ".format(numero))
print("ora dammi 2 num e ti dico se uno e divisibile per l'altro: ")
dividendo= int(input("dividendo: "))
divisore= int(input("divisore: "))
if(dividendo%divisore==0):
    print("{} è divisibile per {}".format(dividendo,divisore))
else:
    print("{} non è divisibile per {}".format(dividendo,divisore))
    
    
ex3:
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
    Instead of printing the elements one by one, make a new list that has all the elements less than 5
    from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a 
    that are smaller than that number given by the user.
-----------------------------------------------------------------------------------------------------------
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num=int(input("dimmi un numero e ti printo i numeri della lista minori di quello dato: "))
print([numero for numero in a if numero < num])


ex4:
Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number. 
-----------------------------------------------------------------------------------------------------------
num=int(input("dimmi il num e ti dico i divisori: "))
print([div for div in range(1,num+1) if (num%div==0)])


ex5:
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
Extras:
    Randomly generate two lists to test this
    Write this in one line of Python
-----------------------------------------------------------------------------------------------------------
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(set([elem for elem in a if(elem in b)])))
c= []
for elem in a:
    if(elem in b and elem not in c):
        c.append(elem)
print(c)


ex6:
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
-----------------------------------------------------------------------------------------------------------
stringa=input("passa una stringa e ti dico se è palindromo: ")
stringainversa=stringa[::-1]
if(stringainversa==stringa):
    print("{} è palindromo ".format(stringa))
else:
    print("{} non è palindormo".format(stringa))
    

ex7:
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
-----------------------------------------------------------------------------------------------------------
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x for x in a if x%2==0])


ex8:
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
-----------------------------------------------------------------------------------------------------------
stop=False
sceltevalide=["sasso","carta","forbice"]
while(stop==False):
    while(True):
        inpgioc1= input("giocatore 1, carta, forbice o sasso? ")
        if(inpgioc1 not in sceltevalide):
            print("non valido ")
        else:
            break
    while(True):
        inpgioc2= input("giocatore 2, carta, forbice o sasso? ")
        if(inpgioc2 not in sceltevalide):
            print("non valido ")
        else:
            break
    if (inpgioc1==inpgioc2):
        print("pareggio ")
    elif((inpgioc1=="carta" and inpgioc2=="sasso")or(inpgioc1=="forbice" and inpgioc2=="carta")or(inpgioc1=="sasso" and inpgioc2=="forbice")):
        print("giocatore1, hai vinto! ")
    else:
        print("giocatore2 hai vinto! ")
    sn=input("volete rifare? (si/no): ")
    if(sn== "no"):
        stop=True
    else:
        continue


ex9:
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
-----------------------------------------------------------------------------------------------------------
import random
exit=False
print("Scegli un numero tra 1 e 9 (compresi), vediamo se lo becchi \nPer uscire dal gioco scrivi exit ")
rnum=random.randint(1,9) 
i=0
ttot=0
esat=0
while(exit==False):
    i+=1
    ttot+=1
    risp=int(input("num: "))
    if(risp==rnum):
        esat+=1
        print("hai vinto!! \nIl num di volte che hai provato ad indovinare il numero è stato {} volte ".format(i))
        sn=input("Vuoi giocare ancora?(si/no): ")
        if(sn=="no"):
            print("tot dei numeri indovinati: \n{}".format(esat))
            print("tentativi totali: \n{}".format(ttot))
            exit=True
        else:
            i=0
            rnum=random.randint(1,9)  
            continue
    elif(risp>rnum):
        print("troppo grande ")
    else:
        print("troppo piccolo")


#ex10:
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.

def lista(lista):
    nl=[lista[0], lista[-1]]
    return nl
a = [5, 10, 15, 20, 25]
print(lista(a))


ex13:
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Make sure to ask the user to enter the number of numbers in the sequence to generate 

def fibo(n):
    seq=[1,1]
    f0=1
    f1=1
    ftot=0
    for i in range(1,n-1):
        ftot=f0+f1
        f0=f1
        f1=ftot
        seq.append(ftot)
    return seq
print(fibo(int(input("dimmi un n e ti dico i primi n numeri di fibonacci "))))


ex14
Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random
# 50 parole a caso
ListaDiParole = [
    "casa", "pane", "sole", "luna", "mare", "mano", "piede", "naso", "bocca", "dito",  
    "testa", "cuore", "libro", "gatto", "cane", "mese", "anno", "giorno", "notte", "fiore",
    "erba", "vento", "fuoco", "acqua", "vino", "cibo", "sera", "porta", "strada", "idea", 
    "vita", "luce", "cosa", "modo", "fine", "forza", "tempo", "mondo", "parte", "senso",
    "fare", "dire", "dare", "vede", "sente", "parla", "bello", "bravo", "bene", "male" 
]
def PasswordGenerator(sic, ListaDiParole):
    password=""
    if(sic=="debole"):
        parola=(random.choice(ListaDiParole))
        caratteriParola=list(parola)
        nvolte=random.randint(1,3)
        for i in range(nvolte):
            puntorandom=random.randint(0,len(caratteriParola))
            numeroran=str(random.randint(0,9))         
            caratteriParola.insert(puntorandom,numeroran)
        password="".join(caratteriParola)
        return password
    else:
        parola=(random.choice(ListaDiParole))
        caratteriParola=list(parola)
        nvolte=random.randint(1,3)
        for i in range(0,nvolte):
            puntorandom=random.randint(0,len(caratteriParola))
            caratteriParola[puntorandom]=caratteriParola
        
while(True):
    SicPass=input("\nsicurezza Password:\n(debole/sicura): \n")
    if(SicPass!= ("debole" or "sicura")):
        print("non valido, rimettere.. ")
    else:
        break
print("La password è {}".format(PasswordGenerator(SicPass,ListaDiParole)))
