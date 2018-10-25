import sqlite3

with sqlite3.connect("cars.db") as connection:

    c = connection.cursor()


    #c.execute("""CREATE TABLE orders
    #        (make TEXT, model TEXT, order_date TEXT)
    #        """)

    orderdata = [
        ("Ford", "Focus", "2003-01-08"),
        ("Ford", "Fiesta", "1999-08-11"),
        ("Ford", "Mustang", "2010-11-19"),
        ("Honda", "CR-V", "2018-01-13"),
        ("Honda", "Accord", "2017-03-03"),
        ("Ford", "Focus", "2018-05-30"),
        ("Ford", "Fiesta", "2017-02-02"),
        ("Ford", "Mustang", "2010-12-31"),
        ("Honda", "CR-V", "2018-08-16"),
        ("Honda", "Accord", "2016-07-12"),
        ("Ford", "Focus", "2015-07-17"),
        ("Ford", "Fiesta", "2011-11-01"),
        ("Ford", "Mustang", "2008-09-11"),
        ("Honda", "CR-V", "2005-04-02"),
        ("Honda", "Accord", "2012-10-09")
    ]

    #c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orderdata)

    c.execute("""SELECT orders.make, orders.model, inventory.quantity, orders.order_date 
            FROM orders, inventory WHERE orders.model =
            inventory.model ORDER BY orders.make, orders.model ASC""")

    rows = c.fetchall()

    prevmake = ""

    for r in rows:
        if (prevmake != r[1]):
            print(r[0], r[1])
            print(r[2])
            #print(r[3])
        print(r[3])
        prevmake = r[1]
