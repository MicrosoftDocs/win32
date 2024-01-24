---
description: To improve rendering performance, you can cull out (or remove) a primitive that faces away from the camera.
ms.assetid: b4b8ff3f-aa20-4422-8f6f-34cae25de0e6
title: Culling State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Culling State (Direct3D 9)

To improve rendering performance, you can cull out (or remove) a primitive that faces away from the camera. For single-sided primitives, this saves rendering time because a back-face is not visible. To enable culling, you need to know the winding order of the vertices (typically counter-clockwise). This example will remove any primitive whose back face is facing forward (given a counter-clockwise winding order):


```
SetRenderState(D3DRS_CULLMODE, D3DCULL_CCW);
```



## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 



