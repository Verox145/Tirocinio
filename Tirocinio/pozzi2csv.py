import json



def check_ndf(data):
    try:
        return float(data.replace(',','.'))
    except:
        return data
    
def check_ndi(data):
    try:
        return int(data)
    except:
        return data

def build_row(row,calls = -1):
    if calls > -1:
        print(calls)
    
    dati = json.loads(row)
    riga = [check_ndf(dati['longitudine']), #x
            check_ndf(dati['latitudine']), #y
            check_ndi(dati['Codice']), #Codice
            'Calabria', #regione
            dati['provincia'],
            dati['comune'],
            check_ndf(dati['profondita']),
            check_ndi(dati['anno']), #anno di realizzazione
            check_ndf(dati['pmax']), #portata massima
            check_ndf(dati['peserc']),
            check_ndi(dati['nfalde'])
            ]

        
    try:
        nfalde = 0
        
        if check_ndi(dati['nfalde']) != 0:
                    
            for fld in dati['falde']:
                riga.append(check_ndf(fld[1]))
                riga.append(check_ndf(fld[3]))
                nfalde += 1
                
        for i in range(3-nfalde):
            riga.append("ND")
            riga.append("ND")


        try:
            riga.append(check_ndf(dati['filtri'][0][1]))
            riga.append(check_ndf(dati['filtri'][0][2]))
        except:
            riga.append("ND")
            riga.append("ND")

        try:
            riga.append(check_ndf(dati['piezometrie'][0][1]))
            riga.append(check_ndf(dati['piezometrie'][0][2]))
        except:
            riga.append("ND")
            riga.append("ND")

        for st in dati['strato']:
            v1 = st[1].replace(',','.')
            v2 = st[2].replace(',','.')
            v3 = st[5]
            riga.append(v1+';'+v2+';'+v3)


        return riga
    except:
        print(row)




with open('dati_pozzi.txt') as f:
    rows = f.readlines()

with open('dati_pozzi.csv','w') as csvf:
    calls=0
    for row in rows:
        r=[str(elem) for elem in build_row(row,calls)]
        print(";".join(r),file=csvf)
        calls += 1
        
    



