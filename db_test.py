import sqlite3
import random
import os
from datetime import datetime


con = sqlite3.connect("darkweb7.db")
cursor = con.cursor()
if os.path.exists("darkweb10.db"):
    os.remove("darkweb10.db")
new_con = sqlite3.connect("darkweb10.db")
new_cursor = new_con.cursor()
new_cursor.execute("CREATE TABLE CrawlerTarget(onion Text PRIMARY KEY, count int, lastdate datetime, status tinyint);")
cursor.execute("select * from CrawlerTarget")
rowList = cursor.fetchall()
for row in rowList:
    onion = row[0]
    count = random.randint(1, 11)
    status = 0
    lastdate = "2023-06-" + str(random.randint(11,30))
    print(onion, count, lastdate, status)
    new_cursor.execute("INSERT INTO CrawlerTarget values(?, ?, ?, ?)", \
                (onion, count, lastdate, status))
new_con.commit()
new_cursor.close()
con.close()