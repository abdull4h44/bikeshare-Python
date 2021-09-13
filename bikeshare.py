#!/usr/bin/env python
# coding: utf-8
# In[1]:


import time
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


# In[3]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).


    while True:
      city = input("Which city would you like to filter by? New York City, Chicago or Washington?\n")
      city = city.lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Sorry, that's invalid city. Try again.")
        continue
      else:
        break

    # get user input for month (january, february, ... , june or all of them)

    while True:
      month = input("Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
      month = month.lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
          print("Sorry, that's invalid month. please enter a month from January until June or type All.")
          continue
      else:
          break
          
    # get user input for day of week (sunday, monday, ... , satarday or all days)

    while True:
      day = input("Are you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
      day = day.lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry, that's invalid day. try again please")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


# In[4]:


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month, day and hour

    popular_month = df['month'].mode()[0]
    popular_day = df['day_of_week'].mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print("\nMost Common Month is {}\nMost Common day is {}\nMost Common Hour is {}".format(popular_month, popular_day, popular_hour ))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station is', Start_Station)


    # display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station is', End_Station)


    # display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip are', Start_Station, " and ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hour,minute,second))

    # display mean travel time

    Mean_Travel_Time = round(df['Trip Duration'].mean())
    m,sec=divmod(Mean_Travel_Time,60)
    print("The total trip duration: {} minute(s) {} second(s)".format(m,sec))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def display_raw_data(df):
    """Displays raw data on user request."""

    print(df.head())
    next = 0
    while True:
        view_raw_data = input('Would you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next += 5
        print(df.iloc[next:next+5])


# In[14]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break                
            display_raw_data(df)
            break
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




