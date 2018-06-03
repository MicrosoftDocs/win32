---
Description: The IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING control code disables local client-side in-memory caching of data when reading data from or writing data to a remote file. This is an internally-defined control code not available in a public header.
ms.assetid: a464671b-253c-4f35-84a2-2619cb15b009
title: IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING control code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING control code

The **IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING** control code disables local client-side in-memory caching of data when reading data from or writing data to a remote file. This is an internally-defined control code not available in a public header.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/windows/desktop/1d35c087-6672-4fc6-baa1-a886dd9d3878) function with the following parameters.


```C++
BOOL DeviceIoControl(
  (HANDLE) hDevice,             // handle to device
  IOCTL_LMR_DISABLE_LOCAL_BUFFERING, // dwIoControlCode
  (LPVOID) NULL,                // lpInBuffer
  (DWORD) 0,                    // nInBufferSize
  (LPVOID) NULL,                // lpOutBuffer
  (DWORD) 0,                    // nOutBufferSize
  (LPDWORD) lpBytesReturned,    // number of bytes returned
  (LPOVERLAPPED) lpOverlapped   // OVERLAPPED structure
);
```



## Parameters

<dl> <dt>

*hDevice* \[in\]
</dt> <dd>

A handle to the remote file. To obtain this handle, call the [**CreateFile**](https://www.bing.com/search?q=**CreateFile**) function.

</dd> <dt>

*dwIoControlCode* \[in\]
</dt> <dd>

The control code for the operation. Use the value 0x140390 for this operation.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

Not used, must be **NULL**.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

The size of the input buffer, in bytes. Must be zero.

</dd> <dt>

*lpOutBuffer* \[out\]
</dt> <dd>

Not used, must be **NULL**.

</dd> <dt>

*nOutBufferSize* \[in\]
</dt> <dd>

The size of the output buffer, in bytes. Must be zero.

</dd> <dt>

*lpBytesReturned* \[out\]
</dt> <dd>

A pointer to a variable that receives the size of the data stored in the output buffer, in bytes.

If the output buffer is too small, then the call fails, the [**GetLastError**](https://msdn.microsoft.com/windows/desktop/d852e148-985c-416f-a5a7-27b6914b45d4) function returns **ERROR\_INSUFFICIENT\_BUFFER**, and *lpBytesReturned* is zero.

If the *lpOverlapped* parameter is **NULL**, *lpBytesReturned* cannot be **NULL**. Even when an operation returns no output data and the *lpOutBuffer* parameter is **NULL**, [**DeviceIoControl**](https://msdn.microsoft.com/windows/desktop/1d35c087-6672-4fc6-baa1-a886dd9d3878) makes use of *lpBytesReturned*. After such an operation, the value of *lpBytesReturned* is meaningless.

If *lpOverlapped* is not **NULL**, *lpBytesReturned* can be **NULL**. If *lpOverlapped* is not **NULL** and the operation returns data, *lpBytesReturned* is meaningless until the overlapped operation has completed. To retrieve the number of bytes returned, call the [**GetOverlappedResult**](https://msdn.microsoft.com/windows/desktop/7f999959-9b22-4491-ae2b-a2674d821110) function. If the *hDevice* parameter is associated with an I/O completion port, you can retrieve the number of bytes returned by calling the [**GetQueuedCompletionStatus**](https://www.bing.com/search?q=**GetQueuedCompletionStatus**) function.

</dd> <dt>

*lpOverlapped* \[in\]
</dt> <dd>

A pointer to an [**OVERLAPPED**](https://msdn.microsoft.com/windows/desktop/5037f6b9-e316-483b-a8e2-b58d2587ebd9) structure.

If the *hDevice* parameter was opened without specifying **FILE\_FLAG\_OVERLAPPED**, *lpOverlapped* is ignored.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, *lpOverlapped* must point to a valid [**OVERLAPPED**](https://msdn.microsoft.com/windows/desktop/5037f6b9-e316-483b-a8e2-b58d2587ebd9) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

For overlapped operations, [**DeviceIoControl**](https://msdn.microsoft.com/windows/desktop/1d35c087-6672-4fc6-baa1-a886dd9d3878) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or until an error occurs.

</dd> </dl>

## Return value

If the operation completes successfully, [**DeviceIoControl**](https://msdn.microsoft.com/windows/desktop/1d35c087-6672-4fc6-baa1-a886dd9d3878) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](https://msdn.microsoft.com/windows/desktop/1d35c087-6672-4fc6-baa1-a886dd9d3878) returns zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/windows/desktop/d852e148-985c-416f-a5a7-27b6914b45d4).

## Remarks

The **IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING** control code is defined internally by the system as 0x140390 and not in a public header file. It is used by special-purpose applications to disable local client-side in-memory caching of data when reading data from or writing data to a remote file. After local buffering is disabled, the setting remains in effect until all open handles to the file are closed and the redirector cleans up its internal data structures.

General-purpose applications should not use **IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING**, because it can result in excessive network traffic and associated loss of performance. The **IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING** control code should be used only in specialized applications moving large amounts of data over the network while attempting to maximize use of network bandwidth. For example, the [**CopyFile**](https://msdn.microsoft.com/windows/desktop/2c8ad002-cef4-499c-acda-c162205f6a8d) and [**CopyFileEx**](https://msdn.microsoft.com/windows/desktop/e19f0299-54fa-4e1e-855a-d2c71d29611b) functions use **IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING** to improve large file copy performance.

**IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING** is not implemented by local file systems and will fail with the error **ERROR\_INVALID\_FUNCTION**. Issuing the **IOCTL\_LMR\_DISABLE\_LOCAL\_BUFFERING** control code on remote directory handles will fail with the error **ERROR\_NOT\_SUPPORTED**.

## See also

<dl> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/windows/desktop/1d35c087-6672-4fc6-baa1-a886dd9d3878)
</dt> </dl>

 

 



