import requests
#import bs4
from bs4 import BeautifulSoup as soup

siteAddress = "hamyarwp.com"
submit_url = "https://www.alexa.com/siteinfo/" + siteAddress
page = requests.get(submit_url)
