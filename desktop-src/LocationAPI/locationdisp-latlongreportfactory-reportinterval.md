---
description: The current latitude/longitude report event interval in milliseconds.
ms.assetid: bb33c4c1-805d-4519-8363-b0221d420b36
title: LocationDisp.LatLongReportFactory.ReportInterval property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.LatLongReportFactory.ReportInterval
api_type: 
- COM
api_location: 
---

# LocationDisp.LatLongReportFactory.ReportInterval property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

The current latitude/longitude report event interval in milliseconds.

This property is read/write.

## Syntax


```JScript
ReportInterval = LocationDisp.LatLongReportFactory.ReportInterval
LocationDisp.LatLongReportFactory.ReportInterval = ReportInterval
```



## Property value

This property is a read/write **ULONG**.

## Remarks

This value is a request to the location provider. The location provider is not required to provide reports at the interval that you request. Read the value of this property to discover the true report interval setting.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

