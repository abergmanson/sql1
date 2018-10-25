import sqlite3

with sqlite3.connect("newnum.db") as connection:

    c = connection.cursor()

    print("0 = MAX, 1 = MIN, 2 = AVG,3 = COUNT, 4 = SUM, 5 = EXIT")
    print("")