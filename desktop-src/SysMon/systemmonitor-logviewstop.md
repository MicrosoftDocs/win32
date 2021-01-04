---
title: SystemMonitor.LogViewStop property
description: Retrieves or sets the ending date used to retrieve counter values from the log files.
ms.assetid: 5dabfb26-fa33-4fb5-a075-ed8955a56f1e
keywords:
- LogViewStop property SysMon
- LogViewStop property SysMon , SystemMonitor object
- SystemMonitor object SysMon , LogViewStop property
topic_type:
- apiref
api_name:
- SystemMonitor.LogViewStop
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.LogViewStop property

Retrieves or sets the ending date used to retrieve counter values from the log files.

This property is read-only.

## Syntax


```VB
Property LogViewStop As Date
```



## Property value

Ending date used to retrieve counter values from the log files.

## Remarks

SYSMON retrieves counter values from the log files that falls within the [**SystemMonitor.LogViewStart**](systemmonitor-logviewstart.md) and stop dates, inclusively.

If you do not specify a stop value or you set this property to a date value that is later than the last date contained in the log file, SYSMON changes the value to the latest date value found in the log files.

If this property is set to a date value that is less than [**LogViewStart**](systemmonitor-logviewstart.md), SYSMON changes the value to the value of **LogViewStart**.

You must set the start date before you set the stop date; otherwise, both values are set to Date.MinValue, and if you set the dates after setting [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md), then only the first counter value is retrieved from the log file.

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

[**SystemMonitor.GetLogViewRange**](systemmonitor-getlogviewrange.md)
</dt> <dt>

[**SystemMonitor.LogSourceStopTime**](systemmonitor-logsourcestoptime.md)
</dt> <dt>

[**SystemMonitor.LogViewStart**](systemmonitor-logviewstart.md)
</dt> <dt>

[**SystemMonitor.SetLogViewRange**](systemmonitor-setlogviewrange.md)
</dt> </dl>

 

 





