---
description: 'When the SetupCommitFileQueue function commits the file queue, it processes the file operations in the following order: file deletion operations, then file renaming operations, and finally, file copying operations.'
ms.assetid: 23aae815-ff1a-435d-b14d-3c62a3355a1b
title: Order of Queue Commitment
ms.topic: article
ms.date: 05/31/2018
---

# Order of Queue Commitment

When the [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) function commits the file queue, it processes the file operations in the following order: file deletion operations, then file renaming operations, and finally, file copying operations. The following outline illustrates the life cycle of a queue's commitment process.

 

-   start the delete subqueue
    -   start a file delete operation <-- repeat for each
    -   finish a file delete operation <-- queued file delete
-   finish the delete subqueue

<!-- -->

-   start the rename subqueue
    -   start a file rename operation <-- repeat for each
    -   finish a file delete operation <-- queued file rename
-   finish the rename subqueue

<!-- -->

-   start the copy subque
    -   start a file copy operation <-- repeat for each
    -   finish a file copy operation <-- queued file copy
    -   finish the copy subqueue
-   finish the queue

 

At each step, or if an error occurs, the [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) function sends a notification to the callback routine. The callback routine can use the information sent by the queue to track the installation progress and, if necessary, interact with the user.

For example, if a file copy operation needed a source file that was not available at the current path, [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) would send a SPFILENOTIFY\_NEEDMEDIA notification to the callback routine, along with information about the file and media required. The callback routine could use this information to generate a dialog box that prompts the user to insert the next disk by calling [**SetupPromptForDisk**](/windows/desktop/api/Setupapi/nf-setupapi-setuppromptfordiska)

A default queue callback routine, [**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka), is included with the Setup API. This routine handles queue notifications and generates error dialog boxes and progress bars for the installation. You can use the default queue callback routine as it is, or write a filter callback routine to handle a subset of the notifications and pass the others on to the default queue callback routine.

If none of the functionality of the callback routine suits your needs, you can write a self-contained custom callback routine that does not call the default queue callback routine.

For more information about queue callback routines, see [Default Queue Callback Routine](default-queue-callback-routine.md), and [Creating a Custom Queue Callback Routine](creating-a-custom-queue-callback-routine.md).

 

 



