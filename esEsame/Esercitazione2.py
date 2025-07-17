"""
class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name
    def get_data(self):
        lista=[]
        with open(self.name,"r") as file:
            next(file)
            for riga in file:
                riga_corretta=riga.strip().split(",")
                try:
                    if riga_corretta[1]== "":
                        continue
                    riga_corretta[1]=int(riga_corretta[1])
                except Exception:
                    raise ExamException("errore2")
                lista.append(riga_corretta)
        return lista
def compute_variations(time_series, first_year, last_year):
    dizionario={}
    
    medie = [0]
    time_series_singole=[]
    for i, _ in enumerate(time_series):
        time_series[i][0]=time_series[i][0][0:4]
        time_series[i][0]=int(time_series[i][0])
    print(time_series)
    for i, elemento in enumerate(time_series):
        data=elemento[0]
        tmp=0   
        contatore=0
        for elemento in time_series:
            if elemento[0] == data:
                tmp+=elemento[1]
                contatore+=1
        if medie[-1]!=tmp/contatore:
            medie.append(tmp/contatore)
    anni=sorted(list(set(elemento[0] for elemento in time_series)))
filepath="/home/cri2725/programmazione/LaboProg/CSVfiles/data.csv"
fileCSV=CSVTimeSeriesFile(filepath)
print(fileCSV.get_data())
compute_variations(fileCSV.get_data(), 1949,1952)
"""           