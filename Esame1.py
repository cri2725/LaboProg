class ExamException(Exception):
    pass


class CSVTimeSeriesFile():
    
    def __init__(self, name):
        self.name=name
        
    def get_data(self):
        lista_anno_data=[]
        file = open(self.name,"r")
        next(file)
        for riga in file:
            valPerRiga=riga.strip().split(",")
            if valPerRiga[1]!="":
                numero=float(valPerRiga[1])
                if numero>0:
                    lista_anno_data.append([valPerRiga[0],numero])
        file.close()
        return lista_anno_data   
    
    
def compute_variations(time_series,first_year,last_year,N):
    lista_Anno_Mese_Valore=[]
    for elemento in time_series:
        elemento0str=str(elemento[0])
        anno=elemento0str.strip().split("/")[0]
        mese=elemento0str.strip().split("/")[1]
        annoint=int(anno)
        meseint=int(mese)
        lista_Anno_Mese_Valore.append([annoint,meseint,elemento[1]])
    print(lista_Anno_Mese_Valore)
    
    dizionario_anno_media={}
    for i,elemento in enumerate(lista_Anno_Mese_Valore):

        for i,elemento in enumerate(lista_Anno_Mese_Valore):
            sommaValori=0
            contatore=0
            if elemento[0] not in dizionario_anno_media.keys():
                dizionario_anno_media[elemento[0]]=0
            if i in range(len(lista_Anno_Mese_Valore)-1):
                sommaValori+=elemento[2]
                print(sommaValori)
                contatore+=1
                if elemento[0]<lista_Anno_Mese_Valore[i+1][0]:
                    continue
            dizionario_anno_media[elemento[0]]=sommaValori/contatore
            
    print(dizionario_anno_media)
            
if __name__ == "__main__":
    filepath="/home/cri2725/programmazione/LaboProg/CSVfiles/GlobalTemperatures.csv"
    file=CSVTimeSeriesFile(filepath)
    compute_variations(file.get_data(),34,34,3)
