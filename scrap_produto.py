import requests
from bs4 import BeautifulSoup
import json
import re

thislist = ["apple", "banana", "cherry"]
otherList= [
    "https://produto.mercadolivre.com.br/MLB-1521639002-tapete-bandeja-porta-malas-nova-tracker-2021-original-gm-_JM?searchVariation=55732461089#searchVariation=55732461089&position=1&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17",
    "https://produto.mercadolivre.com.br/MLB-1205988099-aditivo-radiador-pronto-para-uso-acdelco-1-litro-laranja-_JM#position=2&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17",
    "https://produto.mercadolivre.com.br/MLB-1578913408-alavanca-de-freio-de-mo-cromada-s10-nova-gm-201220132014-_JM#position=3&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17",
    "https://produto.mercadolivre.com.br/MLB-1563289325-emblema-lt-tampa-traseira-tracker-original-gm-2021-_JM#position=4&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17"
]

# for x in otherList:
#   print(x)
url = "https://produto.mercadolivre.com.br/MLB-1563289325-emblema-lt-tampa-traseira-tracker-original-gm-2021-_JM#position=4&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17"


PARAMS = {
    "authority": url,
    "method":"GET",
    "path": url,
    "scheme":"https",
    "referer": url,
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"same-origin",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

page = requests.get(url= url, headers = PARAMS)
soup = BeautifulSoup(page.content, 'lxml')

print ()

titulo = soup.title.contents[0]

try:
    itensVendidos = soup.findAll("dl", class_="vip-title-info")[0].findAll("div",class_="item-conditions")[0].contents[0]
    itensVendidos = re.findall("\d+", itensVendidos)[0]
except:
    itensVendidos = ""

fraction = soup.findAll("span", class_="price-tag-fraction")[0].contents[0]
cents = soup.findAll("span", class_="price-tag-cents")[0].contents[0]
price = str("R$" + fraction + "," + cents)

try:
    qtdDisponivel = soup.findAll("span", class_="dropdown-quantity-available")[0].contents[0]
except:
    qtdDisponivel = ""
    
vendedor = soup.findAll("a", class_="reputation-view-more card-block-link")[0]["href"]

caracteristicas = soup.findAll("li", class_="specs-item specs-item-primary")[2]
caracteristicas = re.findall("\d+", caracteristicas)

print(caracteristicas)
