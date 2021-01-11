---
description: Manages latitude/longitude reports.
ms.assetid: 66025874-32dd-4494-a9ad-12fe3afa60f9
title: LocationDisp.LatLongReportFactory object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.LatLongReportFactory
api_type: 
- COM
api_location: 
---

# LocationDisp.LatLongReportFactory object

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

Manages latitude/longitude reports.

## Members

The **LocationDisp.LatLongReportFactory** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **LocationDisp.LatLongReportFactory** object has these methods.



| Method                                                                                       | Description                                                                                   |
|:---------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**ListenForReports**](locationdisp-latlongreportfactory-listenforreports.md)               | Requests latitude/longitude report events.<br/>                                         |
| [**RequestPermissions**](locationdisp-latlongreportfactory-requestpermissions.md)           | Opens a system dialog box to request user permission for location-enabled devices.<br/> |
| [**StopListeningForReports**](/previous-versions/windows/desktop/legacy/dd317718(v=vs.85)) | Cancels requests for latitude/longitude report events.<br/>                             |



 

### Properties

The **LocationDisp.LatLongReportFactory** object has these properties.



| Property                                                                                | Access type           | Description                                                                                      |
|:----------------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------|
| [**DesiredAccuracy**](locationdisp-latlongreportfactory-desiredaccuracy.md)<br/> | Read/write<br/> | The current desired-accuracy value.<br/>                                                   |
| [**LatLongReport**](locationdisp-latlongreportfactory-latlongreport.md)<br/>     | Read-only<br/>  | The current [**LocationDisp.DispLatLongReport**](locationdisp-displatlongreport.md).<br/> |
| [**ReportInterval**](locationdisp-latlongreportfactory-reportinterval.md)<br/>   | Read/write<br/> | The current latitude/longitude report event interval in milliseconds.<br/>                 |
| [**Status**](locationdisp-latlongreportfactory-status.md)<br/>                   | Read-only<br/>  | The current report status.<br/>                                                            |



 

## Examples

The following example code shows how to create this object in HTML code.


```
<object id="latlongfactory" 
    classid="clsid:9DCC3CC8-8609-4863-BAD4-03601F4C65E8"
    type="application/x-oleobject">
</object>
```



The following example code shows how to create this object in JScript using Windows Script Host.


```JScript
var latlongfactory = WScript.CreateObject("LocationDisp.LatLongReportFactory");
```



The following example code shows how to create this object in VBScript using Windows Script Host.


```VB
Dim latlongfactory
Set latlongfactory = WScript.CreateObject("LocationDisp.LatLongReportFactory")
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



## See also

<dl> <dt>

[**LocationDisp.DispLatLongReport**](locationdisp-displatlongreport.md)
</dt> </dl>

 

