---
Description: 'Releases the previously created device context (DC) for the indicated kernel-mode Microsoft DirectDraw surface object.'
ms.assetid: '98def2a1-878d-4776-a519-32cb70107338'
title: NtGdiDdReleaseDC function
---

# NtGdiDdReleaseDC function

\[This function is subject to change with each operating system revision. Instead, use the DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Releases the previously created device context (DC) for the indicated kernel-mode Microsoft DirectDraw surface object.

## Syntax


```C++
BOOL APIENTRY NtGdiDdReleaseDC(
  _In_ HANDLE hSurface
);
```



## Parameters

<dl> <dt>

*hSurface* \[in\]
</dt> <dd>

Handle to the previously created kernel-mode DirectDraw surface object.

</dd> </dl>

## Return value

If successful, this function returns **TRUE**; otherwise it returns **FALSE**.

## Remarks

Applications that need to obtain a DC for a DirectDraw surface may use [IDirectDrawSurface7::GetDC](directdraw.idirectdrawsurface7_getdc), which exposes this functionality in a manner independent of the operating system.

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

[**DdReleaseDC**](-dxgkernel-ddreleasedc.md)
</dt> </dl>

 

 




