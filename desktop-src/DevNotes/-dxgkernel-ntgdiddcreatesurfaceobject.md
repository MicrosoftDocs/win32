---
description: Creates a kernel-mode surface object that represents the user-mode surface object referenced by puSurfaceLocal.
ms.assetid: 1b2886a8-279b-4bec-9fb8-b88a68ded25b
title: NtGdiDdCreateSurfaceObject function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdCreateSurfaceObject
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdCreateSurfaceObject function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Creates a kernel-mode surface object that represents the user-mode surface object referenced by *puSurfaceLocal*.

## Syntax


```C++
HANDLE APIENTRY NtGdiDdCreateSurfaceObject(
  _In_ HANDLE             hDirectDrawLocal,
  _In_ HANDLE             hSurface,
  _In_ PDD_SURFACE_LOCAL  puSurfaceLocal,
  _In_ PDD_SURFACE_MORE   puSurfaceMore,
  _In_ PDD_SURFACE_GLOBAL puSurfaceGlobal,
  _In_ BOOL               bComplete
);
```



## Parameters

<dl> <dt>

*hDirectDrawLocal* \[in\]
</dt> <dd>

Handle to the kernel-mode DirectDraw object.

</dd> <dt>

*hSurface* \[in\]
</dt> <dd>

Previous handle to the same surface. Used if the surface is being re-created after a mode switch.

</dd> <dt>

*puSurfaceLocal* \[in\]
</dt> <dd>

Pointer to the [**DD\_SURFACE\_LOCAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_local) structure that represents the DirectDraw user-mode surface object with which to associate the allocated memory. See the DDK documentation for details.

</dd> <dt>

*puSurfaceMore* \[in\]
</dt> <dd>

Pointer to the [**DD\_SURFACE\_MORE**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_more) structure that contains additional local data for each individual surface object. See the DDK documentation for details.

</dd> <dt>

*puSurfaceGlobal* \[in\]
</dt> <dd>

Pointer to the [**DD\_SURFACE\_GLOBAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_global) structure that contains surface data shared globally with multiple surfaces. See the DDK documentation for details.

</dd> <dt>

*bComplete* \[in\]
</dt> <dd>

Kernel-mode object completion flag. Can be one of the following values.

<dt>



 (TRUE)


</dt> <dd>

Complete all processing concerning the kernel-mode representation.

</dd> <dt>



 (FALSE)


</dt> <dd>

Create the object, but do not set up internal data such as the memory pointer. Objects created using **FALSE** can be attached using [**NtGdiDdAttachSurface**](-dxgkernel-ntgdiddattachsurface.md) and are completed by a call to [**NtGdiDdCreateSurface**](-dxgkernel-ntgdiddcreatesurface.md).

</dd> </dl> </dd> </dl>

## Return value

If successful, this function returns a handle to the kernel-mode surface representation; otherwise it returns **NULL**.

## Remarks

Applications are advised to use the DirectDraw and [Direct3D](../direct3d10/d3d10-graphics-reference.md) APIs to create and manage graphics device objects. These constructs abstract the device creation process in a simplified and operating-system-independent way.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> <dt>

[**DdCreateSurfaceObject**](/windows/desktop/api/Ddrawgdi/nf-ddrawgdi-ddcreatesurfaceobject)
</dt> <dt>

[**NtGdiDdDeleteSurfaceObject**](-dxgkernel-ntgdidddeletesurfaceobject.md)
</dt> <dt>

[**NtGdiDdAttachSurface**](-dxgkernel-ntgdiddattachsurface.md)
</dt> <dt>

[**NtGdiDdCreateSurface**](-dxgkernel-ntgdiddcreatesurface.md)
</dt> </dl>

 

 
