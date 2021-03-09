---
title: ProcessQuadTessFactorsMin function
description: Generates the corrected tessellation factors for a quad patch. | ProcessQuadTessFactorsMin function
ms.assetid: 19cbd807-e379-4ee3-beba-55e35e4bcbcf
keywords:
- ProcessQuadTessFactorsMin function HLSL
topic_type:
- apiref
api_name:
- ProcessQuadTessFactorsMin
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ProcessQuadTessFactorsMin function

Generates the corrected tessellation factors for a quad patch.

## Syntax

``` syntax
void ProcessQuadTessFactorsMin(
  in  float4 RawEdgeFactors,
  in  float InsideScale,
  out float4 RoundedEdgeTessFactors,
  out float2 RoundedInsideTessFactors,
  out float2 UnroundedInsideTessFactors
);
```

## Parameters

<dl> <dt>

*RawEdgeFactors* \[in\]
</dt> <dd>

Type: **float4**

The edge tessellation factors, passed into the tessellator stage.

</dd> <dt>

*InsideScale* \[in\]
</dt> <dd>

Type: **float**

The scale factor applied to the UV tessellation factors computed by the tessellation stage. The allowable range for InsideScale is 0.0 to 1.0.

</dd> <dt>

*RoundedEdgeTessFactors* \[out\]
</dt> <dd>

Type: **float4**

The rounded edge-tessellation factors calculated by the tessellator stage.

</dd> <dt>

*RoundedInsideTessFactors* \[out\]
</dt> <dd>

Type: **float2**

The rounded tessellation factors calculated by the tessellator stage for inside edges.

</dd> <dt>

*UnroundedInsideTessFactors* \[out\]
</dt> <dd>

Type: **float2**

The tessellation factors calculated by the tessellator stage for inside edges.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Generates the corrected tessellation factors for a quad patch, computing the inside tessellation factors as the minimum of the edge tessellation factors. The inside tess factors will be identical values determined by the minimum of all four edges scaled by InsideScale. The result is then rounded based on the partitioning mode, but the unrounded results are available using the UnroundedInsideTessFactors parameter.

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        | x    |        |          |       |         |



 

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




