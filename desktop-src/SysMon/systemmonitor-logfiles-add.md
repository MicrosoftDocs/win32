---
title: LogFiles.Add method
description: Adds a log file to the collection.
ms.assetid: f6b671ea-9620-49a7-8b0c-0c8e1d9819b0
keywords:
- Add method SysMon
- Add method SysMon , LogFiles class
- LogFiles class SysMon , Add method
topic_type:
- apiref
api_name:
- LogFiles.Add
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# LogFiles.Add method

Adds a log file to the collection.

## Syntax


```VB
LogFiles.Add( _
  ByVal pathname As String _
) As LogFileItem
```



## Parameters

<dl> <dt>

*pathname* \[in\]
</dt> <dd>

Path to the log file. You can specify the path as an absolute, relative, or UNC path. The log file name extension must be either .csv, .tsv, or .blg.

</dd> </dl>

## Remarks

You must use the Logman.exe tool or the Perfmon.msc MMC snap-in to generate the log files that you add to this collection. For Perfmon.msc, the counter logs are located under **Performance Logs and Alerts**. For details on using Logman.exe or Perfmon.msc, search for Logman or Using Performance, respectively, in the **Help and Support Center**.

**Prior to Windows Vista:** You cannot add log files to the [**log file collection**](systemmonitor-logfiles.md) if the value of [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) is set to [**DataSourceTypeConstants.sysmonLogFiles**](/windows/desktop/api/ISysmon/ne-isysmon-datasourcetypeconstants). First, set **SystemMonitor.DataSourceType** to **DataSourceTypeConstants.sysmonNullDataSource**, add your log files and counters, and then set **SystemMonitor.DataSourceType** to **DataSourceTypeConstants.sysmonLogFiles**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[LogFiles](logfiles.md)
</dt> <dt>

[**LogFileItem**](logfileitem.md)
</dt> <dt>

[**LogFiles**](systemmonitor-logfiles.md)
</dt> </dl>

 

 





