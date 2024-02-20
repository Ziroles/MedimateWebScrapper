import spacy
import json
from tqdm import tqdm
import re

bad_carac = ["(", ")", ":", ",", ";", ".", "!", "?", ]
determinant = ["le","voie","population","légère" ,"et","la", "les", "l'", "un", "une", "des", "du", "de", "d'", "au", "aux", "à", "à", "en", "par", "pour", "avec", "sans", "sous", "sur", "vers", "dans", "depuis", "pendant", "après", "avant", "derrière", "devant", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf"]
unite = ["mg", "g", "ml", "l", "mg/ml", "mg/l", "g/ml", "g/l","f","a"]

with open("./data/interaction.json", "r") as f:
    interaction = json.load(f)

with open("./data/medicinebymedicine.json", "r") as f:
    medicine_name = json.load(f)

bmedicine = []

for i in tqdm(medicine_name.keys()):
    for j in medicine_name[i]:
        if j not in bmedicine:
            bmedicine.append(j)

tab = {}

for i in tqdm(interaction.keys()):
    tab[i] = []
    word = str(interaction[i])
    word = word.replace("'", " ").replace("/", " ").replace("\n", " ")
    word = word.lower()
    tempo = word.split(" ")

    for j in tempo:
        
        if (str(j).isnumeric()) == False and j not in bad_carac and j not in determinant and j not in unite and j in bmedicine and j not in tab[i]:
            tab[i].append(j.lower())


        
    


with open ("interactionbymedicine.json", "w") as f:
    json.dump(tab, f, ensure_ascii=False, indent=4)