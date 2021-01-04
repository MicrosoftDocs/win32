---
title: SystemMonitor.ShowTimeAxisLabels property
description: Retrieves or sets a value that determines if the horizontal (X) axis of the graph view contains labels.
ms.assetid: 9e9d2d2c-f053-4afe-85de-25242842498f
keywords:
- ShowTimeAxisLabels property SysMon
- ShowTimeAxisLabels property SysMon , SystemMonitor object
- SystemMonitor object SysMon , ShowTimeAxisLabels property
topic_type:
- apiref
api_name:
- SystemMonitor.ShowTimeAxisLabels
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.ShowTimeAxisLabels property

Retrieves or sets a value that determines if the horizontal (X) axis of the graph view contains labels.

## Syntax


```VB
Property ShowTimeAxisLabels As Boolean
```



## Property value

A value of True will apply labels to the x-axis. A value of False will not. The default is False.

## Remarks

SYSMON ignores this property for bar graphs, reports and histograms.

For line graphs, SYSMON uses the time that the counter value was sampled as the label.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





