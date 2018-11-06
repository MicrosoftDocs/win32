---
Description: Sets the current AC and DC backlight levels.
ms.assetid: baa77811-046d-4a07-b3df-2a31fba2d9a7
title: IOCTL_VIDEO_SET_DISPLAY_BRIGHTNESS control code
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IOCTL_VIDEO_SET_DISPLAY_BRIGHTNESS
api_type: 
- HeaderDef
api_location: 
- Ntddvdeo.h
---

# IOCTL\_VIDEO\_SET\_DISPLAY\_BRIGHTNESS control code

Sets the current AC and DC backlight levels.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.


```C++
BOOL DeviceIoControl(
  (HANDLE) hDevice,            // handle to device
  IOCTL_VIDEO_SET_DISPLAY_BRIGHTNESS, // dwIoControlCode
  (LPVOID) lpInBuffer,         // input buffer
  (DWORD) nInBufferSize,       // size of the input buffer
  NULL,                        // lpOutBuffer
  0,                           // nOutBufferSize 
  (LPDWORD) lpBytesReturned,   // number of bytes returned
  (LPOVERLAPPED) lpOverlapped  // OVERLAPPED structure
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

The control code for the operation. This value identifies the specific operation to be performed and the type of device on which to perform it. Use **IOCTL\_VIDEO\_SET\_DISPLAY\_BRIGHTNESS** for this operation.

</dd> <dt>

*lpInBuffer* 
</dt> <dd>

A pointer to a [**DISPLAY\_BRIGHTNESS**](https://msdn.microsoft.com/en-us/library/Aa372686(v=VS.85).aspx) structure.

</dd> <dt>

*nInBufferSize* 
</dt> <dd>

The size of the buffer pointed to by *lpOutBuffer*, in bytes.

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

A pointer to a variable that receives the actual count of bytes returned by the function in the output buffer.

If *lpOverlapped* is **NULL** (nonoverlapped I/O), *lpBytesReturned* is used internally and cannot be **NULL**.

If *lpOverlapped* is not **NULL** (overlapped I/O), *lpBytesReturned* can be **NULL**.

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

The values specified in the **ucACBrightness** and **ucDCBrightness** members of the [**DISPLAY\_BRIGHTNESS**](https://msdn.microsoft.com/en-us/library/Aa372686(v=VS.85).aspx) structure must have been previously returned by [**IOCTL\_VIDEO\_QUERY\_SUPPORTED\_BRIGHTNESS**](ioctl-video-query-supported-brightness.md). For example, if the supported values are 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100, then using a value of 33 would be an error.

The header file used to build applications that include this functionality, Ntddvdeo.h, is included in the Microsoft Windows Driver Development Kit (DDK). For information on obtaining the DDK, see [http://www.microsoft.com/whdc/devtools/ddk/default.mspx](Http://go.microsoft.com/fwlink/p/?linkid=84136).

Alternatively, you can define this control code as follows:

``` syntax
#define IOCTL_VIDEO_SET_DISPLAY_BRIGHTNESS \
  CTL_CODE(FILE_DEVICE_VIDEO, 0x127, METHOD_BUFFERED, FILE_ANY_ACCESS)
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
</dt> <dt>

[**DISPLAY\_BRIGHTNESS**](https://msdn.microsoft.com/en-us/library/Aa372686(v=VS.85).aspx)
</dt> <dt>

[**IOCTL\_VIDEO\_QUERY\_DISPLAY\_BRIGHTNESS**](ioctl-video-query-display-brightness.md)
</dt> <dt>

[**IOCTL\_VIDEO\_QUERY\_SUPPORTED\_BRIGHTNESS**](ioctl-video-query-supported-brightness.md)
</dt> </dl>

 

 




