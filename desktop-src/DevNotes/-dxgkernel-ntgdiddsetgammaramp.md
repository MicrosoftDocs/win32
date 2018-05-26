---
Description: Sets the gamma ramp for the device.
ms.assetid: 92ea0247-6eec-4c5f-9ea7-65f6b97dde1e
title: NtGdiDdSetGammaRamp function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NtGdiDdSetGammaRamp function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Sets the gamma ramp for the device.

## Syntax


```C++
BOOL APIENTRY NtGdiDdSetGammaRamp(
  _In_ HANDLE hDirectDraw,
  _In_ HDC    hdc,
  _In_ LPVOID lpGammaRamp
);
```



## Parameters

<dl> <dt>

*hDirectDraw* \[in\]
</dt> <dd>

Handle to the kernel-mode driver object for which the ramp is to be set.

</dd> <dt>

*hdc* \[in\]
</dt> <dd>

Reserved.

</dd> <dt>

*lpGammaRamp* \[in\]
</dt> <dd>

Pointer to an array of **DDGAMMARAMP** structures.

</dd> </dl>

## Return value

The return value is **TRUE** if the function is successful. Otherwise, it is **NULL**.

## Remarks

It is recommended that applications use the **IDirectDrawGammaControl::SetGammaRamp** or [**IDirect3DDevice9::SetGammaRamp**](direct3d9.idirect3ddevice9__setgammaramp) methods instead because these methods offer the same functionality independent of the operating system.

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

 

 




