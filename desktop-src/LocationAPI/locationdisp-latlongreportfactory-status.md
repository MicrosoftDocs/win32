---
description: LocationDisp.LatLongReportFactory.Status property - The current report status.
ms.assetid: bcdf76b5-88c4-481a-89ac-2b9558cecfc0
title: LocationDisp.LatLongReportFactory.Status property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.LatLongReportFactory.Status
api_type: 
- COM
api_location: 
---

# LocationDisp.LatLongReportFactory.Status property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

The current report status.

This property is read-only.

## Syntax


```JScript
Status = LocationDisp.LatLongReportFactory.Status
```



## Property value

This property is a read-only **Number** (unsigned long).



| Status                                                                                               | Meaning                          |
|------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Report not supported.<br/> |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Error.<br/>                |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Access denied.<br/>        |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Initializing.<br/>         |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Running.<br/>              |



 

## Examples

For an example of how to use this property, see [Listening for LatLong Report Events](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

