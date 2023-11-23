import requests
from bs4 import BeautifulSoup
from datetime import time

#ecommerce vars
ePrice = 0.0
shippingCost = 0.0
discounts = 0.0
shippingFrom = ""
shippingTime = ""
	
#stock vars
sPrice = 0.0
open = 0.0
pClose = 0.0
volume = 0.0
marketCap = 0.0 
beta = 0.0
PERatio = 0.0
EPS = 0.0

#open website, finds price, returns relevant data
def runPrices(website, item):
	#ecommerce websites
	ebay = "https://www.ebay.com/"
	amazon = "https://www.amazon.com/ref=nav_logo"
	facebookMarketplace = "https://www.facebook.com/marketplace/"

	r = requests.get(website)
	soup = BeautifulSoup(r.content, 'html.parser')

	if(r.status_code == 200): #checks if website is up

		if(website == ebay): #ebay
			print ("ebay")
			s = soup.find('div', class_='entry-content') 
			

		if(website == amazon): #amazon
			print ("ama")

		if(website == facebookMarketplace): #facebook marketplace
			print ("fMarket")
	else:
		print("ERROR - could not connect to website")

def runStock(item):
	stocks = (f"https://www.marketwatch.com/investing/stock/{item}?mod=search_symbol") #stock website
	r = requests.get(stocks) #gets HTML of website

	if(r.status_code == 200): #checks if website is up
		soup = BeautifulSoup(r.content, 'html5lib')
		
		priceElement = soup.find('div', {'class': 'intraday__data'})
		betaElement = soup.find('li', {'class': 'list__item', 'data-template': 'quotes/overview'})
		pCloseElement = soup.find('li', {'class': 'list__item', 'data-template': 'quotes/overview'})

		if betaElement:
			betaTag = betaElement.find('span', {'class': 'primary'})
			if betaTag:
				beta = betaTag.text.strip()

		print(beta)
		sPrice = priceElement.text.strip() if priceElement else 0.0
	
	else:
		print("ERROR - could not connect to website")	


#organizes the variables based on website type and puts them in a pretty format for saveToDisk function
def organizeVars(webType):
	if(webType == "ecommerce"):
			return (f"{price}, {shippingCost}, {discounts}, {shippingFrom}, {shippingTime}")

	elif(webType == "stocks"):
			return (f"{price}, {open}, {pClose}, {volume}, {marketCap}, {beta}, {PERatio}, {EPS}")

print(runStock("AMZN"))