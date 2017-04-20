/*

Adel Abdalllah
Updated April 5, 2017

*/

SELECT ObjectType,InstanceName,AttributeName, UnitNameCV, InstanceName,MasterNetworkName,ScenarioName, ScenarioMapping.ScenarioMappingID,AttributeDataTypeCV,SeasonName,SeasonValue,Mapping.MappingID
FROM Attributes 

-- Join the Attributes to get their Object Types 
Left JOIN  ObjectTypes
ON "ObjectTypes"."ObjectTypeID"="Attributes"."ObjectTypeID"

-- Join the Attributes to get their Mapping 
LEFT JOIN Mapping
ON Mapping.AttributeID= Attributes.AttributeID

-- Join the Mapping to get their Instances   
LEFT JOIN Instances
ON Instances.InstanceID= Mapping.InstanceID

-- Join the Mappings to get their ScenarioMappings   
LEFT JOIN ScenarioMapping
ON ScenarioMapping.MappingID= Mapping.MappingID

-- Join the ScenarioMappings to get their Scenarios   
LEFT JOIN Scenarios
ON Scenarios.ScenarioID= ScenarioMapping.ScenarioID

-- Join the Scenarios to get their MasterNetworks   
LEFT JOIN MasterNetworks
ON MasterNetworks.MasterNetworkID= Scenarios.MasterNetworkID

-- Join the Mappings to get their DataValuesMappers   
LEFT JOIN DataValuesMapper
ON DataValuesMapper.DataValuesMapperID = Mapping.DataValuesMapperID 

-- Join the DataValuesMapper to get their SeasonalParameters   
LEFT JOIN SeasonalParameters
ON SeasonalParameters.DataValuesMapperID = DataValuesMapper.DataValuesMapperID 

--WEAP
WHERE AttributeDataTypeCV='SeasonalParameter' AND InstanceName='Hyrum Reservoir' AND AttributeName='Net Evaporation' and ScenarioName='Reference_LowerBear'

--Wyoming
--WHERE AttributeDataTypeCV='SeasonalParameter' AND InstanceName='Node 2.02' AND AttributeName='Net Evaporation - inches'  AND ScenarioName='Bear Wet Year Model'


