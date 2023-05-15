import csv

# Retourne les en-têtes et les lignes du fichier CSV
def lire_fichier_csv(nom_fichier):
    with open(nom_fichier, 'r', newline='', encoding='utf-8') as csvfile:
        lecteur = csv.reader(csvfile)
        entetes = next(lecteur)  
        lignes = list(lecteur)
    return entetes, lignes


# Creer le fichier CSV de sortie (le résultat final)
def creer_fichier_csv_sortie(nom_fichier_sortie, entetes, lignes):
    with open(nom_fichier_sortie, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(entetes)
        writer.writerows(lignes)

