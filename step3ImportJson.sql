Declare @JSON varchar(max)
SELECT @JSON=BulkColumn

FROM OPENROWSET (BULK 'C:\Users\shz16118.UCONN\Downloads\results\vm20210105.json', SINGLE_CLOB) import
SELECT 
	DataPoints.dataPointId, DataPoints.journeyId, DataPoints.capturedTimestamp, 
	Locations.latitude, Locations.longitude, Locations.geohash, Locations.postalCode, Locations.regionCode, Locations.countryCode,
	Metrics.speed, Metrics.heading,
	Vehicles.wejoVehicleTypeId,
	Statuses.ignitionStatus 
INTO dbo.vm20210105
FROM OPENJSON (@JSON)
WITH  (
	dataPointId nvarchar(100),
	journeyId nvarchar(100),
	capturedTimestamp nvarchar(50),
	location nvarchar(max) as json,
	metrics nvarchar(max) as json,
	vehicle nvarchar(max) as json
) as DataPoints
cross apply openjson (DataPoints.location)
with (
	latitude float, 
	longitude float, 
	geohash nvarchar(20), 
	postalCode nvarchar(10), 
	regionCode nvarchar(5), 
	countryCode nvarchar(5)
) as Locations
cross apply openjson (DataPoints.metrics)
with (
	speed float, 
	heading float
) as Metrics
cross apply openjson (DataPoints.vehicle)
with (
	wejoVehicleTypeId nvarchar(100), 
	status nvarchar(max) as json
) as Vehicles
cross apply openjson (Vehicles.status)
with (
	ignitionStatus nvarchar(50)
) as Statuses



---- create table

--CREATE TABLE [dbo].[testvm](
--    dataPointId nvarchar(100),
--	journeyId nvarchar(100),
--	capturedTimestamp nvarchar(50),
--	location nvarchar(max),
--	metrics nvarchar(max),
--	vehicle nvarchar(max)
--) 
--GO


---- union tables
--SELECT *
--INTO [master].[dbo].[vm20210104and5]
--FROM [master].[dbo].[vm20210104]
--UNION ALL
--SELECT *
--FROM [master].[dbo].[vm20210105]