from cgitb import text
import tkinter as tk
from tkinter import Tk
from tkinter import Label
import requests
from bs4 import BeautifulSoup
from PIL import Image,ImageTk

#the url is from the weather channel
url="https://weather.com/en-IN/weather/today/l/13b68fa68514dc174c71a987397120e97434b74d4b39e030ff4ff9c535791b5e"

#creeating the basic window for the GUI
window = tk.Tk()
window.title('Weather App')
window.config(bg='white')

#importing the imge from a specified folder
img = Image.open('C:/Users/Saurav/Pictures/Camera Roll/weather.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#creating a functin to find the information about the weather forecast
def find_weather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    location2=soup.find("h1",class_="CurrentConditions--location--kyTeL").text
    temperature2 = soup.find('span', class_='CurrentConditions--tempValue--3a50n').text
    forecast1 = soup.find('div', class_='CurrentConditions--phraseValue--2Z18W').text
    
    location.config(text=location2)
    temperature.config(text=temperature2)
    weather_predict.config(text=forecast1)

#it gives the current relevant data regarding the temperature
    temperature.after(60000, find_weather)
    window.update()

#creating different labels for weather forecast
location = Label(window,font=("calibri bold", 20), bg="white")
location.grid(row=0,sticky="N",padx=100)
temperature = Label(window,font=("calibri bold",60), bg="white")
temperature.grid(row=1,sticky="N",padx=40)
Label(window, image=img ,bg='white').grid(row=1,sticky='E')
weather_predict = Label(window,font=("calibri bold", 15), bg="white")
weather_predict.grid(row=2,sticky="W",padx=40)

find_weather()
window.mainloop()
