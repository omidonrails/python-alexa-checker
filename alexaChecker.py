#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup as soup

siteAddress = sys.argv[1]
print("SiteName : " + siteAddress)
submit_url = "https://www.alexa.com/siteinfo/" + siteAddress
page = requests.get(submit_url)


page_content = soup(page.content , "lxml")

strong_tags = page_content.find_all("strong")
#country_name = page_content.find_all('div',
#             {'class': lambda x: x
#                       and 'dynamic-icon' in x.split()
#             }
#            )
#

global_rank = strong_tags[6].text
print("Global Rank : " + global_rank.strip())

country_rank = strong_tags[9].text
print("Country Rank : " + country_rank.strip())
