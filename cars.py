import sqlite3

with sqlite3.connect("cars.db") as connection:

    c = connection.cursor()

    c.execute("""CREATE TABLE inventory
            (make TEXT, model TEXT, quantity INT)
            """)

    cardata = [
        ("Ford", "Focus", 4),
        ("Ford", "Fiesta", 8),
        ("Ford", "Mustang", 3),
        ("Honda", "CR-V", 1),
        ("Honda", "Accord", 10)
    ]

    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", cardata)