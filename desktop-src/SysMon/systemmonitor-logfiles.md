---
title: SystemMonitor.LogFiles property
description: Collection of one or more log files to use as the source of counter values displayed in the System Monitor.
ms.assetid: 6e9e7205-3516-404d-b67d-777e484900da
keywords:
- LogFiles property SysMon
- LogFiles property SysMon , SystemMonitor object
- SystemMonitor object SysMon , LogFiles property
topic_type:
- apiref
api_name:
- SystemMonitor.LogFiles
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.LogFiles property

Collection of one or more log files to use as the source of counter values displayed in the System Monitor.

## Syntax


```VB
Property LogFiles As ILogFiles
```



## Property value

Collection of [**LogFileItem**](logfileitem.md) objects that specify the log files used as the data source for the graph.

## Remarks

To add or remove a log file from the log file collection, the value of [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) must not be set to sysmonLogFiles.

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

[**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md)
</dt> <dt>

[**SystemMonitor.LogViewStart**](systemmonitor-logviewstart.md)
</dt> <dt>

[**SystemMonitor.LogViewStop**](systemmonitor-logviewstop.md)
</dt> <dt>

[**SystemMonitor.SqlLogSetName**](systemmonitor-sqllogsetname.md)
</dt> </dl>

 

 





