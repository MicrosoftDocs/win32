---
Description: Creates a Microsoft Direct3D surface from a Microsoft DirectDraw surface and associates a requested handle value to it.
ms.assetid: 7b1ce714-a56e-4508-8160-af8c1748c5f7
title: NtGdiDdCreateSurfaceEx function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NtGdiDdCreateSurfaceEx function

\[This function is subject to change with each operating system revision. Instead, use the DirectDraw and Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Creates a Microsoft Direct3D surface from a Microsoft DirectDraw surface and associates a requested handle value to it.

## Syntax


```C++
DWORD APIENTRY NtGdiDdCreateSurfaceEx(
  _In_ HANDLE hDirectDraw,
  _In_ HANDLE hSurface,
  _In_ DWORD  dwSurfaceHandle
);
```



## Parameters

<dl> <dt>

*hDirectDraw* \[in\]
</dt> <dd>

Handle to the DirectDraw object created by the application.

</dd> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to the DirectDraw surface to be created for Direct3D. These handles are unique within each different [**DD\_DIRECTDRAW\_LOCAL**](https://msdn.microsoft.com/windows/desktop/58e378b7-863a-46d4-91cb-904ed4e892a3) structure.

</dd> <dt>

*dwSurfaceHandle* \[in\]
</dt> <dd>

Handle to a [**DD\_CREATESURFACEEXDATA**](https://msdn.microsoft.com/windows/desktop/61965d6b-7473-4121-8c85-fb677a665388) structure that contains the information required for the driver to create the surface.

</dd> </dl>

## Return value

**NtGdiDdCreateSurfaceEx** returns one of the following callback codes.



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

 

 




