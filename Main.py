# Name: Giovanni De Leon
# Desc: The Burnout Machine

import pandas as pd
import matplotlib.pyplot as plt
from CompareHoursWorked import compare_hours_worked
from lLoadDataPandas import load_data_pandas

# Global Variables
df = None

# Main menu
def main_menu():
    global df

    print("Welcome to The Burnout Machine!\n")
    print("****************************************************")
    print("*[1] Load data via Pandas..........................*")
    print("*[2] Compare Hours worked and Burnout scale........*")
    print("*[3] End Program...................................*")
    print("****************************************************")
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1: # Creates pandas DataFrame with student data.
        df = load_data_pandas()
        user_choice = 0
        main_menu()

    if user_choice == 2: # Supposed to display scatter plot comparing 2 student data points.
        compare_hours_worked(df, 'Work_Hours', 'Burnout_Scale', "Hours Spent at Work", "Burnout Scale")
        user_choice = 0
        main_menu()
    #main_menu()
    if user_choice == 3: exit() # Option to end program.


# START OF PROGRAM
main_menu()
