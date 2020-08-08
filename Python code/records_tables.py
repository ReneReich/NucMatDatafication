import re, os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def find_entities_in_tables(dirctory_path: str, file_list, entities: dict):
    data_frame = []
    columns= ['DOI', 'Tab_nr', 'Tab_text'] + [key for key in entities.keys()]
    count = 0
    for file_name in file_list:
        with open(os.path.join(dirctory_path, file_name)) as file:
            soup = BeautifulSoup(file)
        tables = []
        tables.extend(soup.find_all("table-wrap"))
        tables.extend(soup.find_all("ce:table"))
        doi = file_name.replace('%', '/').replace('.xml', '')
        print(f'File now being searched: {doi}')
        for table in tables:
            instance = [doi]
            try:
                instance.append(table.find("ce:label").getText())
            except:
                try:
                    instance.append(table.find("label").getText())
                except:
                    instance.append(np.NaN)
            try:
                instance.append(table.find("ce:simple-para").getText())
            except:
                try:
                    instance.append(table.find("p").getText())
                except:
                    instance.append(np.NaN)
            table_string = str(table.text)
            for expression in expressions.values():
                instance.append(len(re.findall(expression, table_string)))
            data_frame.append(instance)
        count += 1
        print(f'file {count} of {len(file_list)} processed')
    df = pd.DataFrame(data_frame, columns=columns)
    df.to_excel("Entities_in_tables_v3_1.xlsx")


file_list = pd.read_excel("Papers_containing_alloys.xlsx")
src = "/Users/Rene/Dropbox/Master Thesis/Paper Population"
expressions = {
    '316SS':    'SS\s*[-]?\s*316|316\w*\s*[-]?\s*SS|316\w*\s*[-]?\s*(stainless)?\s*[-]?\s*steel|(stainless)?\s*[-]?\s*steel\s*[-]?\s*316|AISI\s*[-]?\s*\w*\s*[-]?\s*316',
    'HT9':      '(?:HT|Ht|ht)\s*[-]?\s*9',
    'Zr4':      '([Zz]ircal{1,2}oy|[Zz]r)\s*[-]?\s*4',
    'Dose':     '\b[Dd]ose\b|\bdpa\b|\bDPA\b|n\/cm\^*(<sup loc="post">)*2|[Nn]*(eutron)*\s*[-]?\s*([Ff]luence|[Ff]lux)|[Ff]luence|[Ff]lux',
    'Temp':     '[Tt]emperature|[Tt]emp\.*|°C|°F|\bT\b|\bK\b',
    'YS':       '[Yy]ield[–]?\s*[-]?\s*[Ss](?:trength|tress)|\bYS\b',
    'UTS':      '(?:[Uu]ltimate\s*[-]?\s*(?:[Tt]ensile)*|[Tt]ensile)\s*[-]?\s*[Ss](?:trength|tress)|\bUTS\b|\bTS\b',
    'HV':       '[Hh]ardness|[Hh]ardening|\bHV\b|\bHRC?\b',
    'UE':       '[Uu]niform\s*[-]?\s*(?:[Pp]lastic)?\s*[-]?\s*(?:[Ee]longation|[Ss]train)|\bUE\b',
    'TE':       '(?:[Tt]otal|[Uu]ltimate)\s*[-]?\s*(?:[Pp]lastic)?\s*[-]?\s*(?:[Ee]longation|[Ss]train)|(?:[Ee]longation|[Ss]train)\s*[-]?\s*at\s*[-]?\s*(?:[Bb]reak|[Ff]racture)|\bTE\b',
    'F_tough':  '[Ff]racture\s*[-]?\s*[Tt]oughness|[Jj]\s*[-]?\s*[Ii]ntegral|k?J\/m\^*(<sup loc="post">)*2|MPa\s?.?\s?m\^*(<sup loc="post">)*1\/2|[Ff]racture',
    'Embrit':   '(?:[Dd]uctile\s*[-]?\s*[Bb]rittle)?\s*[-]?\s*[Tt]ransition\s*[-]?\s*(?:[Tt]emperature|[Tt]emp\.*|\bΔT\b|\bTT\b)|(?:[Uu]pper\s*[-]?\s*[Ss]helf\s*[-]?\s*[Ee]nergy|USE)\s*[-]?\s*[Ss]hift|\bΔ?USE\b|[Ee]mbrittlement|[Ii]mpact\s*[-]?\s*[Tt]est|Charpy',
    'Creep':    '[Cc]reep\s*[-]?\s*(?:[Rr]ate|[Ss]train|[Cc]ompliance)|[Tt]ensile\s*[-]?\s*[Ss]train|[Ss]train\s*[-]?\s*[Rr]ate|[Cc]reep',
    'Swelling': '[Ss]welling\s*[-]?\s*[Rr]ate|[Ss]welling'
}
find_entities_in_tables(src, file_list.values, expressions)