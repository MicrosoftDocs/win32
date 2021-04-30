---
description: Polygons that are coplanar in your 3D space can be made to appear as if they are not coplanar by adding a z-bias to each one.
ms.assetid: 0ab4f63b-49de-4bd0-a10f-6f90b9706c58
title: Depth Bias (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Depth Bias (Direct3D 9)

Polygons that are coplanar in your 3D space can be made to appear as if they are not coplanar by adding a z-bias to each one. This is a technique commonly used to ensure that shadows in a scene are displayed properly. For instance, a shadow on a wall will likely have the same depth value as the wall does. If you render the wall first and then the shadow, the shadow might not be visible, or depth artifacts might be visible. You can reverse the order in which you render the coplanar objects in hopes of reversing the effect, but depth artifacts are still likely.

An application can help ensure that coplanar polygons are rendered properly by adding a bias to the z-values that the system uses when rendering the sets of coplanar polygons. To add a z-bias to a set of polygons, call the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) method just before rendering them, setting the *State* parameter to D3DRS\_DEPTHBIAS, and the *Value* parameter to a suitable float value (for example, a suitable value might be from -1.0 to 1.0); to pass this value to **SetRenderState**, you must also cast the value to a **DWORD**. A higher z-bias value increases the likelihood that the polygons you render will be visible when displayed with other coplanar polygons.


```
Offset = m * D3DRS_SLOPESCALEDEPTHBIAS + D3DRS_DEPTHBIAS
```



where m is the maximum depth slope of the triangle being rendered.


```
m = max(abs(delta z / delta x), abs(delta z / delta y)) 
```



The units for the D3DRS\_DEPTHBIAS and D3DRS\_SLOPESCALEDEPTHBIAS render states depend on whether z-buffering or w-buffering is enabled. The application must provide suitable values.

The bias is not applied to any line and point primitive. However, this bias needs to be applied to triangles drawn in wireframe mode.


```
// RenderStates
D3DRS_SLOPESCALEDEPTHBIAS, // Defaults to zero
D3DRS_DEPTHBIAS,           // Defaults to zero
```




```
// Caps
D3DPRASTERCAPS_DEPTHBIAS           
D3DPRASTERCAPS_SLOPESCALEDEPTHBIAS 
```



## Related topics

<dl> <dt>

[Pixel Pipeline](pixel-pipeline.md)
</dt> </dl>

 

 
