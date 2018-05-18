---
Description: 'After you have obtained a handle to a file queue by calling the SetupOpenFileQueue function, you can add file operations to the queue, either file-by-file, or by queuing all the files in an INF section.'
ms.assetid: 'ba2f40cd-b0df-4768-8080-4fd80c50f2c2'
title: Queuing Files
---

# Queuing Files

After you have obtained a handle to a file queue by calling the [**SetupOpenFileQueue**](setupopenfilequeue.md) function, you can add file operations to the queue, either file-by-file, or by queuing all the files in an INF section.

To add a copy operation for an individual file to the file queue, call the [**SetupQueueCopy**](setupqueuecopy.md) function. If you want to queue a file copy operation using the default source media and target destinations specified in an INF file, you can call the [**SetupQueueDefaultCopy**](setupqueuedefaultcopy.md) function.

You can add an individual file delete or rename operation to the open file queue, by calling the [**SetupQueueDelete**](setupqueuedelete.md) or [**SetupQueueRename**](setupqueuerename.md) function.

 

 



