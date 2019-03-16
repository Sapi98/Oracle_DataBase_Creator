import cx_Oracle
import random as r
import datetime as dt


class Essentials:

    def __init__(self):
        self.cursor = None
        self.conn = None
        self.tableName = input('Enter the table name : ')
        self.attrib = dict()
        c = int(input('Enter the number of Columns present in the table : '))
        for i in range(c):
            col = input('Enter Column Name ' + str(i + 1) + ' : ')
            dtype = input('Enter the Data Type : ')
            self.attrib[col] = dtype
        self.n = int(input('Enter the no of entries you want to enter : '))
        self.months = [
            'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
            'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
        ]

    def initialize(self):
        username = input('Enter the Username : ').strip()
        password = input('Enter the Password : ').strip()
        connect_query = '{0}/{1}@{2}'.format(username, password, 'orcl')
        self.conn = cx_Oracle.connect(connect_query)
        self.cursor = self.conn.cursor()

    def gen_date(self):
        day = r.randint(1, 28)
        month = r.choice(self.months)
        year = r.randint(1950, 2019)
        date = str(day)+'-'+month+'-'+str(year)
        return date


if __name__ == '__main__':
    e = Essentials()
