---
title: SystemMonitor DataSourceType property
description: Retrieves or sets the source of the performance counter data.
ms.assetid: 53c1e9bc-dafd-445c-8d82-13a74f6c488a
keywords:
- DataSourceType property SysMon
- DataSourceType property SysMon , SystemMonitor interface
- SystemMonitor interface SysMon , DataSourceType property
topic_type:
- apiref
api_name:
- SystemMonitor.DataSourceType
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor::DataSourceType property

Retrieves or sets the source of the performance counter data.

## Syntax


```VB
Property DataSourceType As DataSourceTypeConstants
```



## Property value

Source of the performance counter data. For possible values, see [**DataSourceTypeConstants**](/windows/win32/api/isysmon/ne-isysmon-datasourcetypeconstants).

## Exceptions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Exception type</th>
<th>Condition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>System.ArgumentException</strong></td>
<td>You can receive this exception for one of the following reasons:
<ul>
<li>The specified data source value is not valid.</li>
<li>If the data source is a log file, SYSMON cannot find one of the specified files. The Err.Number value is 0xC0000BD1.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Remarks

**Prior to Windows Vista:** You cannot add or remove a log files from the [**log file collection**](systemmonitor-logfiles.md) if the value of this property is set to sysmonLogFiles. Only set the value of this property to sysmonLogFiles after creating or modifying the log file collection.

Also, you cannot modify the [**SqlDsnName**](systemmonitor-sqldsnname.md) and [**SqlLogSetName**](systemmonitor-sqllogsetname.md) properties if the value of this property must not be set to sysmonSqlLog. Only set the value of this property to sysmonSqlLog after modifying the server and database names.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 





