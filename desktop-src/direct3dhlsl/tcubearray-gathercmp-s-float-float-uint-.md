---
title: GatherCmp(S,float,float,uint) function
description: Samples a texture, tests the samples against a compare value, and returns all four components along with status about the operation.
ms.assetid: '758CD159-58B6-42AE-92B3-5AA3C72FD0F1'
keywords: ["GatherCmp function HLSL"]
topic_type:
- apiref
api_name:
- GatherCmp
api_type:
- NA
---

# GatherCmp(S,float,float,uint) function

Samples a texture, tests the samples against a compare value, and returns all four components along with status about the operation.

## Syntax


```C++
TemplateType GatherCmp(
  _In_  SamplerState S,
  _In_  float        Location,
  _In_  float        CompareValue,
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

*CompareValue* \[in\]
</dt> <dd>

Type: **float**

A value to compare each against each sampled value.

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

[GatherCmp methods](texturecubearray-gathercmp.md)
</dt> <dt>

[**TextureCubeArray**](texturecubearray.md)
</dt> </dl>

 

 




