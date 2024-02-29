import fitz  # PyMuPDF
import json 
import re
from tqdm import tqdm
determinant = ["le","voie","population","légère" ,"et","la", "les", "l'", "un", "une", "des", "du", "de", "d'", "au", "aux", "à", "à", "en", "par", "pour", "avec", "sans", "sous", "sur", "vers", "dans", "depuis", "pendant", "après", "avant", "derrière", "devant", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf"]

with open ('data/medicines_flat.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('cisfind.json', 'r') as f:
    medicine = json.load(f)

res = {}
for i in tqdm(medicine.keys()):
    for j in medicine[i]:
        for x in data:
            if (x["composition"]["substance_name"] != None ):
                if j in x["composition"]["substance_name"] or j in x["name"]:
                    if i not in res:
                        res[i] = []
                    res[i].append(x["code_cis"])
                    
            elif j in x["name"]:
                if i not in res:
                    res[i] = []
                res[i].append( x["code_cis"])

with open('super.json', 'w') as f:
    json.dump(res, f, ensure_ascii=False, indent=4)