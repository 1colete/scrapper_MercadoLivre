import requests
from bs4 import BeautifulSoup
import json
import re

otherList= [
    "https://produto.mercadolivre.com.br/MLB-1521639002-tapete-bandeja-porta-malas-nova-tracker-2021-original-gm-_JM?searchVariation=55732461089#searchVariation=55732461089&position=1&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17",
    "https://produto.mercadolivre.com.br/MLB-1205988099-aditivo-radiador-pronto-para-uso-acdelco-1-litro-laranja-_JM#position=2&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17",
    "https://produto.mercadolivre.com.br/MLB-1578913408-alavanca-de-freio-de-mo-cromada-s10-nova-gm-201220132014-_JM#position=3&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17",
    "https://produto.mercadolivre.com.br/MLB-1563289325-emblema-lt-tampa-traseira-tracker-original-gm-2021-_JM#position=4&type=item&tracking_id=8cb0a2db-c66e-4a58-9e9b-5f027b7e3e17"
]

# for x in otherList:
#   print(x)
url = "https://produto.mercadolivre.com.br/MLB-1597219305-emblema-lt-nova-tracker-2021-original-gm-_JM#reco_item_pos=0&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=0d3d6cb8-96e4-4142-bf63-f1840e3c7fc3"


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

#titulo e preço do produto
try:
    titulo = soup.title.contents[0]
    fraction = soup.findAll("span", class_="price-tag-fraction")[0].contents[0]
    cents = soup.findAll("span", class_="price-tag-cents")[0].contents[0]
    price = str("R$" + fraction + "," + cents)
except:
    titulo = "x"
    price = "x"

#quantidade disponivel e itens vendidos
try:
    qtdDisponivel = soup.findAll("span", class_="ui-pdp-buybox__quantity__available")[0].contents[0]
    qtdDisponivel = qtdDisponivel[1:-1]

    itensVendidos = soup.findAll("span", class_="ui-pdp-subtitle")[0].contents[0]
    itensVendidos = itensVendidos.split("|")[1]
except:
    itensVendidos = "x"
    qtdDisponivel = "x"

#vendedor
try:
    vendedor = soup.findAll("div", class_="ui-box-component ui-box-component-pdp__visible--desktop")[0]
 
    for link in vendedor.find_all('a'):
        if link is not None:
            vendedor = link['href']
except:
    vendedor = "x"

#caracteristicas do produto
try:
    caracteristicas = soup.findAll("", class_="specs-item specs-item-primary")[2]
    caracteristicas = re.findall("\d+", caracteristicas)
except:
    caracteristicas = "x"

print(titulo,  "\n",price, "\n", qtdDisponivel, "\n", itensVendidos, "\n", caracteristicas, "\n", vendedor)

""" json = {
    "titulo" : titulo,
    "preço": price,
    "itens vendidos": itensVendidos,
}
 """

# listaJson.append(json)