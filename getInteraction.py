import requests

import json
from tqdm import tqdm  
from bs4 import BeautifulSoup

tab_dict = {}

def gethtmlContent(url):
    response = requests.get(url)
    return response.text

def htmlParser(content):
    soup = BeautifulSoup(content, 'html.parser')
    res = ""
    med = ""
    
    for link in soup.find_all('p'):
        res += link.text + "\n"
    
    return res


def getContre_indications(content):
    if "4.5. Interactions avec d'autres médicaments et autres formes d'interactions" not in content:
        return ""
    return content.split("4.5. Interactions avec d'autres médicaments et autres formes d'interactions")[1].split("4.6")[0]

def main(code_cis):
    url = 'https://base-donnees-publique.medicaments.gouv.fr/affichageDoc.php?specid={}&typedoc=R'.format(code_cis)
    content = gethtmlContent(url)
    
    tab_dict[code_cis] = getContre_indications(htmlParser(content))



with open('medicines_flat.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

codes_cis = [obj["code_cis"] for obj in data]


for code in tqdm(codes_cis):
    main(code)


with open('interaction.json', 'w', encoding='utf-8') as f:
    json.dump(tab_dict, f, ensure_ascii=False, indent=4)

print("Exportation terminée. Le fichier 'sideEffect.json' contient les sides effects des médicaments.")

