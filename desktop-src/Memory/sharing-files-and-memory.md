---
Description: 'File mapping can be used to share a file or memory between two or more processes. To share a file or memory, all of the processes must use the name or the handle of the same file mapping object.'
ms.assetid: '942cb50d-df07-444f-bba5-58194556ae66'
title: Sharing Files and Memory
---

# Sharing Files and Memory

File mapping can be used to share a file or memory between two or more processes. To share a file or memory, all of the processes must use the name or the handle of the same file mapping object.

To share a file, the first process creates or opens a file by using the [**CreateFile**](fs.createfile) function. Next, it creates a file mapping object by using the [**CreateFileMapping**](createfilemapping.md) function, specifying the file handle and a name for the file mapping object. The names of event, semaphore, mutex, waitable timer, job, and file mapping objects share the same namespace. Therefore, the **CreateFileMapping** and [**OpenFileMapping**](openfilemapping.md) functions fail if they specify a name that is in use by an object of another type.

To share memory that is not associated with a file, a process must use the [**CreateFileMapping**](createfilemapping.md) function and specify INVALID\_HANDLE\_VALUE as the *hFile* parameter instead of an existing file handle. The corresponding file mapping object accesses memory backed by the system paging file. You must specify a size greater than zero when you specify an *hFile* of INVALID\_HANDLE\_VALUE in a call to **CreateFileMapping**.

The easiest way for other processes to obtain a handle of the file mapping object created by the first process is to use the [**OpenFileMapping**](openfilemapping.md) function and specify the object's name. This is referred to as *named shared memory*. If the file mapping object does not have a name, the process must obtain a handle to it through inheritance or duplication. For more information on inheritance and duplication, see [Inheritance](base.inheritance).

Processes that share files or memory must create file views by using the [**MapViewOfFile**](mapviewoffile.md) or [**MapViewOfFileEx**](mapviewoffileex.md) function. They must coordinate their access using semaphores, mutexes, events, or some other mutual exclusion technique. For more information, see [Synchronization](base.synchronization).

A shared file mapping object will not be destroyed until all processes that use it close their handles to it by using the [**CloseHandle**](base.closehandle) function.

For information about file mapping object security, see [File Mapping Security and Access Rights](file-mapping-security-and-access-rights.md).

## Related topics

<dl> <dt>

[Creating Named Shared Memory](creating-named-shared-memory.md)
</dt> </dl>

 

 



