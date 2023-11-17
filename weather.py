import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # original format 2021-07-02T07:00:00+08:00

    # getdate = datetime.strptime(iso_string, '%Y-%m-%d %H:%M:%S.%f%z')
    # return getdate.strftime("%A,%d %B, %Y")

    # using isoformat so I did not have to specify the y/m/d and timezones, was previously getting a value error using strptime()

    getdate = datetime.fromisoformat(iso_string)
    return getdate.strftime("%A %d %B %Y")
    
    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    
    
    tempc = (5/9) * (float(temp_in_farenheit)-32)

    return round(tempc, 1)
    
    pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    
    """

    sum = 0
    for temp in weather_data:
        sum += float(temp)
        
    
    avg = sum/len(weather_data)
    return avg

    pass

# testing purposes 
# print(calculate_mean([49, 57, 56, 55, 53]))


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    
    # open csv file

    with open(csv_file) as file:
        csv_reader = csv.reader(file)
        # to skip the header
        next(csv_reader)
        # create a new list
        new_list = []
        for line in csv_reader:
            if len(line) == 0:
                continue
            date = line[0]
            my_min = int(line[1])
            my_max = int(line[2])
            new_list.append([date, my_min, my_max])
    
    return new_list
    
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    
    # used same logic as find max

    new_data = []
   
    for item in weather_data:
        new_data.append(float(item))
    mintemp = min(new_data, default=None)
    if mintemp == None:
        return ()
    else:
        position = []
        for place in range(len(new_data)):
            if new_data[place] == mintemp:
                position.append(place)
        return (mintemp, position[-1])

    
    
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    # write code to find max temp in the list, use int data type
    # expected_result = (57.0, 1) maxtemp and index position

    # set maxtemp variable and convert list into float
    
    # attempt 1: found this code on stackoverflow, but returns it as an array and was not sure what numpy is
    # import numpy as np 
    # floattemp = np.array(weather_data, dtype=float)


    # attempt 2:

    # sample_data = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7]
    # new_data = map(float, sample_data)

    # maxtemp = max(new_data)
    # print(maxtemp)

    # did not work as map transforms the list into something else, thus cannot find position number for max value


    # attempt 3: 
    # new_data converts weather data into floats
    new_data = []
   
    for item in weather_data:
        new_data.append(float(item))
    maxtemp = max(new_data, default=None)
    if maxtemp == None:
        return ()
    else:
        position = []
        for place in range(len(new_data)):
            if new_data[place] == maxtemp:
                position.append(place)
        return (maxtemp, position[-1])

    
    pass




def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
#     8 Day Overview
#   The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is 11.4°C.
#   The average high this week is 18.8°C.
    
    # set lists, summary (to be returned), min and max temp lists to find min and max and index

    summary = ""
    list_min = []
    list_max = []
    
    # get data for lists
    for data in weather_data:
        list_min.append (data[1])
        list_max.append (data[2])

    #  8 Day Overview
    days = len(weather_data)
    summary+=f"{days} Day Overview\n"

    
    # The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.

    mintemp = find_min(list_min)
    mintemp_c = format_temperature(convert_f_to_c(mintemp[0]))
    mintemp_index = mintemp[1]
    mintemp_date = convert_date(weather_data[mintemp_index][0])

    summary+=f"  The lowest temperature will be {mintemp_c}, and will occur on {mintemp_date}.\n"

    # same logic for max
    maxtemp = find_max(list_max)
    maxtemp_c = format_temperature(convert_f_to_c(maxtemp[0]))
    maxtemp_index = maxtemp[1]
    maxtemp_date = convert_date(weather_data[maxtemp_index][0])

    summary+=f"  The highest temperature will be {maxtemp_c}, and will occur on {maxtemp_date}.\n"

    # find min_avg

    min_avg = format_temperature(convert_f_to_c(calculate_mean(list_min)))
    summary += f"  The average low this week is {min_avg}.\n"
    

    # find max_avg
    
    max_avg = format_temperature(convert_f_to_c(calculate_mean(list_max)))
    summary += f"  The average high this week is {max_avg}.\n"

    return summary
    
    
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    # set daily_summary to return string
    daily_summary = ""

    # get the stats (date, min/max temp) from weather_Data
    for data in weather_data:
        date = convert_date(data[0])
        min_temp = format_temperature(convert_f_to_c(data[1]))
        max_temp = format_temperature(convert_f_to_c(data[2]))
        # += adds values together and assigns the result to the variable
        daily_summary += (f"---- {date} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n")
     
    return daily_summary
    
    pass
