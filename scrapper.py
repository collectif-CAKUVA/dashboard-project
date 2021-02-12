import requests
import re
from bs4 import BeautifulSoup

# url = 'https://www.pmu.fr/turf/10022021/R1/C1'
url2 = 'https://www.zeturf.fr/fr/programmes-et-pronostics'
response = requests.get(url2)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
