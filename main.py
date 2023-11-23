from datetime import datetime, time
from webScraper import getVars

def saveToDisk(webType):
	if(webType == "ecommerce"):
		with open("eTextData.txt", "w") as file:
            file.write(f"{date.today()} - {date.now()}: {\n getVars("ecommerce", "disk")}")
												
	elif(webType == "stocks"):
		with open("sTextData.txt", "w") as file:
            file.write(f"{date.today()} - {date.now()}: {\n organizeVars("stocks", "disk")}")

	else:
		print("ERROR - printing to Disk")

def writeToGui(webType):
	if((webType == "ecommerce") or (webType == "stocks)):
        return getVars(webType, "gui")
    else:
        print("ERROR - could not write to GUI")