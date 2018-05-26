---
Description: Retrieves multiple completion port entries simultaneously.
ms.assetid: 3996c02c-562c-4697-a091-e241ad54b239
title: GetQueuedCompletionStatusEx function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetQueuedCompletionStatusEx function

Retrieves multiple completion port entries simultaneously. It waits for pending I/O operations that are associated with the specified completion port to complete.

To dequeue I/O completion packets one at a time, use the [**GetQueuedCompletionStatus**](/windows/win32/WinBase/?branch=master) function.

## Syntax


```C++
BOOL WINAPI GetQueuedCompletionStatusEx(
  _In_  HANDLE             CompletionPort,
  _Out_ LPOVERLAPPED_ENTRY lpCompletionPortEntries,
  _In_  ULONG              ulCount,
  _Out_ PULONG             ulNumEntriesRemoved,
  _In_  DWORD              dwMilliseconds,
  _In_  BOOL               fAlertable
);
```



## Parameters

<dl> <dt>

*CompletionPort* \[in\]
</dt> <dd>

A handle to the completion port. To create a completion port, use the [**CreateIoCompletionPort**](createiocompletionport.md) function.

</dd> <dt>

*lpCompletionPortEntries* \[out\]
</dt> <dd>

On input, points to a pre-allocated array of [**OVERLAPPED\_ENTRY**](/windows/win32/MinWinBase/ns-minwinbase-_overlapped_entry?branch=master) structures.

On output, receives an array of [**OVERLAPPED\_ENTRY**](/windows/win32/MinWinBase/ns-minwinbase-_overlapped_entry?branch=master) structures that hold the entries. The number of array elements is provided by *ulNumEntriesRemoved*.

The number of bytes transferred during each I/O, the completion key that indicates on which file each I/O occurred, and the overlapped structure address used in each original I/O are all returned in the *lpCompletionPortEntries* array.

</dd> <dt>

*ulCount* \[in\]
</dt> <dd>

The maximum number of entries to remove.

</dd> <dt>

*ulNumEntriesRemoved* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of entries actually removed.

</dd> <dt>

*dwMilliseconds* \[in\]
</dt> <dd>

The number of milliseconds that the caller is willing to wait for a completion packet to appear at the completion port. If a completion packet does not appear within the specified time, the function times out and returns **FALSE**.

If *dwMilliseconds* is **INFINITE** (0xFFFFFFFF), the function will never time out. If *dwMilliseconds* is zero and there is no I/O operation to dequeue, the function will time out immediately.

</dd> <dt>

*fAlertable* \[in\]
</dt> <dd>

If this parameter is **FALSE**, the function does not return until the time-out period has elapsed or an entry is retrieved.

If the parameter is **TRUE** and there are no available entries, the function performs an alertable wait. The thread returns when the system queues an I/O completion routine or APC to the thread and the thread executes the function.

A completion routine is queued when the [**ReadFileEx**](/windows/win32/FileAPI/nf-fileapi-readfileex?branch=master) or [**WriteFileEx**](/windows/win32/FileAPI/nf-fileapi-writefileex?branch=master) function in which it was specified has completed, and the calling thread is the thread that initiated the operation. An APC is queued when you call [**QueueUserAPC**](https://msdn.microsoft.com/library/windows/desktop/ms684954).

</dd> </dl>

## Return value

Returns nonzero (**TRUE**) if successful or zero (**FALSE**) otherwise.

To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

This function associates a thread with the specified completion port. A thread can be associated with at most one completion port.

This function returns **TRUE** when at least one pending I/O is completed, but it is possible that one or more I/O operations failed. Note that it is up to the user of this function to check the list of returned entries in the *lpCompletionPortEntries* parameter to determine which of them correspond to any possible failed I/O operations by looking at the status contained in the **lpOverlapped** member in each [**OVERLAPPED\_ENTRY**](/windows/win32/MinWinBase/ns-minwinbase-_overlapped_entry?branch=master).

This function returns **FALSE** when no I/O operation was dequeued. This typically means that an error occurred while processing the parameters to this call, or that the *CompletionPort* handle was closed or is otherwise invalid. The [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function provides extended error information.

If a call to [**GetQueuedCompletionStatusEx**](/windows/win32/WinBase/?branch=master) fails because the handle associated with it is closed, the function returns **FALSE** and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) will return **ERROR\_ABANDONED\_WAIT\_0**.

Server applications may have several threads calling the **GetQueuedCompletionStatusEx** function for the same completion port. As I/O operations complete, they are queued to this port in first-in-first-out order. If a thread is actively waiting on this call, one or more queued requests complete the call for that thread only.

For more information on I/O completion port theory, usage, and associated functions, see [I/O Completion Ports](i-o-completion-ports.md).

In Windows 8 and Windows Server 2012, this function is supported by the following technologies.



| Technology                                           | Supported      |
|------------------------------------------------------|----------------|
| Server Message Block (SMB) 3.0 protocol<br/>   | Yes<br/> |
| SMB 3.0 Transparent Failover (TFO)<br/>        | Yes<br/> |
| SMB 3.0 with Scale-out File Shares (SO)<br/>   | Yes<br/> |
| Cluster Shared Volume File System (CsvFS)<br/> | Yes<br/> |
| Resilient File System (ReFS)<br/>              | Yes<br/> |



 

## Requirements



|                                     |                                                                                                                                                                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                             |
| Header<br/>                   | <dl> <dt>IoAPI.h (include Windows.h); </dt> <dt>WinBase.h on Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Kernel32.lib</dt> </dl>                                                                                                                                                                                 |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>                                                                                                                                                                                 |



## See also

<dl> <dt>

**Overview Topics**
</dt> <dt>

[File Management Functions](file-management-functions.md)
</dt> <dt>

[I/O Completion Ports](i-o-completion-ports.md)
</dt> <dt>

[Using the Windows Headers](https://msdn.microsoft.com/library/windows/desktop/aa383745)
</dt> <dt>

**Functions**
</dt> <dt>

[**ConnectNamedPipe**](https://msdn.microsoft.com/library/windows/desktop/aa365146)
</dt> <dt>

[**CreateIoCompletionPort**](createiocompletionport.md)
</dt> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[**GetQueuedCompletionStatusEx**](getqueuedcompletionstatusex-func.md)
</dt> <dt>

[**LockFileEx**](/windows/win32/FileAPI/nf-fileapi-lockfileex?branch=master)
</dt> <dt>

[**ReadFile**](/windows/win32/FileAPI/nf-fileapi-readfile?branch=master)
</dt> <dt>

[**PostQueuedCompletionStatus**](postqueuedcompletionstatus.md)
</dt> <dt>

[**TransactNamedPipe**](https://msdn.microsoft.com/library/windows/desktop/aa365790)
</dt> <dt>

[**WaitCommEvent**](https://msdn.microsoft.com/library/windows/desktop/aa363479)
</dt> <dt>

[**WriteFile**](/windows/win32/FileAPI/nf-fileapi-writefile?branch=master)
</dt> </dl>

 

 




