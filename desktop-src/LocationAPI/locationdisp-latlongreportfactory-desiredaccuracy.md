---
Description: The current desired-accuracy value.
ms.assetid: dfad833b-bb0c-4c66-9942-da10abee5381
title: LocationDisp.LatLongReportFactory.DesiredAccuracy property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LocationDisp.LatLongReportFactory.DesiredAccuracy property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](https://msdn.microsoft.com/library/gg589513). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](https://msdn.microsoft.com/library/windows/apps/br225603) API.\]

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



|                                     |                                            |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

 




