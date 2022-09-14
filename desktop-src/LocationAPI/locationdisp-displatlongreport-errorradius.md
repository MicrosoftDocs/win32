---
description: A distance from the reported location, in meters. Combined with the reported location as the origin, this radius describes the circle in which the actual location is probably located.
ms.assetid: a9565bd5-d1e0-45f8-abeb-3191b16480fa
title: LocationDisp.DispLatLongReport.ErrorRadius property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.DispLatLongReport.ErrorRadius
api_type: 
- COM
api_location: 
---

# LocationDisp.DispLatLongReport.ErrorRadius property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

A distance from the reported location, in meters. Combined with the reported location as the origin, this radius describes the circle in which the actual location is probably located.

This property is read-only.

## Syntax


```JScript
ErrorRadius = LocationDisp.DispLatLongReport.ErrorRadius
```



## Property value

This property is a read-only **Number** (double precision floating point).

## Examples

For an example of how to use this property, see [A Simple LatLong Report Example](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

