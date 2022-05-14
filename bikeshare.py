import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print("Hello! Let\'s explore some US bikeshare data!")


def get_filters():
    """
    #Asks user to specify a city, month, and day to analyze.

    #Returns:
     #   (str) city - name of the city to analyze
      #  (str) month - name of the month to filter by, or "all" to apply no month filter
       # (str) day - name of the day of week to filter by, or "all" to apply no day filter
    #"""

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True: #User input check
        city = input('Choose a city! (Chicago, New York City, or Washington):')
        city = city.casefold() #Removes case sensitivity
        if city not in ('chicago', 'new york city', 'washington'):
            print("Try again!")
        else:
            print("Good Choice!")
            break  
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True: #User input check
        month = input("Which month are you interested in? (all, january, february, ... , june):")
        month = month.casefold() #Removes case sensitivity
       
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Try again!")
        else:
            print("Great Month(s), Champ!")  
            break  
              
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: #User input check
        day = input("Which day of the week are you interested in? (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday):")
        day = day.casefold() #Removes case sensitivity
        
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Try again!")
        else:
            print("Great Day, Champ!")
            break 
            
    print('-'*40)
    return city, month, day
    
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
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }     
    df = pd.read_csv(CITY_DATA[city])
    
    # Add Start End Column
    df['Start_End'] = df['Start Station'] +' TO '+ df['End Station']

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #find mode
    #find unique values in array along with their counts
    vals, counts = np.unique(df['month'], return_counts=True)
    mode_value = np.argwhere(counts == np.max(counts))
    
     # use the index of the months list to get the corresponding int
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months[int(mode_value)]
    
    print('The most common month to bike is ', month)
    
    # TO DO: display the most common day of week
    vals, counts = np.unique(df['day_of_week'], return_counts=True)
    
    mode_value = np.argwhere(counts == np.max(counts))
     # use the index of the months list to get the corresponding int
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = days[int(mode_value)]
    
    print('The most common day to bike is ', day)
    
   

    # TO DO: display the most common start hour
    
    vals, counts = np.unique(df['hour'], return_counts=True)
    
    hour_value = np.argwhere(counts == np.max(counts))

    hour = hour_value + 1
    
    print('The most common start hour is ', int(hour),'00')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return vals, counts, mode_value, month, day, hour

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    vals, counts = np.unique(df['Start Station'], return_counts=True)
    
    mode_value = np.argwhere(counts == np.max(counts))
    
    # mode of the specific column
    start_station_mode = df.loc[:,"Start Station"].mode()
    
    print('The most popular Start Location is: ', start_station_mode.to_string(index = False))

    # TO DO: display most commonly used end station
    end_station_mode = df.loc[:,"End Station"].mode()
    
    print('The most popular End Location is: ', end_station_mode.to_string(index = False))

    # TO DO: display most frequent combination of start station and end station trip
    trip_mode = df.loc[:,"Start_End"].mode()
    
    print('The most popular Trip is: ', trip_mode.to_string(index = False))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return start_station_mode, end_station_mode, trip_mode
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_seconds = df['Trip Duration'].sum()
    
    sum_minutes = np.floor(sum_seconds / 60)
    seconds = sum_seconds % 60
    
    sum_hours = np.floor(sum_minutes / 60)
    minutes = sum_minutes % 60
    
    sum_days = np.floor(sum_minutes / 24)
    hours = sum_hours % 24
    
    sum_years = np.floor(sum_days / 365)
    days = sum_days % 365
    
    print('Total Trip Duration All-Time: ' , sum_years , ' years, ' , days , ' days, ' , hours , ' hours, ' , minutes , ' minutes, ' , seconds , ' seconds.')
    
    # TO DO: display mean travel time
    avg_seconds = df['Trip Duration'].mean()
    
    avg_minutes = np.floor(avg_seconds / 60)
    seconds = avg_seconds % 60
    
    avg_hours = np.floor(avg_minutes / 60)
    minutes = avg_minutes % 60
    
    avg_days = np.floor(avg_minutes / 24)
    hours = avg_hours % 24
    
    avg_years = np.floor(avg_days / 365)
    days = avg_days % 365
    
    print('Average Trip Duration All-Time: ' , avg_years , ' years, ' , days , ' days, ' , hours , ' hours, ' , minutes , ' minutes, ' , seconds , ' seconds.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
  
    subcounts = df[df['User Type'] == 'Subscriber']['User Type'].count()
    customer_counts = df[df['User Type'] == 'Customer']['User Type'].count()

    print('There are ', customer_counts, 'customers and ', subcounts, 'subscribers.')
    
    # TO DO: Display counts of gender
     
    guy_counts = df[df['Gender'] == 'Male']['Gender'].count()
    girl_counts = df[df['Gender'] == 'Female']['Gender'].count()
    print('Male: ', guy_counts, 'Female: ', girl_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    early_birth = df['Birth Year'].min()
    late_birth = df['Birth Year'].max()
    common_birth = df.loc[:,'Birth Year'].mode()
    
    print('The oldest rider was born in ', int(early_birth), '. The youngest rider was born in ', int(late_birth), '. The most common birth year of riders was ', int(common_birth))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 
    
def main():
    ### Main code to initiate each function
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
