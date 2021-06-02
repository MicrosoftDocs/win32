---
title: SystemMonitor.SetLogViewRange method
description: Sets the starting date used to retrieve counter values from the log files.
ms.assetid: ced641d0-cf71-4826-8ff0-c05f20a71aaa
keywords:
- SetLogViewRange method SysMon
- SetLogViewRange method SysMon , SystemMonitor object
- SystemMonitor object SysMon , SetLogViewRange method
topic_type:
- apiref
api_name:
- SystemMonitor.SetLogViewRange
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.SetLogViewRange method

Sets the starting date used to retrieve counter values from the log files.

## Syntax


```VB
SystemMonitor.SetLogViewRange( _
  ByVal StartTime As Date, _
  ByVal StopTime As Date _
)
```



## Parameters

<dl> <dt>

*StartTime* \[in\]
</dt> <dd>

Starting date used to retrieve counter values from the log files.

</dd> <dt>

*StopTime* \[in\]
</dt> <dd>

Ending date used to retrieve counter values from the log files.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

SYSMON retrieves counter values from the log files that falls within the start and stop dates, inclusively.

If you do not specify a start date or if you set the start date to a date value that is outside the range of date values found in the log files, SYSMON changes the value to the earliest date value found in the log files. If the start value is greater than the stop value, SYSMON changes the start value to be the same value as the stop value.

If you do not specify a stop value or you set the stop value to a date value that is later than the last date contained in the log file, SYSMON changes the value to the latest date value found in the log files. If the stop value is less than the stop value, SYSMON changes the stop value to be the same value as the start value.

If you specify a start and stop date, you should specify the dates before setting [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md). If you set the dates after setting **SystemMonitor.DataSourceType**, then only the first counter value is retrieved from the log file.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> <dt>

[**SystemMonitor.GetLogViewRange**](systemmonitor-getlogviewrange.md)
</dt> </dl>

 

 





