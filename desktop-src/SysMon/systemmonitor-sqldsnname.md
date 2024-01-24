---
title: SystemMonitor SqlDsnName property
description: Retrieves or sets the ODBC data source name (DSN).
ms.assetid: 7906204a-a208-42c7-855b-c29689b4d36a
keywords:
- SqlDsnName property SysMon
- SqlDsnName property SysMon , SystemMonitor interface
- SystemMonitor interface SysMon , SqlDsnName property
topic_type:
- apiref
api_name:
- SystemMonitor.SqlDsnName
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor::SqlDsnName property

Retrieves or sets the ODBC data source name (DSN).

## Syntax


```VB
Property SqlDsnName As String
```



## Property value

ODBC data source name that points to a database that contains the correct Perfmon tables. The format is SQL:DSN.

## Remarks

You must use the Perfmon.msc MMC snap-in to generate the SQL log file. The counter logs are located under **Performance Logs and Alerts**. To specify an SQL log, right-click the log file you created and select **Properties** from the menu. On the **Log Files** property page, select **SQL Database** from the **Log file type** drop-down list box.

**Prior to Windows Vista:** You cannot modify this property if the value of [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) is set to [**DataSourceTypeConstants.sysmonSqlLog**](/windows/desktop/api/ISysmon/ne-isysmon-datasourcetypeconstants). You must first specify the name and then set **SystemMonitor.DataSourceType** to **DataSourceTypeConstants.sysmonSqlLog**.

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

[**SystemMonitor.SqlLogSetName**](systemmonitor-sqllogsetname.md)
</dt> </dl>

 

 





