# Using the Edge Driver here instead of the Google Chrome driver because my NVH Laptop uses Edge and
# not Google Chrome:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #just so you can use the enter key
from selenium.webdriver.common.by import By
import time
import datetime
import csv
from selenium.webdriver.support.ui import Select

#Classes for the explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException #to try find if element exists

#Stale Element Stuff
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Date Time Stuff
import datetime
from dateutil.relativedelta import relativedelta
import csv # For the CSV writer


PATH = "C:\\Users\\BNel\\Desktop\\msedgedriver.exe"
#driver = webdriver.Chrome(PATH)
driver = webdriver.Edge() # It seems that you don't need to specify the PATH when using Edge

# Go to the website you want to scrape here:
driver.get("https://matrix.itasoftware.com/")
time.sleep(5)
driver.quit()

print("Done")

# -------------------------- Resources: --------------------------------------------------------------------
# https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python

# Good selenium resource:
# https://www.selenium.dev/documentation/webdriver/elements/finders/
#<input _ngcontent-ng-c1587650989="" placeholder="Add airport" matinput="" autocomplete="off" class="mat-mdc-input-element mat-mdc-chip-input mdc-text-field__input mat-input-element mat-mdc-autocomplete-trigger mat-mdc-form-field-input-control cdk-text-field-autofill-monitored" id="mat-mdc-chip-list-input-1" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-haspopup="listbox">
#//*[@id="mat-mdc-chip-list-input-1"]