# A simple function from ChatGPT that will convert the UNIX time to a normal datetime format.
# UNIX_time_2.py will try and build on 1 and apply that function to a spreadsheet:

import datetime
import pandas as pd
from pandas import ExcelWriter

def unix_to_datetime(unix_time):
    return datetime.datetime.utcfromtimestamp(unix_time)

# Example usage:
unix_time = 1702909800  # Example UNIX timestamp
converted_time = unix_to_datetime(unix_time)
print(converted_time) # 2023-12-18 14:30:00

# Function to split the datetime on space
# Takes 2023-07-06 12:58:00 and returns 2023-07-06
def datetime_split(dtime):
    s_dtime = str(dtime)
    adm_stped = s_dtime.split(" ")
    return adm_stped[0]

# ---------------- Read a csv file into a dataframe---------------------------------------------------------
csv_i_link = 'C:\\Users\\BNel\\Downloads\\BATS_LLY, 1D (1).csv'

df = pd.read_csv(csv_i_link) #This will read in with default index (0,1,2,3) etc
print(df)
# Output:
#            time   close   Volume
# 0    1702909800  579.76  3033944
# 1    1702996200  579.81  2192689
# 2    1703082600  570.21  2647100

print("-----------------------------------------------------------------------------")

# Apply the unix_to_datetime function to the 'time' column in the dataframe:
df["time_d"] = df["time"].apply(unix_to_datetime)
# 1740666600 ---> 27/02/2025  14:30:00

# Now split the time out of it:
df["time_e"] = df["time_d"].apply(datetime_split)

# The date will now be in a string format so you may need to convert it back into a date but
# let's see if that is needed.

# Drop the unnecessary columns ('time' and 'time_d'):
df.drop(['time','time_d'],axis=1,inplace=True)

# Rename column time_e to time to complete the process:

# -------------------- Output to an Excel File --------------------------------------------------------------------------------------
# Define a path to where you would like to create your output Excel file:
xl_o_path = "C:\\Users\\BNel\\Downloads\\BATS_LLY, 1D (1).xlsx"

# Write your list of dataframes to Excel using your list of month names as each new sheet name:
with ExcelWriter(xl_o_path) as writer:
    df.to_excel(writer, 'Output',index = None, header=True)