---
description: The following functions are used with file queues.
ms.assetid: f05e2abf-983f-4418-bf92-f5ca6502196e
title: File Queue Functions
ms.topic: article
ms.date: 05/31/2018
---

# File Queue Functions

The following functions are used with file queues.



| Function                                                             | Description                                                                                           |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**SetupCloseFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupclosefilequeue)                   | Terminates the queue. Any remaining transactions are not committed.                                   |
| [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea)                 | Commits all queued transactions.                                                                      |
| [**SetupOpenFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenfilequeue)                     | Initializes and returns a handle to the file queue.                                                   |
| [**SetupPromptReboot**](/windows/desktop/api/Setupapi/nf-setupapi-setuppromptreboot)                       | Prompts the user to reboot his or her computer, if necessary.                                         |
| [**SetupQueueCopy**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuecopya)                             | Queues a file copy.                                                                                   |
| [**SetupQueueCopySection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuecopysectiona)               | Queues the files in an INF Copy Files section.                                                        |
| [**SetupQueueDefaultCopy**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuedefaultcopya)               | Queues the files in an INF Copy Files section using the default information specified in an INF file. |
| [**SetupQueueDelete**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuedeletea)                         | Queues a file deletion.                                                                               |
| [**SetupQueueDeleteSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuedeletesectiona)           | Queues the files in an INF Delete Files section.                                                      |
| [**SetupQueueRename**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuerenamea)                         | Queues a file rename.                                                                                 |
| [**SetupQueueRenameSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuerenamesectiona)           | Queues the files in an INF Rename Files section.                                                      |
| [**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea)                     | Scans the file queue.                                                                                 |
| [**SetupSetPlatformPathOverride**](/windows/desktop/api/Setupapi/nf-setupapi-setupsetplatformpathoverridea) | Sets the platform path override.                                                                      |



 

 

 



