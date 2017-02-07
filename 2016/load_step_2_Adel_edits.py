__author__ = 'djff'

'''
    load_step_2_Dec29_2016.py is a python script that is used
    to load CV's and structure data in the sqlite
    database.
    it uses xlrd to handle the xlsx files, load, read
    data and workbook sheets from the file.
'''

from step_variables import *

from setup import *

# ****************************************************************************************************************** #
#                                                                                                                    #
#                                         This is the class to load CV data                                          #
#                                                                                                                    #
# ****************************************************************************************************************** #

class Load_CV_To_DB(Parse_Excel_File, DB_Setup):
    """
        Load_CV_To_DB inherits methods from Parse_Excel_Files
        and DB_Setup classes so as to parse excel file and load
        subsequent data received from parser
    """

    def __init__(self, filename):
        super(Load_CV_To_DB, self).__init__(filename)
        self.__session = self.init()
        self.work_sheet = self.parse_object_control_value(cv_sheets_ordered)

    def load_data(self, sheet_names):
        """
            load_data() takes a list of sheet names and using
            the dictionary of rows return from the excel parser
            it load the data in the appropriate table
            :param sheet_names:
            :return: None
        """

        foreing_key = -1
        for sheet_name, sheet_rows in self.work_sheet.items():
            for row in sheet_rows[row_start_cv[sheet_name]:]:
                row = [cell.value for cell in row]
                if sheet_name == sheet_names[0]:
                    object_cat_cv = sq.ObjectCategoryCV()
                    object_cat_cv.ObjectCategoryNameCV = row[0]
                    object_cat_cv.CategoryDefinition = row[1]
                    self.push_data(object_cat_cv)

                elif sheet_name == sheet_names[1]:
                    attrib_cat_cv = sq.AttributeCategoryCV()
                    attrib_cat_cv.AttributeCategoryNameCV = row[0]
                    attrib_cat_cv.CategoryDefinition = row[1]
                    self.push_data(attrib_cat_cv)

                elif sheet_name == sheet_names[2]:
                    attrib_cv = sq.AttributesCV()
                    attrib_cv.AttributeNameCV = row[0]
                    attrib_cv.AttributeDefinition = row[1]
                    if row[foreing_key]:
                        attrib_cv.AttributeCategoryCVID = self.__session.query(sq.AttributeCategoryCV).filter(
                            sq.AttributeCategoryCV.AttributeCategoryNameCV == row[2]
                        ).first().AttributeCategoryCVID
                    self.push_data(attrib_cv)

                elif sheet_name == sheet_names[3]:
                    if all('' == cell for cell in row):
                        break
                    attrib_type_cv = sq.AttributeTypes()
                    attrib_type_cv.AttributeTypeCV = row[0]
                    attrib_type_cv.Definition = row[1]
                    self.push_data(attrib_type_cv)

                elif sheet_name == sheet_names[4]:
                    object_type_cv = sq.ObjectTypesCV()
                    object_type_cv.ObjectTypeCV = row[0]
                    object_type_cv.ObjectTopologyCV = row[1]
                    object_type_cv.ObjectDefinition = row[2]
                    if row[3]:
                        object_type_cv.ObjectCategoryID = self.__session.query(sq.ObjectCategoryCV).filter(
                            sq.ObjectCategoryCV.ObjectCategoryNameCV == row[3]
                        ).first().ObjectCategoryCVID
                    self.push_data(object_type_cv)

                elif sheet_name == sheet_names[5]:
                    units_cv = sq.Units()
                    units_cv.UnitNameCV = row[0]
                    units_cv.UnitType = row[1]
                    units_cv.UnitAbbreviation = row[2]
                    units_cv.UnitSystem = row[3]
                    self.push_data(units_cv)
        self.close_db()


# ****************************************************************************************************************** #
#                                                                                                                    #
#                                         This is the class to load Structure data                                   #
#                                                                                                                    #
# ****************************************************************************************************************** #

class Load_Struct_To_DB(Parse_Excel_File, DB_Setup):
    """
        Load_Struct_To_DB inherits methods from Parse_Excel_Files
        and DB_Setup classes so as to parse excel file and load
        subsequent data received from parser
    """

    def __init__(self, filename):
        super(Load_Struct_To_DB, self).__init__(filename)
        self.__session = self.init()
        self.work_sheet = self.parse_object_control_value(struct_sheets_ordered)

    def load_data(self, sheet_names):
        """
            load_data() takes a list of shit names and using
            the dictionary of rows return from the excel parser
            it load the data in the appropriate table
            :param sheet_names:
            :return: None
        """

        for sheet_name, sheet_rows in self.work_sheet.items():
            for row in sheet_rows[row_start_struct[sheet_name]:]:
                if sheet_name == sheet_names[0]:
                    obj_cat = sq.ObjectCategory()
                    obj_cat.ObjectCategoryName = row[0].value
                    obj_cat.CategoryDefinition = row[1].value
                    self.push_data(obj_cat)

                elif sheet_name == sheet_names[1]:
                    attrib_cat = sq.AttributeTypes()
                    attrib_cat.Term = row[0].value
                    attrib_cat.Definition = row[1].value
                    self.push_data(attrib_cat)

                elif sheet_name == sheet_names[2]:
                    data_struct = sq.Datasets()
                    data_struct.DatasetName = row[0].value
                    data_struct.DatasetAcronym = row[1].value
                    data_struct.SourceID = self.__session.query(sq.Sources).filter(
                        sq.Sources.SourceName == row[2].value
                    ).first().SourceID
                    self.push_data(data_struct)

                elif sheet_name == sheet_names[3]:
                    if all('' == cell.value for cell in row):
                        break
                    obj_type = sq.ObjectTypes()
                    obj_type.ObjectType = row[0].value
                    obj_type.ObjectCode = row[1].value
                    obj_type.ObjectTopology = row[2].value

                    if row[3].value:
                        obj_type.DatasetID = self.__session.query(sq.Datasets).filter(
                            sq.Datasets.DatasetAcronym == row[3].value
                        ).first().DatasetID

                    if row[4].value:
                        obj_type.ObjectTypeCVID = self.__session.query(sq.ObjectTypesCV).filter(
                            sq.ObjectTypesCV.ObjectTypeCV == row[4].value
                        ).first().ObjectTypeCVID

                    obj_type.MapColor = row[5].value
                    obj_type.MapSymbol = row[6].value

                    if row[7].value:
                        obj_type.ObjectCategoryID = self.__session.query(sq.ObjectCategory).filter(
                            sq.ObjectCategory.ObjectCategoryName == row[7].value
                        ).first().ObjectCategoryID

                    obj_type.Description = row[8].value
                    self.push_data(obj_type)

                elif sheet_name == sheet_names[4]:
                    attrib = sq.Attributes()
                    attrib.AttributeName = row[0].value
                    attrib.ObjectTypeID = self.__session.query(sq.ObjectTypes).filter(
                        sq.ObjectTypes.ObjectCode == row[1].value
                    ).first().ObjectTypeID
                    attrib.AttributeCode = row[2].value
                    attrib.UnitCVID = self.__session.query(sq.Units).filter(
                        sq.Units.UnitNameCV == row[3].value
                    ).first().UnitCVID
                    attrib.AttributeTypeCVID = self.__session.query(sq.AttributeTypes).filter(
                        sq.AttributeTypes.AttributeTypeCV == row[4].value
                    ).first().AttributeTypeCVID
                    attrib.AttributeNameCVID = self.__session.query(sq.AttributesCV).filter(
                        sq.AttributesCV.AttributeNameCV == row[5].value
                    ).first().AttributeCVID

                    attrib.ModelInputOrOutput = row[7].value
                    attrib.AttributeDescription = row[8].value
                    self.push_data(attrib)
        self.close_db()


# Main function to load both data
def main():
    parse_cv = Load_CV_To_DB('WaMDaM_InputData.xlsx')
    parse_cv.load_data(cv_sheets_ordered)

    parse_struct = Load_Struct_To_DB('WaMDaM_InputData.xlsx')
    parse_struct.load_data(struct_sheets_ordered)
