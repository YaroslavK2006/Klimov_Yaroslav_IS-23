import sqlite3 as sq
from data_users import info_users

with sq.connect('saper.db') as con:
    cur = con.cursor()
   # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )""")

#cur.executemany("INSERT INTO users VALUES (1, , 'Алексей', 1, 22, 1000)")
cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)


#cur.execute("SELECT * FROM users")
cur.execute("SELECT name, score FROM users where score between 500 and 1000 and sex = 1 ")
result = cur.fetchall()
print(result)