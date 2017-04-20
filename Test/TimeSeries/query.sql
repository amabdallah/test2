-- 4.81 TimeSeries

/*
This query shows time series data values, their time stamps and time series metadata

Result:
Time series data for a specific attribute 
WaM-DaM keeps track of the meanings of data values, their units, to what instance they apply too.... 
*/

SELECT ObjectType,AttributeName,
InstanceName,
ScenarioName,
AggregationStatisticCV,
AggregationInterval,
IntervalTimeUnitCV,
DateTimeStamp,
"Value","Mapping"."MappingID"

FROM "Datasets"

Left JOIN "ObjectTypes" 
ON "ObjectTypes"."DatasetID"="Datasets"."DatasetID"

-- Join the Objects to get their attributes  
Left JOIN  "Attributes"
ON "Attributes"."ObjectTypeID"="ObjectTypes"."ObjectTypeID"

Left JOIN "Mapping"
ON Mapping.AttributeID= Attributes.AttributeID


Left JOIN "Instances" 
ON "Instances"."InstanceID"="Mapping"."InstanceID"

Left JOIN "DataValuesMapper" 
ON "DataValuesMapper"."DataValuesMapperID"="Mapping"."DataValuesMapperID"

LEFT JOIN "ScenarioMapping"
ON "ScenarioMapping"."MappingID"="Mapping"."MappingID"

Left JOIN "Scenarios" 
ON "Scenarios"."ScenarioID"="ScenarioMapping"."ScenarioID"

Left JOIN "MasterNetworks" 
ON "MasterNetworks"."MasterNetworkID"="Scenarios"."ScenarioID"

Left JOIN "TimeSeries" 
ON "TimeSeries"."DataValuesMapperID"="DataValuesMapper"."DataValuesMapperID"

Left JOIN "TimeSeriesValues" 
ON "TimeSeriesValues"."TimeSeriesID"="TimeSeries"."TimeSeriesID"

WHERE AttributeDataTypeCV='TimeSeries' AND InstanceName='Weber Basin Project'
-- InstanceName='Bear River'  AND AttributeTypeCV='TimeSeries' AND AttributeName!='ObjectInstances'

ORDER BY InstanceName DESC