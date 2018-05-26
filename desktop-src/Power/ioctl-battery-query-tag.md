---
Description: Retrieves the batterys current tag.
ms.assetid: 0bbe59ba-e037-47ce-a54a-6500ea7c9bc5
title: IOCTL\_BATTERY\_QUERY\_TAG control code
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_BATTERY\_QUERY\_TAG control code

Retrieves the battery's current tag.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.


```C++
BOOL DeviceIoControl(
  (HANDLE) hDevice,            // handle to battery
  IOCTL_BATTERY_QUERY_TAG,     // dwIoControlCode
  (LPVOID) lpInBuffer,         // input buffer
  (DWORD) nInBufferSize,       // size of input buffer
  (LPVOID) lpOutBuffer,        // output buffer
  (DWORD) nOutBufferSize,      // size of output buffer
  (LPDWORD) lpBytesReturned,   // number of bytes returned
  (LPOVERLAPPED) lpOverlapped);// OVERLAPPED structure
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the battery from which the tag is to be retrieved. To retrieve a device handle, call the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

</dd> <dt>

*dwIoControlCode* 
</dt> <dd>

The control code for the operation. This value identifies the specific operation to be performed and the type of device on which to perform it. Use **IOCTL\_BATTERY\_QUERY\_TAG** for this operation.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

A pointer to a **ULONG** input buffer. The value indicates the number of milliseconds to wait if there is no battery. A value of -1 indicates the request will wait indefinitely (or until canceled by some other event).

</dd> <dt>

*nInBufferSize* 
</dt> <dd>

The size of the input buffer, in bytes.

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

A pointer to a **ULONG** output buffer. On success this buffer contains the current battery tag, which can be any value except BATTERY\_TAG\_INVALID. On failure, if [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns the error code **ERROR\_FILE\_NOT\_FOUND**, this buffer contains the value **BATTERY\_TAG\_INVALID**.

</dd> <dt>

*nOutBufferSize* 
</dt> <dd>

The size of the output buffer, in bytes.

</dd> <dt>

*lpBytesReturned* 
</dt> <dd>

A pointer to a variable that receives the size of the data stored in the *lpOutBuffer* buffer, in bytes.

If the output buffer is too small to return any data then the call fails, [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns the error code **ERROR\_INSUFFICIENT\_BUFFER**, and the returned byte count is zero.

If *lpOverlapped* is **NULL** (nonoverlapped I/O), *lpBytesReturned* cannot be **NULL**.

If *lpOverlapped* is not **NULL** (overlapped I/O), *lpBytesReturned* can be **NULL**. If this is an overlapped operation, you can retrieve the number of bytes returned by calling the [**GetOverlappedResult**](https://msdn.microsoft.com/library/windows/desktop/ms683209) function. If *hDevice* is associated with an I/O completion port, you can get the number of bytes returned by calling the [**GetQueuedCompletionStatus**](https://msdn.microsoft.com/library/windows/desktop/aa364986) function.

</dd> <dt>

*lpOverlapped* 
</dt> <dd>

A pointer to an [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, *lpOverlapped* must point to a valid [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure. In this case, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) is performed as an overlapped (asynchronous) operation. If the device was opened with the **FILE\_FLAG\_OVERLAPPED** flag and *lpOverlapped* is **NULL**, the function fails in unpredictable ways.

If *hDevice* was opened without specifying the **FILE\_FLAG\_OVERLAPPED** flag, *lpOverlapped* is ignored and the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function does not return until the operation has been completed, or until an error occurs.

</dd> </dl>

## Return value

If the operation completes successfully, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

This battery IOCTL retrieves the battery's current tag. The battery tag is a unique nonzero value that changes when the physical battery is reinserted, replaced, or undergoes any characteristic changes. See the Battery Tags section in the [Battery Information](battery-information.md) overview topic for more detail on when a battery tag changes, how to detect the change, and how an application should proceed after a battery tag change. When a battery is not present, this request will wait the indicated time, and if there is still no battery present, then it will return **ERROR\_FILE\_NOT\_FOUND** and set the battery tag to **BATTERY\_TAG\_INVALID**. (See Battery Information for more information.)

All requests for other battery information require the caller to supply the matching battery tag. This ensures that the caller is receiving information for the same battery for every request and ensures that the caller is aware of battery changes without constant polling.

For the implications of overlapped I/O on this operation, see the Remarks section of the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) topic.

## Examples

For an example, see [Enumerating Battery Devices](enumerating-battery-devices.md).

## Requirements



|                                     |                                                                                                                                                                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>Poclass.h; </dt> <dt>BatClass.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[Battery Information](battery-information.md)
</dt> <dt>

[Power Management Control Codes](power-management-control-codes.md)
</dt> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md)
</dt> <dt>

[**IOCTL\_BATTERY\_SET\_INFORMATION**](ioctl-battery-set-information.md)
</dt> </dl>

 

 




