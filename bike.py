# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 08:30:44 2018

@author: emre
"""

DATA_FILE_DIRECTORY="./data/"
availableCities={}


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
    
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    
    
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


def getDataFile():
    import pandas as pd
    my_data = pd.read_csv(get_city())
    print(my_data.head(10))


while input('do you wanna look cities again y/n').lower()=='y':
    getDataFile()
##chicagoprint(get_city())
    

