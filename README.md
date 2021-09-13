# Python Script to Explore US Bikeshare Data

This project Uses Python to understand U.S. bikeshare data. Calculate statistics and build an interactive environment where a user chooses and filter for a dataset to analyze.
# overview
# How to run the script

You can run the script using a Python integrated development environment (IDE) such as **Spyder**. To install Spyder, you will need to download the Anaconda installer. This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing Anaconda, you will find the Spyder IDE by opening Anaconda Navigator.

## Dataset

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

-   Start Time (e.g., 2017-01-01 00:07:57)
-   End Time (e.g., 2017-01-01 00:20:53)
-   Trip Duration (in seconds - e.g., 776)
-   Start Station (e.g., Broadway & Barry Ave)
-   End Station (e.g., Sedgwick St & North Ave)
-   User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

-   Gender
-   Birth Year

## Files

-   chicago.csv
-   new_york_city.csv
-   washington.csv
-   bikeshare.py

## Questions explored

The script answers the following questions about the bike share data:

-   What is the most popular month for start time?
 
-   What is the most popular day of week (Monday, Tuesday, etc.) for start time?
 
-   What is the most popular hour of day for start time?
 
-   What is the total trip duration and average trip duration?
 
-   What is the most popular start station and most popular end station?
 
-   What is the most popular trip?
 
-   What are the counts of each user type?
 
-   What are the counts of gender?

-   What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most 			popular birth years?

## Resources referred to complete this project

**Use parse_dates to recognize datetime columns:**

-   [https://stackoverflow.com/questions/21269399/datetime-dtypes-in-pandas-read-csv](https://stackoverflow.com/questions/21269399/datetime-dtypes-in-pandas-read-csv)
-   [https://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates](https://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates)
-   [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)

**Assess datetime series:**

-   [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html)
-   [https://stackoverflow.com/questions/29366572/pandas-how-to-filter-most-frequent-datetime-objects](https://stackoverflow.com/questions/29366572/pandas-how-to-filter-most-frequent-datetime-objects)

**Filter date:**

-   [https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates](https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates)

**Check validity of date:**

-   [https://stackoverflow.com/questions/9987818/in-python-how-to-check-if-a-date-is-valid/9987935](https://stackoverflow.com/questions/9987818/in-python-how-to-check-if-a-date-is-valid/9987935)

**Add a day to a date:**

-   [http://www.pressthered.com/adding_dates_and_times_in_python/](http://www.pressthered.com/adding_dates_and_times_in_python/)

**Read day of week, month, hour etc.:**

-   [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html)
-   [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.dayofweek.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.dayofweek.html)

**Convert seconds to hours, minutes and seconds:**

-   [https://stackoverflow.com/questions/775049/how-to-convert-seconds-to-hours-minutes-and-seconds](https://stackoverflow.com/questions/775049/how-to-convert-seconds-to-hours-minutes-and-seconds)
-   [https://docs.python.org/3/library/functions.html#divmod](https://docs.python.org/3/library/functions.html#divmod)

**Convert pandas series or dataframes to string:**

-   [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.to_string.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.to_string.html)
-   [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_string.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_string.html)

**Concatenate strings of two columns:**

-   [https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python](https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python)
-   [http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.cat.html#pandas.Series.str.cat](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.cat.html#pandas.Series.str.cat)

**Set column widths:**

-   [https://pandas.pydata.org/pandas-docs/stable/options.html](https://pandas.pydata.org/pandas-docs/stable/options.html)
-   [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.set_option.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.set_option.html)