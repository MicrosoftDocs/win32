---
Description: Retrieves the supported backlight levels.
ms.assetid: b4c1ee3f-af75-477e-b7ed-53be905374d7
title: IOCTL\_VIDEO\_QUERY\_SUPPORTED\_BRIGHTNESS control code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IOCTL_VIDEO_QUERY_SUPPORTED_BRIGHTNESS
api_type: 
- HeaderDef
api_location: 
- Ntddvdeo.h
---

# IOCTL\_VIDEO\_QUERY\_SUPPORTED\_BRIGHTNESS control code

Retrieves the supported backlight levels.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.


```C++
BOOL DeviceIoControl(
  (HANDLE) hDevice,                // handle to device
  IOCTL_VIDEO_QUERY_SUPPORTED_BRIGHTNESS,  // dwIoControlCode
  NULL,                            // lpInBuffer
  0,                               // nInBufferSize
  (LPVOID) lpOutBuffer,            // output buffer
  (DWORD) nOutBufferSize,          // size of output buffer
  (LPDWORD) lpBytesReturned,       // number of bytes returned
  (LPOVERLAPPED) lpOverlapped      // OVERLAPPED structure
);
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the \\\\.\\LCD device. To retrieve a device handle, call the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

</dd> <dt>

*dwIoControlCode* 
</dt> <dd>

The control code for the operation. This value identifies the specific operation to be performed and the type of device on which to perform it. Use **IOCTL\_VIDEO\_QUERY\_SUPPORTED\_BRIGHTNESS** for this operation.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

Not used with this operation; set to **NULL**.

</dd> <dt>

*nInBufferSize* 
</dt> <dd>

Not used with this operation; set to zero.

</dd> <dt>

*lpOutBuffer* 
</dt> <dd>

A pointer to a buffer that receives an array of the available power levels. This buffer should be 256 bytes long.

</dd> <dt>

*nOutBufferSize* 
</dt> <dd>

The size of the output buffer, in bytes.

</dd> <dt>

*lpBytesReturned* 
</dt> <dd>

A pointer to a variable that receives the size, in bytes, of output data returned.

If the output buffer is too small to return any data, then the call fails, [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns the error code ERROR\_INSUFFICIENT\_BUFFER, and the returned byte count is zero.

If the output buffer is too small to hold all of the data but can hold some entries, then the operating system returns as much as fits, the call fails, [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns the error code ERROR\_MORE\_DATA, and *lpBytesReturned* indicates the amount of data returned. Your application should call [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) again with the same operation, specifying a new starting point.

If *lpOverlapped* is **NULL** (nonoverlapped I/O), *lpBytesReturned* cannot be **NULL**.

If *lpOverlapped* is not **NULL** (overlapped I/O), *lpBytesReturned* can be **NULL**. If this is an overlapped operation, you can retrieve the number of bytes returned by calling the [**GetOverlappedResult**](https://msdn.microsoft.com/library/windows/desktop/ms683209) function. If *hDevice* is associated with an I/O completion port, you can get the number of bytes returned by calling the [**GetQueuedCompletionStatus**](https://msdn.microsoft.com/library/windows/desktop/aa364986) function.

</dd> <dt>

*lpOverlapped* 
</dt> <dd>

A pointer to an [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure.

If *hDevice* was opened with the FILE\_FLAG\_OVERLAPPED flag, *lpOverlapped* must point to a valid [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure. In this case, the operation is performed as an overlapped (asynchronous) operation. If the device was opened with the FILE\_FLAG\_OVERLAPPED flag and *lpOverlapped* is **NULL**, the function fails in unpredictable ways.

If *hDevice* was opened without specifying the FILE\_FLAG\_OVERLAPPED flag, *lpOverlapped* is ignored and [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) does not return until the operation has been completed, or until an error occurs.

</dd> </dl>

## Return value

If the operation completes successfully, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

## Remarks

Each element in the *lpOutBuffer* array is one byte in length. Therefore, upon return, the *lpBytesReturned* parameter indicates the number of supported levels. Each level is a value from 0 to 100. The larger the value, the brighter the backlight. All levels are supported whether the power source is AC or DC.

The header file used to build applications that include this functionality, Ntddvdeo.h, is included in the Microsoft Windows Driver Development Kit (DDK). For information on obtaining the DDK, see [http://www.microsoft.com/whdc/devtools/ddk/default.mspx](Http://go.microsoft.com/fwlink/p/?linkid=84136).

Alternatively, you can define this control code as follows:

``` syntax
#define IOCTL_VIDEO_QUERY_SUPPORTED_BRIGHTNESS \
  CTL_CODE(FILE_DEVICE_VIDEO, 0x125, METHOD_BUFFERED, FILE_ANY_ACCESS)
```

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP1 \[desktop apps only\]<br/>                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Ntddvdeo.h</dt> </dl> |



## See also

<dl> <dt>

[Backlight Control Interface](backlight-control-interface.md)
</dt> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> </dl>

 

 




