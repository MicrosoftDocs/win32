---
Description: Controls the luminance and brightness controls of an overlay surface.
ms.assetid: 2f617c89-5505-4d84-be7d-473b216c0571
title: NtGdiDdColorControl function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NtGdiDdColorControl function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Controls the luminance and brightness controls of an overlay surface.

## Syntax


```C++
DWORD APIENTRY NtGdiDdColorControl(
  _In_    HANDLE               hSurface,
  _Inout_ PDD_COLORCONTROLDATA puColorControlData
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to the [**DD\_SURFACE\_LOCAL**](45a41cec-0257-4e26-809d-c2fc4c247328) structure representing the overlay surface.

</dd> <dt>

*puColorControlData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_COLORCONTROLDATA**](7c983faa-de9d-4a04-ac8d-d37fb182a662) structure that contains the color control information for a specified overlay surface.

</dd> </dl>

## Return value

**NtGdiDdColorControl** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> </dl>

 

 




