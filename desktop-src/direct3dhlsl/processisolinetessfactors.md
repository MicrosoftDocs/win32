---
title: ProcessIsolineTessFactors function
description: Generates the rounded tessellation factors for an isoline.
ms.assetid: 0816b3e0-cb03-4a7a-9732-e84c637b3d48
keywords:
- ProcessIsolineTessFactors function HLSL
topic_type:
- apiref
api_name:
- ProcessIsolineTessFactors
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ProcessIsolineTessFactors function

Generates the rounded tessellation factors for an isoline.

## Syntax

``` syntax
void ProcessIsolineTessFactors(
  in  float RawDetailFactor,
  in  float RawDensityFactor,
  out float RoundedDetailFactor,
  out float RoundedDensityFactor
);
```

## Parameters

<dl> <dt>

*RawDetailFactor* \[in\]
</dt> <dd>

Type: **float**

The desired detail factor.

</dd> <dt>

*RawDensityFactor* \[in\]
</dt> <dd>

Type: **float**

The desired density factor.

</dd> <dt>

*RoundedDetailFactor* \[out\]
</dt> <dd>

Type: **float**

The rounded detail factor clamped to a range that can be used by the tessellator.

</dd> <dt>

*RoundedDensityFactor* \[out\]
</dt> <dd>

Type: **float**

The rounded density factor clamped to a rangethat can be used by the tessellator.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

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

 

 




