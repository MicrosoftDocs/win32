---
description: Removes an attachment, created with NtGdiDdAttachSurface, between two kernel-mode surface objects.
ms.assetid: 28037b42-a00c-4063-93ee-5d71761a95d8
title: NtGdiDdUnattachSurface function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdUnattachSurface
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdUnattachSurface function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Removes an attachment, created with [**NtGdiDdAttachSurface**](-dxgkernel-ntgdiddattachsurface.md), between two kernel-mode surface objects.

## Syntax


```C++
VOID APIENTRY NtGdiDdUnattachSurface(
  _In_ HANDLE hSurface,
  _In_ HANDLE hSurfaceAttached
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

The kernel-mode surface object that was passed as the hSurfaceFrom parameter to [**NtGdiDdAttachSurface**](-dxgkernel-ntgdiddattachsurface.md).

</dd> <dt>

*hSurfaceAttached* \[in\]
</dt> <dd>

The kernel-mode surface object that was passed as the hSurfaceTo parameter to [**NtGdiDdAttachSurface**](-dxgkernel-ntgdiddattachsurface.md)

</dd> </dl>

## Return value

**NtGdiDdUnattachSurface** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Remarks

It is recommended that applications use the DirectDraw  API, which handles surface attachments in a higher-level manner.

It is not necessary to call this function because the kernel will automatically destroy all attachments when [**NtGdiDdDestroySurface**](-dxgkernel-ntgdidddestroysurface.md) is called.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> </dl>

 

 




