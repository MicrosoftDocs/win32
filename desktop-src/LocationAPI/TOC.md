# [Location API](windows-location-api-portal.md)
## [Location API C++ Programming Reference](windows-location-programming-reference.md)
### [COM Interfaces](com-interfaces.md)
#### [ICivicAddressReport](/windows/desktop/api/LocationApi/nn-locationapi-icivicaddressreport)
<!-- ERROR:##### [GetAddressLine1 Method](winlocation-com-ref/icivicaddressreport-getaddressline1.md)-->
<!-- ERROR:##### [GetAddressLine2 Method](winlocation-com-ref/icivicaddressreport-getaddressline2.md)-->
<!-- ERROR:##### [GetCity Method](winlocation-com-ref/icivicaddressreport-getcity.md)-->
<!-- ERROR:##### [GetCountryRegion Method](winlocation-com-ref/icivicaddressreport-getcountryregion.md)-->
<!-- ERROR:##### [GetDetailLevel Method](winlocation-com-ref/icivicaddressreport-getdetaillevel.md)-->
<!-- ERROR:##### [GetPostalCode Method](winlocation-com-ref/icivicaddressreport-getpostalcode.md)-->
<!-- ERROR:##### [GetStateProvince Method](winlocation-com-ref/icivicaddressreport-getstateprovince.md)-->
#### [IDefaultLocation](/windows/desktop/api/LocationApi/nn-locationapi-idefaultlocation)
<!-- ERROR:##### [GetReport Method](winlocation-com-ref/idefaultlocation-getreport.md)-->
<!-- ERROR:##### [SetReport Method](winlocation-com-ref/idefaultlocation-setreport.md)-->
#### [ILatLongReport](/windows/desktop/api/LocationApi/nn-locationapi-ilatlongreport)
<!-- ERROR:##### [GetAltitude Method](winlocation-com-ref/ilatlongreport-getaltitude.md)-->
<!-- ERROR:##### [GetAltitudeError Method](winlocation-com-ref/ilatlongreport-getaltitudeerror.md)-->
<!-- ERROR:##### [GetErrorRadius Method](winlocation-com-ref/ilatlongreport-geterrorradius.md)-->
<!-- ERROR:##### [GetLatitude Method](winlocation-com-ref/ilatlongreport-getlatitude.md)-->
<!-- ERROR:##### [GetLongitude Method](winlocation-com-ref/ilatlongreport-getlongitude.md)-->
#### [ILocation](/windows/desktop/api/LocationApi/nn-locationapi-ilocation)
##### [GetDesiredAccuracy Method](/windows/desktop/api/LocationApi/nf-locationapi-ilocation-getdesiredaccuracy)
<!-- ERROR:##### [GetReport Method](winlocation-com-ref/ilocation-getreport.md)-->
<!-- ERROR:##### [GetReportInterval Method](winlocation-com-ref/ilocation-getreportinterval.md)-->
<!-- ERROR:##### [GetReportStatus Method](winlocation-com-ref/ilocation-getreportstatus.md)-->
<!-- ERROR:##### [RegisterForReport Method](winlocation-com-ref/ilocation-registerforreport.md)-->
<!-- ERROR:##### [RequestPermissions Method](winlocation-com-ref/ilocation-requestpermissions.md)-->
##### [SetDesiredAccuracy Method](/windows/desktop/api/LocationApi/nf-locationapi-ilocation-setdesiredaccuracy)
<!-- ERROR:##### [SetReportInterval Method](winlocation-com-ref/ilocation-setreportinterval.md)-->
<!-- ERROR:##### [UnregisterForReport Method](winlocation-com-ref/ilocation-unregisterforreport.md)-->
#### [ILocationEvents](/windows/desktop/api/LocationApi/nn-locationapi-ilocationevents)
<!-- ERROR:##### [OnLocationChanged Method](winlocation-com-ref/ilocationevents-onlocationchanged.md)-->
<!-- ERROR:##### [OnStatusChanged Method](winlocation-com-ref/ilocationevents-onstatuschanged.md)-->
#### [ILocationPower](/windows/desktop/api/LocationApi/nn-locationapi-ilocationpower)
<!-- ERROR:##### [Connect method](winlocation-com-ref/ilocationpower-connect.md)-->
<!-- ERROR:##### [Disconnect method](winlocation-com-ref/ilocationpower-disconnect.md)-->
#### [ILocationReport](/windows/desktop/api/LocationApi/nn-locationapi-ilocationreport)
<!-- ERROR:##### [GetSensorID Method](winlocation-com-ref/ilocationreport-getsensorid.md)-->
<!-- ERROR:##### [GetTimestamp Method](winlocation-com-ref/ilocationreport-gettimestamp.md)-->
<!-- ERROR:##### [GetValue Method](winlocation-com-ref/ilocationreport-getvalue.md)-->
### [Structures and Enumeration Types](structures-and-enumeration-types.md)
#### [LOCATION_DESIRED_ACCURACY](/windows/desktop/api/LocationApi/)
<!-- ERROR:#### [LOCATION_REPORT_STATUS](winlocation-com-ref/location-report-status.md)-->
## [Location API Object Model Reference](windows-location-script-programming-reference.md)
### [LocationDisp.DispCivicAddressReport](locationdisp-dispcivicaddressreport.md)
#### [AddressLine1 Property](locationdisp-dispcivicaddressreport-addressline1.md)
#### [AddressLine2 Property](locationdisp-dispcivicaddressreport-addressline2.md)
#### [City Property](locationdisp-dispcivicaddressreport-city.md)
#### [CountryRegion Property](locationdisp-civicaddressreport-countryregion.md)
#### [DetailLevel Property](locationdisp-dispcivicaddressreport-detaillevel.md)
#### [PostalCode Property](locationdisp-dispcivicaddressreport-postalcode.md)
#### [StateProvince Property](locationdisp-dispcivicaddressreport-stateprovince.md)
#### [Timestamp Property](locationdisp-dispcivicaddressreport-timestamp.md)
### [LocationDisp.CivicAddressReportFactory](locationdisp-civicaddressreportfactory.md)
#### [CivicAddressReport Property](locationdisp-dispcivicaddressreport-civicaddressreport.md)
#### [DesiredAccuracy Property](locationdisp-civicaddressreportfactory-desiredaccuracy.md)
#### [ListenForReports Method](locationdisp-civicaddressreportfactory-listenforreports.md)
#### [ReportInterval Property](locationdisp-civicaddressreportfactory-reportinterval.md)
#### [RequestPermissions Method](locationdisp-civicaddressreportfactory-requestpermissions.md)
#### [Status Property](locationdisp-civicaddressreportfactory-status.md)
#### [StopListeningForReports Method](locationdisp-civicaddressreportfactory-stoplisteningforreports.md)
### [LocationDisp.DispLatLongReport](locationdisp-displatlongreport.md)
#### [Altitude Property](locationdisp-displatlongreport-altitude.md)
#### [AltitudeError Property](locationdisp-displatlongreport-altitudeerror.md)
#### [ErrorRadius Property](locationdisp-displatlongreport-errorradius.md)
#### [Latitude Property](locationdisp-displatlongreport-latitude.md)
#### [Longitude Property](locationdisp-displatlongreport-longitude.md)
#### [Timestamp Property](locationdisp-displatlongreport-timestamp.md)
### [LocationDisp.LatLongReportFactory](locationdisp-latlongreportfactory.md)
#### [DesiredAccuracy Property](locationdisp-latlongreportfactory-desiredaccuracy.md)
#### [LatLongReport Property](locationdisp-latlongreportfactory-latlongreport.md)
#### [ListenForReports Method](locationdisp-latlongreportfactory-listenforreports.md)
#### [ReportInterval Property](locationdisp-latlongreportfactory-reportinterval.md)
#### [RequestPermissions Method](locationdisp-latlongreportfactory-requestpermissions.md)
#### [Status Property](locationdisp-latlongreportfactory-status.md)
#### [StopListeningForReports Method](/windows/desktop/api/locationapi/)
### [LocationDisp Events](locationdisp-events.md)
#### [NewCivicAddressReport Event](newcivicaddressreport.md)
#### [NewLatLongReport Event](newlatlongreport.md)
#### [StatusChanged Event](statuschanged.md)

