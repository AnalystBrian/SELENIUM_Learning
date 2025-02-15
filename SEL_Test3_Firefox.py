# Using the Edge Driver here instead of the Google Chrome driver because my NVH Laptop uses Edge and
# not Google Chrome:

# Starting my Selenium Learning course again 20/07/2024 and using this as a template.
# There are some good websites based on this article:
# https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/
# but this one looks very good:
# https://the-internet.herokuapp.com/


# https://www.baeldung.com/linux/geckodriver-installation

from selenium import webdriver
import time

PATH = '/home/zab/Desktop/msedgedriver'
driver = webdriver.Edge(PATH)


 #-----> Change this to your input folder:
# Windows links
#inputFolderLink = 'C:\\Users\\BNel\\Desktop\\TSX'
#file_seperator = "\\"

# Linux
#inputFolderLink = '/home/abc/Desktop/StockCharts'
#file_seperator = "/"
#-----------------------------------------------------------------------------------------
#

#PATH = "C:\\Users\\BNel\\Desktop\\msedgedriver.exe"
#PATH = '/home/zab/Desktop/msedgedriver.exe'
#driver = webdriver.Chrome(PATH)
#driver = webdriver.Edge(PATH) # It seems that you don't need to specify the PATH when using Edge

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

