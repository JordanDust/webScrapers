from datetime import datetime, time
from webScraper import organizeVars

def saveToDisk(webType):
	if(webType == "ecommerce"):
		with open("eTextData.txt", "w") as file:
            file.write(f"{date.today()} - {date.now()}: {\n organizeVars("ecommerce")}")

	elif(webType == "stocks"):
		with open("sTextData.txt", "w") as file:
            file.write(f"{date.today()} - {date.now()}: {\n organizeVars("stocks")}")

	else:
		print("ERROR - printing to Disk")

def writeToGui(webType):
	if((webType == "ecommerce") or (webType == "stocks)):
        return organizeVars(webType)
    else:
        print("ERROR - could not write to GUI")