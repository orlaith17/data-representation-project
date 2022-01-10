import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = db.cursor()
sql="select * from stock"

cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print (x)