__author__ = 'djff'


# Sheet Names for step 1 loading in order of dependency, independent to dependent.

metadata_sheets_ordered = ['StaticCVs', '1.1_Organiz&People', '1.2_Sources', '1.3_Methods']



# Sheet Names for step 2 loading in order of dependency independent to dependent.

cv_sheets_ordered = ['ObjectCategoryCV', 'AttributeCategoryCV', 'AttributesCV', 'StaticCVs',
                     'ObjectTypesCV', 'UnitsCV']

row_start_cv = {'ObjectCategoryCV': 6, 'AttributeCategoryCV': 6, 'AttributesCV': 6, 'StaticCVs': 5,
                'ObjectTypesCV': 6, 'UnitsCV': 8}


struct_sheets_ordered = ['1_ObjectCategory', '1_AttributeCategory', '2.1_Dataset', '2.2_ObjectTypes',
                         '2.3_Attributes']

row_start_struct = {'1_ObjectCategory': 7, '1_AttributeCategory': 6, '2.1_Dataset': 7, '2.2_ObjectTypes': 8,
                    '2.3_Attributes': 8}


# Sheet Names for step 3 loading in order
Network_sheets_ordered = ['StaticCVs','3.1_Networks&Scenarios','InstanceNameCV']


# Sheet Names for step 4 loading in order
DataValues_ordered = ['StaticCVs','SeasonNameCV']
