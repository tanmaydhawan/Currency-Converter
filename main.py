import requests, json
import tkinter as tk
from tkinter import *



def createWidgets():

    country_list = ["India (INR)","United States Of America(USD)", "Canada(CAD)", "China(CNY)"]

    text_label = Label(root, text="Welcome to python Currency Converter", bg="#E8D579")
    text_label.grid(row=1, column=1,pady=10)

    amount_label = Label(root,text="Enter Amount", bg="#E8D579")
    amount_label.grid(row=2, column=0, padx=20, pady=10)

    global amount_entry1

    amount_entry1 = Entry(root, width=40, textvariable= amount1)
    amount_entry1.grid(row=2, column=1, padx=20, pady=10)

    from_country = Label(root,text="From Country",bg="#E8D579")
    from_country.grid(row=3, column=0, padx=20, pady=10)

    from_menu = OptionMenu(root, variable1, *country_list )
    from_menu.grid(row=3,column=1, padx=20, pady=10)

    To_country = Label(root, text="To Country", bg="#E8D579")
    To_country.grid(row=4, column=0, padx=20, pady=10)

    To_menu = OptionMenu(root, variable2, *country_list)
    To_menu.grid(row=4, column=1, padx=20, pady=10)

    convert_but = (Button(root, width=15, text="Convert", command=calculate, bg="#05E8E0"))
    convert_but.grid(row=4, column=2, padx=20,pady=10)

    converted_text = Label(root, text="Converted Amount", bg="#E8D579")
    converted_text.grid(row=5 ,column=0, padx=20, pady=10)

    global amount_entry2
    amount_entry2 = Entry(root, width=40)
    amount_entry2.grid(row=5, column=1, pady=10)

    clear_but = Button(root, text="Clear", width=10, command=clear, bg="#05E8E0")
    clear_but.grid(row=5, column=2, pady=10)


def data(str):
    for i in str:
        if i=="(":
            start = str.index(i)+1
        if i==")":
            end = str.index(i)
    return str[start:end]



def calculate():
    api_key = "JW45C1BABWV988DT"
    base_url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"
    var1 = data(variable1.get())
    var2 = data(variable2.get())

    main_url = base_url + "&from_country = "+var1+"&apikey = " + api_key
    

    req_ob = requests.get(main_url)
    result = req_ob.json()

    exchange_rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])
    amount = float(amount1.get())
    new_amount = round(amount*exchange_rate, 3)
    amount_entry2.insert(0, str(new_amount))

def clear():

    amount_entry1.delete(0, END)
    amount_entry2.delete(0, END)



root = tk.Tk()
root.geometry("650x250")
root.title("Currency Converter")
root.config(background="#000000")

amount1 = StringVar()
variable1 = StringVar()
variable2 = StringVar()
variable1.set("From Country")
variable2.set("To Country")

createWidgets()

#To keep the tkinter window on.
root.mainloop()