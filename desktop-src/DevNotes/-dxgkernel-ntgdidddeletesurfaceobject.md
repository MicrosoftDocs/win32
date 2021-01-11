---
description: NtGdiDdDeleteSurfaceObject deletes a previously created kernel-mode surface object.
ms.assetid: 95ce6c73-7e41-4ac3-b849-9b8f53aa3ac3
title: NtGdiDdDeleteSurfaceObject function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdDeleteSurfaceObject
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdDeleteSurfaceObject function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

**NtGdiDdDeleteSurfaceObject** deletes a previously created kernel-mode surface object.

## Syntax


```C++
BOOL APIENTRY NtGdiDdDeleteSurfaceObject(
  _In_ HANDLE hSurface
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to the previously created kernel-mode surface object.

</dd> </dl>

## Return value

If successful, this function returns **TRUE**; otherwise it returns **FALSE**.

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

[**DdDeleteSurfaceObject**](/windows/desktop/api/Ddrawgdi/nf-ddrawgdi-dddeletesurfaceobject)
</dt> <dt>

[**NtGdiDdCreateSurfaceObject**](-dxgkernel-ntgdiddcreatesurfaceobject.md)
</dt> </dl>

 

 
