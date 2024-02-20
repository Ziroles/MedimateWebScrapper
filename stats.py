import json

with open('data/medicinebymedicine.json', 'r') as f:
    medicine = json.load(f)


tab = {}


for i in medicine.keys():
    for j in medicine[i]:
        if j not in tab.keys():
            tab[j] = 0
        else:
            tab[j] += 1
tab = {k: v for k, v in sorted(tab.items(), key=lambda item: item[1], reverse=True)}
with open('medicinebycount.json', 'w') as f:
    json.dump(tab, f, ensure_ascii=False, indent=4)