

# remplacement par des underscores

def underscore(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]

# saisie d'une lettre

def saisie():
    lettre = input('Entrez une lettre : ')
    if len( lettre ) > 1:
        return saisie()
    else:
        return lettre.upper()
    

# programme principal

"""lettres_deja_proposees = []
mot_a_deviner = mot
affichage = underscore( mot_a_deviner )
print( 'Mot à deviner : ' , affichage )
nb_erreurs = 3

while '_' in affichage and nb_erreurs >0:
    lettre = saisie()
    if lettre not in lettres_deja_proposees and lettre in mot_a_deviner:
        print(f'{lettres_deja_proposees}')
        lettres_deja_proposees += [ lettre ]
        nb_erreurs = 3
        
    elif lettre not in mot_a_deviner:
        nb_erreurs -= 1
            
    affichage = underscore( mot_a_deviner , lettres_deja_proposees )
    print( f'\nMot à deviner : {affichage } Nombre d\'erreurs restant: {nb_erreurs}' )"""