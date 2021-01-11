---
description: Sets the color key value for the specified surface.
ms.assetid: 052dba97-c047-4ef7-a908-2a66ade3af10
title: NtGdiDdSetColorKey function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdSetColorKey
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdSetColorKey function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Sets the color key value for the specified surface.

## Syntax


```C++
DWORD APIENTRY NtGdiDdSetColorKey(
  _In_    HANDLE              hSurface,
  _Inout_ PDD_SETCOLORKEYDATA puSetColorKeyData
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

Pointer to the [**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local) structure that describes the surface with which the color key is to be associated.

</dd> <dt>

*puSetColorKeyData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_SETCOLORKEYDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_setcolorkeydata) structure that contains the information required to set the color key for the specified surface.

</dd> </dl>

## Return value

**NtGdiDdSetColorKey** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

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

 

 
