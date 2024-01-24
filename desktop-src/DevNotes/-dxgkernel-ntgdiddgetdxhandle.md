---
description: Returns the kernel-mode Microsoft DirectX  API handle to use in subsequent calls to the kernel-mode entry points that control the DirectX  API mechanism.
ms.assetid: c95cb188-305f-4b60-be55-0511b57f0597
title: NtGdiDdGetDxHandle function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdGetDxHandle
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdGetDxHandle function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Returns the kernel-mode Microsoft DirectX  API handle to use in subsequent calls to the kernel-mode entry points that control the DirectX  API mechanism.

## Syntax


```C++
DWORD APIENTRY NtGdiDdGetDxHandle(
  _In_ HANDLE hDirectDraw,
  _In_ HANDLE hSurface,
  _In_ BOOL   bRelease
);
```



## Parameters

<dl> <dt>

*hDirectDraw* \[in\]
</dt> <dd>

Handle to DirectDraw object owning the surface. This parameter is optional and may be set to **NULL**.

</dd> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to surface for which to return a kernel-mode DirectX API handle. This parameter is optional and may be set to **NULL**.

</dd> <dt>

*bRelease* \[in\]
</dt> <dd>

Set to **TRUE** if the DirectX API kernel mode interface should be released. Otherwise, **FALSE**.

</dd> </dl>

## Return value

A DirectX API handle used in subsequent DirectX API-oriented kernel entry points.

## Remarks

If both *hDirectDraw* and *hSurface* are specified, *hSurface* is ignored.

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

 

 




