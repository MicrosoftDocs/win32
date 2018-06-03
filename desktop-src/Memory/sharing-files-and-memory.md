---
Description: File mapping can be used to share a file or memory between two or more processes. To share a file or memory, all of the processes must use the name or the handle of the same file mapping object.
ms.assetid: 942cb50d-df07-444f-bba5-58194556ae66
title: Sharing Files and Memory
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sharing Files and Memory

File mapping can be used to share a file or memory between two or more processes. To share a file or memory, all of the processes must use the name or the handle of the same file mapping object.

To share a file, the first process creates or opens a file by using the [**CreateFile**](https://msdn.microsoft.com/windows/desktop/80a96083-4de9-4422-9705-b8ad2b6cbd1b) function. Next, it creates a file mapping object by using the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function, specifying the file handle and a name for the file mapping object. The names of event, semaphore, mutex, waitable timer, job, and file mapping objects share the same namespace. Therefore, the **CreateFileMapping** and [**OpenFileMapping**](/windows/desktop/api/WinBase/nf-winbase-openfilemappinga) functions fail if they specify a name that is in use by an object of another type.

To share memory that is not associated with a file, a process must use the [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) function and specify INVALID\_HANDLE\_VALUE as the *hFile* parameter instead of an existing file handle. The corresponding file mapping object accesses memory backed by the system paging file. You must specify a size greater than zero when you specify an *hFile* of INVALID\_HANDLE\_VALUE in a call to **CreateFileMapping**.

The easiest way for other processes to obtain a handle of the file mapping object created by the first process is to use the [**OpenFileMapping**](/windows/desktop/api/WinBase/nf-winbase-openfilemappinga) function and specify the object's name. This is referred to as *named shared memory*. If the file mapping object does not have a name, the process must obtain a handle to it through inheritance or duplication. For more information on inheritance and duplication, see [Inheritance](https://msdn.microsoft.com/windows/desktop/c530e723-2d40-4022-a259-dfc650604e44).

Processes that share files or memory must create file views by using the [**MapViewOfFile**](https://www.bing.com/search?q=**MapViewOfFile**) or [**MapViewOfFileEx**](https://www.bing.com/search?q=**MapViewOfFileEx**) function. They must coordinate their access using semaphores, mutexes, events, or some other mutual exclusion technique. For more information, see [Synchronization](https://msdn.microsoft.com/windows/desktop/3e85e61c-d4df-49dd-aa86-1bbd682e375e).

A shared file mapping object will not be destroyed until all processes that use it close their handles to it by using the [**CloseHandle**](https://msdn.microsoft.com/windows/desktop/9b84891d-62ca-4ddc-97b7-c4c79482abd9) function.

For information about file mapping object security, see [File Mapping Security and Access Rights](file-mapping-security-and-access-rights.md).

## Related topics

<dl> <dt>

[Creating Named Shared Memory](creating-named-shared-memory.md)
</dt> </dl>

 

 



