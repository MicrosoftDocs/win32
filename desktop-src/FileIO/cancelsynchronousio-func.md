---
description: Marks pending synchronous I/O operations that are issued by the specified thread as canceled.
ms.assetid: f362c8b2-2193-443e-bb69-78f8b4147117
title: CancelSynchronousIo function (IoAPI.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CancelSynchronousIo
api_type: 
- DllExport
api_location: 
- Kernel32.dll
- API-MS-Win-Core-io-l1-1-1.dll
- KernelBase.dll
- MinKernelBase.dll
- api-ms-win-downlevel-kernel32-l1-1-0.dll
---

# CancelSynchronousIo function

Marks pending synchronous I/O operations that are issued by the specified thread as canceled.

## Syntax


```C++
BOOL WINAPI CancelSynchronousIo(
  _In_ HANDLE hThread
);
```



## Parameters

<dl> <dt>

*hThread* \[in\]
</dt> <dd>

A handle to the thread.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is 0 (zero). To get extended error information, call the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function.

If this function cannot find a request to cancel, the return value is 0 (zero), and [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **ERROR\_NOT\_FOUND**.

## Remarks

The caller must have the [THREAD\_TERMINATE](/windows/desktop/ProcThread/thread-security-and-access-rights) access right.

If there are any pending I/O operations in progress for the specified thread, the **CancelSynchronousIo** function marks them for cancellation. Most types of operations can be canceled immediately; other operations can continue toward completion before they are actually canceled and the caller is notified. The **CancelSynchronousIo** function does not wait for all canceled operations to complete. For more information, see [I/O Completion/Cancellation Guidelines](https://www.microsoft.com/whdc/driver/kernel/iocancel.mspx).

The operation being canceled is completed with one of three statuses; you must check the completion status to determine the completion state. The three statuses are:

-   **The operation completed normally.** This can occur even if the operation was canceled, because the cancel request might not have been submitted in time to cancel the operation.
-   **The operation was canceled.** The [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns **ERROR\_OPERATION\_ABORTED**.
-   **The operation failed with another error.** The [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns the relevant error code.

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
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                                                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                                                                                    |
| Header<br/>                   | <dl> <dt>IoAPI.h (include Windows.h); </dt> <dt>WinBase.h on Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Kernel32.lib</dt> </dl>                                                                                                                                                                                 |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>                                                                                                                                                                                 |



## See also

<dl> <dt>

[**CancelIo**](cancelio.md)
</dt> <dt>

[**CancelIoEx**](cancelioex-func.md)
</dt> <dt>

[File Management Functions](file-management-functions.md)
</dt> <dt>

[Synchronous and Asynchronous I/O](synchronous-and-asynchronous-i-o.md)
</dt> </dl>

 

