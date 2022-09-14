---
title: SYSMON Return Values
description: The following is a list of the System Monitor return values that are defined in Smonmsg.h.
ms.assetid: f1cc7668-4a6f-4b70-9591-62bd447fe8fb
ms.topic: article
ms.date: 05/31/2018
---

# SYSMON Return Values

The following is a list of the System Monitor return values that are defined in Smonmsg.h.



| Return value                                       | Description                                                                                                                                                                                                                                  |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SMON\_STATUS\_DUPL\_COUNTER\_PATH (0xC0001388)     | The counter collection already contains the specified counter.                                                                                                                                                                               |
| SMON\_STATUS\_NO\_SYSMON\_OBJECT (0xC0001389)      | The settings do not contain any complete System Monitor HTML objects.                                                                                                                                                                        |
| SMON\_STATUS\_TOO\_FEW\_SAMPLES (0xC000138A)       | The specified log file contains fewer than two data samples.                                                                                                                                                                                 |
| SMON\_STATUS\_LOG\_FILE\_SIZE\_LIMIT (0xC000138B)  | The specified log file exceeds the size limits of the System Monitor control. If a log file is currently selected, select current activity as the data source in order to unload the current log file, then reselect the specified log file. |
| SMON\_STATUS\_LOG\_FILE\_DATA\_SOURCE (0xC000138C) | To add a new log file to the data source, the data source type must be changed to a type other than sysmonLogFiles.                                                                                                                          |
| SMON\_STATUS\_DUPL\_LOG\_FILE\_PATH (0xC000138D)   | The log file collection already contains the specified log file.                                                                                                                                                                             |



 

For a description of additional return values returned by System Monitor, see [System Error Codes](/windows/desktop/Debug/system-error-codes) and [Performance Data Helper Error Codes](/windows/desktop/PerfCtrs/checking-pdh-interface-return-values).

 

 