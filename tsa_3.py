# Using the Edge Driver here instead of the Google Chrome driver because my NVH Laptop uses Edge and
# not Google Chrome:

# Starting my Selenium Learning course again 20/07/2024 and using this as a template.
# There are some good websites based on this article:
# https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/
# but this one looks very good:
# https://the-internet.herokuapp.com/


# https://www.baeldung.com/linux/geckodriver-installation

# This program is now ---WORKING--- on Ubuntu as of 26/02/2025
# And on Work Laptop Windows as of 26/02/2025
#----------------------------------------------------------------------------------------------------
# This program derives from SEL_Test3_WL_Combo_a1.py. This line of programs is to record the
# Tech Step Academy course from Udemy:

# This particular one will track "12. Skills Challenge" lecture on Udemy:
# https://techstepacademy.com/trial-of-the-stones

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By

edge_options = Options()
edge_options.add_argument("--start-maximized")  # Optional: Customize browser behavior

# Linux
# Specify the path to your msedgedriver
service = Service(executable_path='/home/cde/Desktop/msedgedriver')
driver = webdriver.Edge(service=service, options=edge_options)
#---------------------------------------------------------------------------------------------
# Windows
#service = Service(executable_path="C:\\Users\\BNel\\Desktop\\msedgedriver.exe")
#driver = webdriver.Edge() # It seems that you don't need to specify the PATH when using Edge
#----------------------------------------------------------------------------------------------

# First, go to the training ground that has been set up by Tech Step Academy:
driver.get("https://techstepacademy.com/trial-of-the-stones")

# Next, you want to try and locate an element on the page. The best way to do this is to
# open your normal Edge browser, right click on the element that you want and inspect.
# You can run Python code repeatedly trying to test it but it is far quicker and easier
# to use Console on browser. Click Console and then the circle crossed with a diagonal line
# $$() means CSS selector
# $$("input[id='ipt1']")
# save this as a path as a variable (input1Path) and then build a locator

input1Path = "input[id='ipt1']"

# Remember that the old way (that I learned) of doing this has been deprecated:
# use .find_element_by_css_selector() has been deprecated
# Below is the new way:
#element = driver.find_element(By.CSS_SELECTOR,input1Path)
# Eg:
#time.sleep(5)
input1Element = driver.find_element(By.ID,"r1Input")

# Type something into it:
# The way you do this is using send_keys:
input1Element.send_keys("rock")


# Find the Button:
btn1 = driver.find_element(By.ID,"r1Btn")
btn1.click()

# This will cause the pop-up with the password "bamboo" to appear. Find that part next:
riddle_password = driver.find_element(By.ID,"passwordBanner")
# Print it out:
txt_riddle_password = riddle_password.text
print(txt_riddle_password)
# Note: if something is between 2 tags (like bamboo is), we can call the .text method on it. If not we
# have to call the .value on it.
# <h4>bamboo</h4>
# see above, it is between 2 h4 tags.
#-----------------------------------------------------------------------------------------------------------
# Riddle of Secrets:

# Find the next input element:
input2Element = driver.find_element(By.ID,"r2Input")
input2Element.send_keys(txt_riddle_password)
# Find the next button and click it:
btn2 = driver.find_element(By.ID,"r2Butn")
btn2.click()

#-----------------------------------------------------------------------------------------------------------
time.sleep(2)
driver.quit()
print("Done")

# Next course module is "Finding Tricky Elements using XPATH

# Locating the element
# Clicking the element
# Send something to the element
