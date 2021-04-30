---
description: Requests latitude/longitude report events.
ms.assetid: c26a388b-e042-43da-a220-e3ecfcbd03a8
title: LocationDisp.LatLongReportFactory.ListenForReports method (Locationapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.LatLongReportFactory.ListenForReports
api_type: 
- COM
api_location: 
- locationapi.h
---

# LocationDisp.LatLongReportFactory.ListenForReports method

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

Requests latitude/longitude report events.

## Syntax


```JScript
LocationDisp.LatLongReportFactory.ListenForReports(
  requestedReportInterval
)
```



## Parameters

<dl> <dt>

*requestedReportInterval* 
</dt> <dd> Number (**double word**) representing the requested time between latitude/longitude report events, in milliseconds. See Remarks.</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The location provider is not required to provide reports at the interval that you request. Read the value of the [**ReportInterval**](locationdisp-latlongreportfactory-reportinterval.md) property to discover the true report interval setting.

## Examples

For an example of how to use this method, see [Listening for LatLong Report Events](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | None supported<br/>                                                                |
| Header<br/>                   | <dl> <dt>Locationapi.h</dt> </dl> |



 

