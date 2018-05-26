---
Description: The following functions are used with event logging.
ms.assetid: fd5c12ec-3a3d-4b75-a573-0b27ae7a890b
title: Event Logging Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Event Logging Functions

The following functions are used with event logging.



| Function                                                         | Description                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**BackupEventLog**](/windows/win32/Winbase/nf-winbase-backupeventloga?branch=master)                         | Saves the specified event log to a backup file.                                                     |
| [**ClearEventLog**](/windows/win32/Winbase/nf-winbase-cleareventloga?branch=master)                           | Clears the specified event log, and optionally saves the current copy of the log to a backup file.  |
| [**CloseEventLog**](/windows/win32/Winbase/nf-winbase-closeeventlog?branch=master)                           | Closes a read handle to the specified event log.                                                    |
| [**DeregisterEventSource**](/windows/win32/Winbase/nf-winbase-deregistereventsource?branch=master)           | Closes a write handle to the specified event log.                                                   |
| [**GetEventLogInformation**](/windows/win32/Winbase/nf-winbase-geteventloginformation?branch=master)         | Retrieves information about the specified event log.                                                |
| [**GetNumberOfEventLogRecords**](/windows/win32/Winbase/nf-winbase-getnumberofeventlogrecords?branch=master) | Retrieves the number of records in the specified event log.                                         |
| [**GetOldestEventLogRecord**](/windows/win32/Winbase/nf-winbase-getoldesteventlogrecord?branch=master)       | Retrieves the absolute record number of the oldest record in the specified event log.               |
| [**NotifyChangeEventLog**](/windows/win32/Winbase/nf-winbase-notifychangeeventlog?branch=master)             | Enables an application to receive notification when an event is written to the specified event log. |
| [**OpenBackupEventLog**](/windows/win32/Winbase/nf-winbase-openbackupeventloga?branch=master)                 | Opens a handle to a backup event log.                                                               |
| [**OpenEventLog**](/windows/win32/Winbase/nf-winbase-openeventloga?branch=master)                             | Opens a handle to the specified event log.                                                          |
| [**ReadEventLog**](/windows/win32/Winbase/nf-winbase-readeventloga?branch=master)                             | Reads a whole number of entries from the specified event log.                                       |
| [**RegisterEventSource**](/windows/win32/Winbase/nf-winbase-registereventsourcea?branch=master)               | Retrieves a registered handle to the specified event log.                                           |
| [**ReportEvent**](/windows/win32/Winbase/nf-winbase-reporteventa?branch=master)                               | Writes an entry at the end of the specified event log.                                              |



 

 

 



