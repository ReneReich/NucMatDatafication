import os, re
import xml.etree.ElementTree as ET
import pandas as pd


def classify_file_by(directory_path: str, entities: dict):
    data_frame = []
    count = 0
    file_list = os.listdir(directory_path)
    for file in file_list:
        print(f"File now being classified: {file}")
        try:
            tree = ET.parse(os.path.join(src, file))
        except:
            continue
        root = tree.getroot()
        xml_string = str(ET.tostring(root, encoding='utf8', method='xml'))
        for expression in entities.values():
            if re.search(expression, xml_string) and file not in data_frame:
                data_frame.append(file)
                count += 1
                print(f"Entities found in {count} papers")
    df = pd.DataFrame(data_frame)
    df.to_excel("Files_classifications.xlsx")
    return print('Classifications exported to "Files_classifications.xlsx"')


src = "/directory full of XMLs/path/"
material_list = {
    '316SS':    'SS\s*[-]?\s*316|316\w*\s*[-]?\s*SS|316\w*\s*[-]?\s*(stainless)?\s*[-]?\s*steel|'
                '(stainless)?\s*[-]?\s*steel\s*[-]?\s*316|AISI\s*[-]?\s*\w*\s*[-]?\s*316',
    'HT9':      '(?:HT|Ht|ht)\s*[-]?\s*9',
    'Zr4':      '([Zz]ircal{1,2}oy|[Zz]r)\s*[-]?\s*4',
                 }
classify_file_by(src, material_list)
