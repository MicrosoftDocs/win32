---
description: During rendering, the pipeline interpolates vertex data across each triangle.
ms.assetid: 6fa05e56-c4cd-4623-abe9-2b1c8bbc644b
title: Triangle Interpolation (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Triangle Interpolation (Direct3D 9)

During rendering, the pipeline interpolates vertex data across each triangle. Vertex data can be a broad variety of data and can include (but is not limited to): diffuse color, specular color, diffuse alpha (triangle opacity), specular alpha, and a fog factor (taken from specular alpha for fixed function vertex pipeline and from fog register for programmable vertex pipeline). The vertex data is defined by the [Vertex Declaration (Direct3D 9)](vertex-declaration.md).

For some vertex data, the interpolation is dependent on the current shading mode, as shown in the following table.



| Shading mode | Description                                                                                                                                                                 |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Flat         | Only the fog factor is interpolated in flat shade mode. For all other interpolated values, the color of the first vertex in the triangle is applied across the entire face. |
| Gouraud      | Linear interpolation is performed between all three vertices.                                                                                                               |



 

The diffuse color and specular color are treated differently, depending on the color model. In the RGB color model, the system uses the red, green, and blue color components in the interpolation.

The alpha component of a color is treated as a separate interpolated value because device drivers can implement transparency in two different ways: by using texture blending or by using stippling.

Use the ShadeCaps member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure to determine what forms of interpolation the current device driver supports.

## Related topics

<dl> <dt>

[Coordinate Systems and Geometry](coordinate-systems-and-geometry.md)
</dt> </dl>

 

 



