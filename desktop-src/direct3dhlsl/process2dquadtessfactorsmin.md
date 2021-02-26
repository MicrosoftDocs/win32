---
title: Process2DQuadTessFactorsMin function
description: Generates the corrected tessellation factors for a quad patch. | Process2DQuadTessFactorsMin function
ms.assetid: 45adf78a-9386-4460-97df-59d7739a1eee
keywords:
- Process2DQuadTessFactorsMin function HLSL
topic_type:
- apiref
api_name:
- Process2DQuadTessFactorsMin
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Process2DQuadTessFactorsMin function

Generates the corrected tessellation factors for a quad patch.

## Syntax

``` syntax
void Process2DQuadTessFactorsMin(
  in  float4 RawEdgeFactors,
  in  float2 InsideScale,
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

Type: **float2**

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

Generates the corrected tessellation factors for a quad patch, computing the inside tessellation factors as the minimum of the edge tessellation factors. The U and V inside tessellation factors are computed independently using the minimums of opposing sides of the domain, then are scaled by InsideScale. The result is then rounded based on the partitioning mode, but the unrounded results are available using the UnroundedInsideTessFactors parameter.

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

 

 




