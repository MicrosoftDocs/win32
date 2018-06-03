---
title: IOCTL\_STORAGE\_GET\_PHYSICAL\_ELEMENT\_STATUS control code
description: The IOCTL\_STORAGE\_GET\_PHYSICAL\_ELEMENT\_STATUS control code queries for and returns the physical element status from a device.
ms.assetid: ED46241E-1A71-447A-8D96-E81B4500E070
keywords:
- IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_GET\_PHYSICAL\_ELEMENT\_STATUS control code

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **IOCTL\_STORAGE\_GET\_PHYSICAL\_ELEMENT\_STATUS** control code queries for and returns the physical element status from a device.

## Remarks

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.

``` syntax
BOOL 
   WINAPI 
   DeviceIoControl( (HANDLE)       hDevice,         // handle to device
                    (DWORD)        IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS, // dwIoControlCode
                    (LPDWORD)      lpInBuffer,      // input buffer
                    (DWORD)        nInBufferSize,   // size of input buffer
                    (LPDWORD)      lpOutBuffer,     // output buffer
                    (DWORD)        nOutBufferSize,  // size of output buffer
                    (LPDWORD)      lpBytesReturned, // number of bytes returned
                    (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```

<dl> <dt>

<span id="hDevice__in_"></span><span id="hdevice__in_"></span><span id="HDEVICE__IN_"></span>*hDevice* \[in\]
</dt> <dd>

A handle to the device. To obtain a device handle, call the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

</dd> <dt>

<span id="dwIoControlCode__in_"></span><span id="dwiocontrolcode__in_"></span><span id="DWIOCONTROLCODE__IN_"></span>*dwIoControlCode* \[in\]
</dt> <dd>

The control code for the operation. Use **IOCTL\_STORAGE\_GET\_PHYSICAL\_ELEMENT\_STATUS** for this operation.

</dd> <dt>

<span id="lpInBuffer"></span><span id="lpinbuffer"></span><span id="LPINBUFFER"></span>*lpInBuffer*
</dt> <dd>

A pointer to an input buffer that receives a [**PHYSICAL\_ELEMENT\_STATUS\_REQUEST**](https://www.bing.com/search?q=**PHYSICAL\_ELEMENT\_STATUS\_REQUEST**) structure which defines the starting element to look for the physical element status of a device.

</dd> <dt>

<span id="nInBufferSize__in_"></span><span id="ninbuffersize__in_"></span><span id="NINBUFFERSIZE__IN_"></span>*nInBufferSize* \[in\]
</dt> <dd>

Specifies the size of the input buffer, in bytes.

</dd> <dt>

<span id="lpOutBuffer__out_"></span><span id="lpoutbuffer__out_"></span><span id="LPOUTBUFFER__OUT_"></span>*lpOutBuffer* \[out\]
</dt> <dd>

A pointer to an output buffer that contains a [**PHYSICAL\_ELEMENT\_STATUS**](https://www.bing.com/search?q=**PHYSICAL\_ELEMENT\_STATUS**) structure which defines the physical element status from a device.

</dd> <dt>

<span id="nOutBufferSize__in__"></span><span id="noutbuffersize__in__"></span><span id="NOUTBUFFERSIZE__IN__"></span>*nOutBufferSize* \[in\] 
</dt> <dd>

Specifies the size of the output buffer, in bytes.

</dd> <dt>

<span id="lpBytesReturned__out__"></span><span id="lpbytesreturned__out__"></span><span id="LPBYTESRETURNED__OUT__"></span>*lpBytesReturned* \[out\] 
</dt> <dd>

**LPDWORD**

A pointer to a variable that receives the size of the data stored in the output buffer, in bytes.

If the output buffer is too small, the call fails, [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns **ERROR\_INSUFFICIENT\_BUFFER**, and *lpBytesReturned* is zero.

If *lpOverlapped* is **NULL**, *lpBytesReturned* cannot be **NULL**. Even when an operation returns no output data and *lpOutBuffer* is **NULL**, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) makes use of *lpBytesReturned*. After such an operation, the value of *lpBytesReturned* is meaningless.

If *lpOverlapped* is not **NULL**, *lpBytesReturned* can be **NULL**. If this parameter is not **NULL** and the operation returns data, *lpBytesReturned* is meaningless until the overlapped operation has completed. To retrieve the number of bytes returned, call [**GetOverlappedResult**](https://msdn.microsoft.com/library/windows/desktop/ms683209). If the *hDevice* parameter is associated with an I/O completion port, you can retrieve the number of bytes returned by calling [**GetQueuedCompletionStatus**](https://msdn.microsoft.com/library/windows/desktop/aa364986).

</dd> <dt>

<span id="lpOverlapped__in_"></span><span id="lpoverlapped__in_"></span><span id="LPOVERLAPPED__IN_"></span>*lpOverlapped* \[in\]
</dt> <dd>

**LPOVERLAPPED**

A pointer to an [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure.

If *hDevice* was opened without specifying **FILE\_FLAG\_OVERLAPPED**, *lpOverlapped* is ignored.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, *lpOverlapped* must point to a valid [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

For overlapped operations, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or an error occurs.

</dd> <dt>

<span id="Return_values___"></span><span id="return_values___"></span><span id="RETURN_VALUES___"></span>Return values \[\]
</dt> <dd>

If the operation completes successfully, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include WinIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[**PHYSICAL\_ELEMENT\_STATUS**](https://www.bing.com/search?q=**PHYSICAL\_ELEMENT\_STATUS**)
</dt> <dt>

[**PHYSICAL\_ELEMENT\_STATUS\_REQUEST**](https://www.bing.com/search?q=**PHYSICAL\_ELEMENT\_STATUS\_REQUEST**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






