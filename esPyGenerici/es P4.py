def sum_list(lista):
    totale = 0
    for i in range(len(lista)):
        totale += lista[i]
    return totale
numeri=[]
qnum=int(input("quanti numeri? "))
for i in range(qnum):
    numeri.append(int(input("numero al posto {} ".format(i+1))))
print("la somma è {} ".format(sum_list(numeri)))

    
