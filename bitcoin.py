import requests
import tkinter as tk
from datetime import datetime


def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price) + " " + "USD")
    labelTime.config(text="Updated at: " + time)

    canvas.after(1000, trackBitcoin)


canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Tracker")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")
f4 = ("arial", 16, "normal")

label = tk.Label(canvas, text="Bitcoin Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

labelQuote = tk.Label(canvas, text="If you don’t believe it or don’t get it,\n I don’t have the time to try to "
                                   "convince you,\n sorry. -Satoshi Nakamoto", font=f4)
labelQuote.pack(pady=20)

trackBitcoin()

canvas.mainloop()
