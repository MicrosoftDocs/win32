---
title: SystemMonitor.GetLogViewRange method
description: Retrieves the starting date used to retrieve counter values from the log files.
ms.assetid: c74c3a5b-d2ec-43d8-b715-e399f42e8ae5
keywords:
- GetLogViewRange method SysMon
- GetLogViewRange method SysMon , SystemMonitor object
- SystemMonitor object SysMon , GetLogViewRange method
topic_type:
- apiref
api_name:
- SystemMonitor.GetLogViewRange
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.GetLogViewRange method

Retrieves the starting date used to retrieve counter values from the log files.

## Syntax


```VB
SystemMonitor.GetLogViewRange( _
  ByRef StartTime As Date, _
  ByRef StopTime As Date _
)
```



## Parameters

<dl> <dt>

*StartTime* \[out\]
</dt> <dd>

Starting date used to retrieve counter values from the log files.

</dd> <dt>

*StopTime* \[out\]
</dt> <dd>

Ending date used to retrieve counter values from the log files.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

SYSMON retrieves counter values from the log files that falls within the start and stop dates, inclusively.

Using this method is the same as accessing the [**SystemMonitor.LogViewStart**](systemmonitor-logviewstart.md) and [**SystemMonitor.LogViewStop**](systemmonitor-logviewstop.md) properties.

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

[**SystemMonitor.SetLogViewRange**](systemmonitor-setlogviewrange.md)
</dt> </dl>

 

 





