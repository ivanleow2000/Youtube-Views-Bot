# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:25:34 2022

@author: Ivan Leow
"""
### Directions ###
# If only one screen is available, use Picture-in-Picture (doesn't intefere with GUI)

# Packages used
from selenium import webdriver
import time
import datetime
import pyautogui
import random
from random import seed

# Initiate run time recording
start_time = datetime.datetime.now()

### Mouse position index ###
play = 187, 820
mute = 307, 820
#new = 337, 22
stop_script = 1844, 607
close = 288, 19

# Youtube video link to boost.
my_url = "https://www.youtube.com/watch?v=atpo9gHRZbU"


# Methods {for _ in range(3):} and {while(True):} result in
# Error: {WebDriverException: chrome not reachable (Session info: chrome=97.0.4692.71)}
# Defining it as function seems to fix it.
def get_views():
    # Make sure chromedrive.exe is installed in working directory.
    # Variables have to be defined within function for some reason. Otherwise chromedrive.exe won't run.
    driver_path = r'C:\Users\61435\Downloads\Others\Personal projects\Youtube booster\chromedriver.exe'
    
    browser = webdriver.Chrome(executable_path = driver_path)
    browser.get(my_url)
    browser.maximize_window()
    time.sleep(2)
    pyautogui.click(play)
    pyautogui.click(mute)
    
    browser.minimize_window()
    pyautogui.moveTo(stop_script)
    
    seed(8)
    time.sleep(random.randrange(155, 305)/10) #Randomise watch time.
    browser.maximize_window()   
    pyautogui.click(close)


i = 0 # Set counter
number_of_views = 100 #How many views to add.

print("Initiating function loop...\n")
while i < number_of_views: 
    get_views()
    i += 1
    print(str(i) + ' views added...')

# End of script stats.
execution_time = datetime.datetime.now() - start_time
print(f"\nFinal number of views added: {i}")
print(f"\nExecution time: {execution_time}")
    
