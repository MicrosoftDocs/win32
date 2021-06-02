---
description: If you do not light with a vertex shader or a pixel shader, you may choose to use the lighting engine in the runtime.
ms.assetid: 'vs|directx_sdk|~\lighting_state.htm'
title: Lighting State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Lighting State (Direct3D 9)

If you do not light with a vertex shader or a pixel shader, you may choose to use the lighting engine in the runtime. The lighting engine requires that the vertex data contains per-vertex normals; vertices without normal data will generate a dot product of zero in all lighting computations. The lighting calculations are covered in more detail in [Mathematics of Lighting (Direct3D 9)](mathematics-of-lighting.md).

To enable the lighting engine, use:


```
SetRenderState(D3DRS_LIGHTING, TRUE); 
```



## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 



