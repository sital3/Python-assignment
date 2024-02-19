from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city= city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=46e0fbf0aaf724cee98b09f3e5a1caca").json()
    w1_label.config(text= data["weather"][0]["main"])
    wd1_label.config(text= data["weather"][0]["description"])
    temp1_label.config(text= str(int(data["main"]["temp"]-273.15)))
    pre1_label.config(text= data["main"]["pressure"])

def on_combobox_click(event):
    if com.get() == placeholder:
        com.set("")  

def on_combobox_leave(event):
    if not com.get():
        com.set(placeholder)

win= Tk()
win.title("Weather App")
win.config(bg = "royalblue")
win.geometry("570x570")

name_label= Label(win, text="Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x= 50, y=50, height=50, width=450)

placeholder = "Select a state"
city_name= StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="Weather App", values=list_name, font=("Times New Roman", 15, "bold"),textvariable= city_name)
com.set(placeholder)
com.place(x= 50, y=120, height=50, width=450)
com.bind("<FocusIn>", on_combobox_click)
com.bind("<FocusOut>", on_combobox_leave)

done_button = Button(win, text="Check", font=("Times New Roman", 20, "bold"))
done_button.place(x=230, y=190, height=50, width=100)

w_label= Label(win, text="Weather Climate", font=("Times New Roman", 20))
w_label.place(x= 35, y=260, height=50, width=220)
w1_label= Label(win, text="", font=("Times New Roman", 20))
w1_label.place(x= 280, y=260, height=50, width=220)


wd_label= Label(win, text="Weather Description", font=("Times New Roman", 18))
wd_label.place(x= 35, y=330, height=50, width=220)
wd1_label= Label(win, text="", font=("Times New Roman", 18))
wd1_label.place(x= 280, y=330, height=50, width=220)

temp_label= Label(win, text="Temperature", font=("Times New Roman", 20))
temp_label.place(x= 35, y=400, height=50, width=220)
temp1_label= Label(win, text="", font=("Times New Roman", 20))
temp1_label.place(x= 280, y=400, height=50, width=220)

pre_label= Label(win, text="Pressure", font=("Times New Roman", 20))
pre_label.place(x= 35, y=470, height=50, width=220)
pre1_label= Label(win, text="", font=("Times New Roman", 20))
pre1_label.place(x= 280, y=470, height=50, width=220)

done_button = Button(win, text="Check", font=("Times New Roman", 20, "bold"),command=data_get)
done_button.place(x=230, y=190, height=50, width=100)

win.mainloop()