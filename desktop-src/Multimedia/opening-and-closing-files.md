---
title: Opening and Closing Files
description: Opening and Closing Files
ms.assetid: 72655d33-f685-4205-a982-f7cd20c59f22
keywords:
- AVIFileOpen function
- AVIFileRelease function
ms.topic: article
ms.date: 05/31/2018
---

# Opening and Closing Files

An application must open an AVI file before reading or writing. To open an AVI file, use the [**AVIFileOpen**](/windows/desktop/api/Vfw/nf-vfw-avifileopen) function. **AVIFileOpen** returns the address of an AVI file interface that contains the handle of the open file and increments the reference count of the file.

The **AVIFileOpen** function supports the OF flags used with the [OpenFile](/windows/win32/api/winbase/nf-winbase-openfile) function. If an application writes to an existing file, it must include the OF\_WRITE flag in **AVIFileOpen**. Similarly, if your application creates and writes to a new file, you must include the OF\_CREATE and OF\_WRITE flags in **AVIFileOpen**.

When you open a file using **AVIFileOpen**, you can use a default file handler or you can specify a custom file handler to read and write to the file and its data streams. In either case, AVIFile searches the registry for the correct file handler to use. You must ensure custom file handlers are in the registry before an application can access them.

You can increment the reference count of a file by using the [**AVIFileAddRef**](/windows/desktop/api/Vfw/nf-vfw-avifileaddref) function. For example, you might want to do this when passing a handle of the file interface to another application, or when you want to keep a file open while using a function that would normally close the file.

You can close a file by using the [**AVIFileRelease**](/windows/desktop/api/Vfw/nf-vfw-avifilerelease) function. The **AVIFileRelease** function decrements the reference count of an AVI file, saves changes made to the file, and when the reference count reaches zero, closes the file. Your applications should balance the reference count by including a call to **AVIFileRelease** for each use of [**AVIFileOpen**](/windows/desktop/api/Vfw/nf-vfw-avifileopen) and **AVIFileAddRef**.

> [!NOTE]
> An application can open a file with one or more program threads. However, for the best possible performance, only one thread should access the file at any one time.
