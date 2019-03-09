import cx_Oracle
import random as r
import datetime as dt

def genDate():
    day = r.randint(1, 28)
    month = r.choice()
    year = r.randint(1950, 2019)
    date = str(day)+'-'+month+'-'+str(year)
    return date

username = input('Enter the Username : ').strip()
password = input('Enter the Password : ').strip()
conn = cx_Oracle.connect('username/password@orcl')
cursor = conn.cursor()
tableName = input('Enter the table name : ')
attrib = dict()
c = int(input('Enter the number of Columns present in the table : '))
for i in range(c):
    col = input('Enter Column Name ' + str(i+1) + ' : ')
    dtype = input('Enter the Data Type : ')
    attrib[col] = dtype
n = int(input('Enter the no of entries you want to enter : '))
months = [
    'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
    'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
]

