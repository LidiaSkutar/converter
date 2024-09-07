import requests as rq
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb

def exchange
window=Tk()
window.title("Курсы обмена криптовалют")
window.geometry('360x180')

Label(text="Введите код криптовалюты").pack(padx=10,pady=10)
entry=Entry()
entry.pack(padx=10,pady=10)
Button(text="Получить курс обмена к доллару",comman=exchange).pack(padx=10,pady=10)
window.mainloop()


result=rq.get("https://api.coingecko.com/api/v3/search/trending")
data=json.loads(result.text)
p=pprint.PrettyPrinter(indent=4)

p.pprint(data)