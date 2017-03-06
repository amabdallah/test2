-- 4.90 MultiColumns

/*
This query shows data values for a particular MultiColumns of a reservoir elevation with surface area, and storage 
its attributes, units, object names, and instances, and data source 

Result:
Users can import these data columns to their model 
WaM-DaM keeps track of the meanings of data values, their units, to what instance they apply too.... 
*/

SELECT "ObjectTypes"."ObjectType",
"Instances"."InstanceName","Attributes"."AttributeName",
"AttributesColumns"."AttributeName" AS "ColumName",
"ColumnsUnits"."UnitNameCV" AS "ColUnitName",
"Value","ValueOrder"

FROM "Datasets"

Left JOIN "ObjectTypes" 
ON "ObjectTypes"."DatasetID"="Datasets"."DatasetID"

-- Join the Objects to get their attributes  
Left JOIN  "Attributes"
ON "Attributes"."ObjectTypeID"="ObjectTypes"."ObjectTypeID"

Left JOIN "Mapping"
ON Mapping.AttributeID= Attributes.AttributeID


Left JOIN "DataValuesMapper" 
ON "DataValuesMapper"."DataValuesMapperID"="Mapping"."DataValuesMapperID"


Left JOIN "ScenarioMapping"
ON "ScenarioMapping"."MappingID"="Mapping"."MappingID"

Left JOIN "Scenarios"
ON "Scenarios"."ScenarioID"="ScenarioMapping"."ScenarioID"
AND "Scenarios"."ScenarioName"='Historical records'

Left JOIN "MasterNetworks" 
ON "MasterNetworks"."MasterNetworkID"="Scenarios"."MasterNetworkID"

Left JOIN "Methods" 
ON "Methods"."MethodID"="Mapping"."MethodID"

Left JOIN "Sources" 
ON "Sources"."SourceID"="Mapping"."SourceID"

Left JOIN "MultiColumnArrays"  
ON "MultiColumnArrays" ."DataValuesMapperID"="DataValuesMapper"."DataValuesMapperID"


/*This is extra join to get the column names */

Left JOIN "DataValuesMapper" As "StorageColumns"
ON "StorageColumns"."DataValuesMapperID"="MultiColumnArrays"."ColumnNameID"

Left JOIN "Mapping" As "MetadataColumns"
ON "MetadataColumns"."DataValuesMapperID"="StorageColumns"."DataValuesMapperID"

Left JOIN  "Attributes" As "AttColumns"
ON "AttColumns"."AttributeID"="MetadataColumns"."AttributeID"

Left JOIN  "Attributes" AS "AttributesColumns"
ON "AttributesColumns"."AttributeID"="AttColumns"."AttributeID"

Left JOIN "Units" As "ColumnsUnits"
ON "ColumnsUnits"."UnitCVID"="AttributesColumns"."UnitCVID"

/* Finishes here */

Left JOIN "MultiColumnValues"
ON "MultiColumnValues"."MultiColumnID"="MultiColumnArrays"."MultiColumnID"

Left JOIN "Instances" 
ON "Instances"."InstanceID"="Mapping"."InstanceID"

WHERE "Instances"."InstanceName"='Soda Reservoir' 

Order By ColumName asc

-- how to join the three attributes along one line 