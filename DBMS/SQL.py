import sqlite3

con = sqlite3.connect("data.db")
cursor = con.cursor()
"""con.execute(''' CREATE TABLE hotel
         (FIND INT PRIMARY KEY     NOT NULL,
         FNAME           TEXT    NOT NULL,
         COST            INT     NOT NULL,
         WEIGHT        INT);
         ''')"""
con.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )")
con.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )")
con.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )")
print("All data in food table\n")
cursor.execute("SELECT * from hotel ")
 
# display all data from hotel table
for row in cursor:
    print(row)