---
title: SystemMonitor.LogFileName property
description: Retrieves or sets the name of a log file to use as the source of counter values displayed in the System Monitor.
ms.assetid: a93d1c98-4875-4d8e-940c-4443d1e585e6
keywords:
- LogFileName property SysMon
- LogFileName property SysMon , SystemMonitor class
- SystemMonitor class SysMon , LogFileName property
topic_type:
- apiref
api_name:
- SystemMonitor.LogFileName
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.LogFileName property

Retrieves or sets the name of a log file to use as the source of counter values displayed in the System Monitor.

> [!Note]  
> This property has been made obsolete by the [**LogFiles**](systemmonitor-logfiles.md) property.

 

This property is read-only.

## Syntax


```VB
Property LogFileName As String
```



## Property value

Path to the log file. You can specify an absolute, relative, or UNC path. The log file name extension must be either .csv, .tsv, or .blg.

## Exceptions



| Exception type                                  | Condition                                                              |
|-------------------------------------------------|------------------------------------------------------------------------|
| **System.Runtime.InteropServices.COMException** | Unable to find the specified file. The Err.Number value is 0xC0000BD1. |
| **System.ArgumentException**                    | You cannot specify an empty string.                                    |



 

## Remarks

This property returns the log file name from the first member of the [**LogFiles**](systemmonitor-logfiles.md) collection.

Setting this property will fail if the [**LogFiles**](systemmonitor-logfiles.md) collection contains one or more members.

You must use the Logman.exe tool or the Perfmon.msc MMC snap-in to generate the log files that you add to this collection. For Perfmon.msc, the counter logs are located under **Performance Logs and Alerts**. For details on using Logman.exe or Perfmon.msc, search for Logman or Using Performance, respectively, in the **Help and Support Center**.

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
</dt> </dl>

 

 





