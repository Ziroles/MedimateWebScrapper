import json
from tqdm import tqdm

with open('data/medicinebymedicine.json', 'r') as f:
    medicine = json.load(f)

with open('interactionbymedicine.json', 'r') as f:
    interaction = json.load(f)


tab = {}
for i in tqdm(interaction.keys()):
    tab[i] = []
    for x in interaction[i]:
        for j in medicine.keys():
            if x in medicine[j] and j not in tab[i]:
                tab[i].append(j)

with open('medicinebyinteraction.json', 'w') as f:
    json.dump(tab, f, ensure_ascii=False, indent=4)
        