---
description: The Direct3D lighting engine can use per-vertex color data when performing lighting if you tell the runtime the data is present.
ms.assetid: acb43921-f0d4-4151-9371-1b99e5d30c0e
title: Per-Vertex Color State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Per-Vertex Color State (Direct3D 9)

The Direct3D lighting engine can use per-vertex color data when performing lighting if you tell the runtime the data is present. This is done by turning on the following render state:


```
// disable per-vertex color
SetRenderState(D3DRS_COLORVERTEX, FALSE);

// enable per-vertex color
SetRenderState(D3DRS_COLORVERTEX, TRUE);
```



If per-vertex color is enabled, applications can configure the source from which the system retrieves color information for a vertex. The D3DRS\_AMBIENTMATERIALSOURCE, D3DRS\_DIFFUSEMATERIALSOURCE, D3DRS\_EMISSIVEMATERIALSOURCE, and D3DRS\_SPECULARMATERIALSOURCE render states control the ambient, diffuse, emissive, and specular color component sources, respectively. Each state can be set to members of the [**D3DMATERIALCOLORSOURCE**](./d3dmaterialcolorsource.md) enumerated type, which defines constants that instruct the system to use the current material, diffuse color, or specular color as the source for the specified color component.

## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 
