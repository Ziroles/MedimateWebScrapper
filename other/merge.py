import json

with open('super.json', 'r', encoding='utf-8') as f:
    cis = json.load(f)

with open('sideEffect.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in data.keys():
    #print(i, i in data.keys())
    if i in cis.keys():
        data[i]['sideEffect'] = ','.join(str(nombre) for nombre in cis[i])  
        #print(data[i]['sideEffect'])
    else:
        data[i]['sideEffect'] = ""
        

with open('sideInfo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
