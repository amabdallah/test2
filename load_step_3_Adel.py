__author__ = 'djff'

'''
    load_step_3_Jan3_2017.py is a python script that is used
    to load CV's and Networks data in the sqlite
    database.
    it uses xlrd to handle the xlsx files, load, read
    data and workbook sheets from the file.
'''

from setup import *
from step_variables import Network_sheets_ordered


class Load_Networks_Data(Parse_Excel_File, DB_Setup):
    def __init__(self, filename):
        super(Load_Networks_Data, self).__init__(filename)
        self.__session = self.init()
        self.work_sheet = self.parse_object_control_value(Network_sheets_ordered[:])

    def load_data(self):
        for sheet_name, sheet_rows in self.work_sheet.items():
            temp = sheet_rows[:]
            for row_id, row in enumerate(temp):
                if sheet_name == Network_sheets_ordered[0]:
                    temp_row = [cell.value for cell in row]
                    if 'SpatialReferenceCV' in temp_row:
                        cur_table = sheet_rows[row_id + 3:]
                        for row_id, row in enumerate(cur_table):
                            if all('' == cell.value for cell in row):
                                break
                            Spatial_Reference = sq.SpatialReference()
                            Spatial_Reference.SRSCode = row[0].value
                            Spatial_Reference.SRSNameCV = row[1].value
                            Spatial_Reference.SRSWebpage = row[2].value
                            Spatial_Reference.SRSDescription = row[3].value
                            self.push_data(Spatial_Reference)
                        break
                if sheet_name == Network_sheets_ordered[0]:
                    temp_row = [cell.value for cell in row]
                    if 'VerticalDatum,' in temp_row:
                        cur_table = sheet_rows[row_id + 3:]
                        for row_id, row in enumerate(cur_table):
                            if all('' == cell.value for cell in row):
                                break
                            Vertical_Datum = sq.VerticalDatum()
                            Vertical_Datum.VerticalDatumCV = row[0].value
                            Vertical_Datum.Definition = row[1].value
                            self.push_data(Vertical_Datum)
                        break

                if sheet_name == Network_sheets_ordered[0]:
                    temp_row = [cell.value for cell in row]
                    if 'InstanceNames,' in temp_row:
                        cur_table = sheet_rows[row_id + 3:]
                        for row_id, row in enumerate(cur_table):
                            if all('' == cell.value for cell in row):
                                break
                            Instance_Names = sq.InstanceNames()
                            Instance_Names.InstanceNameCV = row[0].value
                            Instance_Names.Definition = row[1].value
                            self.push_data(Instance_Names)
                        break

                    if sheet_name == Network_sheets_ordered[0]:
                        temp_row = [cell.value for cell in row]
                        if 'MasterNetworks,' in temp_row:
                            cur_table = sheet_rows[row_id + 3:]
                            for row_id, row in enumerate(cur_table):
                                if all('' == cell.value for cell in row):
                                    break
                                Master_Networks = sq.MasterNetworks()
                                Master_Networks.MasterNetworkName = row[0].value
                                Master_Networks.SpatialReferenceCVID = row[1].value
                                Master_Networks.VerticalDatumCVID = row[1].value
                                Master_Networks.Description = row[1].value
                                self.push_data(Master_Networks)
                            break

                    if sheet_name == Network_sheets_ordered[0]:
                        temp_row = [cell.value for cell in row]
                        if 'Scenarios,' in temp_row:
                            cur_table = sheet_rows[row_id + 3:]
                            for row_id, row in enumerate(cur_table):
                                if all('' == cell.value for cell in row):
                                    break
                                Scenario = sq.Scenarios()
                                Scenario.ScenarioName = row[0].value
                                Scenario.StartTime = row[1].value
                                Scenario.EndTime = row[1].value
                                Scenario.TimeStep = row[1].value
                                Scenario.TimeStepUnitCVID = row[1].value
                                Scenario.Description = row[1].value
                                Scenario.MasterNetworkID = row[1].value

                                self.push_data(Scenario)
                            break




if __name__ == '__main__':
    instance = Load_Networks_Data('./WaMDaM_InputData.xlsx')
    instance.load_data()
