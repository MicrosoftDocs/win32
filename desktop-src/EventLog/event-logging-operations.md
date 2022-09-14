---
description: The OpenEventLog, OpenBackupEventLog, RegisterEventSource, DeregisterEventSource, and CloseEventLog functions open and close event log handles.
ms.assetid: e42a66c2-2f1e-46f8-99c7-4701075c8ec3
title: Event Logging Operations
ms.topic: article
ms.date: 05/31/2018
---

# Event Logging Operations

The [**OpenEventLog**](/windows/desktop/api/Winbase/nf-winbase-openeventloga), [**OpenBackupEventLog**](/windows/desktop/api/Winbase/nf-winbase-openbackupeventloga), [**RegisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-registereventsourcea), [**DeregisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-deregistereventsource), and [**CloseEventLog**](/windows/desktop/api/Winbase/nf-winbase-closeeventlog) functions open and close event log handles.

The following table shows the operations that can be performed on an open event log, and the corresponding function for each operation.



| Operation | Function                                                                                                                     |
|-----------|------------------------------------------------------------------------------------------------------------------------------|
| Backup    | [**BackupEventLog**](/windows/desktop/api/Winbase/nf-winbase-backupeventloga)                                                                                     |
| Clear     | [**ClearEventLog**](/windows/desktop/api/Winbase/nf-winbase-cleareventloga)                                                                                       |
| Monitor   | [**NotifyChangeEventLog**](/windows/desktop/api/Winbase/nf-winbase-notifychangeeventlog)                                                                         |
| Query     | [**GetOldestEventLogRecord**](/windows/desktop/api/Winbase/nf-winbase-getoldesteventlogrecord), [**GetNumberOfEventLogRecords**](/windows/desktop/api/Winbase/nf-winbase-getnumberofeventlogrecords) |
| Read      | [**ReadEventLog**](/windows/desktop/api/Winbase/nf-winbase-readeventloga)                                                                                         |
| Write     | [**ReportEvent**](/windows/desktop/api/Winbase/nf-winbase-reporteventa)                                                                                           |



 

The [**OpenEventLog**](/windows/desktop/api/Winbase/nf-winbase-openeventloga) and [**ReportEvent**](/windows/desktop/api/Winbase/nf-winbase-reporteventa) functions take an optional server name as a parameter so the operations can be performed on the remote server. Use [**OpenEventLog**](/windows/desktop/api/Winbase/nf-winbase-openeventloga) for reading or performing administrative operations (backup, clear, monitor, and query) on the log, and use [**RegisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-registereventsourcea) for writing to the log.

Each call to an event logging function is an atomic operation. When you read from the event log, only whole event records are returned. When you write to the event log, each event record is guaranteed to be written sequentially as a complete record in the log. The following list describes how the event-logging service handles special conditions:

-   The event-logging service receives a read operation and a write operation at the same time: If the read position is at the end of the file, either the read operation fails with an "end-of-file" status (if the write operation has not been completed), or it returns the new record (if the write operation has been completed).
-   The event-logging service completes a clear operation before receiving a read operation: The read operation fails with "end-of-file" status.
-   The event-logging service completes a clear operation before receiving a write operation: The clear operation truncates the log, then the write operation adds the new record at the beginning of the log.

 

 



