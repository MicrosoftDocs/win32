---
title: GatherCmpGreen(S,float,float,int2,int2,int2,int2) function
description: Samples a texture, tests the samples against a compare value, and returns the green component.
ms.assetid: 5A4B8AEB-B278-4456-893A-CAE61BFD6CA5
keywords:
- GatherCmpGreen function HLSL
topic_type:
- apiref
api_name:
- GatherCmpGreen
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# GatherCmpGreen(S,float,float,int2,int2,int2,int2) function

Samples a texture, tests the samples against a compare value, and returns the green component.

## Syntax


```C++
TemplateType GatherCmpGreen(
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

[GatherCmpGreen methods](texture2darray-gathercmpgreen.md)
</dt> </dl>

 

 




