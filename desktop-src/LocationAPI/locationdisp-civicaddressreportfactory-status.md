---
Description: The current report status.
ms.assetid: 3aae0b61-cdaa-4131-b6e1-406813bb1848
title: LocationDisp.CivicAddressReportFactory.Status property
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocationDisp.CivicAddressReportFactory.Status
api_type: 
- COM
api_location: 
---

# LocationDisp.CivicAddressReportFactory.Status property

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](https://msdn.microsoft.com/library/gg589513). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](https://msdn.microsoft.com/library/windows/apps/br225603) API.\]

The current report status.

This property is read-only.

## Syntax


```JScript
Status = LocationDisp.CivicAddressReportFactory.Status
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

For an example of how to use this property, see [Listening for Civic Address Report Events](https://msdn.microsoft.com/library/windows/apps/br225603).

## Requirements



|                                     |                                            |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

 




