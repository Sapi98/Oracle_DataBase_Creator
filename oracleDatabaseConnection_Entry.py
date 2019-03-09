import cx_Oracle

username = input('Enter the Username : ').strip()
password = input('Enter the Password : ').strip()
conn = cx_Oracle.connect('username/password@orcl')
cursor = conn.cursor()
tableName = input('Enter the table name : ')
attrib = input('Enter the Column Names with spaces : ').strip().split()
