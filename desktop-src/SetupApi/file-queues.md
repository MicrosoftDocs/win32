---
Description: The setup functions include file queue functionality.
ms.assetid: 9ad42c37-1d6b-4f1b-8173-629e2d3678f2
title: File Queues
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# File Queues

The setup functions include file queue functionality. A file queue is a list of file copying, renaming, and deletion operations. These operations can be sent to the queue in any order. When the queue is committed, these operations are processed as a batch, in order of the operation type.

The following sections explain what a queue is and how to use it when creating a setup application. Also discussed is the order in which the enqueued file operations are processed as the queue commits and what notifications the queue sends to a callback routine at each stage.

-   [About File Queues](about-file-queues.md)
-   [Using File Queues](using-file-queues.md)
-   [File Queue Reference](file-queue-reference.md)

 

 



