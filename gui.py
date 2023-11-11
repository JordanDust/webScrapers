from tkinter import *
from webScrapper import *

m = Tk() #creates window
tracker = 0 #keeps track of whether eccomerce or stocks

#moves stock input out of range, moves eccomerce inputs in place, sets tracker
def selE():
    sInputL.place_configure(relx = 1, rely = 1)
    sInput.place_configure(relx = 1, rely = 1)

    eInputL.place(relx = 0.2, rely = 0.1)
    eInput.place(relx = 0.5, rely = 0.1)

    tracker = 1

#moves eccomerce input out of range, moves stock inputs in place, sets tracker
def selS():
    eInputL.place_configure(relx = 1, rely = 1)
    eInput.place_configure(relx = 1, rely = 1)

    sInputL.place(relx = 0.2, rely = 0.1)
    sInput.place(relx = 0.55, rely = 0.1)

    tacker = 2

#checks tracker, then unwraps the corresponding list (either eccomerce or stock) from webScrapper.py, and then assigns the data to output
def writeToOutput():
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

    if(tracker == 1):
        price = ((writeToGui(eccomerce))[0])
        shippingCost = ((writeToGui(eccomerce))[1])
        discounts = ((writeToGui(eccomerce))[2])
        shippingFrom = ((writeToGui(eccomerce))[3])
        shippingTime = ((writeToGui(eccomerce))[4])

        output.insert(1, "Price: " + price)
        output.insert(2, "Shipping Cost: " + shippingCost)
        output.insert(3, "Discounts: " + discounts)
        output.insert(4, "Shipping From: " + shippingFrom)
        output.insert(5, "Shipping Time: " + shippingTime)

        output.place_configure(relx = 0.2, rely = 0.2)

    elif(tracker == 2):
        price = ((writeToGui(stocks))[0])
        open = ((writeToGui(stocks))[1])
        pClose = ((writeToGui(stocks))[2])
        volume = ((writeToGui(stocks))[3])
        marketCap = ((writeToGui(stocks))[4])
        beta = ((writeToGui(stocks))[5])
        PERatio = ((writeToGui(stocks))[6])
        EPS = ((writeToGui(stocks))[7])

        output.insert(1, "Price: " + price)
        output.insert(2, "Opening Price: " + open)
        output.insert(3, "Previous Close " + pClose)
        output.insert(4, "Volume " + volume)
        output.insert(5, "Market Cap: " + marketCap)
        output.insert(6, "Beta: " + beta)
        output.insert(7, "P/E Ratio: " + PERatio)
        output.insert(8, "EPS: " + EPS)

        output.place_configure(relx = 0.2, rely = 0.2)

m.title("Web Scraper")
m.geometry("1000x1000")
m.configure(bg = "gray20")

a = Label(m, text = "Bee & Mele's Hopefully Functioning Web Scraper!", font = ("Impact", 20), fg = "white", bg = "gray20").place(relx = 0.5, rely = 0.02, anchor = CENTER)

#Buttons that decide whether eccomerce or stocks
eButton = Button(m, text = "Eccomerce", bg = "gray20", fg = "white", font = ("Impact", 16), command = selE).place(relx = 0.2, rely = 0.05)
sButton = Button(m, text = "Stocks", bg = "gray20", fg = "white", font = ("Impact", 16), command = selS).place(relx = 0.7, rely = 0.05)

#Eccomerce Inputs
eInputL = Label(m, text = "Input What You Want To Search: ", bg = "gray20", fg = "white", font = ("Impact", 16))
eInput = Entry(m, bg = "gray20", fg = "white", font = ("Impact", 16))
#eInputL.place(relx = 0.2, rely = 0.1)
#eInput.place(relx = 0.5, rely = 0.1)

#Stocks Inputs
sInputL = Label(m, text = "Input What Stock You Want To Search: ", bg = "gray20", fg = "white", font = ("Impact", 16))
sInput = Entry(m, bg = "gray20", fg = "white", font = ("Impact", 16))
#sInputL.place(relx = 0.2, rely = 0.1)
#sInput.place(relx = 0.55, rely = 0.1)

#Output
Label(m, text = "OUTPUT", font = ("Impact", 16), fg = "white", bg = "gray20").place(relx = 0.5, rely = 0.18, anchor = CENTER)
output = Listbox(m, bg = "gray20", fg = "white", font = ("Impact", 16), width = 60)

output.place(relx = 0.2, rely = 0.2)


m.mainloop() 