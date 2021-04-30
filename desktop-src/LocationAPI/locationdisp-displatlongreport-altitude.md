---
description: Current altitude, in meters. Altitude is relative to the reference ellipsoid.
ms.assetid: fbe9984c-aa9d-4ce0-9f8b-d79ca06764d4
title: LocationDisp.DispLatLongReport.Altitude property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.DispLatLongReport.Altitude
api_type: 
- COM
api_location: 
---

# LocationDisp.DispLatLongReport.Altitude property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

Current altitude, in meters. Altitude is relative to the reference ellipsoid.

This property is read-only.

## Syntax


```JScript
Altitude = LocationDisp.DispLatLongReport.Altitude
```



## Property value

This property is a read-only **Number** (double precision floating point).

## Remarks

Location sensors are not required to provide this property. You should handle exceptions when attempting to access this property.

The **Altitude** method retrieves the altitude relative to the reference ellipsoid that is defined by the latest revision of the World Geodetic System (WGS 84), rather than the altitude relative to sea level.

## Examples

For an example of how to use this property, see [A Simple LatLong Report Example](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

