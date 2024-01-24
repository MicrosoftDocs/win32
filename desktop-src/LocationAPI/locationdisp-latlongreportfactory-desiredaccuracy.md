---
description: LocationDisp.LatLongReportFactory.DesiredAccuracy property - The current desired-accuracy value.
ms.assetid: dfad833b-bb0c-4c66-9942-da10abee5381
title: LocationDisp.LatLongReportFactory.DesiredAccuracy property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.LatLongReportFactory.DesiredAccuracy
api_type: 
- COM
api_location: 
---

# LocationDisp.LatLongReportFactory.DesiredAccuracy property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

The current desired-accuracy value.

This property is read/write.

## Syntax


```JScript
DesiredAccuracy = LocationDisp.LatLongReportFactory.DesiredAccuracy
LocationDisp.LatLongReportFactory.DesiredAccuracy = DesiredAccuracy
```



## Property value

This property is a read/write **ULONG**.



| Value                                                                        | Meaning                                                                                                                                                                                            |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Default. The sensor should use the accuracy for which it can optimize power use and other cost considerations.<br/>                                                                          |
| <dl> <dt>1</dt> </dl> | The sensor should deliver the most accurate report possible. This includes using services that might charge money, or consuming higher levels of battery power or connection bandwidth.<br/> |



 

## Remarks

This value is a request to the location provider. The location provider is not required to provide reports at the interval you requested. Read the value of this property to discover the true report interval setting.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

