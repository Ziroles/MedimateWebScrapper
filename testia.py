import spacy
import json

nlp = spacy.load("fr_core_news_sm")

with open('interaction.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

tab = []
for i in data.keys():
    texte = data[i]
    doc = nlp(texte)


    mots_a_garder = [token.text for token in doc if not token.is_stop and token.pos_ not in ["DET", "PUNCT", "ADP", "AUX", "CONJ", "CCONJ", "SCONJ", "INTJ", "PRON", "PROPN", "VERB", "ADJ", "ADV", "NOUN"]]


    tab.append(mots_a_garder)

print(tab)
