---
Description: 'The OpenEventLog, OpenBackupEventLog, RegisterEventSource, DeregisterEventSource, and CloseEventLog functions open and close event log handles.'
ms.assetid: 'e42a66c2-2f1e-46f8-99c7-4701075c8ec3'
title: Event Logging Operations
---

# Event Logging Operations

The [**OpenEventLog**](openeventlog.md), [**OpenBackupEventLog**](openbackupeventlog.md), [**RegisterEventSource**](registereventsource.md), [**DeregisterEventSource**](deregistereventsource.md), and [**CloseEventLog**](closeeventlog.md) functions open and close event log handles.

The following table shows the operations that can be performed on an open event log, and the corresponding function for each operation.



| Operation | Function                                                                                                                     |
|-----------|------------------------------------------------------------------------------------------------------------------------------|
| Backup    | [**BackupEventLog**](backupeventlog.md)                                                                                     |
| Clear     | [**ClearEventLog**](cleareventlog.md)                                                                                       |
| Monitor   | [**NotifyChangeEventLog**](notifychangeeventlog.md)                                                                         |
| Query     | [**GetOldestEventLogRecord**](getoldesteventlogrecord.md), [**GetNumberOfEventLogRecords**](getnumberofeventlogrecords.md) |
| Read      | [**ReadEventLog**](readeventlog.md)                                                                                         |
| Write     | [**ReportEvent**](reportevent.md)                                                                                           |



 

The [**OpenEventLog**](openeventlog.md) and [**ReportEvent**](reportevent.md) functions take an optional server name as a parameter so the operations can be performed on the remote server. Use [**OpenEventLog**](openeventlog.md) for reading or performing administrative operations (backup, clear, monitor, and query) on the log, and use [**RegisterEventSource**](registereventsource.md) for writing to the log.

Each call to an event logging function is an atomic operation. When you read from the event log, only whole event records are returned. When you write to the event log, each event record is guaranteed to be written sequentially as a complete record in the log. The following list describes how the event-logging service handles special conditions:

-   The event-logging service receives a read operation and a write operation at the same time: If the read position is at the end of the file, either the read operation fails with an "end-of-file" status (if the write operation has not been completed), or it returns the new record (if the write operation has been completed).
-   The event-logging service completes a clear operation before receiving a read operation: The read operation fails with "end-of-file" status.
-   The event-logging service completes a clear operation before receiving a write operation: The clear operation truncates the log, then the write operation adds the new record at the beginning of the log.

 

 



