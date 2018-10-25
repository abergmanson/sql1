import sqlite3

with sqlite3.connect("new.db") as connection:

    c = connection.cursor()

    c.execute("""SELECT population.city, population.population, regions.region 
            FROM population, regions WHERE population.city = regions.city ORDER BY population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print("city: ", r[0])
        print("population: ", str(r[1]))
        print("region: ", r[2])
        print("")

