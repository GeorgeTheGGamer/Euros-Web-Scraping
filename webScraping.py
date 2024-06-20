import requests
#download the html for the page 

standings_url = "https://fbref.com/en/comps/676/2021/2021-European-Championship-Stats"
#this is the url link for the euros championship stats 

data = requests.get(standings_url)

data.text
#using print for this it will show the html for the page 

from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text)
