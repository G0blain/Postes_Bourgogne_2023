from mes_enums import *

from lecture_ecriture_csv import *
from mes_fonctions_kml import *


# Ajoute une colonne pour indiquer si l'école est une REP, REP+ ou ni l'un ni l'autre
def ajouter_colonne_rep_csv(entetes, lignes):
    entetes.append("REP")  
    for ligne in lignes:
        nom_ecole = ligne[1]
        if "REP+" in nom_ecole:
            ligne.append("REP+")
        elif "REP" in nom_ecole:
            ligne.append("REP")
        else:
            ligne.append("")
    return entetes, lignes

# Completer les valeurs de la colonne Secteur à partir de l'Enum
def transformer_colonne_secteur_csv(lignes):
    for ligne in lignes:
        ligne[0] =  Secteur[ligne[0]].value
    return lignes

# Renvoie le niveau de la classe si il est indiqué dans le nom de l'école
def obtenir_niveau_ecole(nom_ecole):
    niveaux_possibles = [member.value for member in Niveaux]
    for niveau in niveaux_possibles:
        if niveau.lower() in nom_ecole.lower().replace("é", "e"):
            return niveau
    return ""

# Ajoute une colonne pour indiquer le niveau de la classe
def ajouter_colonne_niveau_csv(entetes, lignes):
    entetes.append("Niveau")  
    for ligne in lignes:
        ligne.append(obtenir_niveau_ecole(ligne[1]))
    return entetes, lignes




if __name__ == '__main__':
    # source
    fichier_csv = 'Inputs/brut.csv'
    # sortie
    nom_fichier_sortie = 'Outputs/Postes_Bourgogne'

    # lecture
    entetes, lignes = lire_fichier_csv(fichier_csv)
    # ajouter la mention de REP
    entetes, lignes = ajouter_colonne_rep_csv(entetes, lignes)
    # completer le secteur
    lignes = transformer_colonne_secteur_csv(lignes)
    # ajouter le niveau
    entetes, lignes = ajouter_colonne_niveau_csv(entetes, lignes)

    # Création du fichier CSV en sortie
    creer_fichier_csv_sortie(nom_fichier_sortie + '.csv', entetes, lignes)

    # Création du fichier KML en sortie
    creer_fichier_kml_sortie(nom_fichier_sortie+ '.kml', lignes)


