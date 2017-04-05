-- 4.90 MultiColumns

/*

Adel Abdalllah
Updated April 5, 2017


This query shows data values for a particular MultiColumns of a reservoir InstanceName: area, and capacity, and stage 

Result:
Users can import these data columns to their model 
WaM-DaM keeps track of the meanings of data values, their CV_Units, to what instance they apply too.... 
*/

SELECT "ObjectTypes"."ObjectType",
"Instances"."InstanceName","Attributes"."AttributeName","Attributes".AttributeDataTypeCV,
"AttributesColumns"."AttributeName" AS "ColumName",
"AttributesColumns"."UnitNameCV" AS "ColUnitName",
"Value","ValueOrder"

FROM "Datasets"

-- Join the dataset to get its Object Types 
Left JOIN "ObjectTypes" 
ON "ObjectTypes"."DatasetID"="Datasets"."DatasetID"

-- Join the Object types to get their attributes  
Left JOIN  "Attributes"
ON "Attributes"."ObjectTypeID"="ObjectTypes"."ObjectTypeID"

-- Join the Attributes to get their Mappings   
Left JOIN "Mapping"
ON Mapping.AttributeID= Attributes.AttributeID

-- Join the Mapping to get their Instances   
Left JOIN "Instances" 
ON "Instances"."InstanceID"="Mapping"."InstanceID"

-- Join the Mappings to get their ScenarioMappings   
Left JOIN "ScenarioMapping"
ON "ScenarioMapping"."MappingID"="Mapping"."MappingID"

-- Join the ScenarioMappings to get their Scenarios   
Left JOIN "Scenarios"
ON "Scenarios"."ScenarioID"="ScenarioMapping"."ScenarioID"
AND "Scenarios"."ScenarioName"='Historical records'

-- Join the Scenarios to get their MasterNetworks   
Left JOIN "MasterNetworks" 
ON "MasterNetworks"."MasterNetworkID"="Scenarios"."MasterNetworkID"

-- Join the Mappings to get their Methods   
Left JOIN "Methods" 
ON "Methods"."MethodID"="Mapping"."MethodID"

-- Join the Mappings to get their Sources   
Left JOIN "Sources" 
ON "Sources"."SourceID"="Mapping"."SourceID"

-- Join the Mappings to get their DataValuesMappers   
Left JOIN "DataValuesMapper" 
ON "DataValuesMapper"."DataValuesMapperID"="Mapping"."DataValuesMapperID"

-- Join the DataValuesMapper to get their MultiColumnArrays   
Left JOIN "MultiColumnArrays"  
ON "MultiColumnArrays" ."DataValuesMapperID"="DataValuesMapper"."DataValuesMapperID"


/*This is extra join to get to each column name within the MultiColumn Array */

-- Join the MultiColumnArrays to get to their specific DataValuesMapper, now called DataValuesMapperColumn
Left JOIN "DataValuesMapper" As "DataValuesMapperColumn"
ON "DataValuesMapperColumn"."DataValuesMapperID"="MultiColumnArrays"."ColumnNameID"

-- Join the DataValuesMapperColumn to get back to their specific Mapping, now called MappingColumns
Left JOIN "Mapping" As "MappingColumns"
ON "MappingColumns"."DataValuesMapperID"="DataValuesMapperColumn"."DataValuesMapperID"

-- Join the MappingColumns to get back to their specific Attribute, now called AttributeColumns
Left JOIN  "Attributes" AS "AttributesColumns"
ON "AttributesColumns"."AttributeID"="MappingColumns"."AttributeID"
/* Finishes here */

-- Join the MultiColumnArrays to get access to their MultiColumnValues   
Left JOIN "MultiColumnValues"
ON "MultiColumnValues"."MultiColumnID"="MultiColumnArrays"."MultiColumnID"

-- Select one InstanceName and restrict the query AttributeDataTypeCV that is MultiColumnArray   
WHERE "Instances"."InstanceName"='Hyrum Reservoir' AND Attributes.AttributeDataTypeCV='MultiColumnArray'


-- Sort the the values of each column name based on their ascending order
Order By ColumName,ValueOrder asc



