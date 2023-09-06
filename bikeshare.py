import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Would you want to explore some US bikeshare data?\n Let\'s dive in!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city = input('Which one of these beautiful cities do you want to explore? \n Chicago, New York or Washington \n').lower()
        if city in cities:
            break
        else:
            print('Sorry, I wish I can help you with some bikeshare information in {}'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        filter = input('How would you like to filter the data? month, day, or none? \n').lower()
        if filter == 'month':
            month = input('Kindly enter the month you want to explore. \n You can enter 'all', if you do not want to filter by month.\n Options: All, January, February, March, April, May, June \n').lower()
            day = 'all'
            if month in months:
                break
            else:
                print('Enter a valid month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        elif filter == 'day':
            day = input('Kindly enter the day of the week you want to explore. If you do not want to apply a weekly filter then enter 'all'. \n Options: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday \n').lower()
            month = 'all'
            if day in day:
                break
            else:
                print('kindly enter a valid day of the week')
        else:
            month = 'all'
            day = 'all'

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        popular_month = 'January'
    elif popular_month == 2:
        popular_month = 'February'
    elif popular_month == 3:
        popular_month = 'March'
    elif popular_month == 4:
        popular_month = 'April'
    elif popular_month == 5:
        popular_month = 'May'
    elif popular_month == 6:
        popular_month = 'June'
    print('Most common month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_weekday = df['day_of_week'].mode()[0]
    print('Most common day of the week: {}'.format(most_common_weekday))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    if most_common_hour < 12: 
        print('Most common start hour: {} AM'.format(most_common_hour))
    else:
        print('Most common start hour: {} PM'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df['Start Station'] + ' and ' + df['End Station']
    common_stations = station_combination.mode()[0]
    print('Most frequent combination of start station and end station trip: {}'.format(common_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The total trip duration: {} seconds'.format(total_trip_duration))

    # TO DO: display mean travel time
    avg_duration = round(df['Trip Duration'].mean())
    print('The average duration of trips: {}'.format(avg_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = [


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
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
