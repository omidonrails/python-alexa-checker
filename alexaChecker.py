#import requests
#import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

siteAddress = "hamyarwp.com"
submit_url = "https://www.alexa.com/siteinfo/" + siteAddress
uClient = uReq(submit_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


metrics = page_soup.findAll("section", {"id":"traffic-rank-content"})
#global_rank = metrics[0].find("span", {"class":"align-vmiddle change-wrapper change-up change-r2"})
country_rank = metrics[0].findAll("div", {"class":"rank-row"})

#print("global rank = " + global_rank.text)
print("country rank = " + country_rank)
