---
Description: After you have obtained a handle to a file queue by calling the SetupOpenFileQueue function, you can add file operations to the queue, either file-by-file, or by queuing all the files in an INF section.
ms.assetid: ba2f40cd-b0df-4768-8080-4fd80c50f2c2
title: Queuing Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Queuing Files

After you have obtained a handle to a file queue by calling the [**SetupOpenFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupopenfilequeue?branch=master) function, you can add file operations to the queue, either file-by-file, or by queuing all the files in an INF section.

To add a copy operation for an individual file to the file queue, call the [**SetupQueueCopy**](/windows/win32/Setupapi/nf-setupapi-setupqueuecopya?branch=master) function. If you want to queue a file copy operation using the default source media and target destinations specified in an INF file, you can call the [**SetupQueueDefaultCopy**](/windows/win32/Setupapi/nf-setupapi-setupqueuedefaultcopya?branch=master) function.

You can add an individual file delete or rename operation to the open file queue, by calling the [**SetupQueueDelete**](/windows/win32/Setupapi/nf-setupapi-setupqueuedeletea?branch=master) or [**SetupQueueRename**](/windows/win32/Setupapi/nf-setupapi-setupqueuerenamea?branch=master) function.

 

 



