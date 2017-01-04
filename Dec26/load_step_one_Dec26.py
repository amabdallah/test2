__author__ = 'djff'

'''
    load_step_one.py is a python script that is used
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
            for row in sheet_rows[4:]:
                row = [cell.value for cell in row]
                if sheet_name == sheet_names[0]:
                    object_cat_cv = sq.ObjectCategoryCV()
                    object_cat_cv.ObjectCategoryCVName, \
                        object_cat_cv.CategoryDefinition = tuple(row)
                    self.push_data(object_cat_cv)

                elif sheet_name == sheet_names[1]:
                    attrib_cat_cv = sq.AttributeCategoryCV()
                    attrib_cat_cv.AttributeCategoryNameCV, \
                        attrib_cat_cv.CategoryDefinition = tuple(row)
                    self.push_data(attrib_cat_cv)

                elif sheet_name == sheet_names[2]:
                    attrib_cv = sq.AttributesCV()
                    attrib_cv.AttributeNameCV, \
                        attrib_cv.AttributeDefinition = tuple(row[:foreing_key])
                    if row[foreing_key]:
                        attrib_cv.AttributeCategoryCVID = self.__session.query(sq.AttributeCategoryCV).filter(
                            sq.AttributeCategoryCV.AttributeCategoryNameCV == row[foreing_key]
                        ).first().AttributeCategoryCVID
                    self.push_data(attrib_cv)

                elif sheet_name == sheet_names[3]:
                    attrib_type_cv = sq.AttributeTypes()
                    attrib_type_cv.AttributeTypeCV, \
                        attrib_type_cv.Definition = tuple(row)
                    self.push_data(attrib_type_cv)

                elif sheet_name == sheet_names[4]:
                    object_type_cv = sq.ObjectTypesCV()
                    object_type_cv.ObjectType, \
                        object_type_cv.ObjectTopology, \
                        object_type_cv.ObjectDefinition = tuple(row[:foreing_key])
                    if row[foreing_key]:
                        object_type_cv.ObjectCategoryCVID = self.__session.query(sq.ObjectCategoryCV).filter(
                            sq.ObjectCategoryCV.ObjectCategoryName == row[foreing_key]
                        ).first().ObjectCategoryCVID
                    self.push_data(object_type_cv)

                elif sheet_name == sheet_names[5]:
                    units_cv = sq.Units()
                    units_cv.UnitNameCV, \
                        units_cv.UnitType, \
                        units_cv.UnitAbbreviation, \
                        units_cv.UnitSystem = tuple(row)
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
            for row in sheet_rows[4:]:
                if sheet_name == sheet_names[0]:
                    data_struct = sq.Dataset()
                    data_struct.DatasetName = row[0].value
                    data_struct.DataStrucutureAcronym = row[1].value
                    data_struct.DatasetWebpage = row[2].value
                    data_struct.DatasetDescription = row[3].value
                    self.push_data(data_struct)

                elif sheet_name == sheet_names[1]:
                    obj_cat = sq.ObjectCategory()
                    obj_cat.CategoryName = row[0].value
                    obj_cat.CategoryDefinition = row[1].value
                    self.push_data(obj_cat)

                elif sheet_name == sheet_names[2]:
                    attrib_cat = sq.AttributeTypes()
                    attrib_cat.Term = row[0].value
                    attrib_cat.Definition = row[1].value
                    self.push_data(attrib_cat)

                elif sheet_name == sheet_names[3]:
                    attrib = sq.Attributes()
                    attrib.AttributeName = row[0].value
                    attrib.AttributeCode = row[1].value

                    if row[2].value:
                        try:
                            attrib.UnitCVID = self.__session.query(sq.Units).filter(
                                sq.Units.UnitNameCV == row[2].value
                            ).first().UnitCVID
                        except:
                            pass

                    if row[3].value:
                        attrib.AttributeNameCVID = self.__session.query(sq.AttributesCV).filter(
                            sq.AttributesCV.AttributeName == row[3].value
                        ).first().AttributeID

                    attrib.AttributeCategory = row[4].value
                    attrib.AttributeDescription = row[5].value
                    self.push_data(attrib)

                elif sheet_name == sheet_names[4]:
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
                            sq.ObjectTypesCV.ObjectType == row[4].value
                        ).first().ObjectTypeID

                    obj_type.MapColor = row[5].value
                    obj_type.MapSymbol = row[6].value

                    if row[7].value:
                        obj_type.ObjectCategoryID = self.__session.query(sq.ObjectCategory).filter(
                            sq.ObjectCategory.CategoryName == row[7].value
                        ).first().ObjectCategoryID

                    obj_type.Description = row[8].value
                    self.push_data(obj_type)

                elif sheet_name == sheet_names[5]:
                    pass
        self.close_db()


# Main function to load both data
def main():
    parse_cv = Load_CV_To_DB('WaMDaM_InputData.xlsx')
    parse_cv.load_data(cv_sheets_ordered)

    parse_struct = Load_Struct_To_DB('WaMDaM_InputData.xlsx')
    parse_struct.load_data(struct_sheets_ordered)
