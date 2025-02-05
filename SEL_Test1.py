# This program derives from Flight_Hunter_v1.py in your pythonProject folder

# Note: Selenium has deprecated find_element_by_* and find_elements_by_* are now removed (#10712)
# so the line:
# dpt_srch = driver.find_element_by_xpath("//*[@id='cityPair-orig-0']")
# will be replaced with:
# driver.find_element("xpath", '//*[@id='cityPair-orig-0']')
# See the resource:
# https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath

from selenium import webdriver
from selenium.webdriver.common.keys import Keys #just so you can use the enter key
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

#Function to determine if an element exists
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def flight_finder(departure_airport,arrival_airport,dep_date,return_date):

    # Open up the CHROME port
    #PATH = "C:\Program Files (x86)\chromedriver.exe"
    #driver = webdriver.Chrome(PATH)

    # PATH = "C:\\Users\\BNel\\Desktop\\msedgedriver.exe"
    driver = webdriver.Edge()

    # Go to the website you want to scrape here:
    driver.get("https://matrix.itasoftware.com/")
    time.sleep(3)

    # print(departure_airport + " to " + arrival_airport)
    # ----Arrival and Departure Airports------------------------------------------------------------
    # Enter the departure airport
    #dpt_srch = driver.find_element_by_xpath("//*[@id='cityPair-orig-0']")
    #dpt_srch = driver.find_element("xpath","//*[@id='cityPair-orig-0']")
    dpt_srch = driver.find_element("xpath", "//*[@id='mat-mdc-chip-list-input-1']")
    dpt_srch.clear()
    dpt_srch.send_keys(departure_airport)
    # dpt_srch.send_keys(Keys.DOWN)
    time.sleep(2)  # This sleep is very NB. If not included - the program can't the drop down list and crashes
    dpt_srch.send_keys(Keys.RETURN)

    # Enter the arrival airport
    #arriv_srch = driver.find_element_by_xpath("//*[@id='cityPair-dest-0']")
    #arriv_srch = driver.find_element("xpath","//*[@id='cityPair-dest-0']") #//*[@id="mat-mdc-chip-list-input-1"]
    arriv_srch = driver.find_element("xpath", "//*[@id='mat-mdc-chip-list-input-1']")
    arriv_srch.clear()
    arriv_srch.send_keys(arrival_airport)
    time.sleep(2)
    arriv_srch.send_keys(Keys.RETURN)
    # ------end of Airports Inputs------------------------------------------------------------------------

    # ------ Date Inputter -----------------------------------------------------------------------------

    # Outbound date mm/dd/yy
    #out_date_srch = driver.find_element_by_xpath("//*[@id='cityPair-outDate-0']")
    out_date_srch = driver.find_element("xpath","//*[@id='cityPair-outDate-0']")
    out_date_srch.clear()
    out_date_srch.send_keys(dep_date)
    time.sleep(2)
    out_date_srch.send_keys(Keys.RETURN)

    # Return date mm/dd/yy
    #return_date_srch = driver.find_element_by_xpath("//*[@id='cityPair-retDate-0']")
    return_date_srch = driver.find_element("xpath","//*[@id='cityPair-retDate-0']")
    return_date_srch.clear()
    return_date_srch.send_keys(return_date)
    time.sleep(2)
    return_date_srch.send_keys(Keys.RETURN)
    # As you hit Enter - it automatically starts the search
    # ---- End of Dates -----------------------------------------------------------------------------

    # Search button
    #time.sleep(3)
    # srch_btn = driver.find_element_by_xpath("//*[@id='searchButton-0']")
    # driver.execute_script("arguments[0].click();",srch_btn)
    #time.sleep(2)
    # -------------------------------------------------------------------------------------------------
    # The next page - Brings up all the flight details
    # time.sleep(50)
    # Gonna have to do a wait here:
    price1_path = "//*[@id='contentwrapper']/div[1]/div/div[5]/div[4]/div[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div/button/span"
    # price2_path = "//*[@id='contentwrapper']/div[1]/div/div[4]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div/div/table/tbody/tr[4]/td[1]/div/a"

    # //*[@id="contentwrapper"]/div[1]/div/div[4]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div/div/table/tbody/tr[3]/td[1]/div/a

    price1 = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, price1_path)))
    # price2 = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,price2_path)))

    price1_txt = price1.text
    # price2_txt = price2.text

    # You will need to click the Back Button here and possibly clear the elements
    #modify_srch_btn = driver.find_element_by_xpath("//*[@id='contentwrapper']/div[1]/div/div[1]/div[1]/table/tbody/tr/td[2]/div/a")
    #modify_srch_btn.click()
    #time.sleep(3)

    #Clear the elements

    #Close
    #time.sleep(2)
    driver.quit()

    return price1_txt

    #------ End of flight_finder Function -----------------------------------------

def dateiterator(start_date,days_stay,months_search):
    all_dates_str = []

    dep_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    dur_period = datetime.timedelta(days=days_stay)  # adding days_stay to your start_date
    step = datetime.timedelta(days=1) #iterating through each day in the calendar


    #Month date
    s = dep_date + relativedelta(months=months_search)  # adding months_search (1 month) to yourstart_date
    dates_list_str = []

    while s >= dep_date:
        return_dte = dep_date + dur_period
        #print(str(dep_date.date()) + " - " + str(return_dte.date())) #output here
        # the .date() removes the hh:mm:ss component so output is changed (see example below):
        # 2022-03-09 00:00:00 changes to 2022-03-09

        #Date List
        dates_list_str.append(str(dep_date.date()))
        dates_list_str.append(str(return_dte.date()))

        #Next Step in the While Loop
        dep_date = dep_date + step

        #Global Array
        #print(dates_list_str)
        all_dates_str.append(dates_list_str)
        dates_list_str = []
        #.clear() doesn't work here
        # -------------------------While Loop End ------------------------------

    #Out the while loop
    #print(all_dates_str)
    #return [['2022-02-05','2022-02-15'], ['2022-02-06','2022-02-16'], ['2022-02-07','2022-02-17']]
    return all_dates_str #returns the list of dates

#------------------------------------------------------------------------

departure_airport = "London, United Kingdom - All airports"
arrival_airport = "Johannesburg"
#Cape Town International, Johannesburg, Palma de Mallorca, Tashkent

start_date = "2022-03-03"
end_date = "2024-03-15"

p1 = flight_finder(departure_airport,arrival_airport,start_date,end_date)
print(p1)


# Commenting out all the previous stuff below:
#Date iterator
#days_stay = 8
#start_date = "2022-02-03"
#months_search = 1

#Destinations
#departure_airport = "London, United Kingdom - All airports"
#arrival_airport = "Johannesburg"
#Cape Town International, Johannesburg, Palma de Mallorca, Tashkent
#d_list = []
#Searching on multiple days
#for b in range(3,7):
    #temp_list = dateiterator(start_date,b,months_search)
    #d_list = d_list + temp_list

#print(d_list)
#d_list_sze = len(d_list)
#print(d_list_sze)

#l_outpt_array = []
#g_outpt_array = []

# FOR LOOP to print out each start date
#for t in range(d_list_sze):
    #temp_list = d_list[t]
    #dep_date = temp_list[0]
    #return_date = temp_list[1]
    #cheapest_price = flight_finder(departure_airport,arrival_airport,dep_date,return_date)
    #print(cheapest_price)

    #Append to local array
    #l_outpt_array.append(dep_date)
    #l_outpt_array.append(return_date)
    #l_outpt_array.append(cheapest_price)
    #g_outpt_array.append(l_outpt_array)
    #Clear the local array
    #l_outpt_array = []

#print(g_outpt_array)
# DONT FORGET TO WRITE TO THE CSV FILE HERE
# -----------Try append an Excel CSV File---------------------------------------------------------------------------
#csv_data = [['a','b','c'],['d','e','f']]
# This will output based on the lists inside, so:
# a b c
# d e f

#csv_data = g_outpt_array #Assigning the global putput array (g_output_array) to the excel writer

# opening a csv file in 'a' mode a opens a file for appending only so data is added at the bottom
# of your existing csv file.
# opening a csv file in 'w+' mode a opens a file for reading and writing
#file = open('Flight_writer_main.csv', 'w+', newline='')
# Flight_writer.csv should appear amongst your python programs on the left window
# Also in C:\Users\Brian Dell1\PycharmProjects\pythonProject

# writing the data into the file
#with file:
    #write = csv.writer(file)
    #write.writerows(csv_data)