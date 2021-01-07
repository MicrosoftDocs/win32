---
description: The following notifications are used with file queues. For more information about the format and use of notifications, see Notifications.
ms.assetid: 4a171b4a-8623-4be3-81ee-99081fe23034
title: File Queue Notifications
ms.topic: article
ms.date: 05/31/2018
---

# File Queue Notifications

The following notifications are used with file queues. For more information about the format and use of notifications, see [Notifications](notifications.md).



| Notification                                                      | Description                                                                                         |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**SPFILENOTIFY\_COPYERROR**](spfilenotify-copyerror.md)         | An error occurred during a file copying operation.                                                  |
| [**SPFILENOTIFY\_DELETEERROR**](spfilenotify-deleteerror.md)     | An error occurred during a file deletion operation.                                                 |
| [**SPFILENOTIFY\_ENDCOPY**](spfilenotify-endcopy.md)             | A file copying operation has ended.                                                                 |
| [**SPFILENOTIFY\_ENDDELETE**](spfilenotify-enddelete.md)         | A file deletion operation has ended.                                                                |
| [**SPFILENOTIFY\_ENDQUEUE**](spfilenotify-endqueue.md)           | The queue has finished committing.                                                                  |
| [**SPFILENOTIFY\_ENDRENAME**](spfilenotify-endrename.md)         | A file rename operation has ended.                                                                  |
| [**SPFILENOTIFY\_ENDSUBQUEUE**](spfilenotify-endsubqueue.md)     | A subqueue (either copy, rename or delete) has ended.                                               |
| [**SPFILENOTIFY\_FILEOPDELAYED**](spfilenotify-fileopdelayed.md) | The file was in use, and the current operation has been delayed until the system is rebooted.       |
| [**SPFILENOTIFY\_LANGMISMATCH**](spfilenotify-langmismatch.md)   | The language of the current operation does not match the system language.                           |
| [**SPFILENOTIFY\_NEEDMEDIA**](spfilenotify-needmedia.md)         | New source media is needed.                                                                         |
| [**SPFILENOTIFY\_QUEUESCAN**](spfilenotify-queuescan.md)         | A node in the file queue has been scanned. ( [**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea) only) |
| [**SPFILENOTIFY\_RENAMEERROR**](spfilenotify-renameerror.md)     | An error occurred during a file renaming operation.                                                 |
| [**SPFILENOTIFY\_STARTCOPY**](spfilenotify-startcopy.md)         | A file copy operation has started.                                                                  |
| [**SPFILENOTIFY\_STARTDELETE**](spfilenotify-startdelete.md)     | A file delete operation has started.                                                                |
| [**SPFILENOTIFY\_STARTQUEUE**](spfilenotify-startqueue.md)       | The queue has started to commit.                                                                    |
| [**SPFILENOTIFY\_STARTRENAME**](spfilenotify-startrename.md)     | A file rename operation has started.                                                                |
| [**SPFILENOTIFY\_STARTSUBQUEUE**](spfilenotify-startsubqueue.md) | A subqueue (either copy, rename or delete) has started.                                             |
| [**SPFILENOTIFY\_TARGETEXISTS**](spfilenotify-targetexists.md)   | A copy of the specified file already exists on the target.                                          |
| [**SPFILENOTIFY\_TARGETNEWER**](spfilenotify-targetnewer.md)     | A newer version of the specified file exists on the target.                                         |



 

 

 



