# -*- coding: utf-8 -*-

# récupération de l'entré utilisateur
valeur = raw_input('Saisissez un chiffre :')

# on change le typage de la variable en chiffre entier
valeur = int(valeur)

# on calcule le carré de la valeur et on le stocke dans une variable
carre = valeur * valeur

# on affiche le carré de la valeur saisie
print("Le carré de %s est %s" % (valeur, carre))
