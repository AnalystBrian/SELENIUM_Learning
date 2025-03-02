# This program derives from SEL_Test3_WL_Combo_a1.py and the tsa_3.py program line.
# This line of programs is to try and automate tradingview

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

# First, go to your website:
driver.get("https://www.tradingview.com/")


btn1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[2]/div[3]/button[2]")
btn1.click()
time.sleep(2)

# Use Ctrl+Shift+C to open the inspector.
btn2 = driver.find_element(By.XPATH,"//*[@id='overlap-manager-root']/div[2]/span/div[1]/div/div/div/button[1]/span")
btn2.click()
time.sleep(2)
email_btn = driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div[1]/div/div[2]/div[2]/div/div/button/span[2]/span[1]")
email_btn.click()

#username_elem = driver.find_element(By.ID,'id_username')
#username_elem = driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/div[1]/span[2]")
# //*[@id="id_username"]
username_elem = driver.find_element(By.XPATH,"//*[@id='id_username']")
username_elem.send_keys("brianknel@yahoo.com")

pword_elem = driver.find_element(By.ID,"id_password")
#pword_elem = driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/div[2]/span[2]")
pword_elem.send_keys("Joburg2023&1")
time.sleep(20)

sign_in_btn = driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div[1]/div/div[2]/div[2]/div/div/div/form/button")
sign_in_btn.click()
#-----------------------------------------------------------------------------------------------------------
# Searching the element:
time.sleep(2)
srch_btn = driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div[2]/div[2]/div/div/div/button[1]/span")
srch_btn.click()

time.sleep(2)
srch_inpt = driver.find_element(By.XPATH,"//*[@id='overlap-manager-root']/div[2]/div/div[2]/div/div/div[1]/div/div[1]/span/form/input")
srch_inpt.send_keys("NVDA")

time.sleep(2)
selector1 = driver.find_element(By.XPATH,"//*[@id='overlap-manager-root']/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div[1]/div[2]/div")
selector1.click()

#-----------------------------------------------------------------------------------------------------------
time.sleep(24)
driver.quit()
print("Done")


