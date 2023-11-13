import requests
from bs4 import BeautifulSoup

#ecommerce websites
ebay = "https://www.ebay.com/"
amazon = "https://www.amazon.com/ref=nav_logo"
facebookMarketplace = "https://www.facebook.com/marketplace/"

#stocks websites
stocks = "https://finance.yahoo.com/"

#ecommerce vars
price = 0.0
shippingCost = 0.0
discounts = 0.0
shippingFrom = ""
shippingTime = ""

#stocks vars
price = 0.0
open = 0.0
pClose = 0.0
volume = 0.0
marketCap = 0.0 
beta = 0.0
PERatio = 0.0
EPS = 0.0

#open website, finds price, returns relevant data
def runPrices(website, item):	
	w = requests.get(website)
	soup = BeautifulSoup(w.content, 'html.parser')

	if(w.status_code == 200): #checks if website is up

		if(website == ebay): #ebay
			print ("ebay")
			s = soup.find('div', class_='entry-content') 
			

		if(website == amazon): #amazon
			print ("ama")

		if(website == facebookMarketplace): #facebook marketplace
			print ("fMarket")
	else:
		print("error - could not connect to website")

def runStock(item):
	print("stocks")

def saveToDisk(webType):
	print("save")

def writeToGui(webType):
	if(webType == "eccomerce"):
		return [price, shippingCost, discounts, shippingFrom, shippingCost]

	elif(webType == "stocks"):
		return [price, open, pClose, volume, marketCap, beta, PERatio, EPS]

	else:
		print("error - could not write to GUI")


runPrices(ebay, "h")	
