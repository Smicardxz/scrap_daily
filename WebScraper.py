import pandas as pd
import numpy as np
from googlesearch import search
import requests
from bs4 import BeautifulSoup


#----------------------------------------INPUT----------------------------

#------------------------DESACTIVATION POUR DEV ----------
#recherche = input("Saisissez votre sujet de recherche : ")
#filtre = [str(x) for x in input("saisissez le nonmbre de filtre: ").split()]
recherche = "Ecole"
filtre =["IA","Informatique"]


#-----------------------Recherche / DF et Chaine Filtre-------------------
result = search(recherche, lang="fr", num_results=25)    
dfurl = pd.DataFrame(data=result, columns=["URL"])
dfurl = dfurl.assign(**dict.fromkeys(filtre, 0))


#-----------------------Bs4 Scrape les liens extraits---------------------
def BS4Scraping(df):
    for links in dfurl["URL"]:
        html_text = requests.get(links).text
        soup = BeautifulSoup(html_text, 'html.parser')
        for keyword in filtre:
            if keyword in html_text:
                print(links, keyword)
            elif keyword not in html_text:
                print(links + " Pas de mot clés")
            else:
                break
            

print(BS4Scraping(dfurl))