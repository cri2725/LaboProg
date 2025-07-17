"""
import os
gwd=os.getcwd()
print("{}".format(gwd))

file = open("/home/cri2725/programmazione/LaboProg/CSVfiles/shampoo_sales.csv", "r")
print(file.readline())
file.close()
"""
"""
def contarighe(file):
    righe=0
    for riga in open(file):
        righe+=1
    return righe
file="LaboProg/CSVfiles/shampoo_sales.csv"
print("il file "+ file[30:] +" ha {} righe \n".format(contarighe(file)))
"""
"""
file=open("/home/cri2725/programmazione/LaboProg/CSVfiles/shampoo_sales.csv","r")
date=[]
sales=[]
for riga in file:
    rigapulita=riga.strip()
    elementi=rigapulita.split(",")
    if elementi[0]!="Date":
        date.append(elementi[0])
        sales.append(elementi[1])
print(f"le date sono: {date} \n")
print(f"gli elementi sono: {sales} \n")
"""
"""
def sumCSV(filepath):
    with open(filepath,"r") as fileCSV:
        valori=[]
        for riga in fileCSV:
            rigapulita=riga.strip()
            elementi=rigapulita.split(",")
            if elementi[0] != "Date": 
                valori.append(float(elementi[1]))
        return sum(valori)
file="/home/cri2725/programmazione/LaboProg/CSVfiles/shampoo_sales.csv"
print(f"la somma è {sumCSV(file)}")
"""
"""
1. Definire una funzione che prende in input un file ed una parola e conta quante volte
quella parola è presente sul file
"""
"""
def contaparole(fileconta, parola):
    contatore=0
    with open(fileconta, "r") as files:
        bob=files.read()
        elementi=bob.split()
        for elemento in elementi:
                if elemento == parola:
                    contatore+=1
    return contatore
parola="\n"
print(f"il num di volte che {parola} è stato usato è {contaparole("/home/cri2725/programmazione/LaboProg/CSVfiles/testoProva.txt", parola)}")
"""
        
"""
2. Definire una funzione che prende come input un file e conta quante volte ogni parola è
presente
"""
"""
def contpar(filepath):
    panum=[]
    with open(filepath, "r") as file:
        fileStringa=file.read()
        parole=fileStringa.split()
        for parola in parole:
            if parola not in panum:
                panum.append(parola)
                panum.append(1)
            else:
                for i,par in enumerate(panum):
                    if par==parola:
                        panum[i+1]+=1
    return panum
file="/home/cri2725/programmazione/LaboProg/CSVfiles/testoProva.txt"
print(f"{contpar(file)}")
"""
"""
3. Definire una funzione che prende in input un file e costruisce un dizionario con chiavi la
lettere iniziali e con valore le parole di lunghezza maggiore contenute nel file che
iniziano con quelle lettere.
"""
"""
def dizion(filepath):
    dizionario={}
    with open(filepath, "r") as file:
        fileStringa=file.read()
        parole=fileStringa.split()
        for parola in parole:
            if parola[0] not in dizionario:
                dizionario[parola[0]]=parola
            else:
                if len(parola)> len(dizionario[parola[0]]):
                    dizionario[parola[0]]=parola
    return dizionario
file="/home/cri2725/programmazione/LaboProg/CSVfiles/testoProva.txt"
print(f"il dizionario è {dizion(file)}")
"""
        
"""
4. Definire una funzione conteggio che prende come input un file e ritorna un dizionario
con chiave la prima parola di ogni frase e valore il numero di volte che una frase inizia
con quella parola. Considerare come inizio di frase qualsiasi parola che segue un
punto, un punto esclamativo, un punto interrogativo o si trova all'inizio del testo.
"""
"""
def conteggio(filepath):
    dizionario={}
    with open(filepath, "r") as file:
        parole=file.read().strip().lower().split()
        for parola in parole:
            if parola not in dizionario:
                dizionario[parola]=1
            else:
                dizionario[parola]+=1        
    return dizionario
file="/home/cri2725/programmazione/LaboProg/CSVfiles/testoProva.txt"
print(f"il dizionario è {conteggio(file)}")
"""
"""
5. Definire una funzione che prende come input un file, rimuove tutte le righe duplicate,
scrive il risultato in un nuovo file chiamato unique.txt
"""
"""
def rm(filepath):
    righeviste=[]
    with open(filepath, "r") as fileinput, open("/home/cri2725/programmazione/LaboProg/CSVfiles/unique.txt","w") as fileoutput:
        for riga in fileinput:
            rigaPulita=riga.strip()
            if rigaPulita not in righeviste:
                righeviste.append(rigaPulita)
                fileoutput.write(riga)
        return 0
fpath="/home/cri2725/programmazione/LaboProg/CSVfiles/testoProva.txt"
rm(fpath)
with open("/home/cri2725/programmazione/LaboProg/CSVfiles/unique.txt","r") as unico:

    stringa=unico.read()
    print(stringa)
"""