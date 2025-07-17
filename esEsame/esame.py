def sum_csv(filepath):
    try:
        with open(filepath,"r") as fileCSV:
            valori=[]
            for riga in fileCSV:
                rigapulita=riga.strip()
                elementi=rigapulita.split(",")
                if elementi[0] != "Date": 
                    try:
                        valori.append(float(elementi[1]))
                    except ValueError:
                        print("non riesco a convertire in float")
            if valori==[]:
                return 0
            else:
                return sum(valori)
    except IOError:
        print("non riesco a leggere il file ")
file="/home/cri2725/programmazione/LaboProg/CSVfiles/shampoo_sales.csv"
print(f"la somma è {sum_csv(file)}")