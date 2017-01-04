__author__ = 'djff'

'''
    load_step_4.py is a python script that is used
    to load some CV's of Data Values to the sqlite
    database.
    it uses xlrd to handle the xlsx files, load, read
    data and workbook sheets from the file.
'''

from setup import *
from step_variables import DataValues_ordered


class Load_Data_Values(Parse_Excel_File, DB_Setup):
    def __init__(self, filename):
        super(Load_Data_Values, self).__init__(filename)
        self.__session = self.init()
        self.work_sheet = self.parse_object_control_value(DataValues_ordered[:])

    def load_data(self):
        for sheet_name, sheet_rows in self.work_sheet.items():
            temp = sheet_rows[:]
            for row_id, row in enumerate(temp):
                if sheet_name == DataValues_ordered[0]:
                    temp_row = [cell.value for cell in row]
                    if 'SeasonName,' in temp_row:
                        cur_table = sheet_rows[row_id + 3:]
                        for row_id, row in enumerate(cur_table):
                            if all('' == cell.value for cell in row):
                                break
                            Season_Name = sq.SeasonName()
                            Season_Name.SeasonNameCV = row[0].value
                            Season_Name.Definition = row[1].value
                            self.push_data(Season_Name)
                        break
                if sheet_name == DataValues_ordered[0]:
                    temp_row = [cell.value for cell in row]
                    if 'FileFormat,' in temp_row:
                        cur_table = sheet_rows[row_id + 3:]
                        for row_id, row in enumerate(cur_table):
                            if all('' == cell.value for cell in row):
                                break
                            File_Format = sq.FileFormat()
                            File_Format.FileFormatCV = row[0].value
                            File_Format.Definition = row[1].value
                            self.push_data(File_Format)
                        break
                if sheet_name == DataValues_ordered[0]:
                    temp_row = [cell.value for cell in row]
                    if 'AggregationStatistic,' in temp_row:
                        cur_table = sheet_rows[row_id + 3:]
                        for row_id, row in enumerate(cur_table):
                            if all('' == cell.value for cell in row):
                                break
                            Aggregation_Statistic = sq.AggregationStatistic()
                            Aggregation_Statistic.AggregationStatisticCV = row[0].value
                            Aggregation_Statistic.Definition = row[1].value
                            self.push_data(Aggregation_Statistic)
                        break

if __name__ == '__main__':
    instance = Load_Data_Values('./WaMDaM_InputData.xlsx')
    instance.load_data()
