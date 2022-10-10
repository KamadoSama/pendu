import Pyro4
import unidecode
from random import choice

# un mot au hasard
# def word():
#     f = open('mots.txt', 'r' , encoding = 'utf8')
#     contenu = f.readlines()
#     return unidecode.unidecode( choice(contenu) ).upper().replace('\n','')
mot = input("Entrer le mot: ")

# remplacement par des underscores
def underscore(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]
    
    
@Pyro4.expose
class MyServer(object):
    
    lettres_deja_proposees = []
    @Pyro4.expose
    @property
    def getLettre(self):
        return self.lettres_deja_proposees


    mot_a_deviner = ""
    affichage = ""
    def __init__(self):
        # self.mot_a_deviner = word()
        self.mot_a_deviner = mot.upper()
        self.affichage = underscore( self.mot_a_deviner )
        self.lettres_deja_proposees = []

    def renitialize (self):
        self.affichage = underscore( self.mot_a_deviner )
        self.lettres_deja_proposees = []

    @Pyro4.expose
    @property
    def getMot(self):
        return self.mot_a_deviner

    @Pyro4.expose
    @property
    def getAffichage(self):
        return self.affichage
    
    def verifyLetterIn(self, letter, nb_erreurs):        
        if letter not in self.lettres_deja_proposees and letter in self.mot_a_deviner:
            self.lettres_deja_proposees += [ letter ]
            nb_erreurs = 3
        
        elif letter not in self.mot_a_deviner:
            nb_erreurs -= 1
                
        self.affichage = underscore( self.mot_a_deviner , self.lettres_deja_proposees )
        sentence = f'\nMot à deviner : {self.affichage } il vous reste: {nb_erreurs} tentative(s)'
        return sentence, nb_erreurs
        

daemon = Pyro4.Daemon(host="0.0.0.0",port=5051)                # make a Pyro daemon, precise your ip adress here
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(MyServer())   # register the greeting maker as a Pyro object
ns.register("tp.middleware", uri)   # register the object with a name in the name server

print("Ready.")
print(uri)
daemon.requestLoop()        