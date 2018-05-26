---
title: SampleLevel(S,float,float,int,uint) function
description: Samples a texture on the specified mipmap level and returns status about the operation.
ms.assetid: B797C7F9-7436-4DD5-9CAB-EFF81D410174
keywords:
- SampleLevel function HLSL
topic_type:
- apiref
api_name:
- SampleLevel
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SampleLevel(S,float,float,int,uint) function

Samples a texture on the specified mipmap level and returns status about the operation.

## Syntax


```C++
DXGI_FORMAT SampleLevel(
  _In_  SamplerState S,
  _In_  float        Location,
  _In_  float        LOD,
  _In_  int          Offset,
  _Out_ uint         Status
);
```



## Parameters

<dl> <dt>

*S* \[in\]
</dt> <dd>

Type: **SamplerState**

A [Sampler state](dx-graphics-hlsl-sampler.md). This is an object declared in an effect file that contains state assignments.

</dd> <dt>

*Location* \[in\]
</dt> <dd>

Type: **float**

The texture coordinates. The argument type is dependent on the texture-object type.



| Texture-Object Type                    | Parameter Type |
|----------------------------------------|----------------|
| Texture1D                              | float          |
| Texture1DArray, Texture2D              | float2         |
| Texture2DArray, Texture3D, TextureCube | float3         |
| TextureCubeArray                       | float4         |



 

</dd> <dt>

*LOD* \[in\]
</dt> <dd>

Type: **float**

\[in\] A number that specifies the mipmap level. If the value is ≤ 0, mipmap level 0 (biggest map) is used. The fractional value (if supplied) is used to interpolate between two mipmap levels.

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

Type: **int**

An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the location before sampling. Use an offset only at an integer miplevel; otherwise, you may get results that do not translate well to hardware. The argument type is dependent on the texture-object type. For more info, see [Applying Integer Offsets](dx-graphics-hlsl-to-sample.md#applying-texture-coordinate-offsets).



| Texture-Object Type           | Parameter Type |
|-------------------------------|----------------|
| Texture1D, Texture1DArray     | int            |
| Texture2D, Texture2DArray     | int2           |
| Texture3D                     | int3           |
| TextureCube, TextureCubeArray | not supported  |



 

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Type: **uint**

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](https://msdn.microsoft.com/library/windows/desktop/dn312084#tile). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type: **[**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059)**

The texture format, which is one of the typed values listed in [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059).

## See also

<dl> <dt>

[SampleLevel methods](texture1d-samplelevel.md)
</dt> </dl>

 

 




