import json

with open('data/medicines_flat.json','r', encoding='utf-8') as f:
    data = json.load(f)

with open('resultats.json', 'r') as f:
    resultats = json.load(f)
    
cisfind = {}
cisnotfind = {}
for j in resultats.keys():
    check = False
    for i in data:
        if i["composition"]["substance_name"] != None:
            if j in i["name"] or j in j in i["composition"]["substance_name"]:
                cisfind[i["code_cis"]] = resultats[j]
                check = True
        else :
            if j in i["name"]:
                cisfind[i["code_cis"]] = resultats[j]
                check = True
    if check == False:
        cisnotfind[j] = resultats[j]

with open('cisnotfind.json', 'w') as f:
    json.dump(cisnotfind, f, ensure_ascii=False, indent=4)

with open('cisfind.json', 'w') as f:
    json.dump(cisfind, f, ensure_ascii=False, indent=4)