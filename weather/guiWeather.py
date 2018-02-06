import os
import tkinter as tk
from tkinter import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# This is the msn url where the current temp is displayed
my_url = "https://www.msn.com/en-us/weather/today/madisonsouth-dakotaunited-states/we-city?q=madison-south-dakota&form=PRWLAS&iso=US&el=762HMuF3%2f1kxFKWiADMtdA%3d%3d"
# This parses the location out of the query string from your msn url
location = (my_url.split(sep="?q=", maxsplit=1)[1].split(sep="-", maxsplit=1)[0]).title()

root = tk.Tk()
userprofile = str(os.environ['USERPROFILE'])

def refresh(root):
    root.destroy()
    os.popen("pythonw " + userprofile + "/Documents/python/weather/guiWeather.py")

def add_item(text):
    T = Text(root, height=2, width=30)
    T.pack()
    T.insert(END, text)

def  parse_info(headers, final_list):
    """reformats the data gathered"""
    add_item(location + " at " + current_time() + "\n")
    temp = 1
    for item in final_list:
        add_item(str(headers[temp]) + str(item))
        temp += 1

def current_time():
    """Grab the current time"""
    if int(datetime.now().strftime('%H')) > 12:
        current_time = str(int(datetime.now().strftime('%H'))-12)+ ":" + datetime.now().strftime('%M')
    else:
        current_time = (datetime.now().strftime('%H:%M'))

    # Determine AM or PM
    night_or_morn = " " + datetime.now().strftime('%p')
    return current_time + night_or_morn
    

class Application(tk.Frame):
    B = Button(root, text="Reload", command=lambda: refresh(root))
    root.title('Current Weather')
    root.iconbitmap(r''+ userprofile +'/Documents/python/icons/serpent_icon.ico')

    # Downloads the raw source code and stores it as url_page
    url_html = requests.get(my_url)
    # parses the html with 
    soup = BeautifulSoup(url_html.content, "html.parser")
    list_items = soup.find('div', attrs={'class':'weather-info'})
    ### list_headers = list(list_items.find_all('span')) ###
    headers = []
    final_list = []

    for span_tag in list_items.find_all('span'):
        final_list.append(span_tag.next_sibling)
        headers.append(span_tag.text)
    ## Removes the first item which should be blank ##
    del final_list[0]
    parse_info(headers, final_list)
    B.pack()


app = Application(master=root)
app.mainloop()
