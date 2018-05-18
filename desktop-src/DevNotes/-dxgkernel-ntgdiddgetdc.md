---
Description: 'Creates a device context (DC) for the specified surface.'
ms.assetid: 'c2eaaed6-db19-4dab-ac12-6b4e7eeb58e4'
title: NtGdiDdGetDC function
---

# NtGdiDdGetDC function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Creates a device context (DC) for the specified surface.

## Syntax


```C++
HDC APIENTRY NtGdiDdGetDC(
  _In_ HANDLE       hSurface,
  _In_ PALETTEENTRY *puColorTable
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to a kernel-mode DirectDraw surface previously returned by [**NtGdiDdCreateSurface**](-dxgkernel-ntgdiddcreatesurface.md) or [**NtGdiDdCreateSurfaceObject**](-dxgkernel-ntgdiddcreatesurfaceobject.md).

</dd> <dt>

*puColorTable* \[in\]
</dt> <dd>

Pointer to an override color table for the returned DC.

</dd> </dl>

## Return value

If successful, this function returns a valid **HDC**; otherwise it returns **NULL**.

## Remarks

Only one DC is allowed per surface at any given time. Subsequent calls to **NtGdiDdGetDC** will fail until the previous DC is released.

Applications are advised to call [IDirectDrawSurface7::GetDC](directdraw.idirectdrawsurface7_getdc) instead, which provides the same functionality in a manner independent of the operating system.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> <dt>

[**DdGetDC**](-dxgkernel-ddgetdc.md)
</dt> </dl>

 

 




