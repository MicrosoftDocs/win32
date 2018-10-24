---
Description: Occurs when a new latitude/longitude report is generated.
ms.assetid: 2b1a25a1-ccd6-43f8-979b-c2d414d666a2
title: NewLatLongReport event
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NewLatLongReport
api_type: 
- COM
api_location: 
---

# NewLatLongReport event

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](https://msdn.microsoft.com/library/gg589513). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](https://msdn.microsoft.com/library/windows/apps/br225603) API.\]

Occurs when a new latitude/longitude report is generated.

## Syntax


```JScript
.NewLatLongReport(
  newReport
)
```



## Parameters

<dl> <dt>

*newReport* 
</dt> <dd>

The new [**LocationDisp.DispLatLongReport**](locationdisp-displatlongreport.md) object.

</dd> </dl>

## Return value

This event does not return a value.

## Examples

For an example of how to use this event, see [Listening for LatLong Report Events](https://msdn.microsoft.com/library/windows/apps/br225603).

## Requirements



|                                     |                                            |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

 




