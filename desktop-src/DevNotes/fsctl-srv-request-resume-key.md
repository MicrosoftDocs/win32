---
description: The FSCTL\_SRV\_REQUEST\_RESUME\_KEY control code is used to retrieve an opaque file reference for use with the IOCTL\_COPYCHUNK control code.
ms.assetid: a6e0d253-5beb-4de8-8c40-d004f5794d47
title: FSCTL_SRV_REQUEST_RESUME_KEY control code
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FSCTL_SRV_REQUEST_RESUME_KEY
api_type: 
- NA
api_location: 
---

# FSCTL\_SRV\_REQUEST\_RESUME\_KEY control code

The **FSCTL\_SRV\_REQUEST\_RESUME\_KEY** control code is used to retrieve an opaque file reference for use with the [**IOCTL\_COPYCHUNK**](ioctl-copychunk.md) control code.

To perform this operation, call the [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.


```C++
BOOL DeviceIoControl(
  (HANDLE) hDevice,             // handle to device
  FSCTL_SRV_REQUEST_RESUME_KEY, // dwIoControlCode
  NULL,                         // lpInBuffer
  0,                            // nInBufferSize
  (LPVOID) lpOutBuffer,         // output buffer
  (DWORD) nOutBufferSize,       // size of output buffer
  (LPDWORD) lpBytesReturned,    // number of bytes returned
  (LPOVERLAPPED) lpOverlapped   // OVERLAPPED structure
);
```



## Parameters

<dl> <dt>

*hDevice* \[in\]
</dt> <dd>

A handle to the file for which the source file key is to be requested. To obtain this handle, call the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function.

</dd> <dt>

*dwIoControlCode* \[in\]
</dt> <dd>

The control code for the operation. Use **FSCTL\_SRV\_REQUEST\_RESUME\_KEY** for this operation.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

Not used with this operation; set to **NULL**.

</dd> <dt>

*nInBufferSize* \[in\]
</dt> <dd>

Not used with this operation; set to zero.

</dd> <dt>

*lpOutBuffer* \[out\]
</dt> <dd>

A pointer to the output buffer, a **SRV\_REQUEST\_RESUME\_KEY** structure. For more information, see the Remarks section.

</dd> <dt>

*nOutBufferSize* \[in\]
</dt> <dd>

The size of the output buffer, in bytes.

</dd> <dt>

*lpBytesReturned* \[out\]
</dt> <dd>

A pointer to a variable that receives the size of the data stored in the output buffer, in bytes.

If the output buffer is too small, the call fails, the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns **ERROR\_INSUFFICIENT\_BUFFER**, and *lpBytesReturned* is zero.

If the *lpOverlapped* parameter is **NULL**, *lpBytesReturned* cannot be **NULL**. Even when an operation returns no output data and the *lpOutBuffer* parameter is **NULL**, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) makes use of *lpBytesReturned*. After such an operation, the value of *lpBytesReturned* is meaningless.

If *lpOverlapped* is not **NULL**, *lpBytesReturned* can be **NULL**. If *lpOverlapped* is not **NULL** and the operation returns data, *lpBytesReturned* is meaningless until the overlapped operation has completed. To retrieve the number of bytes returned, call the [**GetOverlappedResult**](/windows/win32/api/ioapiset/nf-ioapiset-getoverlappedresult) function. If the *hDevice* parameter is associated with an I/O completion port, you can retrieve the number of bytes returned by calling the [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function.

</dd> <dt>

*lpOverlapped* \[in\]
</dt> <dd>

A pointer to an [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure.

If the *hDevice* parameter was opened without specifying **FILE\_FLAG\_OVERLAPPED**, *lpOverlapped* is ignored.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, *lpOverlapped* must point to a valid [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

For overlapped operations, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or until an error occurs.

</dd> </dl>

## Return value

If the operation completes successfully, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

This control code has no associated header file. You must define the control code and data structures as follows.

``` syntax
#define FSCTL_SRV_REQUEST_RESUME_KEY CTL_CODE(FILE_DEVICE_NETWORK_FILE_SYSTEM, 30, METHOD_BUFFERED, FILE_ANY_ACCESS)

typedef struct _SRV_RESUME_KEY {
    UINT64 ResumeKey;
    UINT64 Timestamp;
    UINT64 Pid;
} SRV_RESUME_KEY, *PSRV_RESUME_KEY;

typedef struct _SRV_REQUEST_RESUME_KEY {
    SRV_RESUME_KEY Key;
    ULONG  ContextLength;
    BYTE   Context[1];
} SRV_REQUEST_RESUME_KEY, *PSRV_REQUEST_RESUME_KEY;
```

These members can be described as follows.



| Member                                                                                                                       | Description                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ResumeKey"></span><span id="resumekey"></span><span id="RESUMEKEY"></span>**ResumeKey**<br/>                 | An opaque value that identifies the source file to the server.<br/>                                                                                                   |
| <span id="Timestamp"></span><span id="timestamp"></span><span id="TIMESTAMP"></span>**Timestamp**<br/>                 | An opaque value that identifies the time when the file was opened.<br/>                                                                                               |
| <span id="Pid"></span><span id="pid"></span><span id="PID"></span>**Pid**<br/>                                         | An opaque value that identifies the process that opened the file.<br/>                                                                                                |
| <span id="Key"></span><span id="key"></span><span id="KEY"></span>**Key**<br/>                                         | A **SRV\_RESUME\_KEY** structure. To perform a server-side copy operation, use this structure with the [**IOCTL\_COPYCHUNK**](ioctl-copychunk.md) control code.<br/> |
| <span id="ContextLength"></span><span id="contextlength"></span><span id="CONTEXTLENGTH"></span>**ContextLength**<br/> | This member is reserved for system use; do not use.<br/>                                                                                                              |
| <span id="Context"></span><span id="context"></span><span id="CONTEXT"></span>**Context**<br/>                         | This member is reserved for system use; do not use.<br/>                                                                                                              |



 

## See also

<dl> <dt>

[**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)
</dt> <dt>

[**IOCTL\_COPYCHUNK**](ioctl-copychunk.md)
</dt> </dl>

 

 
