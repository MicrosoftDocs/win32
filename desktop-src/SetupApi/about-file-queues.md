---
description: A file queue is a list of file operations that are processed at one time. The file operations in the queue may be copy, rename, or delete operations. The file queue organizes file operations by type, creating copy, rename, and delete subqueues.
ms.assetid: 9ad42c37-1d6b-4f1b-8173-629e2d3678f2
title: About File Queues
ms.topic: article
ms.date: 05/31/2018
---

# About File Queues

A file queue is a list of file operations that are processed at one time. The file operations in the queue may be copy, rename, or delete operations. The file queue organizes file operations by type, creating copy, rename, and delete subqueues.

These operations may be sent to the queue in any order, and the enqueuing process need not be contiguous. When the queue is committed, the [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) function performs file operations in order of the operation type.

Typically, all of the file operations necessary for an entire installation are queued to the file queue, and then processed in a single batch when the queue is committed.

One advantage of queuing file operations over installing files section-by-section from an INF file is that you can streamline the installation process. Instead of having to obtain information from the user for each section to be installed, you can obtain installation information from the user for all the files to be installed while building the queue. This frees the user to pursue other activities while the time-intensive copy operations are processed by the [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) function.

Another advantage of file queues is that you can track the progress of the installation as a whole. When installing section-by-section from an INF file, progress indicators such as progress bars can track only the current INF section. When the next section is installed, the progress bar starts over. With a queue, the total number of files to be processed during the entire installation is known before the queue is committed, and thus, a progress bar can be generated to track the entire installation.

For more information, see the following topics:

-   [Order of Queue Commitment](order-of-queue-commitment.md)
-   [Queue Notifications](queue-notifications.md)

 

 



