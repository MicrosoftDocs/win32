---
description: Retrieves the attributes of the specified disk device.
ms.assetid: 2FF81F67-9E70-43C6-A504-0D60382E0945
title: IOCTL_DISK_GET_CLUSTER_INFO control code (Ntdddisk.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- IOCTL_DISK_GET_CLUSTER_INFO
api_type:
- HeaderDef
api_location:
- Ntdddisk.h
---

# IOCTL\_DISK\_GET\_CLUSTER\_INFO control code

Retrieves the attributes of the specified disk device.

To perform this operation, call the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.


```C++
BOOL 
WINAPI 
DeviceIoControl( (HANDLE)       hDevice,         // handle to device 
                 IOCTL_DISK_GET_CLUSTER_INFO,    // dwIoControlCode
                 (LPVOID)       NULL,            // lpInBuffer 
                 (DWORD)        0,               // nInBufferSize 
                 (LPVOID)       lpOutBuffer,     // output buffer:GET_DISK_ATTRIBUTES
                 (DWORD)        nOutBufferSize,  // size of output buffer
                 (LPDWORD)      lpBytesReturned, // number of bytes returned
                 (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the disk.

To retrieve a device handle, call the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function.

</dd> <dt>

*dwIoControlCode* 
</dt> <dd>

The control code for the operation.

Use **IOCTL\_DISK\_GET\_CLUSTER\_INFO** for this operation.

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

A pointer to a buffer that receives a [**DISK\_CLUSTER\_INFO**](disk-cluster-info.md) data structure.

</dd> <dt>

*nOutBufferSize* 
</dt> <dd>

The size of the output buffer, in bytes.

</dd> <dt>

*lpBytesReturned* 
</dt> <dd>

Not used with this operation. Set to **NULL**.

</dd> <dt>

*lpOverlapped* 
</dt> <dd>

A pointer to an [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure.

If *hDevice* was opened without specifying **FILE\_FLAG\_OVERLAPPED**, *lpOverlapped* is ignored.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, *lpOverlapped* must point to a valid [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

For overlapped operations, [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or an error occurs.

</dd> </dl>

## Return value

If the operation completes successfully, indicating that all volumes on the disk are ready for use, [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) returns zero. To get extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntdddisk.h</dt> </dl> |



## See also

<dl> <dt>

[**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol)
</dt> <dt>

[Disk Management Control Codes](disk-management-control-codes.md)
</dt> <dt>

[**DISK\_CLUSTER\_INFO**](disk-cluster-info.md)
</dt> <dt>

[**IOCTL\_DISK\_SET\_CLUSTER\_INFO**](ioctl-disk-set-cluster-info.md)
</dt> </dl>

 

