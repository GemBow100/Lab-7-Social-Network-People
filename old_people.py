"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
from create_db import db_path, script_dir
import sqlite3
from pprint import pprint
from openpyxl import Workbook
import pandas as pd

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    # Query the database for all information for all people.
    cur.execute('''SELECT name, age FROM people
                    WHERE age > 49''')
    # Fetch all query results.
    # The fetchall() method returns a list, where each list item
    # is a tuple containing data from one row in the people table.
    all_people = cur.fetchall()
    # Pretty print (pprint) outputs data in an easier to read format.
    pprint(all_people)
    con.commit()
    
    con.close()

    return all_people

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    
    """
    #while loop to print
    for i 
    print(f'{name} is {age} years old.')
    return name_and_age_list

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """

    DataFramelist = [] 
    for name, age in name_and_age_list:
        DataFramelist.append({'name': name,
                              'age': age})
    
    df = pd.DataFrame(DataFramelist)

    df.to_csv(csv_path,'Social Network.csv', index=False,)

    print(df)
# grab the active worksheet
    
# Data can be assigned directly to cells

# Rows can also be appended
    
# Python types will automatically be converted
    
# Save the files
    
    return

if __name__ == '__main__':
   main()