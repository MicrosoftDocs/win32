---
description: Occurs when the operational status of a report changes.
ms.assetid: f0c4e678-1666-4f99-89de-85879eacd0ac
title: StatusChanged event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- StatusChanged
api_type: 
- COM
api_location: 
---

# StatusChanged event

\[The Location API object model is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, to access location from a website, use the [W3C Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85)). To access location from a desktop application, use the [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API.\]

Occurs when the operational status of a report changes.

## Syntax


```JScript
.StatusChanged(
  status
)
```



## Parameters

<dl> <dt>

*status* 
</dt> <dd>

The new status.



| Status                                                                                               | Meaning                          |
|------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Report not supported.<br/> |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Error.<br/>                |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Access denied.<br/>        |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Initializing.<br/>         |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Running.<br/>              |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

You should implement separate status change report handlers for civic address reports and latitude/longitude reports.

## Examples

For an example of how to use this event, see [Listening for LatLong Report Events](/uwp/api/Windows.Devices.Geolocation).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                  |



 

