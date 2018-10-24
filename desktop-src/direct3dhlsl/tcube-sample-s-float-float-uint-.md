---
title: Sample(S,float,float,uint) function
description: Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to, and returns status of the operation.
ms.assetid: 8FA17583-9002-4DEC-A6D5-85B25DEA19B7
keywords:
- Sample function HLSL
topic_type:
- apiref
api_name:
- Sample
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# Sample(S,float,float,uint) function

Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to, and returns status of the operation.

## Syntax


```C++
DXGI_FORMAT Sample(
  _In_  SamplerState S,
  _In_  float        Location,
  _In_  float        Clamp,
  _Out_ uint         Status
);
```



## Parameters

<dl> <dt>

*S* \[in\]
</dt> <dd>

A [Sampler state](dx-graphics-hlsl-sampler.md). This is an object declared in an effect file that contains state assignments.

</dd> <dt>

*Location* \[in\]
</dt> <dd>

The texture coordinates. The argument type is dependent on the texture-object type.



| Texture-Object Type                    | Parameter Type |
|----------------------------------------|----------------|
| Texture1D                              | float          |
| Texture1DArray, Texture2D              | float2         |
| Texture2DArray, Texture3D, TextureCube | float3         |
| TextureCubeArray                       | float4         |



 

</dd> <dt>

*Clamp* \[in\]
</dt> <dd>

An optional value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f.

</dd> <dt>

*Status* \[out\]
</dt> <dd>

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](https://msdn.microsoft.com/library/windows/desktop/dn312084#tile). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

The texture format, which is one of the typed values listed in [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059).

## See also

<dl> <dt>

[Sample methods](texturecube-sample.md)
</dt> <dt>

[**TextureCube**](texturecube.md)
</dt> </dl>

 

 




