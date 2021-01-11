---
description: Sets various battery information.
ms.assetid: b827983d-5fb8-43f2-b732-541d16b3eb7b
title: IOCTL_BATTERY_SET_INFORMATION control code (Poclass.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- IOCTL_BATTERY_SET_INFORMATION
api_type:
- HeaderDef
api_location:
- Poclass.h
- Batclass.h
---

# IOCTL\_BATTERY\_SET\_INFORMATION control code

Sets various battery information. The input parameter structure, [**BATTERY\_SET\_INFORMATION**](battery-set-information-str.md), indicates which battery status information is to be set.

To perform this operation, call the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.


```C++
BOOL DeviceIoControl(
  (HANDLE) hDevice,              // handle to battery
  IOCTL_BATTERY_SET_INFORMATION, // dwIoControlCode
  (LPVOID) lpInBuffer,           // input buffer
  (DWORD) nInBufferSize,         // size of input buffer
  NULL,                          // lpOutBuffer
  0,                             // nOutBufferSize
  (LPDWORD) lpBytesReturned,     // number of bytes returned
  (LPOVERLAPPED) lpOverlapped    // OVERLAPPED structure
);
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the battery on which the information is to be set. To retrieve a device handle, call the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function.

</dd> <dt>

*dwIoControlCode* 
</dt> <dd>

The control code for the operation. This value identifies the specific operation to be performed and the type of device on which to perform it. Use **IOCTL\_BATTERY\_SET\_INFORMATION** for this operation.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

A pointer to a [**BATTERY\_SET\_INFORMATION**](battery-set-information-str.md) structure.

</dd> <dt>

*nInBufferSize* 
</dt> <dd>

The size of the input buffer, in bytes.

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

Not used with this operation; set to **NULL**.

</dd> <dt>

*nOutBufferSize* 
</dt> <dd>

Not used with this operation; set to zero.

</dd> <dt>

*lpBytesReturned* 
</dt> <dd>

A pointer to a variable that receives the size of data returned in the *lpOutBuffer* buffer, in bytes.

If the output buffer is too small to return any data, then the call fails, [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns the error code ERROR\_INSUFFICIENT\_BUFFER, and the returned byte count is zero.

If *lpOverlapped* is **NULL** (nonoverlapped I/O), *lpBytesReturned* cannot be **NULL**, even if *lpOutBuffer* is **NULL**.

If *lpOverlapped* is not **NULL** (overlapped I/O), *lpBytesReturned* can be **NULL**. If this is an overlapped operation, you can retrieve the number of bytes returned by calling the [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) function. If *hDevice* is associated with an I/O completion port, you can get the number of bytes returned by calling the [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function.

</dd> <dt>

*lpOverlapped* 
</dt> <dd>

A pointer to an [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure.

If *hDevice* was opened with the FILE\_FLAG\_OVERLAPPED flag, *lpOverlapped* must point to a valid [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure. In this case, [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) is performed as an overlapped (asynchronous) operation. If the device was opened with the FILE\_FLAG\_OVERLAPPED flag and *lpOverlapped* is **NULL**, the function fails in unpredictable ways.

If *hDevice* was opened without specifying the FILE\_FLAG\_OVERLAPPED flag, *lpOverlapped* is ignored and the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function does not return until the operation has been completed, or until an error occurs.

</dd> </dl>

## Return value

If the operation completes successfully, [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) returns zero. To get extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

All requests to set battery information will complete with the status of ERROR\_FILE\_NOT\_FOUND if the battery tag of the request does not match that of the current battery tag.

For the implications of overlapped I/O on this operation, see the Remarks section of the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) topic.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>Poclass.h; </dt> <dt>Batclass.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[Battery Information](battery-information.md)
</dt> <dt>

[Power Management Control Codes](power-management-control-codes.md)
</dt> <dt>

[**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol)
</dt> <dt>

[**BATTERY\_SET\_INFORMATION**](battery-set-information-str.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md)
</dt> </dl>

 

