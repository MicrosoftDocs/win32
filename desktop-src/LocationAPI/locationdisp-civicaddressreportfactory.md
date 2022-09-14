---
description: Manages civic address reports.
ms.assetid: 46c2d001-409a-4a0a-9006-1c2c9d327c13
title: LocationDisp.CivicAddressReportFactory object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.CivicAddressReportFactory
api_type: 
- COM
api_location: 
---

# LocationDisp.CivicAddressReportFactory object

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

Manages civic address reports.

## Members

The **LocationDisp.CivicAddressReportFactory** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **LocationDisp.CivicAddressReportFactory** object has these methods.



| Method                                                                                            | Description                                                                                   |
|:--------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**ListenForReports**](locationdisp-civicaddressreportfactory-listenforreports.md)               | Requests civic address report events.<br/>                                              |
| [**RequestPermissions**](locationdisp-civicaddressreportfactory-requestpermissions.md)           | Opens a system dialog box to request user permission for location-enabled devices.<br/> |
| [**StopListeningForReports**](locationdisp-civicaddressreportfactory-stoplisteningforreports.md) | Cancels civic address report event requests.<br/>                                       |



 

### Properties

The **LocationDisp.CivicAddressReportFactory** object has these properties.



| Property                                                                                        | Access type           | Description                                                                                                |
|:------------------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------|
| [**CivicAddressReport**](locationdisp-dispcivicaddressreport-civicaddressreport.md)<br/> | Read-only<br/>  | The current [**LocationDisp.DispCivicAddressReport**](locationdisp-dispcivicaddressreport.md).<br/> |
| [**DesiredAccuracy**](locationdisp-civicaddressreportfactory-desiredaccuracy.md)<br/>    | Read/write<br/> | The current desired-accuracy setting.<br/>                                                           |
| [**ReportInterval**](locationdisp-civicaddressreportfactory-reportinterval.md)<br/>      | Read/write<br/> | The current civic address report event interval in milliseconds.<br/>                                |
| [**Status**](locationdisp-civicaddressreportfactory-status.md)<br/>                      | Read-only<br/>  | The current report status.<br/>                                                                      |



 

## Examples

The following example code shows how to create this object in HTML code.


```Text
<object id="civicfactory" 
    classid="clsid:2A11F42C-3E81-4ad4-9CBE-45579D89671A"
    type="application/x-oleobject">
</object>
```



The following example code shows how to create this object in JScript using Windows Script Host.


```JScript
var civicfactory = WScript.CreateObject("LocationDisp.CivicAddressReportFactory");
```



The following example code shows how to create this object in VBScript using Windows Script Host.


```VB
Dim civicfactory
Set civicfactory = WScript.CreateObject("LocationDisp.CivicAddressReportFactory")
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



## See also

<dl> <dt>

[**LocationDisp.CivicAddressReport**](locationdisp-dispcivicaddressreport.md)
</dt> </dl>

 

