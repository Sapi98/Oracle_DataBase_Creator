from openpyxl import load_workbook
import os


class Create:
    def __init__(self):
        cd = os.getcwd()
        self.path1 = cd + '/Indian_first_names.xlsx'
        self.path2 = cd + '/Indian_middle_names.xlsx'
        self.path3 = cd + '/Indian_last_names.xlsx'

    def generate_data_list(self, name_length = 2):
        wb1 = load_workbook(filename=self.path1)
        wb2 = None
        wb3 = load_workbook(filename=self.path3)

        first_names = []
        last_names = []
        middle_names = []

        if name_length == 3:
            wb2 = load_workbook(filename=self.path2)
