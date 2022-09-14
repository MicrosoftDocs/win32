---
description: LocationDisp.CivicAddressReportFactory.DesiredAccuracy property - The current desired-accuracy value.
ms.assetid: 296164cf-a8ed-4277-bb4c-83ac09e63291
title: LocationDisp.CivicAddressReportFactory.DesiredAccuracy property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.CivicAddressReportFactory.DesiredAccuracy
api_type: 
- COM
api_location: 
---

# LocationDisp.CivicAddressReportFactory.DesiredAccuracy property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

The current desired-accuracy value.

This property is read/write.

## Syntax


```JScript
DesiredAccuracy = LocationDisp.CivicAddressReportFactory.DesiredAccuracy
LocationDisp.CivicAddressReportFactory.DesiredAccuracy = DesiredAccuracy
```



## Property value

This property is a read/write **ULONG**.



| Value                                                                        | Meaning                                                                                                                                                                                            |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Default. The sensor should use the accuracy for which it can optimize power use and other cost considerations.<br/>                                                                          |
| <dl> <dt>1</dt> </dl> | The sensor should deliver the most accurate report possible. This includes using services that might charge money, or consuming higher levels of battery power or connection bandwidth.<br/> |



 

## Remarks

This value is a request to the location provider. The location provider is not required to provide the accuracy that you request. Read the value of this property to discover the true accuracy setting.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

