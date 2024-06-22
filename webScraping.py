import requests
#download the html for the page 

standings_url = "https://fbref.com/en/comps/676/2021/2021-European-Championship-Stats"
#this is the url link for the euros championship stats 

data = requests.get(standings_url)

data.text
#using print for this it will show the html for the page 

from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text)
#passing in our html data to the beautiful soup class 

standings_table = soup.select()

links = standings_table.find_all('a')
#Using findall instead of select, select using css selectors and find all only finds tags
#want to get the href property of each link
#The href attribute specifies the URL of the page the link goes to

#Make a list comprehension, remember from haskell
links = [l.get("href") for l in links]
#Now have the href for every links