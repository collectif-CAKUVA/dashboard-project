import requests
import re
from bs4 import BeautifulSoup

# url = 'https://www.pmu.fr/turf/10022021/R1/C1'
url2 = 'https://www.turf-fr.com/courses-pmu/pronostics/presse/r1-prix-de-grasse-229363'
response = requests.get(url2)
soup = BeautifulSoup(response.text, 'html.parser')

#arrivée
#arrivées = soup.select('strong')
#for e in arrivées :
#    print(e)

def scrap_pronos_journaux():
    pronos = soup.find_all("data", id="valeur")
    journaux = soup.find_all("data",{"class":"pull-left balise_h4"}, id="nom")

    list = [{ 'magasine':b.text.strip(),'prono':a.text.strip()} for a,b in zip(pronos, journaux)]
    print(list)

scrap_pronos_journaux()