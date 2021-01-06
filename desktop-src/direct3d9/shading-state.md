---
description: Direct3D supports both flat and Gouraud shading. The default is Gouraud shading. To control the current shading mode, your C++ application specifies a member of the D3DSHADEMODE enumerated type for the D3DRS\_SHADEMODE render state.
ms.assetid: 0019b1b7-65f2-4009-8d0f-5a99cf32a410
title: Shading State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Shading State (Direct3D 9)

Direct3D supports both flat and Gouraud shading. The default is Gouraud shading. To control the current shading mode, your C++ application specifies a member of the [**D3DSHADEMODE**](./d3dshademode.md) enumerated type for the D3DRS\_SHADEMODE render state.

The following C++ code example demonstrates the process of setting the shading state to flat shading mode.


```
// This code example assumes that d3dDevice is a
// valid pointer to a IDirect3DDevice9 interface.
// Set the shading state.
d3dDevice->SetRenderState(D3DRS_SHADEMODE, D3DSHADE_FLAT);
```



## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 
