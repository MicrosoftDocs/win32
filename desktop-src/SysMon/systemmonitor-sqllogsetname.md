---
title: SystemMonitor SqlLogSetName property
description: Retrieves or sets the friendly name of the log set.
ms.assetid: a4593743-6b70-4f70-8e91-3324a808d97b
keywords:
- SqlLogSetName property SysMon
- SqlLogSetName property SysMon , SystemMonitor interface
- SystemMonitor interface SysMon , SqlLogSetName property
topic_type:
- apiref
api_name:
- SystemMonitor.SqlLogSetName
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor::SqlLogSetName property

Retrieves or sets the friendly name of the log set.

## Syntax


```VB
Property SqlLogSetName As String
```



## Property value

Friendly name of the log set, which corresponds to a single log file containing binary or text data in the SQL database.

## Remarks

**Prior to Windows Vista:** You cannot modify this property if the value of [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) is set to sysmonSqlLog.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> <dt>

[**SystemMonitor.SqlDsnName**](systemmonitor-sqllogsetname.md)
</dt> </dl>

 

 





