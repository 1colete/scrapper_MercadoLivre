# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
from difflib import SequenceMatcher
from selenium import webdriver
import time
from datetime import date

from requests_futures.sessions import FuturesSession

import re

# Creating a List 
List = [] 


def buscarDadosMercadoLivre(pages = 1):
    for x in range (0, pages):
        url = "https://lista.mercadolivre.com.br/chevrolet_Loja_chevrolet_NoIndex_True"
        if x ==0:
            print  ("primeira pagina")
            print (url)
        else:
            url = "https://lista.mercadolivre.com.br/chevrolet" + "_Desde_" + str((x*48+1)) +"_Loja_chevrolet_NoIndex_True"
            print (url)

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

        results = soup.findAll("section", {"class":"ui-search-results"})
        # print(results)
        
        try:
            itens = results[0].findAll("li", class_="ui-search-layout__item")
            #print (itens)
        except:
            print (" erro na busca da classe na url: " + url)
        
        for a in itens: 
            try:
                nome_produto = a.findAll("h2")[0].contents[0]
                preco_produto = a.findAll("span", class_="price-tag-fraction")[0].contents[0]
                preco_produto = float(preco_produto.replace(".",""))
                url_produto = a.findAll("a", class_="ui-search-link")[0]["href"]
                            
                # print (url_produto)
                
                # print (type(url_produto))
                
                List.append(url_produto)
                
            except:
                print ("erro de busca mercado livre")
        
        #print (List)
        
# def buscarProdutosMercadoLivre():
    
        

        
        
buscarDadosMercadoLivre()
print (List)