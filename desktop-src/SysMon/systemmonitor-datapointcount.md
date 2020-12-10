---
title: SystemMonitor.DataPointCount property
description: Retrieves or sets the number of data points displayed in a line graph.
ms.assetid: bc1a86c2-635b-4e93-ac96-e7be4b1d375a
keywords:
- DataPointCount property SysMon
- DataPointCount property SysMon , SystemMonitor object
- SystemMonitor object SysMon , DataPointCount property
topic_type:
- apiref
api_name:
- SystemMonitor.DataPointCount
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.DataPointCount property

Retrieves or sets the number of data points displayed in a line graph.

## Syntax


```VB
Property DataPointCount As Long
```



## Property value

Number of data points displayed in the view for a line graph. The default value is 100 data points. The valid range of values is 2 to 1,000.

## Remarks

This property is used only if [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) is **sysmonCurrentActivity**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





