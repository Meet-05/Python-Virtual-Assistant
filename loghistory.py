#the inserthistory method logs the commands in the postgress databas inside a table called history
import psycopg2
from datetime import date
from datetime import datetime

def inserthistory(search_text):
    # establishing connection
    con = psycopg2.connect(
        host='localhost',
        database='Auth',
        user='postgres',
        password='00000000')
    cur = con.cursor()


    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    s=search_text
    cur.execute("insert into history values(%s,%s)",(dt_string,s))
    cur.close()
    con.commit()
    return