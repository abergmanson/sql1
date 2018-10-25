#Create a SQLite Database and table

import sqlite3

#create a new database if it doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL
cursor = conn.cursor()

#insert data
cursor.execute("INSERT INTO population VALUES('New York City',  \
        'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco',  \
        'CA', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()