from enum import Enum

# Différents secteurs de Bourgogne
class Secteur(Enum):
    APPLI = "école d'application"
    DC = "Dijon Centre"
    AVS = "Auxonne Val de Saone"
    DE = "Dijon Est"
    BEA = "Beaune"
    DN = "Dijon Nord"
    CHA = "Chatillon"
    DO = "Dijon Ouest"
    CHE = "Chenove"
    DS = "Dijon Sud"
    SEM = "SOMBERNON"

# Différents niveaux que peuvent avoir les classes
class Niveaux(Enum) :
    primaire = "Primaire"
    elementaire = "Elementaire"
    maternelle = "Maternelle"
