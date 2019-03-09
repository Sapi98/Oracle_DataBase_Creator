import cx_Oracle

username = input('Enter the Username : ').strip()
password = input('Enter the Password : ').strip()
conn = cx_Oracle.connect('username/password@orcl')
cursor = conn.cursor()
