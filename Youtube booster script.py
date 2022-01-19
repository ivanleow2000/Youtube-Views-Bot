# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:25:34 2022

@author: Ivan Leow
"""
### Directions ###
#If only one screen is available, use Picture-in-Picture (doesn't intefere with GUI)

from selenium import webdriver
import time
import datetime
import pyautogui

start_time = datetime.datetime.now()

def get_views():
    driver_path = r'C:\Users\61435\Downloads\Others\Personal projects\Youtube booster\chromedriver.exe'
    browser = webdriver.Chrome(executable_path = driver_path)
    my_url = "https://www.youtube.com/watch?v=atpo9gHRZbU"
    
    ### Mouse position index ###
    play = 187, 820
    mute = 307, 820
    #new = 337, 22
    stop_script = 1844, 607
    close = 288, 19
    
    #for _ in range(3):
    # AND
    #while(True):
    # RESULTS IN
    #WebDriverException: chrome not reachable
    #  (Session info: chrome=97.0.4692.71)
    # DEFINED AS A FUNCTION TO GET PASS THIS ERROR.
    
    browser.get(my_url)
    browser.maximize_window()
    time.sleep(2)
    pyautogui.click(play)
    pyautogui.click(mute)
    
    browser.minimize_window()
    pyautogui.moveTo(stop_script)
    
    time.sleep(15.23) #How long to watch video for.
    browser.maximize_window()   
    pyautogui.click(close)


i = 0 # Set counter
number_of_views = 100 #How many views to add.

print("Initiating function loop...\n")
while i < number_of_views: 
    get_views()
    i += 1
    print(str(i) + ' views added...')

execution_time = datetime.datetime.now() - start_time
print(f"\nFinal number of views added: {i}")
print(f"\nExecution time: {execution_time}")
    
