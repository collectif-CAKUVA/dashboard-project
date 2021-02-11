import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.pmu.fr/turf/10022021/R1/C1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
