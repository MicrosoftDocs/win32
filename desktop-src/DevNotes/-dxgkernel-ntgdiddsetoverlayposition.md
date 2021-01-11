---
description: Sets the position for an overlay.
ms.assetid: dd495118-9ceb-4100-a7ec-794659bb4461
title: NtGdiDdSetOverlayPosition function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdSetOverlayPosition
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdSetOverlayPosition function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Sets the position for an overlay.

## Syntax


```C++
DWORD APIENTRY NtGdiDdSetOverlayPosition(
  _In_    HANDLE                     hSurfaceSource,
  _In_    HANDLE                     hSurfaceDestination,
  _Inout_ PDD_SETOVERLAYPOSITIONDATA puSetOverlayPositionData
);
```



## Parameters

<dl> <dt>

*hSurfaceSource* \[in\]
</dt> <dd>

Handle to a [**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local) structure that represents the DirectDraw overlay surface.

</dd> <dt>

*hSurfaceDestination* \[in\]
</dt> <dd>

Pointer to a [**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local) structure representing the surface that is being overlaid.

</dd> <dt>

*puSetOverlayPositionData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_SETOVERLAYPOSITIONDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_setoverlaypositiondata) structure that contains the information required to set the overlay position.

</dd> </dl>

## Return value

**NtGdiDdSetOverlayPosition** returns one of the following callback codes.



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

 

 
