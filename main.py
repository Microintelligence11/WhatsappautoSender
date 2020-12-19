# import required modle here 

import pyautogui as pg 
import webbrowser
import time
import pandas as pd 

# read the csv file here

data = pd.read_csv("data.csv")
data_dict = data.to_dict('list')
leads = data_dict['LeadNumber']
messages = data_dict['Message']

combo = zip(leads,messages)

# functions to send msg to whatsapp massenger hare 

first = True

for leads,messages in combo:
    time.sleep(4)
    webbrowser.open("https://web.whatsapp.com/send?phone="+leads+"&text="+messages)
    if first:
        time.sleep(6)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    
    time.sleep(8)
    pg.hotkey('ctrl','w')    