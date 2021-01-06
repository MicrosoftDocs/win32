---
description: Destroys a previously allocated kernel-mode Microsoft DirectDraw surface object.
ms.assetid: 65419fce-9e82-4621-9906-832144888a3b
title: NtGdiDdDestroySurface function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdDestroySurface
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdDestroySurface function

\[This function is subject to change with each operating system revision. Instead, use the DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Destroys a previously allocated kernel-mode Microsoft DirectDraw surface object.

## Syntax


```C++
DWORD APIENTRY NtGdiDdDestroySurface(
  _In_ HANDLE hSurface,
  _In_ BOOL   bRealDestroy
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to previously allocated kernel-mode surface object.

</dd> <dt>

*bRealDestroy* \[in\]
</dt> <dd>

Specifies how to destroy the surface. Can be one of the following values.

<dt>



 (TRUE)


</dt> <dd>

Destroy the surface and free video memory.

</dd> <dt>



 (FALSE)


</dt> <dd>

Free the video memory but leave the surface in an uninitialized state.

</dd> </dl> </dd> </dl>

## Return value

**NtGdiDdDestroySurface** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Remarks

It is recommended that applications use the DirectDraw and Direct3D APIs to create and destroy surfaces instead of this function.

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

 

 




