import sqlite3

with sqlite3.connect("cars.db") as connection:

    c = connection.cursor()

    c.execute("SELECT * FROM inventory")

    invrows = c.fetchall()

    for i in invrows:
        print(i[0], i[1])
        print(i[2])
        c.execute("SELECT count(model) FROM orders WHERE make=? and model=?", (i[0], i[1]))
        cnt = c.fetchone()
        print(cnt[0])




