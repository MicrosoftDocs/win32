---
Description: Occurs when a new civic address report is generated.
ms.assetid: a8df870e-6744-4e8a-a103-56b446da135f
title: NewCivicAddressReport event
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewCivicAddressReport event

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](https://msdn.microsoft.com/library/gg589513). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](https://msdn.microsoft.com/library/windows/apps/br225603) API.\]

Occurs when a new civic address report is generated.

## Syntax


```JScript
.NewCivicAddressReport(
  newReport
)
```



## Parameters

<dl> <dt>

*newReport* 
</dt> <dd>

The new [**LocationDisp.DispCivicAddressReport**](locationdisp-dispcivicaddressreport.md) object.

</dd> </dl>

## Return value

This event does not return a value.

## Examples

For an example of how to use this event, see [Listening for Civic Address Report Events](https://msdn.microsoft.com/library/windows/apps/br225603).

## Requirements



|                                     |                                            |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

 




