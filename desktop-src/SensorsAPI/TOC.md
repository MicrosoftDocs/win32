# [Sensor API](portal.md)
## [Getting Started](getting-started.md)
### [Introduction to the Sensor and Location Platform in Windows](introduction-to-the-sensor-and-location-platform-in-windows.md)
### [Privacy and Security in the Sensor and Location Platform](privacy-and-security-in-the-sensor-and-location-platform.md)
### [General Requirements for Application Development](general-requirements-for-application-development.md)
### [About the Samples and Tools](about-the-samples.md)
### [For More Information](for-more-information.md)
## [About the Sensor API](about-the-sensor-api.md)
### [The Sensor Manager Object](the-sensor-manager.md)
### [The Sensor Object](the-sensor-object.md)
### [The Sensor Collection Object](the-sensor-collection-object.md)
### [The Sensor Data Report Object](the-sensor-data-report-object.md)
### [About Sensor API Events](about-sensor-events.md)
### [About Sensor Constants](about-sensor-constants.md)
### [Managing User Permissions](managing-user-permissions.md)
### [About Logical Sensors](about-logical-sensors.md)
## [Sensor API Programming Guide](sensor-api-programming-guide.md)
### [Retrieving a Sensor Object](retrieving-a-sensor.md)
### [Requesting User Permissions](requesting-user-permissions.md)
### [Retrieving and Setting Sensor Properties](setting-and-retrieving-sensor-properties.md)
### [Checking for Supported Sensor Data Fields](checking-for-supported-sensor-data-fields.md)
### [Using Sensor API Events](using-sensor-api-events.md)
### [Retrieving Sensor Data Values](retrieving-sensor-data-fields.md)
### [Retrieving Vector Types](retrieving-vector-types.md)
### [Using Logical Sensors](using-logical-sensors.md)
### [Creating Light-Aware User Interfaces](creating-light-aware-user-interfaces.md)
#### [Fundamentals of Light-Aware User Interfaces](fundamentals-of-light-aware-user-interfaces.md)
#### [Examples of Light-Aware User Interfaces](examples-of-light-aware-user-interfaces.md)
#### [Optimizing the User Experience](optimizing-the-user-experience.md)
#### [Understanding and Interpreting Lux Values](understanding-and-interpreting-lux-values.md)
#### [Using Light Sensor Data](handling-data-from-multiple-light-sensors.md)
## [Sensor API Programming Reference](sensor-api-programming-reference.md)
### [COM Interfaces](windows-sensors-com-interfaces.md)
#### [ILocationPermissions](/windows/desktop/api/sensorsapi/nn-sensorsapi-ilocationpermissions)
<!-- ERROR:##### [GetGlobalLocationPermission method](winsensors-com-ref/ilocationpermissions-getgloballocationpermission.md)-->
##### [CheckLocationCapability method](/windows/desktop/api/sensorsapi/nf-sensorsapi-ilocationpermissions-checklocationcapability)
#### [ILogicalSensorManager](https://msdn.microsoft.com/en-us/library/Dd318934(v=VS.85).aspx)
<!-- ERROR:##### [Connect Method](winsensors-com-ref/ilogicalsensormanager-connect.md)-->
<!-- ERROR:##### [Disconnect Method](winsensors-com-ref/ilogicalsensormanager-disconnect.md)-->
<!-- ERROR:##### [Uninstall Method](winsensors-com-ref/ilogicalsensormanager-uninstall.md)-->
#### [ISensor](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensor)
<!-- ERROR:##### [GetCategory Method](winsensors-com-ref/isensor-getcategory.md)-->
<!-- ERROR:##### [GetData Method](winsensors-com-ref/isensor-getdata.md)-->
<!-- ERROR:##### [GetEventInterest Method](winsensors-com-ref/isensor-geteventinterest.md)-->
<!-- ERROR:##### [GetFriendlyName Method](winsensors-com-ref/isensor-getfriendlyname.md)-->
<!-- ERROR:##### [GetID Method](winsensors-com-ref/isensor-getid.md)-->
<!-- ERROR:##### [GetProperties Method](winsensors-com-ref/isensor-getproperties.md)-->
<!-- ERROR:##### [GetProperty Method](winsensors-com-ref/isensor-getproperty.md)-->
<!-- ERROR:##### [GetState Method](winsensors-com-ref/isensor-getstate.md)-->
<!-- ERROR:##### [GetSupportedDataFields Method](winsensors-com-ref/isensor-getsupporteddatafields.md)-->
<!-- ERROR:##### [GetType Method](winsensors-com-ref/isensor-gettype.md)-->
<!-- ERROR:##### [SetEventInterest Method](winsensors-com-ref/isensor-seteventinterest.md)-->
<!-- ERROR:##### [SetEventSink Method](winsensors-com-ref/isensor-seteventsink.md)-->
<!-- ERROR:##### [SetProperties Method](winsensors-com-ref/isensor-setproperties.md)-->
<!-- ERROR:##### [SupportsDataField Method](winsensors-com-ref/isensor-supportsdatafield.md)-->
<!-- ERROR:##### [SupportsEvent Method](winsensors-com-ref/isensor-supportsevent.md)-->
#### [ISensorCollection](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensorcollection)
<!-- ERROR:##### [Add Method](winsensors-com-ref/isensorcollection-add.md)-->
<!-- ERROR:##### [Clear Method](winsensors-com-ref/isensorcollection-clear.md)-->
<!-- ERROR:##### [GetAt Method](winsensors-com-ref/isensorcollection-getat.md)-->
<!-- ERROR:##### [GetCount Method](winsensors-com-ref/isensorcollection-getcount.md)-->
<!-- ERROR:##### [Remove Method](winsensors-com-ref/isensorcollection-remove.md)-->
<!-- ERROR:##### [RemoveByID Method](winsensors-com-ref/isensorcollection-removebyid.md)-->
#### [ISensorDataReport](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensordatareport)
<!-- ERROR:##### [GetSensorValue Method](winsensors-com-ref/isensordatareport-getsensorvalue.md)-->
<!-- ERROR:##### [GetSensorValues Method](winsensors-com-ref/isensordatareport-getsensorvalues.md)-->
<!-- ERROR:##### [GetTimestamp Method](winsensors-com-ref/isensordatareport-gettimestamp.md)-->
#### [ISensorEvents](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensorevents)
<!-- ERROR:##### [OnEvent Method](winsensors-com-ref/isensorevents-onevent.md)-->
<!-- ERROR:##### [OnDataUpdated Method](winsensors-com-ref/isensorevents-ondataupdated.md)-->
<!-- ERROR:##### [OnLeave Method](winsensors-com-ref/isensorevents-onleave.md)-->
<!-- ERROR:##### [OnStateChanged Method](winsensors-com-ref/isensorevents-onstatechanged.md)-->
#### [ISensorManager](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensormanager)
<!-- ERROR:##### [GetSensorByID Method](winsensors-com-ref/isensormanager-getsensorbyid.md)-->
<!-- ERROR:##### [GetSensorsByCategory Method](winsensors-com-ref/isensormanager-getsensorsbycategory.md)-->
<!-- ERROR:##### [GetSensorsByType Method](winsensors-com-ref/isensormanager-getsensorsbytype.md)-->
<!-- ERROR:##### [RequestPermissions Method](winsensors-com-ref/isensormanager-requestpermissions.md)-->
<!-- ERROR:##### [SetEventSink Method](winsensors-com-ref/isensormanager-seteventsink.md)-->
#### [ISensorManagerEvents](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensormanagerevents)
<!-- ERROR:##### [OnSensorEnter Method](winsensors-com-ref/isensormanagerevents-onsensorenter.md)-->
### [Enumeration Types](enumeration-types.md)
#### [MagnetometerAccuracy](/windows/desktop/api/sensorsapi/ne-sensorsapi-magnetometeraccuracy)
<!-- ERROR:#### [SensorConnectionType](winsensors-com-ref/sensorconnectiontype.md)-->
<!-- ERROR:#### [SensorState](winsensors-com-ref/sensorstate.md)-->
### [Constants](constants.md)
#### [Sensor Categories, Types, and Data Fields](sensor-categories--types--and-datafields.md)
##### [SENSOR_CATEGORY_ALL](sensor-category-all.md)
##### [SENSOR_CATEGORY_BIOMETRIC](sensor-category-biometric.md)
##### [SENSOR_CATEGORY_ELECTRICAL](sensor-category-electrical.md)
##### [SENSOR_CATEGORY_ENVIRONMENTAL](sensor-category-environmental.md)
##### [SENSOR_CATEGORY_LIGHT](sensor-category-light.md)
##### [SENSOR_CATEGORY_LOCATION](sensor-category-location.md)
##### [SENSOR_CATEGORY_MECHANICAL](sensor-category-mechanical.md)
##### [SENSOR_CATEGORY_MOTION](sensor-category-motion.md)
##### [SENSOR_CATEGORY_ORIENTATION](sensor-category-orientation.md)
##### [SENSOR_CATEGORY_OTHER](sensor-category-other.md)
##### [SENSOR_CATEGORY_SCANNER](sensor-category-scanner.md)
##### [SENSOR_CATEGORY_UNSUPPORTED](sensor-category-unsupported.md)
#### [Sensor Properties](sensor-properties.md)
#### [Event Constants](event-constants.md)
## [Sensor API Glossary](sensors-glossary.md)

