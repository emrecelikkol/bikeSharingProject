# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 08:30:44 2018

@author: emre
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime



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
    
    city_data = pd.read_csv(city_file)
    
    month=[]
    week_day_int=[]
    
    for row in city_data['Start Time']:
        d=datetime.strptime(row,'%Y-%m-%d %H:%M:%S')
        month.append(d.month)
        week_day_int.append(d.isoweekday())
    
    
    city_data['Month']=month
    city_data['Week Day']=week_day_int
    
    
    #print(my_data['Month'].count())
    #print('January count {}'.format(my_data.loc[my_data['Month']==1].count()))
    #print(my_data.head(10))
    #my_data.info(memory_usage='deep')'''
    return city_data


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    
    #month_count_list={'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'October':0,'September':0,'November':0,'December':0}
    #nmonth_list=[1,2,3,4,5,6,7,8,9,10,11,12]
    month_count_list=[]
    
    city=get_data_file(city_file)
    popular_month=1;
    popular_month_trip_count=0;
    for index in range(1,13):
        month_count_list.append(city['Month'].loc[city['Month']==index].count())
        if popular_month_trip_count<month_count_list[index-1]:
            popular_month_trip_count=month_count_list[index-1]
            popular_month=index
    

    print(month_count_list)
    plt.plot(range(1,13),month_count_list)
    plt.xlabel('Months')
    plt.ylabel('Count of Hiring Bike')
    plt.title('Monthly Counts ofBike Sharing')
    plt.show()
    
    return popular_month
    
    
    
    
    


def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function


def statistics():
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    city=get_city()
    
    popular_month(city,'')
    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')
    
    
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    


if __name__ == "__main__":
	statistics()
