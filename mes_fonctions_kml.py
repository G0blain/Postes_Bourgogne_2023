from enum import Enum

# Blocs de base utilisés dans le fichier KML
class Blocs_kml(Enum) :
    encodage = '<?xml version="1.0" encoding="UTF-8"?>\n'
    balise_kml_debut = '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    balise_kml_fin = '</kml>\n'
    balise_Document_debut = '  <Document>\n'
    balise_Document_fin = '  </Document>\n'


couleurs = ["ff646000" "ffd18802" "ff589d0f" "ffb73a67" "ff42b37c" "ff177781" "ff5b18c2" "ff0051e6" "ff007cf5" "ff2dc0fb"]

# Styles
class Styles_kml(Enum) :
    style1 = [
        "style1", 
        "ffd18802",
        "1",
        "https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png",
        "32",
        "64",
        "0",
    ]  

# Créer un style personnalisé
def recuperer_style(style_kml):
    style = '    <Style id="' + style_kml.value[0] + '">\n'
    style += '      <IconStyle>\n'
    style += '        <color>' + style_kml.value[1] + '</color>\n'
    style += '        <scale>' + style_kml.value[2] + '</scale>\n'
    style += '        <Icon>\n'
    style += '          <href>' + style_kml.value[3] + '</href>\n'
    style += '        </Icon>\n'
    style += '        <hotSpot x="' + style_kml.value[4] + '" xunits="pixels" y="' + style_kml.value[5] + '" yunits="insetPixels"/>\n'
    style += '      </IconStyle>\n'
    style += '      <LabelStyle>\n'
    style += '        <scale>' + style_kml.value[6] + '</scale>\n'
    style += '      </LabelStyle>\n'
    style += '    </Style>\n'
    return style


# Créer un point à partir d'une ligne du CSV et du style qu'on veut lui donner
def creer_point(ligne, style_id):
    point = '    <Placemark>\n'
    point += '      <name>' + ligne[1] + '</name>\n'
    point += '      <address>' + ligne[1] + ' ' + ligne[2]+ '</address>\n'
    point += '      <description> </description>\n'
    point += '      <styleUrl>#' + style_id + '</styleUrl>\n'
    point += '      <ExtendedData>\n'
    point += '        <Data name="Secteur">\n'
    point += '          <value>' + ligne[0] + '</value>\n'
    point += '        </Data>\n'
    point += '        <Data name="Ville">\n'
    point += '          <value>' + ligne[2] + '</value>\n'
    point += '        </Data>\n'
    point += '        <Data name="REP">\n'
    point += '          <value>' + ligne[3] + '</value>\n'
    point += '        </Data>\n'
    point += '        <Data name="Niveau">\n'
    point += '          <value>' + ligne[4] + '</value>\n'
    point += '        </Data>\n'
    point += '      </ExtendedData>\n'
    point += '    </Placemark>\n'
    return point


def creer_fichier_kml_sortie(nom_fichier_sortie, lignes):
    kml = Blocs_kml.encodage.value
    kml += Blocs_kml.balise_kml_debut.value
    kml += Blocs_kml.balise_Document_debut.value
    kml += recuperer_style(Styles_kml.style1)
    for ligne in lignes :
        kml += creer_point(ligne, Styles_kml.style1.value[0])
    kml += Blocs_kml.balise_Document_fin.value
    kml += Blocs_kml.balise_kml_fin.value
    with open(nom_fichier_sortie, "w", encoding="utf-8") as fichier:
        fichier.write(kml)



