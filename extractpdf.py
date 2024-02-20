import fitz  # PyMuPDF
import json 
import re
determinant = ["le","voie","population","doses",'dose',"","légère","l","puissants","ou","+" ,"ii","iii","non","oraux","et","la", "les", "l'", "un", "une", "des", "du", "de", "d'", "au", "aux", "à", "à", "en", "par", "pour", "avec", "sans", "sous", "sur", "vers", "dans", "depuis", "pendant", "après", "avant", "derrière", "devant", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf", "chez", "contre", "dans", "en", "entre", "jusque", "hors", "hormis", "malgré", "sauf"]

    

def extraire_elements_dict(pdf_path):
    doc = fitz.open(pdf_path)
    resultats = {}
    
    taille_10_courant = None
    
    for page in doc:
        blocs = page.get_text("dict")["blocks"]
        
        for bloc in blocs:
            # Vérifier si le bloc contient des lignes de texte
            
            if "lines" in bloc.keys():
                    for line in bloc["lines"]:
                        for span in line["spans"]:
                            
                            if span["size"] == 10.000425338745117:  # Récupération des titres
                                
                                taille_10_courant = span["text"]
                                
                                if taille_10_courant not in resultats:
                                    resultats[taille_10_courant] = []
                            elif span["size"] == 8.000325202941895 and taille_10_courant is not None and span["text"] != "+" and span["text"] not in determinant: #Récupération des sous titres
                                tempo = span["text"]
                                
                               
                                if str(tempo).isnumeric() == False:
                                    tempo = tempo.replace("(", " ").replace(")", " ").replace(":", " ").replace(",", " ").replace(";", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace("[", " ").replace("]", " ").replace("'"," ").replace("/"," ")
                                    tempo = tempo.split(" ")
                                    if len(tempo) > 1 :

                                        for i in tempo:
                                            if i not in resultats[taille_10_courant] and i.lower() not in determinant and i != "":
                                                resultats[taille_10_courant].append(i)
                                    else:
                                        if tempo[0] not in resultats[taille_10_courant] and tempo[0].lower() not in determinant and tempo[0] != "" :
                                            resultats[taille_10_courant].append(tempo[0])
                                   
                                
                                
    
    doc.close()
    return resultats



# Utiliser la fonction
pdf_path = "20230915-thesaurus-interactions-medicamenteuses-septembre-2023.pdf"
resultats = extraire_elements_dict(pdf_path)
print("---------- Fin extraction éléments pdf ----------")
with open ("resultats.json", "w") as f:
    json.dump(resultats, f, indent=4)

print("---------- Fin écriture fichier json ----------")