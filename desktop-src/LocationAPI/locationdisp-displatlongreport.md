---
Description: Represents a latitude/longitude report.
ms.assetid: efa8d805-8546-4bab-95a0-69e1edc28753
title: LocationDisp.DispLatLongReport object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.DispLatLongReport
api_type: 
- COM
api_location: 
---

# LocationDisp.DispLatLongReport object

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](https://msdn.microsoft.com/library/gg589513). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](https://msdn.microsoft.com/library/windows/apps/br225603) API.\]

Represents a latitude/longitude report.

## Members

The **LocationDisp.DispLatLongReport** object has these types of members:

-   [Properties](#properties)

### Properties

The **LocationDisp.DispLatLongReport** object has these properties.



| Property                                                                         | Access type          | Description                                                                                                                                                                                       |
|:---------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Altitude**](locationdisp-displatlongreport-altitude.md)<br/>           | Read-only<br/> | Current altitude, in meters.<br/>                                                                                                                                                           |
| [**AltitudeError**](locationdisp-displatlongreport-altitudeerror.md)<br/> | Read-only<br/> | Altitude error, in meters.<br/>                                                                                                                                                             |
| [**ErrorRadius**](locationdisp-displatlongreport-errorradius.md)<br/>     | Read-only<br/> | A distance from the reported location, in meters. Combined with the reported location as the origin, this radius describes the circle in which the actual location is proably located.<br/> |
| [**Latitude**](locationdisp-displatlongreport-latitude.md)<br/>           | Read-only<br/> | Current latitude, in degrees.<br/>                                                                                                                                                          |
| [**Longitude**](locationdisp-displatlongreport-longitude.md)<br/>         | Read-only<br/> | Current longitude, in degrees.<br/>                                                                                                                                                         |
| [**Timestamp**](locationdisp-displatlongreport-timestamp.md)<br/>         | Read-only<br/> | The date and time when the report was generated.<br/>                                                                                                                                       |



 

## Remarks

You can retrieve this object through the [**LatLongReport**](locationdisp-latlongreportfactory-latlongreport.md) property of the [**LatLongReportFactory**](locationdisp-latlongreportfactory.md) object. You can receive this object through the [**NewLatLongReport**](newlatlongreport.md) event.

## Requirements



|                                     |                                            |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

 




