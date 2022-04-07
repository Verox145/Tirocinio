from urllib.request import urlopen
from scraper import *
from time import sleep

f = open('Perforazioni.csv')
raw = f.readlines()
f.close()    

pozzi = []
nline = 1

for line in raw[1:]:
    ls = line.split(',')
    url = ls[5]
    page = urlopen(url)
    info = scrape_info(page)
    pozzi.append(info)
    print("%.2f %%"%(100*nline/len(raw)))
    nline += 1
    sleep(0.2)

with open('dati_pozzi.txt','w') as f:
    for p in pozzi:
        print(p,file=f)
        
