---
title: SystemMonitor.EnableDigitGrouping property
description: Retrieves or sets a value that determines if SYSMON uses digit grouping when displaying numeric values.
ms.assetid: 6a277960-fd01-423c-af2a-b35ed46c6d9a
keywords:
- EnableDigitGrouping property SysMon
- EnableDigitGrouping property SysMon , SystemMonitor object
- SystemMonitor object SysMon , EnableDigitGrouping property
topic_type:
- apiref
api_name:
- SystemMonitor.EnableDigitGrouping
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.EnableDigitGrouping property

Retrieves or sets a value that determines if SYSMON uses digit grouping when displaying numeric values.

## Syntax


```VB
Property EnableDigitGrouping As Boolean
```



## Property value

If True, SYSMON will group digits when displaying numeric values, for example, 1,214. If False, numeric values are not grouped, for example, 1214. True is the default.

## Remarks

The digit grouping symbol is localized.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





