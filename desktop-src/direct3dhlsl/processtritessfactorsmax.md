---
title: ProcessTriTessFactorsMax function
description: Generates the corrected tessellation factors for a tri patch. | ProcessTriTessFactorsMax function
ms.assetid: a24cc1a8-5e6e-4963-b36b-e2265475580e
keywords:
- ProcessTriTessFactorsMax function HLSL
topic_type:
- apiref
api_name:
- ProcessTriTessFactorsMax
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ProcessTriTessFactorsMax function

Generates the corrected tessellation factors for a tri patch.

## Syntax

``` syntax
void ProcessTriTessFactorsMax(
  in  float3 RawEdgeFactors,
  in  float InsideScale,
  out float3 RoundedEdgeTessFactors,
  out float RoundedInsideTessFactor,
  out float UnroundedInsideTessFactor
);
```

## Parameters

<dl> <dt>

*RawEdgeFactors* \[in\]
</dt> <dd>

Type: **float3**

The edge tessellation factors, passed into the tessellator stage.

</dd> <dt>

*InsideScale* \[in\]
</dt> <dd>

Type: **float**

The scale factor applied to the UV tessellation factors computed by the tessellation stage. The allowable range for InsideScale is 0.0 to 1.0.

</dd> <dt>

*RoundedEdgeTessFactors* \[out\]
</dt> <dd>

Type: **float3**

The rounded edge-tessellation factors calculated by the tessellator stage.

</dd> <dt>

*RoundedInsideTessFactor* \[out\]
</dt> <dd>

Type: **float**

The tessellation factors calculated by the tessellator stage, and rounded.

</dd> <dt>

*UnroundedInsideTessFactor* \[out\]
</dt> <dd>

Type: **float**

The original, unrounded, UV tessellation factors computed by the tessellation stage.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Generates the corrected tessellation factors for a tri patch, computing the inside tessellation factor as the maximum of the edge tessellation factors, which is then scaled by InsideScale. The result is then rounded based on the partitioning mode, but the unrounded results are available using the UnroundedInsideTessFactor parameter.

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

 

 




