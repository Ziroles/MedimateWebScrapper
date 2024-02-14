import requests

import json
from tqdm import tqdm  # Importation de tqdm pour la barre de progression
from bs4 import BeautifulSoup
# Initialisation du dictionnaire au lieu de la liste
tab_dict = {}

# Liste des mots à ignorer (déterminants, prépositions, etc.)
mots_ignores = {".", ",", ":", ";", "(", ")", "[", "]", "«", "»", "<", ">", "/", "–", ""
                ,"1","2","4","5","6","7","8","9","0"," ","''","``","-"}

def gethtmlContent(url):
    response = requests.get(url)
    return response.text

def htmlParser(content):
    soup = BeautifulSoup(content, 'html.parser')
    res = ""
    for link in soup.find_all('p'):
        res += link.text + "\n"
    return res

def getContre_indications(content):
    if "4.3. Contre-indications" not in content:
        return ""
    return content.split("4.3. Contre-indications")[1].split("4.4")[0]

def main(code_cis):
    url = 'https://base-donnees-publique.medicaments.gouv.fr/affichageDoc.php?specid={}&typedoc=R'.format(code_cis)
    content = gethtmlContent(url)
    
    tab_dict[code_cis] = getContre_indications(htmlParser(content))


# Chargement des données
with open('medicines_flat.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

codes_cis = [obj["code_cis"] for obj in data]

# Ajout de tqdm autour de votre boucle pour afficher la barre de progression
for code in tqdm(codes_cis):
    main(code)

# Exportation du dictionnaire dans un fichier JSON
with open('sideEffect.json', 'w', encoding='utf-8') as f:
    json.dump(tab_dict, f, ensure_ascii=False, indent=4)

print("Exportation terminée. Le fichier 'sideEffect.json' contient les sides effects des médicaments.")

