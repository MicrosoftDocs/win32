---
Description: A log can be an abstraction and a physical file.
ms.assetid: 6d0417ec-02df-40ff-8353-80f9a7a026f2
title: Log Storage
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Log Storage

A log can be an abstraction and a physical file. Common Log File System (CLFS) makes a distinction between a log and the physical storage that backs it, which allows physical storage to be managed independently from the log. For example, you can allocate more space to the log without moving or copying it. CLFS is also independent from the file system that provides the storage files, so it can be used over any file system.

> \[!Important\]  
> Log security is only available on a secure file system, such as an NTFS file system.

 

A *container* is a contiguous file that the underlying file system allocates to store a CLFS log. A container holds the client data. For each log, all containers are the same size, which must be a nonzero multiple of 512 KB.

CLFS strings multiple containers together logically to form a single, logical, sequential disk extent that contains a log. Initially, at least two containers must be allocated to each log, but a client can dynamically expand or shrink the size of a log by adding or deleting containers. You can only shrink the log until it holds only one container. Resizing the log involves minimal synchronization and performance overhead.

The following functions can be used to manage log containers.



| Function                                                               | Description                                                                                                                                                                                |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddLogContainer**](/windows/win32/Clfsw32/nf-clfsw32-addlogcontainer?branch=master)                             | Adds a container to the log that is associated with a log handle.                                                                                                                          |
| [**AddLogContainerSet**](/windows/win32/Clfsw32/nf-clfsw32-addlogcontainerset?branch=master)                       | Adds multiple log containers to the physical log stream that is associated with a log handle.                                                                                              |
| [**CreateLogContainerScanContext**](/windows/win32/Clfsw32/nf-clfsw32-createlogcontainerscancontext?branch=master) | Creates a scan context to be used with [**ScanLogContainers**](/windows/win32/Clfsw32/nf-clfsw32-scanlogcontainers?branch=master) to enumerate and scan all log containers that are associated with an underlying physical log stream. |
| [**GetLogContainerName**](/windows/win32/Clfsw32/nf-clfsw32-getlogcontainername?branch=master)                     | Gets the full path name of a container.                                                                                                                                                    |
| [**RemoveLogContainer**](/windows/win32/Clfsw32/nf-clfsw32-removelogcontainer?branch=master)                       | Removes a container from the log that is associated with a log handle.                                                                                                                     |
| [**RemoveLogContainerSet**](/windows/win32/Clfsw32/nf-clfsw32-removelogcontainerset?branch=master)                 | Removes multiple containers from a physical log that is associated with a physical log stream handle.                                                                                      |
| [**ScanLogContainers**](/windows/win32/Clfsw32/nf-clfsw32-scanlogcontainers?branch=master)                         | Reads the log metadata to get the descriptors for the log containers that make up a physical log.                                                                                          |



 

 

 



