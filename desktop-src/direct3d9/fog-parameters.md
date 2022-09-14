---
description: Fog parameters are controlled through device render states.
ms.assetid: a3c5f439-6937-4ba9-991f-5a4154447cf9
title: Fog Parameters (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Fog Parameters (Direct3D 9)

Fog parameters are controlled through device render states. Both pixel and vertex fog types support all the fog formulas introduced in [Fog Formulas (Direct3D 9)](fog-formulas.md). The [**D3DFOGMODE**](./d3dfogmode.md) enumerated type defines constants that you can use to identify the fog formula you want Microsoft Direct3D to use. The D3DRS\_FOGTABLEMODE render state controls the fog mode that Direct3D uses for pixel fog, and the D3DRS\_FOGVERTEXMODE render state controls the mode for vertex fog.

When using the linear fog formula, you set the starting and ending distances through the D3DRS\_FOGSTART and D3DRS\_FOGEND render states. How the system interprets these values depends on the type of fog your application uses - pixel or vertex fog - and, when using pixel fog, if z-based or w-based depth is being used. The following table summarizes fog types and their start and end units.



| Fog type  | Fog start/end units      |
|-----------|--------------------------|
| Pixel (Z) | Device space \[0.0,1.0\] |
| Pixel (W) | Camera space             |
| Vertex    | Camera space             |



 

The D3DRS\_FOGDENSITY render state controls the fog density applied when an exponential fog formula is enabled. Fog density is essentially a weighting factor, ranging from 0.0 to 1.0 (inclusive), that scales the distance value in the exponent.

The color that the system uses for fog blending is controlled through the D3DRS\_FOGCOLOR device render state. For more information, see [Fog Color (Direct3D 9)](fog-color.md) and [Fog Blending (Direct3D 9)](fog-blending.md).

## Related topics

<dl> <dt>

[Fog Types](fog-types.md)
</dt> </dl>

 

 
