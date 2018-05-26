---
Description: Ambient light is surrounding light that radiates from all directions. For information about how Direct3D uses ambient light, see Mathematics of Lighting (Direct3D 9).
ms.assetid: c5aa493e-09b8-433c-a21c-e39af795b3c9
title: Ambient Lighting State (Direct3D 9)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ambient Lighting State (Direct3D 9)

Ambient light is surrounding light that radiates from all directions. For information about how Direct3D uses ambient light, see [Mathematics of Lighting (Direct3D 9)](mathematics-of-lighting.md).

A C++ application sets the color of ambient lighting by invoking the [**IDirect3DDevice9::SetRenderState**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-setrenderstate?branch=master) method and passing the enumerated value D3DRS\_AMBIENT as the first parameter. The second parameter is a color value. The default value is zero.


```
// This code example assumes that d3dDevice is a
// valid pointer to an IDirect3DDevice9 interface.

// Set the ambient light.

d3dDevice->SetRenderState(D3DRS_AMBIENT, 0x00202020);
```



## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 



