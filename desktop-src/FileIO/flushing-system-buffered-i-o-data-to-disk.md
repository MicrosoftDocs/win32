---
description: Windows stores the data in file read and write operations in system-maintained data buffers to optimize disk performance.
ms.assetid: e8c12a1d-f6a4-4850-814d-6f0a712f8f9a
title: Flushing System-Buffered I/O Data to Disk
ms.topic: article
ms.date: 05/31/2018
---

# Flushing System-Buffered I/O Data to Disk

Windows stores the data in file read and write operations in system-maintained data buffers to optimize disk performance. When an application writes to a file, the system usually buffers the data and writes the data to the disk on a regular basis. An application can force the operating system to write the contents of these data buffers to the disk by using the [**FlushFileBuffers**](/windows/desktop/api/FileAPI/nf-fileapi-flushfilebuffers) function. Alternatively, an application can specify that write operations are to bypass the data buffer and write directly to the disk by setting the **FILE\_FLAG\_NO\_BUFFERING** flag when the file is created or opened using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function.

If there is data in the internal buffer when the file is closed, the operating system does not automatically write the contents of the buffer to the disk before closing the file. If the application does not force the operating system to write the buffer to disk before closing the file, the caching algorithm determines when the buffer is written.

> [!Note]  
> Accessing a data buffer while a read or write operation is using it may corrupt the buffer. Applications must not read from, write to, reallocate, or free the data buffer that a read or write operation is using until the operation completes.

 

 

 



