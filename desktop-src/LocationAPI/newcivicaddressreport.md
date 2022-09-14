---
description: Occurs when a new civic address report is generated.
ms.assetid: a8df870e-6744-4e8a-a103-56b446da135f
title: NewCivicAddressReport event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NewCivicAddressReport
api_type: 
- COM
api_location: 
---

# NewCivicAddressReport event

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

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

For an example of how to use this event, see [Listening for Civic Address Report Events](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

