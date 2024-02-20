import spacy
import json
from tqdm import tqdm
import re

def clean(texte):
    
    regex = re.compile(r'\\u([0-9a-fA-F]{4})')   
    def remplacer(match):
        return chr(int(match.group(1), 16))
    
    return regex.sub(remplacer, texte)


#generic_group generic_group_name le premier
#name split si besoin pas oublié le /
#composition substance_name

medicine_name = []


def contient_sequence_unicode(texte):
    # Expression régulière pour détecter des séquences d'échappement Unicode (\u suivi de 4 chiffres hexadécimaux)
    motif_unicode = re.compile(r'\\u[0-9a-fA-F]{4}')

    # Rechercher le motif dans la chaîne
    if motif_unicode.search(texte):
        return True
    else:
        return False

bymedicine = {}

with open('data/medicines_flat.json','r', encoding='utf-8') as f:
    data = json.load(f)


for i in tqdm(data):
        bymedicine[i["code_cis"]] = []
        tempo = clean(i["name"])
    
        
        if "/" in tempo:
            tempo = tempo.replace("'", " ")
            
            
            tempo = tempo.replace(" /", "/")
            tempo = tempo.replace("/ ", "/")
            tempo = tempo.replace("/", " ")
            tempo = tempo.replace("(", " ")
            tempo = tempo.split(" ")
            
            for j in range(len(tempo[:2])):
                if str(j).isnumeric() ==False:
                    bymedicine[i["code_cis"]].append(tempo[j].lower())

        else:
            bymedicine[i["code_cis"]].append(tempo.lower())


        
        if i["composition"]["substance_name"] != None:
        
            if contient_sequence_unicode(i["composition"]["substance_name"]):

                tempo = clean(i["composition"]["substance_name"])
            else :
                tempo = i["composition"]["substance_name"]
            tempo = tempo.replace("/", " ")
            tempo = tempo.replace("'", " ")
            tempo = tempo.replace("(", " ")
            tempo = tempo.split(" ")
            if (len(tempo) > 1):
                for j in tempo:
                    if j not in bymedicine[i["code_cis"]]:
                        bymedicine[i["code_cis"]].append(j.lower())
                        
            else:
                if tempo not in bymedicine[i["code_cis"]]:
                    bymedicine[i["code_cis"]].append(tempo[0].lower())
                          
        

        if i["generic_group"]["generic_group_name"] != None:
        
            tempo = clean(i["generic_group"]["generic_group_name"])
            tempo = tempo.replace("/", "")
            tempo = tempo.replace("'", " ")
            tempo = tempo.replace("(", " ")
            tempo = tempo.split(" ")[0]
            

            if j not in bymedicine[i["code_cis"]]:
                bymedicine[i["code_cis"]].append(tempo.lower())
                
bad_carac = ["(", ")", ":", ",", ";", ".", "!", "?","-" ]
determinant = ["le","de)","base","d","sulfate","calcium","extraitextrait","humaine","carbone","sec","alfa","rein","bleu","forme","respiratoire","actif","ayant","jaune","rouge","fièvre","forme","ayant","acide","préparations","jus","actif","contenant","humains","vitamine","","voie","population","légère" ,"et","la", "les", "l'", "un", "une", "des", "du", "de", "d'", "au", "aux", "à", "à", "en", "par", "pour", "avec", "sans", "sous", "sur", "vers", "dans", "depuis", "pendant", "après", "avant", "derrière", "devant", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf"]
unite = ["mg", "g", "ml","k", "y","iii","ii","l", "mg/ml", "mg/l", "g/ml", "g/l","f","a","b"]


for i in tqdm(bymedicine.keys()):
    for j in range(len(bymedicine[i])):
        if bymedicine[i][j] in bad_carac or bymedicine[i][j] in determinant or bymedicine[i][j] in unite:
            bymedicine[i][j] = ""
    bymedicine[i]= list(filter(None, bymedicine[i]))
    


    

with open ("data/medicinebymedicine.json", "w") as f:
    json.dump(bymedicine, f, indent=4, ensure_ascii=False)   