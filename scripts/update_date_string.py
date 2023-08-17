# This script will use yesterdays date to replace %y with the year %m with the month and %d with the day
# for all occurrences in the inputfile and then have the actual dates in the outputfile
import sys
import datetime

def date_preceding_zero(input: int):
    if input < 10:
        return f"0{input}"
    else:
        return str(input)

# datetime.timedelta(days=1) moves the date back one day
def update(input_file_path):
    dtToday = datetime.datetime.today()
    dtYesterday = dtToday - datetime.timedelta(days=1)
    
    updated_string = input_file_path.replace('%y', str(dtYesterday.year))
    updated_string = updated_string.replace('%m', date_preceding_zero(dtYesterday.month))
    updated_string = updated_string.replace('%d', date_preceding_zero(dtYesterday.day))
    return updated_string

