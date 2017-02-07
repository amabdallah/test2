-- This is a Data Definition Language (DDL) script that
-- generates a blank schema of the Water Management Data Model (WaM-DaM)
-- for SQLite database

-- Generated by Adel Abdallah October 26,2016 based on WaM-DaM XML design named WaMDaMOct26_2016.xml generated by DbWrench V3.3.7
-- WaM-DaM All rights reserved. See Licence @ https://github.com/amabdallah/WaM-DaM 

--Use the SQLite Manager Add-on to Mozilla Firefox
--Create a new empty database. Click on the Execute SQL button and delete the text "SELECT * FROM tablename"
--Simply copy all this script and paste into this Execute SQL window
--Then click Run SQL. The script should run successfully and create the 42 empty tables of WaM-DaM

--------------------------------------------------------------------------------------------------
/***************************************************************************/
/******************************* CREATE CVS ********************************/
/***************************************************************************/

CREATE TABLE AggregationStatistic (
	AggregationStatisticID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	AggregationStatistic VARCHAR (255)  NOT NULL,
	Definition TEXT   NULL
);

CREATE TABLE AttributeCategoryCV (
	AttributeCategoryID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	AttributeCategoryName VARCHAR (255)  NOT NULL,
	CategoryDefinition TEXT   NULL,
	ParentAttributeCategoryID INTEGER   NULL,
	FOREIGN KEY (ParentAttributeCategoryID) REFERENCES AttributeCategoryCV (AttributeCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE AttributesCV (
	AttributeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	AttributeName VARCHAR (255)  NOT NULL,
	AttributeDefinition TEXT   NULL,
	AttributeCategoryID INTEGER   NULL,
	FOREIGN KEY (AttributeCategoryID) REFERENCES AttributeCategoryCV (AttributeCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE AttributeTypeCode (
	AttributeTypeCodeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	AttributeTypeCode VARCHAR (255)  NOT NULL,
	Definition TEXT   NULL
);

CREATE TABLE BinaryValueMeaning (
	BinaryValueMeaningID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	BinaryAttribute VARCHAR (255)  NOT NULL,
	BinaryValue BINARY (1)  NOT NULL,
	ValueDefinition TEXT   NOT NULL
);

CREATE TABLE FileFormat (
	FileFormatID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	FileFormat VARCHAR (255)  NOT NULL,
	Definition TEXT   NULL
);

CREATE TABLE InstanceName (
	InstanceNameID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	InstanceName VARCHAR (255)  NOT NULL,
	Definition TEXT   NULL
);

CREATE TABLE MethodType (
	MethodTypeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	MethodType VARCHAR (255)  NOT NULL,
	Definition TEXT   NULL
);

CREATE TABLE ObjectCategoryCV (
	ObjectCategoryID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ObjectCategoryName VARCHAR (255)  NOT NULL,
	CategoryDefinition TEXT   NULL,
	ParentObjectCategoryID INTEGER   NULL,
	FOREIGN KEY (ParentObjectCategoryID) REFERENCES ObjectCategoryCV (ObjectCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE ObjectTypesCV (
	ObjectTypeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ObjectType VARCHAR (255)  NOT NULL,
	ObjectTopology VARCHAR (50)  NULL,
	ObjectDefinition TEXT   NULL,
	ObjectCategoryID INTEGER   NULL,
	FOREIGN KEY (ObjectCategoryID) REFERENCES ObjectCategoryCV (ObjectCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE SeasonName (
	SeasonNameID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	SeasonName VARCHAR (255)  NOT NULL,
	Definition TEXT   NULL
);

CREATE TABLE SpatialReference (
	SpatialReferenceID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	SRSName VARCHAR (500)  NOT NULL,
	SRSID INTEGER   NOT NULL,
	IsGeographic INTEGER   NOT NULL,
	Notes TEXT   NULL
);

CREATE TABLE TextControlledValues (
	TextControlledValueID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	TextControlledValue VARCHAR (255)  NOT NULL,
	TextControlledAttribute VARCHAR (255)  NOT NULL,
	ValueDefinition TEXT   NULL
);

CREATE TABLE Units (
	UnitID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	UnitType VARCHAR (255)  NOT NULL,
	UnitName VARCHAR (255)  NOT NULL,
	UnitSystem VARCHAR (255)  NULL,
	UnitAbbreviation char (50)  NOT NULL
);

CREATE TABLE VerticalDatum (
	VerticalDatumID INTEGER  AUTO_INCREMENT NOT NULL,
	VerticalDatum VARCHAR (255)  NOT NULL,
	Definition TEXT   NULL
);

/***************************************************************************/
/**************************** CREATE DATAVALUES ****************************/
/***************************************************************************/

CREATE TABLE Binarys (
	BinaryID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	BinaryValue BINARY (1)  NOT NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	BinaryValueMeaningCVID INTEGER   NOT NULL,
	FOREIGN KEY (BinaryValueMeaningCVID) REFERENCES BinaryValueMeaning (BinaryValueMeaningID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE DataValuesMapper (
	DataValuesMapperID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY
);

CREATE TABLE FileBased (
	FileBasedID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	FileName VARCHAR (255)  NOT NULL,
	FileLocationOnDesk VARCHAR (255)  NOT NULL,
	Description TEXT   NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	FileFormatID INTEGER   NOT NULL,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (FileFormatID) REFERENCES FileFormat (FileFormatID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE MultiColumnArray (
	MultiColumnID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ColumnNameID INTEGER   NOT NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (ColumnNameID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE MultiColumnValues (
	MultiColumnValueID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	Value VARCHAR (255)  NOT NULL,
	ValueOrder INTEGER   NOT NULL,
	MultiColumnID INTEGER   NOT NULL,
	FOREIGN KEY (MultiColumnID) REFERENCES MultiColumnArray (MultiColumnID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Parameters (
	ParameterID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ParameterValue FLOAT   NOT NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE SeasonalParameters (
	SeasonalParameterID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	SeasonStartDateTime VARCHAR (50)  NULL,
	SeasonEndDateTime VARCHAR (50)  NULL,
	SeasonValue VARCHAR (500)  NOT NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	SeasonNameID INTEGER   NOT NULL,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (SeasonNameID) REFERENCES SeasonName (SeasonNameID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE TextControlled (
	TextControlledID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	TextControlledValueCVID INTEGER   NOT NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	FOREIGN KEY (TextControlledValueCVID) REFERENCES TextControlledValues (TextControlledValueID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE TextFree (
	TextFreeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	TextFreeValue VARCHAR (500)  NOT NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE TimeSeries (
	TimeSeriesID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	AggregationInterval DOUBLE   NOT NULL,
	IntervalTimeUnitID INTEGER   NOT NULL,
	BeginDateTime DATETIME   NULL,
	EndDateTime DATETIME   NULL,
	IsRegular BIT   NULL,
	NoDataValue VARCHAR (50)  NULL,
	Description TEXT   NULL,
	DataValuesMapperID INTEGER   NOT NULL,
	AggregationStatisticID INTEGER   NOT NULL,
	FOREIGN KEY (AggregationStatisticID) REFERENCES AggregationStatistic (AggregationStatisticID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (IntervalTimeUnitID) REFERENCES Units (UnitID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE TimeSeriesValues (
	TimeSeriesValueID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	TimeSeriesID INTEGER   NOT NULL,
	DateTimeStamp DATETIME   NOT NULL,
	Value FLOAT   NOT NULL,
	FOREIGN KEY (TimeSeriesID) REFERENCES TimeSeries (TimeSeriesID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

/***************************************************************************/
/***************************** CREATE METADATA *****************************/
/***************************************************************************/

CREATE TABLE AttributeCategory (
	AttributeCategoryID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	CategoryName VARCHAR (255)  NOT NULL,
	CategoryDefinition TEXT   NULL,
	CategoryGroup VARCHAR (255)  NULL,
	ParentCategoryID INTEGER   NULL,
	FOREIGN KEY (ParentCategoryID) REFERENCES AttributeCategory (AttributeCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Methods (
	MethodID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	MethodName VARCHAR (255)  NOT NULL,
	MethodCode VARCHAR (50)  NOT NULL,
	MethodWebpage VARCHAR (255)  NULL,
	MethodCitation VARCHAR (500)  NULL,
	Description TEXT   NULL,
	PersonID INTEGER   NOT NULL,
	MethodTypeID INTEGER   NOT NULL,
	FOREIGN KEY (MethodTypeID) REFERENCES MethodType (MethodTypeID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (PersonID) REFERENCES People (PersonID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE ObjectCategory (
	ObjectCategoryID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	CategoryName VARCHAR (255)  NOT NULL,
	CategoryDefinition TEXT   NULL,
	ObjectGroup VARCHAR (500)  NULL,
	ParentCategoryID INTEGER   NULL,
	FOREIGN KEY (ParentCategoryID) REFERENCES ObjectCategory (ObjectCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Organizations (
	OrganizationID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	OrganizationName VARCHAR (255)  NOT NULL,
	OrganizationType VARCHAR (255)  NULL,
	OrganizationWebpage VARCHAR (255)  NULL,
	Description TEXT   NULL
);

CREATE TABLE People (
	PersonID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ContactName VARCHAR (255)  NOT NULL,
	Address VARCHAR (255)  NULL,
	Email VARCHAR (255)  NULL,
	Phone VARCHAR (50)  NULL,
	PersonWebpage VARCHAR (255)  NULL,
	Position VARCHAR (255)  NULL,
	OrganizationID INTEGER   NOT NULL,
	FOREIGN KEY (OrganizationID) REFERENCES Organizations (OrganizationID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Sources (
	SourceID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	SourceName VARCHAR (500)  NOT NULL,
	SourceCode VARCHAR (50)  NOT NULL,
	SourceWebpage VARCHAR (500)  NULL,
	SourceCitation VARCHAR (500)  NULL,
	Description TEXT   NULL,
	PersonID INTEGER   NOT NULL,
	FOREIGN KEY (PersonID) REFERENCES People (PersonID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

/***************************************************************************/
/***************************** CREATE NETWORKS *****************************/
/***************************************************************************/

CREATE TABLE Connections (
	ConnectivityID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	LinkInstanceID INTEGER   NOT NULL,
	StartNodeInstanceID INTEGER   NOT NULL,
	EndNodeInstanceID INTEGER   NOT NULL,
	FOREIGN KEY (LinkInstanceID) REFERENCES Instances (InstanceID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (StartNodeInstanceID) REFERENCES Instances (InstanceID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (EndNodeInstanceID) REFERENCES Instances (InstanceID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Instances (
	InstanceID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	InstanceName VARCHAR (255)  NOT NULL,
	InstanceCode VARCHAR (255)  NULL,
	Longitude FLOAT   NULL,
	Latitude FLOAT   NULL,
	Description TEXT   NULL,
	InstanceNameCVID INTEGER   NULL,
	FOREIGN KEY (InstanceNameCVID) REFERENCES InstanceName (InstanceNameID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Mapping (
	MappingID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ObjectAttributeID INTEGER   NOT NULL,
	InstanceID INTEGER   NOT NULL,
	SourceID INTEGER   NOT NULL,
	MethodID INTEGER   NOT NULL,
	DataValuesMapperID INTEGER   NULL,
	FOREIGN KEY (DataValuesMapperID) REFERENCES DataValuesMapper (DataValuesMapperID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (InstanceID) REFERENCES Instances (InstanceID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (MethodID) REFERENCES Methods (MethodID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (ObjectAttributeID) REFERENCES ObjectAttributes (ObjectAttributeID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (SourceID) REFERENCES Sources (SourceID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE MasterNetworks (
	MasterNetworkID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	MasterNetworkName VARCHAR (255)  NOT NULL,
	SpatialReferenceCVID INTEGER   NULL,
	ParenMasterNetwork INTEGER   NULL,
	Description TEXT   NULL,
	VerticalDatumID INTEGER   NULL,
	FOREIGN KEY (ParenMasterNetwork) REFERENCES MasterNetworks (MasterNetworkID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (SpatialReferenceCVID) REFERENCES SpatialReference (SpatialReferenceID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (VerticalDatumID) REFERENCES VerticalDatum (VerticalDatumID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE ScenarioMapping (
	ScenarioMappingID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ScenarioID INTEGER   NOT NULL,
	MappingID INTEGER   NOT NULL,
	FOREIGN KEY (MappingID) REFERENCES Mapping (MappingID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (ScenarioID) REFERENCES Scenarios (ScenarioID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Scenarios (
	ScenarioID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ScenarioName VARCHAR (255)  NOT NULL,
	StartTime DATETIME   NULL,
	EndTime DATETIME   NULL,
	TimeStep INTEGER   NULL,
	TimeStepUnitID INTEGER   NULL,
	Description TEXT   NULL,
	MasterNetworkID INTEGER   NOT NULL,
	FOREIGN KEY (MasterNetworkID) REFERENCES MasterNetworks (MasterNetworkID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (TimeStepUnitID) REFERENCES Units (UnitID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

/***************************************************************************/
/**************************** CREATE STRUCTURES ****************************/
/***************************************************************************/

CREATE TABLE Attributes (
	AttributeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	AttributeName VARCHAR (255)  NOT NULL,
	AttributeCode VARCHAR (50)  NOT NULL,
	UnitID INTEGER   NOT NULL,
	AttributeNameCVID INTEGER   NULL,
	AttributeDescription TEXT   NULL,
	FOREIGN KEY (AttributeNameCVID) REFERENCES AttributesCV (AttributeID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (UnitID) REFERENCES Units (UnitID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE DataStructure (
	DataStructureID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	DataStructureName VARCHAR (255)  NOT NULL,
	DataStrucutureAcronym  VARCHAR (255)  NULL,
	DataStructureDomain VARCHAR (255)  NULL,
	DataStructureWebpage VARCHAR (255)  NULL,
	DataStructureDescription TEXT   NULL
);

CREATE TABLE ObjectAttributes (
	ObjectAttributeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ObjectTypeID INTEGER   NOT NULL,
	AttributeID INTEGER   NOT NULL,
	ObjectAttributeCode VARCHAR (50)  NULL,
	ModelInputOrOutput char (50)  NULL,
	AttributeCategoryID INTEGER   NULL,
	AttributeTypeCodeID INTEGER   NOT NULL,
	FOREIGN KEY (AttributeID) REFERENCES Attributes (AttributeID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (AttributeTypeCodeID) REFERENCES AttributeTypeCode (AttributeTypeCodeID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (AttributeCategoryID) REFERENCES AttributeCategory (AttributeCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (ObjectTypeID) REFERENCES ObjectTypes (ObjectTypeID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE ObjectTypes (
	ObjectTypeID INTEGER  AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ObjectType VARCHAR (255)  NOT NULL,
	ObjectCode VARCHAR (50)  NULL,
	ObjectTopology VARCHAR (50)  NOT NULL,
	MapColor VARCHAR (50)  NULL,
	MapSymbol VARCHAR (50)  NULL,
	Description TEXT   NULL,
	ObjectTypeCVID INTEGER   NULL,
	ObjectCategoryID INTEGER   NULL,
	DataStructureID INTEGER   NOT NULL,
	FOREIGN KEY (ObjectTypeCVID) REFERENCES ObjectTypesCV (ObjectTypeID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (DataStructureID) REFERENCES DataStructure (DataStructureID)
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY (ObjectCategoryID) REFERENCES ObjectCategory (ObjectCategoryID)
	ON UPDATE NO ACTION ON DELETE NO ACTION
);