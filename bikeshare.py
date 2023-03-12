import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """Ask user to specify city that they want"""
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        #Asks user to input city that they choose
        city = input("Choose a city name (chicago, new york city, washington): \n").lower()
        cities = ("chicago", "new york city", "washington")
        #Checks if the user input matches the cities list
        if city not in cities:
            #Handles invalid input of city
            print("City not valid. Please enter a valid city.")
            continue
        else:
            break
            
    while True:
        #Asks user to input month that they choose
        month = input("Please choose a month: january, february, march, april, may, june, all: \n").lower()
        months = ["january", "february", "march", "april", "may", "june", "all"]
        if month in months:
            break
        else:
            #Handles invalid input of month
            print("Please enter a valid month")
        
    while True:
        #Asks user to input day that they choose
        day = input("Please choose a day: sunday, monday, tuesday, wednesday, thursday, friday, saturday, all: \n").lower()
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
        if day in days:
            break
        else:
            #Handles invalid input of day
            print("Please enter a valid day")
 
    return city, month, day

    print('-'*40)
    


def load_data(city, month, day):
    """Loads data from selected city, month, and day"""
    #Loads files into DataFrame
    df = pd.read_csv(CITY_DATA[city])
    #Converts the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Takes out month, day, and hour from the Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    #Filter by month
    if month != 'all':
        #The six months available in the dataset
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #Create index for months 
        month = months.index(month) + 1
        df = df[df['month'] == month]
    #Filter by day
    if day != 'all':
        #Filter by day of the week
        df = df[df['day_of_week'] == day.title()]
    

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Displays the busiest month
    busiest_month = df['month'].mode()
    print(f"The busiest busiest month is {busiest_month[0]}")
    #Displays the busiest day
    busiest_day = df['day_of_week'].mode()
    print(f"The busiest day is: {busiest_day[0]}")
    #Displays the busiest hour
    busiest_hour = df['hour'].mode()
    print(f"The busiest hour is: {busiest_hour[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Displays most common start station
    busiest_start_station = df['Start Station'].mode()
    print(f"The busiest start station is: {busiest_start_station[0]}")
    #Displays most common end station
    busiest_end_station = df['End Station'].mode()
    print(f"The busiest end station is: {busiest_end_station[0]}")
    #Combine start station and end station 
    combination = df['Start Station'] + " "  + df['End Station']
    #Displays most frequent combination of start and end station trips
    station_combination = combination.mode()[0]
    print(f"Most frequent combination of start and end station trips are: {station_combination}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Displays total travel time
    total_travel_time = df['Trip Duration'].sum()
    #Total travel time divided by 60 in order to be converted into minutes
    print(f"The total travel time is: {(total_travel_time/60).round(1)} minutes")
    #Displays average travel time
    avg_travel_time = df['Trip Duration'].mean()
    #Average travel time divided by 60 in order to be converted into minutes
    print(f"The average travel time is: {(avg_travel_time/60).round(1)} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].mode()
    print(f"Most common User type is: {user_types[0]}")

    
    try:
        #Displays the gender that gets counted the most
        gender_count = df['Gender'].mode()
        print(f"Most common gender is: {gender_count[0]}")
    except KeyError:
        #KeyError added for if there is no data available for a certain city
        print("There is no gender for this city")

    
    try:
        #Displays earliest birth year
        earliest_birth_year = df['Birth Year'].min()
        earliest_birth_year = earliest_birth_year.astype(int)
        print(f"The earliest birth year is: {earliest_birth_year}")
    except KeyError:
        #KeyError added for if there is no data available for a certain city
        print("No data available for this city")
    try:
        #Displays most rcent year of birth
        recent_birth_year = df['Birth Year'].max()
        recent_birth_year = recent_birth_year.astype(int)
        print(f"The most recent birth year is: {recent_birth_year}")
    except KeyError:
        #KeyError added for if there is no data available for a certain city
        print("No data available for this city")
    try:
        #Displays most common birth year
        most_common_birth_year = df['Birth Year'].mode()
        most_common_birth_year = most_common_birth_year.astype(int)
        print(f"The most common birth year is: {most_common_birth_year[0]}")
    except KeyError:
        #KeyError added for if there is no data available for a certain city
        print("No data available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """ Displays 5 lines of raw data at a time when yes is selected."""
    # Defining the index (i) and starting at line 1
    i = 0
    while True:
        #Asks user if he wants to display 5 lines of raw data
        rawdata = input("Would you like to see 5 line of the raw data? Please answer with yes or no\n").lower()
        if rawdata == 'yes':
            #Prints first 5 lines
            print(df[i:i+5])
            #Increases i by 5 to display next five lines of data
            i = i+5
        else:
             #When user inputs no then the loop stops
             break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #Added to main function in order for it to be displayed 
        raw_data(df)
        #Asks user if they want to restart the process
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
