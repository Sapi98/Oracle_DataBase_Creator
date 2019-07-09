import cx_Oracle
import random as r
from dataset_utils import *


class Essentials:

    def __init__(self):
        pass

    @staticmethod
    def gen_date(self, x):
        day = r.randint(1, 28)
        month = r.choice(x.months)
        year = r.randint(1950, 2019)
        date = str(day)+'-'+month+'-'+str(year)
        return date

    @staticmethod
    def gen_string(self, x, length=0, first_names=[], last_names=[], mid_names=[]):
        name = None
        if first_names == [] and last_names == []:
            name = r.choice(x.cap_char_bank)
            length -= 1
            for _ in range(length):
                name = name + r.choice(x.small_char_bank)
        elif first_names != [] and last_names != []:
            mid = ''
            if mid_names != []:
                mid = r.choice(mid_names) + ' '
            name = r.choice(first_names) + ' ' + mid + r.choice(last_names)

        return name


class Control(Essentials, CreateDataset):

    def __init__(self):
        Essentials.__init__()
        CreateDataset.__init__()

        self.cap_char_bank = [chr(i) for i in range(65, 91)]
        self.small_char_bank = [chr(i) for i in range(97, 123)]

        chances = 3
        self.cursor = None
        self.conn = None

        while chances >= 0:
            try:
                self.initialize()
                break

            except:
                print('!!!You have entered wrong Username or Password!!!')
                chances -= 1
                if chances == 0:
                    exit(0)
                else:
                    print('You have {0} tries left'.format(chances))

        self.initialize()
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
        try:
            self.conn = cx_Oracle.connect(connect_query)
        except:
            print('Wrong, username / password')
            return 0
        self.cursor = self.conn.cursor()
        return 1



if __name__ == '__main__':
    e = Essentials()
