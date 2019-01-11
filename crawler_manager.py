import urllib
import requests
from bs4 import BeautifulSoup
import json

url = "https://studio.uipath.com"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

print(soup)




#def main():
