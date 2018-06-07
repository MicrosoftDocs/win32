---
title: GatherCmpAlpha(S,float,float,int,uint) function
description: Samples a texture, tests the samples against a compare value, and returns the alpha component along with status about the operation.
ms.assetid: DCCF7F40-8A0D-47B8-910A-508382D3AE3F
keywords:
- GatherCmpAlpha function HLSL
topic_type:
- apiref
api_name:
- GatherCmpAlpha
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GatherCmpAlpha(S,float,float,int,uint) function

Samples a texture, tests the samples against a compare value, and returns the alpha component along with status about the operation.

## Syntax


```C++
TemplateType GatherCmpAlpha(
  _In_  SamplerState S,
  _In_  float        Location,
  _In_  float        CompareValue,
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

*CompareValue* \[in\]
</dt> <dd>

Type: **float**

A value to compare each against each sampled value.

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

[GatherCmpAlpha methods](texture2darray-gathercmpalpha.md)
</dt> </dl>

 

 




