#Create a SQLite Database and table

import sqlite3

#create a new database
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

# close the database connection
conn.close()