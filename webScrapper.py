import requests
from bs4 import BeautifulSoup
from datetime import time

#ecommerce websites
ebay = "https://www.ebay.com/"
amazon = "https://www.amazon.com/ref=nav_logo"
facebookMarketplace = "https://www.facebook.com/marketplace/"

#stocks websites
stocks = "finviz.com"

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
	nStocks = (f"{stocks}quote.ashx?t={item}&p=d")
	r = requests.get(nStocks)

	if(r.status_code == 200):
		soup = BeautifulSoup(r.content, 'html5lib')
		table = soup.find_all()

		#for row in table.find_all('kv__item'):
		#	open = row.h5.text
		
		print(table)


	else:
		print("ERROR - could not connect to website")	


#organizes the variables based on website type and puts them in a pretty format for saveToDisk function
def organizeVars(webType):
	if(webType == "ecommerce"):
			return (f"{price}, {shippingCost}, {discounts}, {shippingFrom}, {shippingTime}")

	elif(webType == "stocks"):
			return (f"{price}, {open}, {pClose}, {volume}, {marketCap}, {beta}, {PERatio}, {EPS}")

def saveToDisk(webType):
	if(webType == "ecommerce"):
		with open("eTextData.txt", "w") as file:
			file.write(date.today() + "\n" + organizeVars("ecommerce"))

	elif(webType == "stocks"):
		with open("sTextData.txt", "w") as file:
			file.write(date.today() + "\n" + organizeVars("stocks"))

	else:
		print("ERROR - printing to Disk")

def writeToGui(webType):
	if(webType == "ecommerce"):
		return [price, shippingCost, discounts, shippingFrom, shippingTime]

	elif(webType == "stocks"):
		return [price, open, pClose, volume, marketCap, beta, PERatio, EPS]

	else:
		print("error - could not write to GUI")

runStock("AMZN")