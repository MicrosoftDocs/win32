---
title: TextureCube::GatherGreen(S,float,uint) function
description: Returns the green components of the four texel values that would be used in a bi-linear filtering operation, along with tile-mapping status. | TextureCube::GatherGreen(S,float,uint) function
ms.assetid: DB0A6386-70ED-4D8C-A4EE-C058496D2F12
keywords:
- GatherGreen function HLSL
topic_type:
- apiref
api_name:
- GatherGreen
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TextureCube::GatherGreen(S,float,uint) function

Returns the green components of the four texel values that would be used in a bi-linear filtering operation, along with tile-mapping status.

## Syntax


``` syntax
TemplateType GatherGreen(
  in  SamplerState S,
  in  float        Location,
  out uint         Status
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

[GatherGreen methods](texturecube-gathergreen.md)
</dt> <dt>

[**TextureCube**](texturecube.md)
</dt> </dl>

 

 
