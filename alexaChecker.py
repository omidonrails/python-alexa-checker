import requests
#import bs4
from bs4 import BeautifulSoup as soup
import os

siteAddress = "hamyarwp.com"
submit_url = "https://www.alexa.com/siteinfo/" + siteAddress
page = requests.get(submit_url)


page_content = soup(page.content , "lxml")

strong_tags = page_content.findAll("strong")

global_rank = strong_tags[6].text
print("Global Rank : " + global_rank.strip())

country_rank = strong_tags[9].text
print("Country Rank : " + country_rank.strip())
