---
description: The following code example shows how to use the IDirect3DDevice9::GetDepthStencilSurface method to retrieve a pointer to the depth-buffer surface owned by the device.
ms.assetid: cd5c158a-d2c4-4ced-aa6f-cd8c0e426a74
title: Retrieving a Depth Buffer (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving a Depth Buffer (Direct3D 9)

The following code example shows how to use the [**IDirect3DDevice9::GetDepthStencilSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getdepthstencilsurface) method to retrieve a pointer to the depth-buffer surface owned by the device.


```
LPDIRECT3DSURFACE9 pZBuffer;

m_d3dDevice->GetDepthStencilSurface( &pZBuffer );
```



## Related topics

<dl> <dt>

[Depth Buffers](depth-buffers.md)
</dt> </dl>

 

 
