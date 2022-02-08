# Youtube-views-bot
Bot that boosts your views automatically.

Directions: Can be used while watching Netflix or whatever, but one screen needs to be free for pyautogui to work. Alternatively, use Picture-In-Picture feature if only one screen is available, this does not interfere with pyautogui. "chromedriver.exe" has to be installed.

TDL:

Youtube was able to detect these views and have cut views gained by bot by ~70%. Added rng to randomise watch time, to be tested.

Pyautogui used because selenium works with html and not with embedded videos. Investigate {video} tag and see if there is any way to play and mute video via html and selenium.

Look into threading to run multiple tabs at once. How to manage different tabs without clicks intefering with each other?

Setup process so that view count and execution time are still printed if script is interrupted before run end.
