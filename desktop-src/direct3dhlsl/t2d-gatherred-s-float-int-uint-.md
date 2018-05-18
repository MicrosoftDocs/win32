---
title: GatherRed(S,float,int,uint) function
description: Samples a texture and returns the red component along with status about the operation.
ms.assetid: 'B49F738F-FB5C-4004-A3F3-D87C566DB597'
keywords: ["GatherRed function HLSL"]
topic_type:
- apiref
api_name:
- GatherRed
api_type:
- NA
---

# GatherRed(S,float,int,uint) function

Samples a texture and returns the red component along with status about the operation.

## Syntax


```C++
TemplateType GatherRed(
  _In_  SamplerState S,
  _In_  float        Location,
  _In_  int          Offset,
  _Out_ uint         Status
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

*Offset* \[in\]
</dt> <dd>

Type: **int**

The offset applied to the texture coordinates before sampling.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](https://msdn.microsoft.com/library/windows/desktop/dn312084#tile). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

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

[GatherRed methods](texture2d-gatherred.md)
</dt> </dl>

 

 




