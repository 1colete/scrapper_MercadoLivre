import requests
from bs4 import BeautifulSoup

"""
Se tiver mais que 1969 itens o mercado livre so vai exibir 42 paginas ou seja, so da pra iterar sobre isso
"""

def numeroPaginas():
    url = "https://lista.mercadolivre.com.br/chevrolet_Loja_chevrolet_NoIndex_True"

    print(url)

    path = "/chevrolet" + url.split("/chevrolet")[1]
    authority = "/chevrolet" + url.split("/chevrolet")[0]
    
    PARAMS = {
        "authority": authority,
        "method":"GET",
        "path": path,
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

    results = soup.findAll("aside", {"class":"ui-search-sidebar"})
    
    try:
        itens = results[0].findAll("span", class_="ui-search-search-result__quantity-results")[0].contents[0]
        text = list(itens.split(" "))[0]
        qtdResultados = float(text.replace(".",""))
        print (qtdResultados)
    except:
        print (" erro na busca da classe na url: " + url)       


numeroPaginas()