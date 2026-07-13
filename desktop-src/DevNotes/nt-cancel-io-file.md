---
description: User-mode API - cancels all pending input and output (I/O) operations that are issued by the calling thread for the specified file.
title: NtCancelIoFile function
ms.topic: reference
ms.date: 09/08/2022
---

# NtCancelIoFile function

Cancels all pending input and output (I/O) operations that are issued by the calling thread for the specified file. The function does not cancel I/O operations that other threads issue for a file handle.

To cancel I/O operations from another thread, use the [**NtCancelIoFileEx**](nt-cancel-io-file-ex.md) function.

> [!NOTE]
> This function is the user-mode equivalent to the [**CancelIo**](/windows/win32/fileio/cancelio) Win32 function.

## Syntax


```C++
BOOL WINAPI NtCancelIoFile(
  _In_ HANDLE hFile
);
```

## Parameters

#### *hFile* \[in\]

A handle to the file.

The function cancels all pending I/O operations for this file handle.

## Returns

If the function succeeds, the return value is nonzero. The cancel operation for all pending I/O operations issued by the calling thread for the specified file handle was successfully requested. The thread can use the [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) function to determine when the I/O operations themselves have been completed.

If the function fails, the return value is zero (0). To get extended error information, call the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function.

## Remarks

If there are any pending I/O operations in progress for the specified file handle, and they are issued by the calling thread, the **NtCancelIoFile** function cancels them. **NtCancelIoFile** cancels only outstanding I/O on the handle, it does not change the state of the handle; this means that you cannot rely on the state of the handle because you cannot know whether the operation was completed successfully or canceled.

The I/O operations must be issued as overlapped I/O. If they are not, the I/O operations do not return to allow the thread to call the **NtCancelIoFile** function. Calling the **NtCancelIoFile** function with a file handle that is not opened with **FILE\_FLAG\_OVERLAPPED** does nothing.

All I/O operations that are canceled complete with the error **ERROR\_OPERATION\_ABORTED**, and all completion notifications for the I/O operations occur normally.

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
|-----------------|-------------------------------------------------|
| Header<br/>                   | <dl> <dt>ntioapi.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>ntdll.lib</dt> </dl> |


## See also

<dl> <dt>

[**CancelIoEx**](nt-cancel-io-file-ex.md)
</dt> <dt>

 

