# Using the Edge Driver here instead of the Google Chrome driver because my NVH Laptop uses Edge and
# not Google Chrome:

# Starting my Selenium Learning course again 20/07/2024 and using this as a template.
# There are some good websites based on this article:
# https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/
# but this one looks very good:
# https://the-internet.herokuapp.com/


# https://www.baeldung.com/linux/geckodriver-installation

# This program is now working on Ubuntu as of 15/02/2025

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

edge_options = Options()
edge_options.add_argument("--start-maximized")  # Optional: Customize browser behavior

# Specify the path to your msedgedriver
service = Service(executable_path='/home/zab/Desktop/msedgedriver')

driver = webdriver.Edge(service=service, options=edge_options)
#driver.get('https://www.example.com')
driver.get("https://matrix.itasoftware.com/")
time.sleep(5)
driver.quit()

print("Done")