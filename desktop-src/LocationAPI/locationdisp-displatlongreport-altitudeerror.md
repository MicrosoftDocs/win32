---
description: Altitude error, in meters.
ms.assetid: 36ebb079-26e6-4b3f-ad73-547a47bd23d7
title: LocationDisp.DispLatLongReport.AltitudeError property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.DispLatLongReport.AltitudeError
api_type: 
- COM
api_location: 
---

# LocationDisp.DispLatLongReport.AltitudeError property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

Altitude error, in meters.

This property is read-only.

## Syntax


```JScript
AltitudeError = LocationDisp.DispLatLongReport.AltitudeError
```



## Property value

This property is a read-only **Number** (double precision floating point).

## Remarks

Location sensors are not required to provide this property. You should handle exceptions when attempting to access this property.

## Examples

For an example of how to use this property, see [A Simple LatLong Report Example](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

