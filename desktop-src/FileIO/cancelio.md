---
Description: Cancels all pending input and output (I/O) operations that are issued by the calling thread for the specified file.
ms.assetid: b28162dc-0da8-41c6-9901-29381d2d72c4
title: CancelIo function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CancelIo function

Cancels all pending input and output (I/O) operations that are issued by the calling thread for the specified file. The function does not cancel I/O operations that other threads issue for a file handle.

To cancel I/O operations from another thread, use the [**CancelIoEx**](cancelioex-func.md) function.

## Syntax


```C++
BOOL WINAPI CancelIo(
  _In_ HANDLE hFile
);
```



## Parameters

<dl> <dt>

*hFile* \[in\]
</dt> <dd>

A handle to the file.

The function cancels all pending I/O operations for this file handle.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero. The cancel operation for all pending I/O operations issued by the calling thread for the specified file handle was successfully requested. The thread can use the [**GetOverlappedResult**](https://msdn.microsoft.com/library/windows/desktop/ms683209) function to determine when the I/O operations themselves have been completed.

If the function fails, the return value is zero (0). To get extended error information, call the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

## Remarks

If there are any pending I/O operations in progress for the specified file handle, and they are issued by the calling thread, the **CancelIo** function cancels them. **CancelIo** cancels only outstanding I/O on the handle, it does not change the state of the handle; this means that you cannot rely on the state of the handle because you cannot know whether the operation was completed successfully or canceled.

The I/O operations must be issued as overlapped I/O. If they are not, the I/O operations do not return to allow the thread to call the **CancelIo** function. Calling the **CancelIo** function with a file handle that is not opened with **FILE\_FLAG\_OVERLAPPED** does nothing.

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



|                                     |                                                                                                                                                                                                                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>IoAPI.h (include Windows.h); </dt> <dt>WinBase.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Kernel32.lib</dt> </dl>                                                                                                                                                                                                                  |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>                                                                                                                                                                                                                  |



## See also

<dl> <dt>

[**CancelIoEx**](cancelioex-func.md)
</dt> <dt>

[**CancelSynchronousIo**](cancelsynchronousio-func.md)
</dt> <dt>

[**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master)
</dt> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[File Management Functions](file-management-functions.md)
</dt> <dt>

[**LockFileEx**](/windows/win32/FileAPI/nf-fileapi-lockfileex?branch=master)
</dt> <dt>

[**ReadDirectoryChangesW**](/windows/win32/WinBase/nf-winbase-readdirectorychangesw?branch=master)
</dt> <dt>

[**ReadFile**](/windows/win32/FileAPI/nf-fileapi-readfile?branch=master)
</dt> <dt>

[**ReadFileEx**](/windows/win32/FileAPI/nf-fileapi-readfileex?branch=master)
</dt> <dt>

[Synchronous and Asynchronous I/O](synchronous-and-asynchronous-i-o.md)
</dt> <dt>

[**WriteFile**](/windows/win32/FileAPI/nf-fileapi-writefile?branch=master)
</dt> <dt>

[**WriteFileEx**](/windows/win32/FileAPI/nf-fileapi-writefileex?branch=master)
</dt> </dl>

 

 




