---
title: SystemMonitor.EnableToolTips property
description: Retrieves or sets a value that determines if a tool tip is shown when the mouse hovers over a counter in one of the graph views (not supported for report view).
ms.assetid: af9a78ea-a9de-4343-8978-4316769a5f30
keywords:
- EnableToolTips property SysMon
- EnableToolTips property SysMon , SystemMonitor object
- SystemMonitor object SysMon , EnableToolTips property
topic_type:
- apiref
api_name:
- SystemMonitor.EnableToolTips
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.EnableToolTips property

Retrieves or sets a value that determines if a tool tip is shown when the mouse hovers over a counter in one of the graph views (not supported for report view).

## Syntax


```VB
Property EnableToolTips As Boolean
```



## Property value

True displays a tool tip with the counter information in it; otherwise, False.

## Remarks

For line graphs, the tool tip is anchored to the data point that is closest to the mouse. For bar charts and histograms, the tool tip represents the total data value of the bar, not a point within the bar.

The tool tip contains different information based upon the data source. For log files, the tool tip contains the counter path, counter value, time stamp, number of data samples included in the data point, and the minimum and maximum data values.

For real time activity, the tool tip contains the counter path, counter value, and time stamp.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





