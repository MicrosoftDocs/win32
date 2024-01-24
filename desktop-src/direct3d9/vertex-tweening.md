---
description: Vertex tweening blends two user-provided positions (or normals).
ms.assetid: 'vs|directx_sdk|~\vertex_tweening.htm'
title: Vertex Tweening (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Vertex Tweening (Direct3D 9)

Vertex tweening blends two user-provided positions (or normals). Tweening is mutually exclusive from vertex blending with weights. Tweening is performed before lighting and clipping, and is enabled by setting D3DRS\_VERTEXBLEND to D3DVBF\_TWEENING. The resulting vertex position is computed by:


```
POSITION = POSITION1 * (1.0 - TWEENFACTOR) + POSITION2 * TWEENFACTOR
```



The same approach is used for calculating normals. For more information, see [Using Vertex Tweening (Direct3D 9)](using-vertex-tweening.md).

## Related topics

<dl> <dt>

[Geometry Blending](geometry-blending.md)
</dt> </dl>

 

 



