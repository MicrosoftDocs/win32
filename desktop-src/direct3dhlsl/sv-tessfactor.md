---
title: SV_TessFactor
description: Defines the tessellation amount on each edge of a patch.
ms.assetid: 970ff744-da5b-4933-866c-dd38b85fb48d
keywords:
- SV_TessFactor HLSL
topic_type:
- apiref
api_name:
- SV_TessFactor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SV\_TessFactor

Defines the tessellation amount on each edge of a patch.

## Type



|  Type          |  Input topology              |
|------------|----------------|
| float\[4\] | quad patch     |
| float\[3\] | tri patch      |
| float\[2\] | isoline        |



 

Tessellation factors must be declared as an array; they cannot be packed into a single vector.

## Remarks

The value for tessellation factor must be defined during the patch constant function of the hull shader.

Required output value for the hull shader if using quad or tri patches. This value is also a required input value for the domain shader to match the patch-constant data signatures between the tessellation stages.

For an isoline, the first value in SV\_TessFactor is the line-density tessellation factor, the second value is the line-detail tessellation factor.

### Tri Patch Tessellation Factors

The first component provides the tesselation factor for the u==0 edge of the patch. The second component provides the tesselation factor for the v==0 edge of the patch. The third component provides the tesselation factor for the w==0 edge of the patch.

### Quad Patch Tessellation Factors

The first component provides the tesselation factor for the u==0 edge of the patch. The second component provides the tesselation factor for the v==0 edge of the patch. The third component provides the tesselation factor for the u==1 edge of the patch. The fourth component provides the tesselation factor for the v==1 edge of the patch. The ordering of the edges is clockwise, starting from the u==0 edge, which is the left side of the patch, and from the v==0 edge, which is the top of the patch.

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        | x    | x      |          |       |         |



 

## See also

<dl> <dt>

[Semantics](dx-graphics-hlsl-semantics.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




