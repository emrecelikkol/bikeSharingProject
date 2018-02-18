# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 08:30:44 2018

@author: emre
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import time



DATA_FILE_DIRECTORY="../data/"
availableCities={}
city_data=pd.DataFrame()

def get_city_filenames():
    
    '''finds city files under data folder and fills availableCities folder
        Args:
            none
        Returns:
            none
    '''
    import os

    files=os.listdir(DATA_FILE_DIRECTORY) 

    for file in files:
        if file.split('.')[-1] == 'csv':
            availableCities[file.split('.')[0].replace('_',' ')]=file


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    
    #check if there is city
    if availableCities=={}:
        get_city_filenames()
        
    if availableCities=={}:
        print('Couldn\'t find any city please check {} folder!'.format(DATA_FILE_DIRECTORY))
        return ''
    
    
    
    print('\nHello! Let\'s explore some US bikeshare data!\nWould you like to see data for:')
    
    for city in availableCities.keys():
        print(' + {}'.format(city))
        
        
    return DATA_FILE_DIRECTORY+availableCities[input('Type city name:').lower()]
                 


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    
    
    if time_period=='month':
        time_period = int(input('Please choose a month (month must be between 1 and 12)'))

    if time_period=='day':
        time_period = int(input('Please choose a day (day must be between 1 and 7)'))

        
    return time_period

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    return month

def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    return day


def get_data_file(city_file):
    global city_data
    city_data = pd.read_csv(city_file)
    
    month=[]
    week_day_int=[]
    hours=[]
    
    for row in city_data['Start Time']:
        d=datetime.strptime(row,'%Y-%m-%d %H:%M:%S')
        month.append(d.month)
        week_day_int.append(d.isoweekday())
        hours.append(d.hour)
    
    city_data['Month']=month
    city_data['Week Day']=week_day_int
    city_data['Hour']=hours
    
    #print(my_data['Month'].count())
    #print('January count {}'.format(my_data.loc[my_data['Month']==1].count()))
    #print(my_data.head(10))
    #my_data.info(memory_usage='deep')'''


def popular_month():
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    
    #month_count_list={'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'October':0,'September':0,'November':0,'December':0}
    #nmonth_list=[1,2,3,4,5,6,7,8,9,10,11,12]
    month_count_list=[]
    
    
    popular_month=1;
    popular_month_trip_count=0;
    for index in range(1,13):
        month_count_list.append(city_data['Month'].loc[city_data['Month']==index].count())
        if popular_month_trip_count<month_count_list[index-1]:
            popular_month_trip_count=month_count_list[index-1]
            popular_month=index
    
    
    plt.plot(range(1,13),month_count_list)
    plt.xlabel('Months')
    plt.ylabel('Count of Hiring Bike')
    plt.title('Monthly Counts of Bike Sharing')
    plt.show()
    
    return (popular_month,month_count_list)
    
    
    
    
    


def popular_day():
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    days_of_week=[]
    
    
    popular_day=1;
    popular_day_trip_count=0;
    for index in range(1,8):
        days_of_week.append(city_data['Week Day'].loc[city_data['Week Day']==index].count())
        if popular_day_trip_count<days_of_week[index-1]:
            popular_day_trip_count=days_of_week[index-1]
            popular_day=index
    
    
    plt.plot(range(1,8),days_of_week)
    plt.xlabel('Days of Week')
    plt.ylabel('Count of Hiring Bike')
    plt.title('Counts of Bike Sharing (Weekdays)')
    plt.show()
    
    return (popular_day,popular_day_trip_count)

def popular_hour():
    
    hours=[]
    
    
    popular_hour=0;
    popular_hour_trip_count=0;
    for index in range(0,24):
        hours.append(city_data['Hour'].loc[city_data['Hour']==index].count())
        if popular_hour_trip_count<hours[index-1]:
            popular_hour_trip_count=hours[index-1]
            popular_hour=hours
    
    
    plt.plot(range(0,24),hours)
    plt.xlabel('Hour of Day')
    plt.ylabel('Count of Hiring Bike')
    plt.title('Counts of Bike Sharing (Hours of Day)')
    plt.show()
    
    return (popular_hour,popular_hour_trip_count)
    
    


def statistics():
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    city_name=get_city()
    
    # Filter by time period (month, day, none)
    time_period = get_time_period()
    print('Fetching Data...')
    start_time = time.time()
    get_data_file(city_name)
    print("Data fetching complated in %s seconds." % (time.time() - start_time))
    
    print('Calculating the first statistic...')
    
    
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        popular_month()
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        popular_day()
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")  

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour()
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()



if __name__ == "__main__":
	statistics()
