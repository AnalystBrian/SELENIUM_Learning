# A simple function from ChatGPT that will convert the UNIX time to a normal datetime format:

import datetime

def unix_to_datetime(unix_time):
    return datetime.datetime.utcfromtimestamp(unix_time)

# Example usage:
unix_time = 1702909800  # Example UNIX timestamp
converted_time = unix_to_datetime(unix_time)
print(converted_time) # 2023-12-18 14:30:00
