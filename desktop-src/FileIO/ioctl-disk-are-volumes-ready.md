---
Description: 'Waits for all volumes on the specified disk to be ready for use.'
ms.assetid: '6cf619bb-7ff5-485e-b533-0f7f6503c6e0'
title: 'IOCTL\_DISK\_ARE\_VOLUMES\_READY control code'
---

# IOCTL\_DISK\_ARE\_VOLUMES\_READY control code

Waits for all volumes on the specified disk to be ready for use.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.


```C++
BOOL 
WINAPI 
DeviceIoControl( (HANDLE)       hDevice,         // handle to device 
                 IOCTL_DISK_ARE_VOLUMES_READY,   // dwIoControlCode
                 (LPVOID)       NULL,            // lpInBuffer 
                 (DWORD)        0,               // nInBufferSize 
                 (LPVOID)       NULL,            // lpOutBuffer 
                 (DWORD)        0,               // nOutBufferSize
                 (LPDWORD)      lpBytesReturned, // number of bytes returned
                 (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the disk.

To retrieve a device handle, call the [**CreateFile**](createfile.md) function.

</dd> <dt>

*dwIoControlCode* 
</dt> <dd>

The control code for the operation.

Use **IOCTL\_DISK\_ARE\_VOLUMES\_READY** for this operation.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

Not used with this operation. Set to **NULL**.

</dd> <dt>

*nInBufferSize* 
</dt> <dd>

The size of the input buffer, in bytes. Set to 0 (zero).

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

Not used with this operation. Set to **NULL**.

</dd> <dt>

*nOutBufferSize* 
</dt> <dd>

Not used with this operation. Set to 0 (zero).

</dd> <dt>

*lpBytesReturned* 
</dt> <dd>

Not used with this operation. Set to **NULL**.

</dd> <dt>

*lpOverlapped* 
</dt> <dd>

A pointer to an [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure.

If *hDevice* was opened without specifying **FILE\_FLAG\_OVERLAPPED**, *lpOverlapped* is ignored.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, *lpOverlapped* must point to a valid [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

For overlapped operations, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or an error occurs.

</dd> </dl>

## Return value

If the operation completes successfully, indicating that all volumes on the disk are ready for use, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntdddisk.h</dt> </dl> |



## See also

<dl> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[Disk Management Control Codes](disk-management-control-codes.md)
</dt> </dl>

 

 




