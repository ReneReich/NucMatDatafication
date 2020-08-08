import requests
import numpy as np
from bs4 import BeautifulSoup
from elsapy.elssearch import ElsSearch
from elsapy.elsclient import ElsClient


def get_DOI_from_Springer(query: str, api_key: str) -> list:
    springer_url = "http://api.springernature.com/metadata/pam"
    page_step = 50
    doi_list = []
    url = springer_url + f"?q={query}&s=1&p=1&api_key={api_key}"
    soup = BeautifulSoup(requests.get(url).text, "xml")
    total = soup.find("total").get_text()
    print("Total articles found: " + total)
    for page in list(np.arange(1, int(total), page_step)):
        url = springer_url + f"?q={query}&s={page}&p={page_step}&api_key={api_key}"
        soup = BeautifulSoup(requests.get(url).text, "xml")
        doi_list.extend([doi.get_text() for doi in soup.find_all("dc:identifier")])
    return doi_list


def get_DOI_from_Elsevier(query: str, api_key: str) -> list:
    config = {"apikey": api_key, "insttoken": ""}
    client = ElsClient(config['apikey'])
    client.inst_token = config['insttoken']
    doc_srch = ElsSearch(query, 'sciencedirect')
    doc_srch.execute(client, get_all=True)
    doi_list = []
    for element in doc_srch.results:
        doi_list.append(element.get('dc:identifier'))
    print("Total articles found: " + str(len(doi_list)))
    return doi_list


def download_XML(publisher: str, doi_list: list, dst_path: str, api_key: str):
    if not publisher == "Elsevier" or publisher == "Springer":
        return print("Please choose the publisher correctly: 'Elsevier' or 'Springer'")
    count = 0

    for doi in doi_list:
        file_path = doi.replace('/', '%')
        if publisher == "Elsevier":
            headers = {
                'Accept': 'application/xml',
                'X-ELS-APIKey': api_key
            }
            url = 'https://api.elsevier.com/content/article/doi/' + str(doi)
            r = requests.get(url, stream=True, headers=headers)
        else:
            springer_url = 'https://spdi.public.springernature.app/xmldata'
            r = requests.get(springer_url + f'/jats?q={doi}&api_key={api_key}')
        with open(dst_path + f'/{file_path}.xml', 'wb') as path:
            path.write(r.content)
        count += 1
        print(f"Downloaded: {count} of {len(doi_list)} XML files")