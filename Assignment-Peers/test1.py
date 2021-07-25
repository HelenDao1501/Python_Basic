import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('CREATE TABLE Ages(name VARCHAR(128), age INTEGER)')
cur.execute('DELETE FROM Ages')
cur.execute("INSERT INTO Ages (name, age) VALUES ('Beinn', 20)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Laurel', 35)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Tylar', 33)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Aon', 31)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Nasifa', 24)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Rudi', 33)")
cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")

for row in cur:
    print (row)
