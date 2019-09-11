from tkinter import *
import requests
import json

window = Tk()
window.title("Bitmex calculator")
window.geometry("600x400+750+290")
window.resizable(0,0)

f0 = Frame(window, bg = "powder blue", relief=RAISED)
f0.place(x=0,y=0, height=60, width=600)

lbl = Label(f0, text="Bitmex Calculator", font=("Calibri Bold", 30), fg="steel blue", bg="powder blue")
lbl.pack(side=TOP)

#==========================================================================

f1 = Frame(window, width = 300, height = 280, bg = "azure", relief=SUNKEN)
f1.place(x=0,y=60, height=280, width=300)

lbl0 = Label(f1, text="BTC Capital", font=("Roboto bold", 15), padx=5, pady=5, bd=10, bg = "azure")
lbl0.grid(row=0, column=0)
txt0 = Entry(f1, width=20, bd=8, bg = "azure")
txt0.grid(row=0, column=2)

lbl1 = Label(f1, text="Entry Price",font=("Roboto bold", 15), padx=5, pady=5, bd=10, bg = "azure")
lbl1.grid(row=1, column=0)
txt1 = Entry(f1, width=20, bd=8, bg = "azure")
txt1.grid(row=1, column=2)

lbl2 = Label(f1, text="Stop Loss",font=("Roboto bold", 15), padx=5, pady=5, bd=10, bg = "azure")
lbl2.grid(row=2, column=0)
txt2 = Entry(f1,width=20, bd=8, bg = "azure")
txt2.grid(row=2, column=2)

lbl3 = Label(f1, text="Exit Price",font=("Roboto bold", 15), padx=5, pady=5, bd=10, bg = "azure")
lbl3.grid(row=3, column=0)
txt3 = Entry(f1,width=20, bd=8, bg = "azure")
txt3.grid(row=3, column=2)

lbl4 = Label(f1, text="Risk in %",font=("Roboto bold", 15), padx=5, pady=5, bd=10, bg = "azure")
lbl4.grid(row=4, column=0)
txt4 = Entry(f1,width=20, bd=8, bg = "azure")
txt4.grid(row=4, column=2)

#===================================================================================

f2 = Frame(window, width = 300, height = 280, relief=SUNKEN, bg = "lavender blush")
f2.place(x=301,y=60, height=280, width=300)

lbl5 = Label(f2, text="Position Size",font=("Roboto bold", 15), padx=5, pady=5, bd=10, bg = "lavender blush")
lbl5.grid(row=0, column=0)
txt5 = Entry(f2,width=20, bd=8, bg = "lavender blush")
txt5.grid(row=0, column=2)

lbl6 = Label(f2, text="Profit %",font=("Roboto bold", 15), padx=5, pady=5, bd=10, bg = "lavender blush")
lbl6.grid(row=1, column=0)
txt6 = Entry(f2,width=20, bd=8, bg = "lavender blush")
txt6.grid(row=1, column=2)

#=======================================================================================

f3 = Frame(window, width = 600, height = 60, bg = "powder blue", relief=RAISED)
f3.place(y=340, height=60, width=600)

price = (requests.get('https://www.bitmex.com/api/v1/trade?symbol=XBT&count=1&reverse=true').json())[0]['price']

def calc():
    capital = txt0.get()
    entry_p = txt1.get()
    exit_p = txt2.get()
    sl = txt3.get()
    risk = txt4.get()
    capital1 = float(capital) * float(price)
    size = (float(capital1) * float(risk) / 100)/((float(entry_p) - float(sl))/float(entry_p))
    profit = (float(exit_p)-float(entry_p)) * 100 /float(entry_p)
    txt5.delete(0, END)
    txt5.insert(END, int(size))
    txt6.delete(0, END)
    txt6.insert(END, int(profit))

def rst():
    txt0.delete(0, END)
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)

btn1 = Button(f3, text="Calculate", padx=5, pady=5, command=calc, bd=10)
btn1.grid(row=0, column=0)
btn1.place(x=100, y=5)

btn2 = Button(f3, text="Reset", padx=5, pady=5, command=rst, bd=10)
btn2.grid(row=0, column=1)
btn2.place(x=400,y=5)

window.mainloop()
