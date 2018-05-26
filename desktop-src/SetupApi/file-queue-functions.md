---
Description: The following functions are used with file queues.
ms.assetid: f05e2abf-983f-4418-bf92-f5ca6502196e
title: File Queue Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# File Queue Functions

The following functions are used with file queues.



| Function                                                             | Description                                                                                           |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**SetupCloseFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupclosefilequeue?branch=master)                   | Terminates the queue. Any remaining transactions are not committed.                                   |
| [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master)                 | Commits all queued transactions.                                                                      |
| [**SetupOpenFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupopenfilequeue?branch=master)                     | Initializes and returns a handle to the file queue.                                                   |
| [**SetupPromptReboot**](/windows/win32/Setupapi/nf-setupapi-setuppromptreboot?branch=master)                       | Prompts the user to reboot his or her computer, if necessary.                                         |
| [**SetupQueueCopy**](/windows/win32/Setupapi/nf-setupapi-setupqueuecopya?branch=master)                             | Queues a file copy.                                                                                   |
| [**SetupQueueCopySection**](/windows/win32/Setupapi/nf-setupapi-setupqueuecopysectiona?branch=master)               | Queues the files in an INF Copy Files section.                                                        |
| [**SetupQueueDefaultCopy**](/windows/win32/Setupapi/nf-setupapi-setupqueuedefaultcopya?branch=master)               | Queues the files in an INF Copy Files section using the default information specified in an INF file. |
| [**SetupQueueDelete**](/windows/win32/Setupapi/nf-setupapi-setupqueuedeletea?branch=master)                         | Queues a file deletion.                                                                               |
| [**SetupQueueDeleteSection**](/windows/win32/Setupapi/nf-setupapi-setupqueuedeletesectiona?branch=master)           | Queues the files in an INF Delete Files section.                                                      |
| [**SetupQueueRename**](/windows/win32/Setupapi/nf-setupapi-setupqueuerenamea?branch=master)                         | Queues a file rename.                                                                                 |
| [**SetupQueueRenameSection**](/windows/win32/Setupapi/nf-setupapi-setupqueuerenamesectiona?branch=master)           | Queues the files in an INF Rename Files section.                                                      |
| [**SetupScanFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupscanfilequeuea?branch=master)                     | Scans the file queue.                                                                                 |
| [**SetupSetPlatformPathOverride**](/windows/win32/Setupapi/nf-setupapi-setupsetplatformpathoverridea?branch=master) | Sets the platform path override.                                                                      |



 

 

 



