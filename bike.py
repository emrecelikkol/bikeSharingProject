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
graphics_visible=False

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
        month = get_month()
        day = get_day(month)        
        return (month,day)
    
    return(0,0)

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    
    month_count_list={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'October':9,'September':10,'November':11,'December':12}
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    
    if month=='none':
        return 0
    
    return month_count_list[month]

def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.Type "none" for no time filter\n')
    # TODO: handle raw input and complete function
    if day=='none':
        return 0
    return int(day)


def get_data_file(city_file,filter_month,filter_day):
    global city_data
    city_data = pd.read_csv(city_file)
    
    month=[]
    week_day_int=[]
    hours=[]
    days=[]
    for row in city_data['Start Time']:
        d=datetime.strptime(row,'%Y-%m-%d %H:%M:%S')
        month.append(d.month)
        week_day_int.append(d.isoweekday())
        hours.append(d.hour)
        days.append(d.day)
    city_data['Month']=month
    city_data['Week Day']=week_day_int
    city_data['Hour']=hours
    city_data['Day']=days
    
    if filter_month>0 and filter_month<13:
        city_data=city_data.loc[city_data['Month']==filter_month]
        
    if filter_day>0 and filter_day<32:
        city_data=city_data.loc[city_data['Day']==filter_day]
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
    
    
def trip_duration():
    print('Total trip duration is {} seconds'.format(city_data['Trip Duration'].sum()))
    print('Average trip duration is {} seconds'.format(city_data['Trip Duration'].mean()))
    
    
    


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
    
def popular_stations():
    start_station_df=city_data.groupby(['Start Station']).agg({'Start Time':'count'})
    end_station_df=city_data.groupby(['End Station']).agg({'Start Time':'count'})
    
    popular_start_station=start_station_df.loc[start_station_df['Start Time']==start_station_df['Start Time'].max()]
    
    popular_end_station=end_station_df.loc[end_station_df['Start Time']==end_station_df['Start Time'].max()]
    
    print('Popular Start Station :{} \nTotal Trip Count :{}'.format(popular_start_station))
    print('Popular End Station   :{} \nTotal Trip Count :{}'.format(popular_end_station))
    
    '''
    to head map analyse
    
    import seaborn as sns
    test=city_data.groupby(['Start Station','Day']).agg({'Start Time':'count'})
    df_wide=test.pivot_table( index='Start Station', columns='Day', values='Start Time' )
    sns.heatmap( df_wide )
    '''


def statistics():
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    graphics_visible=input('Would you like to analyse with graphics (y/n)')=='y'
    city_name=get_city()
    
    # Filter by time period (month, day, none)
    month,day = get_time_period()
    print('Fetching Data...')
    start_time = time.time()
    get_data_file(city_name,month,day)
    print("Data fetching complated in %s seconds." % (time.time() - start_time))
    
    print('Calculating the first statistic...')
    
    
    # What is the most popular month for start time?
    if month == 0:
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        popular_month()
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if day == 0 or month == 0:
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


    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration()
    
    
    print("That took %s seconds." % (time.time() - start_time))    
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations()
    popular_stations()
    print("That took %s seconds." % (time.time() - start_time))


if __name__ == "__main__":
	statistics()
