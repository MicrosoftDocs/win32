---
title: LogFiles object (Isysmon.h)
description: Use this class to manage a collection of one or more log files that contain performance counter data.To retrieve this object, call SystemMonitor.LogFiles.
ms.assetid: 1af475c5-ed0c-49b4-a558-13eb8758a986
keywords:
- LogFiles object SysMon
- LogFiles object SysMon , described
topic_type:
- apiref
api_name:
- LogFiles
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# LogFiles object

Use this class to manage a collection of one or more log files that contain performance counter data.

To retrieve this object, call [**SystemMonitor.LogFiles**](systemmonitor-logfiles.md).

## Members

The **LogFiles** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **LogFiles** object has these methods.



| Method                                          | Description                                                                           |
|:------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**Add**](systemmonitor-logfiles-add.md)       | Adds a [**LogFileItem**](logfileitem.md) instance to the collection.<br/>      |
| [**Remove**](systemmonitor-logfiles-remove.md) | Removes a [**LogFileItem**](logfileitem.md) instance from the collection.<br/> |



 

### Properties

The **LogFiles** object has these properties.



| Property                                                 | Description                                                                                         |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**Count**](systemmonitor-logfiles-count.md)<br/> | Retrieves the number of [**LogFileItem**](logfileitem.md) instances in the collection.<br/>  |
| [**Item**](systemmonitor-logfiles-item.md)<br/>   | Retrieves the specified [**LogFileItem**](logfileitem.md) instance from the collection.<br/> |



 

## Remarks

To have SYSMON display performance counters from a log file, set [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) to [**DataSourceTypeConstants.sysmonLogFiles**](/windows/desktop/api/ISysmon/ne-isysmon-datasourcetypeconstants). After adding the log files to the collection, use the [**Counters**](counters.md) collection to specify the counters data that you want to read from the log files. Note that if **SystemMonitor.DataSourceType** is set to **DataSourceTypeConstants.sysmonLogFiles**, SYSMON will resample the log files each time you add a log file or counter to their respective collections.

**Prior to Windows Vista:** You cannot add log files to the [**log file collection**](systemmonitor-logfiles.md) if the value of [**SystemMonitor.DataSourceType**](systemmonitor-datasourcetype.md) is set to [**DataSourceTypeConstants.sysmonLogFiles**](/windows/desktop/api/ISysmon/ne-isysmon-datasourcetypeconstants). First, set **SystemMonitor.DataSourceType** to **DataSourceTypeConstants.sysmonNullDataSource**, add your log files and counters, and then set **SystemMonitor.DataSourceType** to **DataSourceTypeConstants.sysmonLogFiles**.

The [**SystemMonitor.LogViewStart**](systemmonitor-logviewstart.md) and [**SystemMonitor.LogViewStop**](systemmonitor-logviewstop.md) properties specify the range of sampled values from the log files to graph. SYSMON graphs only one view worth of data from the log file (the graph view does not scroll as it does when graphing the current activity of the computer). If the sampled data exceeds what can be shown on a single graph view, SYSMON compresses the sampled data (each graphed point represents the average of multiple sampled values) to fit all the sampled data from the log files on the graph.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Isysmon.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 





