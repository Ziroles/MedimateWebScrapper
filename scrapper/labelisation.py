import json
from tqdm import tqdm

with open('../data/sideEffect.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


classifier =["Enfant","enceintes","enceinte","allaitement","nouveau-né","nourrisson","allaité"]

allergie = ["blé","tiaprofénique","AINS", "acide acétylsalicylique","constituant","anesthésiques","cromoglicate de sodium","naproxène","sodique", "soja", "céphalosporines","salicylés","chlorhexidine"
            "ibuprofène","antihistaminiques","Astéracées","dhuile darachide","photosensibilité","céthexonium","arachine","carboplatine","céfuroxime","lysozyme","excipients","macrolides","foins","urticaire","un des composants","aspirine","anti-inflammatoires non stéroïdiens","hexamidine","tétracyclines",
            "angiœdème","angio-dème","rhinite aiguë","diclofénac","paracétamol","maïs","fénofibrate","kétoprofène","piroxicam","fibrates","atopiques","lactose","formotérol","furosémide","sulfonamides","sulfamides","viande rouge","abats","escargots","tropomyosine","prostaglandines","héparines","héparinoïdes"
            "ammoniums","indométacine","lévocétirizine","cétirizine","hydroxyzine","pipérazine","sulfamides","chélates","mupirocine","polyéthylène","glycol","macrogol","niflumique","morniflumate",
            "thrombocytes","flurbiprofène","phénoxyméthylpénicilline","pénicillines","théophylline","méfénamique","benzocaïne","atropine","ipratropium","oxitropium"
            "tiotropium","formaldéhyde","néomycine","gentamicine","protamine","chlorhydrate","amide","sulfite","salbutamol","monohydraté","cobalamines","parahydroxybenzoates","parabens","méthylparaben","propylparaben","butylparaben","éthylparaben","isobutylparaben","isopropylparaben"
            ]


tab  ={}

for obj in tqdm(data.keys()):
    
    tab[obj] = {"Warning":[e for e in data[obj].split(" ") if e in classifier],"Allergie":[e for e in data[obj].split(" ") if e in allergie],"Content":data[obj].replace("  \n","")}
    
print(tab)
with open("../data/tab.json", 'w') as file:
    json.dump(tab, file, ensure_ascii=False, indent=4)


