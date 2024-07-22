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
import pandas

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
    cur.execute('SELECT * FROM people')
# Fetch all query results.
# The fetchall() method returns a list, where each list item
# is a tuple containing data from one row in the people table.
    all_people = cur.fetchall('name, age')
# Pretty print (pprint) outputs data in an easier to read format.
    pprint(all_people)
    con.commit()
    con.close()

    return

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    for row in cur.execute ("Select name and age t FROM data"):
        print (row)
        rows = [
        ("Name",),
        ("Age",),
        ]
        cur.excutemany("Insert into data values(?)", rows)
        cur.executescript="""
        CREATE TABLE
        (
            name,
            age,

        )
        """


        cur.execute(rows, db_path)
        con.commit
    con.close()
    return name_and_age_list

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """

    wb = Workbook(csv_path)

# grab the active worksheet
    ws = wb.active

# Data can be assigned directly to cells
    ws['name'] = name_and_age_list

# Rows can also be appended
    ws.append([1, 2, 3])

# Python types will automatically be converted

    ws['age'] = name_and_age_list

# Save the files
    wb.save("Social Network")
    return

if __name__ == '__main__':
   main()