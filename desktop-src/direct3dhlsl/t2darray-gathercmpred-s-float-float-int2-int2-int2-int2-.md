---
title: GatherCmpRed(S,float,float,int2,int2,int2,int2) function
description: Samples a texture, tests the samples against a compare value, and returns the red component.
ms.assetid: B436FB9A-C55C-477F-B8BE-933B1EB04AE1
keywords:
- GatherCmpRed function HLSL
topic_type:
- apiref
api_name:
- GatherCmpRed
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GatherCmpRed(S,float,float,int2,int2,int2,int2) function

Samples a texture, tests the samples against a compare value, and returns the red component.

## Syntax


```C++
TemplateType GatherCmpRed(
  _In_ SamplerState S,
  _In_ float        Location,
  _In_ float        CompareValue,
  _In_ int2         Offset1,
  _In_ int2         Offset2,
  _In_ int2         Offset3,
  _In_ int2         Offset4
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

*Offset1* \[in\]
</dt> <dd>

Type: **int2**

The first offset component applied to the texture coordinates before sampling.

</dd> <dt>

*Offset2* \[in\]
</dt> <dd>

Type: **int2**

The second offset component applied to the texture coordinates before sampling.

</dd> <dt>

*Offset3* \[in\]
</dt> <dd>

Type: **int2**

The third offset component applied to the texture coordinates before sampling.

</dd> <dt>

*Offset4* \[in\]
</dt> <dd>

Type: **int2**

The fourth offset component applied to the texture coordinates before sampling.

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

[GatherCmpRed methods](texture2darray-gathercmpred.md)
</dt> </dl>

 

 




