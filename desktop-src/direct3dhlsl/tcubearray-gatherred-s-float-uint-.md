---
title: TextureCubeArray::GatherRed(S,float,uint) function
description: Returns the red components of the four texel values that would be used in a bi-linear filtering operation, along with tile-mapping status. | TextureCubeArray::GatherRed(S,float,uint) function
ms.assetid: 9776A4B5-6DDB-4B9F-96CD-F97B8908B057
keywords:
- GatherRed function HLSL
topic_type:
- apiref
api_name:
- GatherRed
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TextureCubeArray::GatherRed(S,float,uint) function

Returns the red components of the four texel values that would be used in a bi-linear filtering operation, along with tile-mapping status.

## Syntax


``` syntax
TemplateType GatherRed(
  in  SamplerState S,
  in  float4       Location,
  out uint         Status
);
```



## Parameters

<dl> <dt>

*S* \[in\]
</dt> <dd>

Type: **SamplerState**

The zero-based sampler index.

</dd> <dt>

*Location* \[in\]
</dt> <dd>

Type: **float**

The sample coordinates (u,v).

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type: **TemplateType**

A four-component value whose type is the same as the template type.

## Remarks

The texture samples can be used for bilinear interpolation.

This function is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |





## See also

<dl> <dt>

[GatherRed methods](texturecubearray-gatherred.md)
</dt> <dt>

[**TextureCubeArray**](texturecubearray.md)
</dt> </dl>




