#!/usr/bin/env python
# -*- coding: utf-8 -*-#


from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, Numeric, Text, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

__engine = create_engine('sqlite:///wdm.db')
__Session = sessionmaker(bind=__engine)
__session = __Session()

def init():
    metadata = Base.metadata.create_all(__engine)

def get_session():
    return __session


class AggregationStatistic(Base):
    __tablename__ = 'AggregationStatistic'

    AggregationStatisticCVID =Column(Integer, primary_key=True)
    AggregationStatisticCV = Column(Text(255), primary_key=True)
    Definition = Column(Text)


class AttributeCategoryCV(Base):
    __tablename__ = 'AttributeCategoryCV'

    AttributeCategoryCVID = Column(Integer, primary_key=True)
    AttributeCategoryNameCV = Column(Text(255), nullable=False)
    CategoryDefinition = Column(Text)

class AttributeTypes(Base):
    __tablename__ = 'AttributeTypes'

    AttributeTypeCVID=Column(Integer, primary_key=True)
    AttributeTypeCV = Column(Text(255), primary_key=True)
    Definition = Column(Text)


class Attributes(Base):
    __tablename__ = 'Attributes'

    AttributeID = Column(Integer, primary_key=True)
    AttributeName = Column(Text(255), nullable=False)
    AttributeCode = Column(Text(50), nullable=False)
    UnitCVID = Column(ForeignKey('Units.UnitCVID'), nullable=False)
    AttributeNameCVID = Column(ForeignKey('AttributesCV.AttributeCVID'))
    AttributeDescription = Column(Text)

    AttributesCV = relationship('AttributesCV')
    Units = relationship('Units')


class AttributesCV(Base):
    __tablename__ = 'AttributesCV'

    AttributeCVID = Column(Integer, primary_key=True)
    AttributeNameCV = Column(Text(255), nullable=False)
    AttributeDefinition = Column(Text)
    AttributeCategoryCVID = Column(ForeignKey('AttributeCategoryCV.AttributeCategoryCVID'))

    AttributeCategoryCV = relationship('AttributeCategoryCV')


class BinaryValueMeaning(Base):
    __tablename__ = 'BinaryValueMeaning'

    BinaryValueMeaningCVID = Column(Integer, primary_key=True)
    ObjectAttributeCodeBinary = Column(Text(255), nullable=False)
    BinaryValue = Column(Numeric(1), nullable=False)
    BinaryValueMeaningCV = Column(Text, nullable=False)


class Binary(Base):
    __tablename__ = 'Binarys'

    BinaryID = Column(Integer, primary_key=True)
    BinaryValue = Column(Numeric(1), nullable=False)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)
    BinaryValueMeaningCVID = Column(ForeignKey('BinaryValueMeaning.BinaryValueMeaningCVID'), nullable=False)

    BinaryValueMeaning = relationship('BinaryValueMeaning')
    DataValuesMapper = relationship('DataValuesMapper')


class Connection(Base):
    __tablename__ = 'Connections'

    ConnectivityID = Column(Integer, primary_key=True)
    LinkInstanceID = Column(ForeignKey('Instances.InstanceID'), nullable=False)
    StartNodeInstanceID = Column(ForeignKey('Instances.InstanceID'), nullable=False)
    EndNodeInstanceID = Column(ForeignKey('Instances.InstanceID'), nullable=False)

    Instance = relationship('Instances', primaryjoin='Connection.EndNodeInstanceID == Instances.InstanceID')
    Instance1 = relationship('Instances', primaryjoin='Connection.LinkInstanceID == Instances.InstanceID')
    Instance2 = relationship('Instances', primaryjoin='Connection.StartNodeInstanceID == Instances.InstanceID')


class DataValuesMapper(Base):
    __tablename__ = 'DataValuesMapper'

    DataValuesMapperID = Column(Integer, primary_key=True)


class Datasets(Base):
    __tablename__ = 'Datasets'

    DatasetID = Column(Integer, primary_key=True)
    DatasetName = Column(Text(255), nullable=False)
    DatasetAcronym = Column(Text(255), nullable=False)
    SourceID = Column(ForeignKey('Sources.Sources'), nullable=False)
    DatasetCitation = Column(Text(500))
    DatasetDomain = Column(Text(255))
    DatasetWebpage = Column(Text(255))
    DatasetDescription = Column(Text)

    Sources = relationship('Sources')


class FileBased(Base):
    __tablename__ = 'FileBased'

    FileBasedID = Column(Integer, primary_key=True)
    FileName = Column(Text(255), nullable=False)
    FileFormatCVID = Column(ForeignKey('FileFormat.FileFormatCVID'), nullable=False)
    FileLocationOnDesk = Column(Text(255), nullable=False)
    Description = Column(Text)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)

    DataValuesMapper = relationship('DataValuesMapper')
    FileFormat = relationship('FileFormat')


class FileFormat(Base):
    __tablename__ = 'FileFormat'

    FileFormatCVID = Column(Integer, primary_key=True)
    FileFormatCV = Column(Text(255), primary_key=True)
    Definition = Column(Text)


class InstanceNames(Base):
    __tablename__ = 'InstanceNames'

    InstanceNameCVID = Column(Integer, primary_key=True)
    InstanceNameCV = Column(Text(255), primary_key=True)
    Definition = Column(Text)


class Instances(Base):
    __tablename__ = 'Instances'

    InstanceID = Column(Integer, primary_key=True)
    InstanceName = Column(ForeignKey('InstanceNames.InstanceNameCVID'), nullable=False)
    InstanceCode = Column(Text(255))
    Longitude_x = Column(Float)
    Latitude_y = Column(Float)
    Description = Column(Text)

    InstanceNames = relationship('InstanceNames')


class Mapping(Base):
    __tablename__ = 'Mapping'

    MappingID = Column(Integer, primary_key=True)
    ObjectAttributeID = Column(ForeignKey('ObjectAttributes.ObjectAttributeID'), nullable=False)
    InstanceID = Column(ForeignKey('Instances.InstanceID'), nullable=False)
    SourceID = Column(ForeignKey('Sources.SourceID'), nullable=False)
    MethodID = Column(ForeignKey('Methods.MethodID'), nullable=False)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'))

    DataValuesMapper = relationship('DataValuesMapper')
    Instances = relationship('Instances')
    Methods = relationship('Methods')
    ObjectAttributes = relationship('ObjectAttributes')
    Sources = relationship('Sources')


class MasterNetworks(Base):
    __tablename__ = 'MasterNetworks'

    MasterNetworkID = Column(Integer, primary_key=True)
    MasterNetworkName = Column(Text(255), nullable=False)
    SpatialReferenceCVID = Column(ForeignKey('SpatialReference.SpatialReferenceCVID'))
    VerticalDatumCVID = Column(ForeignKey('VerticalDatum.VerticalDatumCVID'))
    Description = Column(Text)

    SpatialReference = relationship('SpatialReference')
    VerticalDatum = relationship('VerticalDatum')


class MethodType(Base):
    __tablename__ = 'MethodType'

    MethodTypeCVID = Column(Integer, primary_key=True)
    MethodTypeCV = Column(Text(255), primary_key=True)
    Definition = Column(Text)

class Methods(Base):
    __tablename__ = 'Methods'

    MethodID = Column(Integer, primary_key=True)
    MethodName = Column(Text(255), nullable=False)
    MethodWebpage = Column(Text(255))
    MethodCitation = Column(Text(500))
    Description = Column(Text)
    MethodTypeID = Column(ForeignKey('MethodType.MethodTypeCVID'), nullable=False)
    PersonID = Column(ForeignKey('People.PersonID'), nullable=False)

    MethodType = relationship('MethodType')
    People = relationship('People')


class MultiColumnArrays(Base):
    __tablename__ = 'MultiColumnArrays'

    MultiColumnID = Column(Integer, primary_key=True)
    ColumnNameID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)

    DataValuesMapper = relationship('DataValuesMapper', primaryjoin='MultiColumnArrays.ColumnNameID == DataValuesMapper.DataValuesMapperID')
    DataValuesMapper1 = relationship('DataValuesMapper', primaryjoin='MultiColumnArrays.DataValuesMapperID == DataValuesMapper.DataValuesMapperID')


class MultiColumnValue(Base):
    __tablename__ = 'MultiColumnValues'

    MultiColumnValueID = Column(Integer, primary_key=True)
    Value = Column(Text(255), nullable=False)
    ValueOrder = Column(Integer, nullable=False)
    MultiColumnID = Column(ForeignKey('MultiColumnArrays.MultiColumnID'), nullable=False)

    MultiColumnArrays = relationship('MultiColumnArrays')



class ObjectAttributes(Base):
    __tablename__ = 'ObjectAttributes'

    ObjectAttributeID = Column(Integer, primary_key=True)
    ObjectTypeID = Column(ForeignKey('ObjectTypes.ObjectTypeID'), nullable=False)
    AttributeID = Column(ForeignKey('Attributes.AttributeID'), nullable=False)
    ObjectAttributeCode = Column(Text(50))
    ModelInputOrOutput = Column(Text(50))
    AttributeTypeCVID = Column(ForeignKey('AttributeTypes.AttributeTypeCVID'), nullable=False)

    Attributes = relationship('Attributes')
    AttributeTypes = relationship('AttributeTypes')
    ObjectType = relationship('ObjectTypes')


class ObjectCategory(Base):
    __tablename__ = 'ObjectCategory'

    ObjectCategoryID = Column(Integer, primary_key=True)
    ObjectCategoryName = Column(Text(255), nullable=False)
    CategoryDefinition = Column(Text)


class ObjectCategoryCV(Base):
    __tablename__ = 'ObjectCategoryCV'

    ObjectCategoryCVID = Column(Integer, primary_key=True)
    ObjectCategoryNameCV = Column(Text(255), nullable=False)
    CategoryDefinition = Column(Text)


class ObjectTypes(Base):
    __tablename__ = 'ObjectTypes'

    ObjectTypeID = Column(Integer, primary_key=True)
    ObjectType = Column(Text(255), nullable=False)
    ObjectCode = Column(Text(50))
    ObjectTopology = Column(Text(50), nullable=False)
    MapColor = Column(Text(50))
    MapSymbol = Column(Text(50))
    Description = Column(Text)
    ObjectTypeCVID = Column(ForeignKey('ObjectTypesCV.ObjectTypeCVID'))
    ObjectCategoryID = Column(ForeignKey('ObjectCategory.ObjectCategoryID'))
    DatasetID = Column(ForeignKey('Datasets.DatasetID'), nullable=False)

    Datasets = relationship('Datasets')
    ObjectCategory = relationship('ObjectCategory')
    ObjectTypesCV = relationship('ObjectTypesCV')


class ObjectTypesCV(Base):
    __tablename__ = 'ObjectTypesCV'

    ObjectTypeCVID = Column(Integer, primary_key=True)
    ObjectTypeCV = Column(Text(255), nullable=False)
    ObjectTopologyCV = Column(Text(50))
    ObjectDefinition = Column(Text)
    ObjectCategoryID = Column(ForeignKey('ObjectCategoryCV.ObjectCategoryCVID'))

    ObjectCategoryCV = relationship('ObjectCategoryCV')


class Organizations(Base):
    __tablename__ = 'Organizations'

    OrganizationID = Column(Integer, primary_key=True)
    OrganizationName = Column(Text(255), nullable=False)
    OrganizationType = Column(Text(255))
    Webpage = Column(Text(255))
    Description = Column(Text)


class Parameters(Base):
    __tablename__ = 'Parameters'

    ParameterID = Column(Integer, primary_key=True)
    ParameterValue = Column(Float, nullable=False)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)

    DataValuesMapper = relationship('DataValuesMapper')


class People(Base):
    __tablename__ = 'People'

    PersonID = Column(Integer, primary_key=True)
    PersonName = Column(Text(255), nullable=False)
    Address = Column(Text(255))
    Email = Column(Text(255))
    Phone = Column(Text(50))
    Webpage = Column(Text(255))
    Position = Column(Text(255))
    OrganizationID = Column(ForeignKey('Organizations.OrganizationID'), nullable=False)

    Organizations = relationship('Organizations')


class ScenarioMapping(Base):
    __tablename__ = 'ScenarioMapping'

    ScenarioMappingID = Column(Integer, primary_key=True)
    ScenarioID = Column(ForeignKey('Scenarios.ScenarioID'), nullable=False)
    MappingID = Column(ForeignKey('Mapping.MappingID'), nullable=False)

    Mapping = relationship('Mapping')
    Scenarios = relationship('Scenarios')


class Scenarios(Base):
    __tablename__ = 'Scenarios'

    ScenarioID = Column(Integer, primary_key=True)
    ScenarioName = Column(Text(255), nullable=False)
    StartTime = Column(DateTime)
    EndTime = Column(DateTime)
    TimeStep = Column(Integer)
    TimeStepUnitCVID = Column(ForeignKey('Units.UnitCVID'))
    Description = Column(Text)
    MasterNetworkID = Column(ForeignKey('MasterNetworks.MasterNetworkID'), nullable=False)

    MasterNetworks = relationship('MasterNetworks')
    Units = relationship('Units')


class SeasonName(Base):
    __tablename__ = 'SeasonName'

    SeasonNameCVID = Column(Integer, primary_key=True)
    SeasonNameCV = Column(Text(255), primary_key=True)
    Definition = Column(Text)


class SeasonalParameters(Base):
    __tablename__ = 'SeasonalParameters'

    SeasonalParameterID = Column(Integer, primary_key=True)
    SeasonStartDateTime = Column(Text(50))
    SeasonEndDateTime = Column(Text(50))
    SeasonNameCV = Column(ForeignKey('SeasonName.SeasonNameCVID'), nullable=False)
    SeasonValue = Column(Text(500), nullable=False)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)

    DataValuesMapper = relationship('DataValuesMapper')
    SeasonName = relationship('SeasonName')


class Sources(Base):
    __tablename__ = 'Sources'

    SourceID = Column(Integer, primary_key=True)
    SourceName = Column(Text(500), nullable=False)
    SourceCode = Column(Text(50), nullable=False)
    Webpage = Column(Text(500))
    Citation = Column(Text(500))
    Description = Column(Text)
    PersonID = Column(ForeignKey('People.PersonID'))

    People = relationship('People')


class SpatialReference(Base):
    __tablename__ = 'SpatialReference'

    SpatialReferenceCVID = Column(Integer, primary_key=True)
    SRSNameCV = Column(Text(500), nullable=False)
    SRSID = Column(Integer, nullable=False)
    IsGeographic = Column(Integer, nullable=False)
    Notes = Column(Text)


class TextControlled(Base):
    __tablename__ = 'TextControlled'

    TextControlledID = Column(Integer, primary_key=True)
    TextControlledValueCVID = Column(ForeignKey('TextControlledValues.TextControlledValueCVID'), nullable=False)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)

    DataValuesMapper = relationship('DataValuesMapper')
    TextControlledValues = relationship('TextControlledValues')


class TextControlledValues(Base):
    __tablename__ = 'TextControlledValues'

    TextControlledValueCVID = Column(Integer, primary_key=True)
    TextControlledValueCV = Column(Text(255), nullable=False)
    TextControlledAttribute = Column(Text(255), nullable=False)
    ValueDefinition = Column(Text)


class TextFree(Base):
    __tablename__ = 'TextFree'

    TextFreeID = Column(Integer, primary_key=True)
    TextFreeValue = Column(Text(500), nullable=False)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)

    DataValuesMapper = relationship('DataValuesMapper')


class TimeSeries(Base):
    __tablename__ = 'TimeSeries'

    TimeSeriesID = Column(Integer, primary_key=True)
    AggregationStatisticCVID = Column(ForeignKey('AggregationStatistic.AggregationStatisticCVID'), nullable=False)
    AggregationInterval = Column(Float, nullable=False)
    IntervalTimeUnitCVID = Column(ForeignKey('Units.UnitCVID'), nullable=False)
    BeginDateTime = Column(DateTime)
    EndDateTime = Column(DateTime)
    IsRegular = Column(Numeric)
    NoDataValue = Column(Text(50))
    Description = Column(Text)
    DataValuesMapperID = Column(ForeignKey('DataValuesMapper.DataValuesMapperID'), nullable=False)

    AggregationStatistic = relationship('AggregationStatistic')
    DataValuesMapper = relationship('DataValuesMapper')
    Units = relationship('Units')


class TimeSeriesValues(Base):
    __tablename__ = 'TimeSeriesValues'

    TimeSeriesValueID = Column(Integer, primary_key=True)
    TimeSeriesID = Column(ForeignKey('TimeSeries.TimeSeriesID'), nullable=False)
    DateTimeStamp = Column(DateTime, nullable=False)
    CorrespondingValue = Column(Float, nullable=False)

    TimeSeries = relationship('TimeSeries')


class Units(Base):
    __tablename__ = 'Units'

    UnitCVID = Column(Integer, primary_key=True)
    UnitType = Column(Text(255), nullable=False)
    UnitNameCV = Column(Text(255), nullable=False)
    UnitSystem = Column(Text(255))
    UnitAbbreviation = Column(Text(50), nullable=False)


class VerticalDatum(Base):
    __tablename__ = 'VerticalDatum'

    VerticalDatumCVID = Column(Integer, primary_key=True)
    VerticalDatumCV = Column(Text(255), primary_key=True)
    Definition = Column(Text)



