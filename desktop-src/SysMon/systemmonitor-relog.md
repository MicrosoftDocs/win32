---
title: SystemMonitor.Relog method
description: Relogs the counter data to a new file. You can also use this method to specify a new file type and to reduce the number of samples contained in the log file.
ms.assetid: 4439f9ef-99e0-47d4-8f6f-d08afcba672d
keywords:
- Relog method SysMon
- Relog method SysMon , SystemMonitor object
- SystemMonitor object SysMon , Relog method
topic_type:
- apiref
api_name:
- SystemMonitor.Relog
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.Relog method

Relogs the counter data to a new file. You can also use this method to specify a new file type and to reduce the number of samples contained in the log file.

## Syntax


```VB
SystemMonitor.Relog( _
  ByVal fileName As String, _
  ByVal fileType As SysmonFileType, _
  ByVal filter As Long _
)
```



## Parameters

<dl> <dt>

*fileName* \[in\]
</dt> <dd>

File path of the log file. You can specify the path as an absolute, relative, or UNC path. The log file name extension must be either .blg, .tsv, or .csv. If a folder in the path does not exist, SYSMON will create it. If the file exists, the file is overwritten. SYSMON applies the default ACLs from the parent directory.

</dd> <dt>

*fileType* \[in\]
</dt> <dd>

Format of the counter data saved to the log file. You can specify either [**SysmonFileType.sysmonFileBlg**](/windows/win32/api/isysmon/ne-isysmon-sysmonfiletype), **SysmonFileType.sysmonFileCsv**, or **SysmonFileType.sysmonFileTsv**.

</dd> <dt>

*filter* \[in\]
</dt> <dd>

Number of samples from the old log files to save in the new log file. Specify 1 to save every sample from the old files to the new files. Specify 2 to save one out of every two samples from the old file. Specify 3 to save one out of every three samples from the old file. And so on.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method uses the log files contained in the [**SystemMonitor.LogFiles**](systemmonitor-logfiles.md) collection to relog the counter data.

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

[**SystemMonitor.SaveAs**](systemmonitor-saveas.md)
</dt> </dl>

 

 





