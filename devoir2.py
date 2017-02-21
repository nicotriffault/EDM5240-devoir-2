#coding: utf-8

# script python3, devoir2

# longTitre = longueur du titre de chaque thèse ou mémoire.
# type = à partir de la colonne thesis_degree_name, s'il s'agit d'une maîtrise ou d'un doctorat.
# nbPages = nombre de pages total de chaque thèse ou mémoire à partir des information contenues dans la colonnes pages_aacr.

# titre = ligne 2
# nbre de page  = ligne 5
# type de thèses = ligne 6

import csv

fichier = "concordia1.csv"
f = open(fichier)

lignes = csv.reader(f)
next(lignes)

# Pour calculer le nbre total de pages incluant les pages exprimées en chiffres romains, il faudrait que je fasse un dictionnaire définissant les équivalences avec les chiffres arabes puis que j'additionne. Je ne l'ai pas fait. 

d = {
     "i" : "1",
     "ii" : "2",
     "iii": "3",
     "iv" : "4",
     "v" : "5",
     "vi" : "6",
     "vii" : "7",
     "viii" : "8",
     "ix" : "9",
     "x" : "10",
     }

for ligne in lignes:
    
    longTitre = (len(ligne[2]) +1)
  
    titre = ligne[2]
    
    nom = (ligne[1] + ligne[0])
    
    nbPages = ligne(5)
    
    if "Theses" in ligne(6):
      type = "La thèse"
    else:
      type = "Le mémoire"
    
        
# formatage final
print("{} de {} compte {} pages. Son titre est {} ({} caratères).".format(type,nom,nbPages,titre,longTitre))
