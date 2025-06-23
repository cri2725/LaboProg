class persona:
    def __init__ (self,nome,cognome,anni):
        self.nome=nome
        self.cognome=cognome
        self.anni=anni
    def presentazione(self):
        print("sono {} {} ed ho {} anni",self.nome,self.cognome,self.anni)
class studente(persona):
    def __init__(self,nome,cognome,anni,corsi):
        super().__init__(nome,cognome,anni)
        self.corsi=corsi
        self.n=len(corsi)
    def presentazione(self):
        persona.presentazione(self)
        for i in self.corsi:
            print("partecipo al corso: {}",self.corsi[i])

