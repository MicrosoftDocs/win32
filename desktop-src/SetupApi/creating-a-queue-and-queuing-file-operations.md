---
description: Queuing the file operations is useful because it enables you to process the installation as a whole, instead of by INF section.
ms.assetid: 6519c2fb-142d-4071-865f-c00a98c2fe35
title: Creating a Queue and Queuing File Operations
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Queue and Queuing File Operations

Queuing the file operations is useful because it enables you to process the installation as a whole, instead of by INF section.

To create a file queue, declare a variable to store the queue handle, then call the [**SetupOpenFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenfilequeue) function. After the queue is created, you can queue copy, rename, and delete operations, as well as scan the file queue to verify enqueued operations.

To add single file operations to the queue, use the [**SetupQueueCopy**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuecopya), [**SetupQueueRename**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuerenamea), and [**SetupQueueDelete**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuedeletea) functions.

All the file operations listed in a **Copy Files**, **Delete Files**, or **Rename Files** section can be added to the queue by using [**SetupQueueCopySection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuecopysectiona), [**SetupQueueDeleteSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuedeletesectiona), or [**SetupQueueRenameSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuerenamesectiona), respectively.

Another way to queue all the files in the **Copy Files** sections listed in an **Install** section of an INF is to use the function, [**SetupInstallFilesFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfilesfrominfsectiona).

The following example uses the [**SetupQueueCopySection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuecopysectiona) function to enqueue copy operations for all the files listed in a **Copy Files** section of an INF file.

``` syntax
test = SetupQueueCopySection(
     MyQueue,                  \\Handle to the open queue
     "A:\",                    \\Source root path
     MyInf,                    \\Inf containing the source info
     NULL,                     \\specifies that MyInf contains 
                               \\  the section to copy as well
     MySection,                \\the name of the section to queue
  
                               \\flags specifying the copy style
     SP_COPY_NOSKIP | SP_COPY_NOBROWSE,
);
```

In the example, MyQueue is the queue to add copy operations to, "A:\\" specifies the path to the source, and MyInf is the handle to the open INF file. The parameter *ListInfHandle* is set to **NULL**, indicating that the section for copying is in MyInf. MySection is the section in MyInf containing the files to queue for copying.

The flags SP\_COPY\_NOSKIP and SP\_COPY\_NOBROWSE have been combined using an OR operator to indicate that the user should not be offered options to skip or browse for files if errors occur.

 

 



