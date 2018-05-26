---
title: GatherBlue(S,float,int,uint) function
description: Samples a texture and returns the blue component along with status about the operation.
ms.assetid: 9E2A57C3-4EC4-4414-B16A-64AF759F04E9
keywords:
- GatherBlue function HLSL
topic_type:
- apiref
api_name:
- GatherBlue
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GatherBlue(S,float,int,uint) function

Samples a texture and returns the blue component along with status about the operation.

## Syntax


```C++
TemplateType GatherBlue(
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

[GatherBlue methods](texture2d-gatherblue.md)
</dt> </dl>

 

 




