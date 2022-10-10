import Pyro4

def controleSaisie ():
    lettre = input('Entrez une lettre : ')
    while (len( lettre ) > 1 or ord(lettre) < 65 or ord(lettre) > 122):
        input('Entrez une lettre : ')
    return lettre.upper()

nameserver = Pyro4.locateNS()

server = Pyro4.Proxy("PYRONAME:tp.middleware")    # use name server object lookup uri shortcut


print('\nMot à deviner : ' + server.getAffichage)

nb_erreurs = 1

server.renitialize()

while '_' in server.getAffichage and nb_erreurs < 8:
    lettre = controleSaisie()
            
    # Appeler la fonction du serveur verifyIci
    sentence, nb_erreurs = server.verifyLetterIn(lettre, nb_erreurs)
    print(sentence)
    
if ("_" in server.getAffichage) :
    print("\nPerdu ! Vous avez ete pendu :D\nLe mot etait: " + server.getMot)
else:
    print("Felicitations !")