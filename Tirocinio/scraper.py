from bs4 import BeautifulSoup


def get_tab(t):
    elems = []
    rows = t.find_all('tr')
    for r in rows[1:]:
        f = tuple(str(ch).replace('<','').replace('>','').replace('td','').replace('/','') for ch in r.children if str(ch) != '\n')
        elems.append(f)
    return elems  

def scrape_info(page):
    soup = BeautifulSoup(page, 'html.parser')

    spans = soup.find_all('span')
    info = {}  
    for s in spans:
        ids = s.get_attribute_list('id')
        if ids[0] == 'ContentPlaceHolder1_codice':
            info['Codice'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_profondita':
            info['profondita'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_lon':
            info['longitudine'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_lat':
            info['latitudine'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_provincia':
            info['provincia'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_comune':
            info['comune'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_anno':
            info['anno'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_nfalde':
            info['nfalde'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_pmax':
            info['pmax'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_peserc':
            info['peserc'] = s.getText()
        if ids[0] == 'ContentPlaceHolder1_anno':
            info['anno'] = s.getText()



    tabs = soup.find_all('table')    

    for t in tabs:
        if t.has_attr('id'):
            id = t.get_attribute_list('id')[0]
            if id == 'ContentPlaceHolder1_falde':
                info['falde'] = get_tab(t)
                
            if id == 'ContentPlaceHolder1_filtri':
                info['filtri'] = get_tab(t)

            if id == 'ContentPlaceHolder1_piezo':
                info['piezometrie'] = get_tab(t)

            if id == 'ContentPlaceHolder1_strato':
                info['strato'] = get_tab(t)

    return info

if __name__=='__main__':
    f = open('test.html')
    page = f.read()
    f.close()
    info = scrape_info(page)
    print(info)
