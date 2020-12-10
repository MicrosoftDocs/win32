---
title: SystemMonitor.ChartScroll property
description: Retrieves or sets a value that determines if the line graph scrolls in the view.
ms.assetid: df4806be-dfd3-4ff7-985d-b46c00bb19f8
keywords:
- ChartScroll property SysMon
- ChartScroll property SysMon , SystemMonitor object
- SystemMonitor object SysMon , ChartScroll property
topic_type:
- apiref
api_name:
- SystemMonitor.ChartScroll
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.ChartScroll property

Retrieves or sets a value that determines if the line graph scrolls in the view.

## Syntax


```VB
Property ChartScroll As Boolean
```



## Property value

True if the line graph scrolls continuously from right to left; otherwise, False if the line graph is drawn from left to right and wraps around on itself in the view. False is the default.

## Remarks

This value is ignored if the [**SystemMonitor.DisplayType**](systemmonitor-displaytype.md) is not [**DisplayTypeConstants.sysmonLineGraph**](/windows/win32/api/isysmon/ne-isysmon-displaytypeconstants).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





