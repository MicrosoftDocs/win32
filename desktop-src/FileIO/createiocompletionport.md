---
description: Creates an input/output (I/O) completion port and associates it with a specified file handle, or creates an I/O completion port that is not yet associated with a file handle, allowing association at a later time.
ms.assetid: 40cb47fc-7b15-47f6-bee2-2611d4686053
title: CreateIoCompletionPort function (IoAPI.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateIoCompletionPort
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-io-l1-1-0.dll
- KernelBase.dll
- MinKernelBase.dll
- API-MS-Win-Core-io-l1-1-1.dll
- api-ms-win-downlevel-kernel32-l1-1-0.dll
---

# CreateIoCompletionPort function

Creates an input/output (I/O) completion port and associates it with a specified file handle, or creates an I/O completion port that is not yet associated with a file handle, allowing association at a later time.

Associating an instance of an opened file handle with an I/O completion port allows a process to receive notification of the completion of asynchronous I/O operations involving that file handle.

> [!Note]
>
> The term *file handle* as used here refers to a system abstraction that represents an overlapped I/O endpoint, not only a file on disk. Any system objects that support overlapped I/O such as network endpoints, TCP sockets, named pipes, and mail slots can be used as file handles. For additional information, see the Remarks section.

 

## Syntax


```C++
HANDLE WINAPI CreateIoCompletionPort(
  _In_     HANDLE    FileHandle,
  _In_opt_ HANDLE    ExistingCompletionPort,
  _In_     ULONG_PTR CompletionKey,
  _In_     DWORD     NumberOfConcurrentThreads
);
```



## Parameters

<dl> <dt>

*FileHandle* \[in\]
</dt> <dd>

An open file handle or **INVALID\_HANDLE\_VALUE**.

The handle must be to an object that supports overlapped I/O.

If a handle is provided, it has to have been opened for overlapped I/O completion. For example, you must specify the **FILE\_FLAG\_OVERLAPPED** flag when using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function to obtain the handle.

If **INVALID\_HANDLE\_VALUE** is specified, the function creates an I/O completion port without associating it with a file handle. In this case, the *ExistingCompletionPort* parameter must be **NULL** and the *CompletionKey* parameter is ignored.

</dd> <dt>

*ExistingCompletionPort* \[in, optional\]
</dt> <dd>

A handle to an existing I/O completion port or **NULL**.

If this parameter specifies an existing I/O completion port, the function associates it with the handle specified by the *FileHandle* parameter. The function returns the handle of the existing I/O completion port if successful; it does not create a new I/O completion port.

If this parameter is **NULL**, the function creates a new I/O completion port and, if the *FileHandle* parameter is valid, associates it with the new I/O completion port. Otherwise no file handle association occurs. The function returns the handle to the new I/O completion port if successful.

</dd> <dt>

*CompletionKey* \[in\]
</dt> <dd>

The per-handle user-defined completion key that is included in every I/O completion packet for the specified file handle. For more information, see the Remarks section.

</dd> <dt>

*NumberOfConcurrentThreads* \[in\]
</dt> <dd>

The maximum number of threads that the operating system can allow to concurrently process I/O completion packets for the I/O completion port. This parameter is ignored if the *ExistingCompletionPort* parameter is not **NULL**.

If this parameter is zero, the system allows as many concurrently running threads as there are processors in the system.

</dd> </dl>

## Return value

If the function succeeds, the return value is the handle to an I/O completion port:

-   If the *ExistingCompletionPort* parameter was **NULL**, the return value is a new handle.

-   If the *ExistingCompletionPort* parameter was a valid I/O completion port handle, the return value is that same handle.

-   If the *FileHandle* parameter was a valid handle, that file handle is now associated with the returned I/O completion port.

If the function fails, the return value is **NULL**. To get extended error information, call the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function.

## Remarks

The I/O system can be instructed to send I/O completion notification packets to I/O completion ports, where they are queued. The **CreateIoCompletionPort** function provides this functionality.

An I/O completion port and its handle are associated with the process that created it and is not sharable between processes. However, a single handle is sharable between threads in the same process.

**CreateIoCompletionPort** can be used in three distinct modes:

-   Create only an I/O completion port without associating it with a file handle.
-   Associate an existing I/O completion port with a file handle.
-   Perform both creation and association in a single call.

To create an I/O completion port without associating it, set the *FileHandle* parameter to **INVALID\_HANDLE\_VALUE**, the *ExistingCompletionPort* parameter to **NULL**, and the *CompletionKey* parameter to zero (which is ignored in this case). Set the *NumberOfConcurrentThreads* parameter to the desired concurrency value for the new I/O completion port, or zero for the default (the number of processors in the system).

The handle passed in the *FileHandle* parameter can be any handle that supports overlapped I/O. Most commonly, this is a handle opened by the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function using the **FILE\_FLAG\_OVERLAPPED** flag (for example, files, mail slots, and pipes). Objects created by other functions such as [**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket) can also be associated with an I/O completion port. For an example using sockets, see [**AcceptEx**](/windows/desktop/api/mswsock/nf-mswsock-acceptex). A handle can be associated with only one I/O completion port, and after the association is made, the handle remains associated with that I/O completion port until it is closed.

For more information on I/O completion port theory, usage, and associated functions, see [I/O Completion Ports](i-o-completion-ports.md).

Multiple file handles can be associated with a single I/O completion port by calling **CreateIoCompletionPort** multiple times with the same I/O completion port handle in the *ExistingCompletionPort* parameter and a different file handle in the *FileHandle* parameter each time.

Use the *CompletionKey* parameter to help your application track which I/O operations have completed. This value is not used by **CreateIoCompletionPort** for functional control; rather, it is attached to the file handle specified in the *FileHandle* parameter at the time of association with an I/O completion port. This completion key should be unique for each file handle, and it accompanies the file handle throughout the internal completion queuing process. It is returned in the [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function call when a completion packet arrives. The *CompletionKey* parameter is also used by the [**PostQueuedCompletionStatus**](postqueuedcompletionstatus.md) function to queue your own special-purpose completion packets.

After an instance of an open handle is associated with an I/O completion port, it cannot be used in the [**ReadFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-readfileex) or [**WriteFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-writefileex) function because these functions have their own asynchronous I/O mechanisms.

It is best not to share a file handle associated with an I/O completion port by using either handle inheritance or a call to the [**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle) function. Operations performed with such duplicate handles generate completion notifications. Careful consideration is advised.

The I/O completion port handle and every file handle associated with that particular I/O completion port are known as *references to the I/O completion port*. The I/O completion port is released when there are no more references to it. Therefore, all of these handles must be properly closed to release the I/O completion port and its associated system resources. After these conditions are satisfied, close the I/O completion port handle by calling the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function.

In Windows 8 and Windows Server 2012, this function is supported by the following technologies.



| Technology                                           | Supported      |
|------------------------------------------------------|----------------|
| Server Message Block (SMB) 3.0 protocol<br/>   | Yes<br/> |
| SMB 3.0 Transparent Failover (TFO)<br/>        | Yes<br/> |
| SMB 3.0 with Scale-out File Shares (SO)<br/>   | Yes<br/> |
| Cluster Shared Volume File System (CsvFS)<br/> | Yes<br/> |
| Resilient File System (ReFS)<br/>              | Yes<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>IoAPI.h (include Windows.h); </dt> <dt>WinBase.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Kernel32.lib</dt> </dl>                                                                                                                                                                                                                  |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>                                                                                                                                                                                                                  |



## See also

<dl> <dt>

**Overview Topics**
</dt> <dt>

[File Management Functions](file-management-functions.md)
</dt> <dt>

[I/O Completion Ports](i-o-completion-ports.md)
</dt> <dt>

[Using the Windows Headers](/windows/desktop/WinProg/using-the-windows-headers)
</dt> <dt>

[Windows Sockets 2](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

**Functions**
</dt> <dt>

[**AcceptEx**](/windows/desktop/api/mswsock/nf-mswsock-acceptex)
</dt> <dt>

[**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea)
</dt> <dt>

[**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle)
</dt> <dt>

[**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus)
</dt> <dt>

[**GetQueuedCompletionStatusEx**](getqueuedcompletionstatusex-func.md)
</dt> <dt>

[**PostQueuedCompletionStatus**](postqueuedcompletionstatus.md)
</dt> <dt>

[**ReadFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-readfileex)
</dt> <dt>

[**WriteFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-writefileex)
</dt> </dl>

 

