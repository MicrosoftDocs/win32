---
title: SampleCmpLevelZero::SampleCmpLevelZero(S,float,float,int,uint) function
description: Samples a texture on mipmap level 0 only and compares the result to a comparison value. Returns status about the operation. | SampleCmpLevelZero::SampleCmpLevelZero(S,float,float,int,uint) function
ms.assetid: A2F7FD4A-49D8-41B3-A5AF-7B54A8B5266C
keywords:
- SampleCmpLevelZero function HLSL
topic_type:
- apiref
api_name:
- SampleCmpLevelZero
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SampleCmpLevelZero::SampleCmpLevelZero(S,float,float,int,uint) function

Samples a texture on mipmap level 0 only and compares the result to a comparison value. Returns status about the operation.

## Syntax


``` syntax
DXGI_FORMAT SampleCmpLevelZero(
  in  SamplerState S,
  in  float        Location,
  in  float        CompareValue,
  in  int          Offset,
  out uint         Status
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

*CompareValue* \[in\]
</dt> <dd>

Type: **float**

A floating-point value to use as a comparison value.

</dd> <dt>

*Offset* \[in\]
</dt> <dd>

Type: **int**

An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the location before sampling. Use an offset only at an integer miplevel; otherwise, you may get results that do not translate well to hardware. The argument type is dependent on the texture-object type. For more info, see [Applying Integer Offsets](dx-graphics-hlsl-to-sample.md).



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

The status of the operation. You can't access the status directly; instead, pass the status to the [**CheckAccessFullyMapped**](checkaccessfullymapped.md) intrinsic function. **CheckAccessFullyMapped** returns **TRUE** if all values from the corresponding **Sample**, **Gather**, or **Load** operation accessed mapped tiles in a [tiled resource](/windows/desktop/direct3d11/direct3d-11-2-features). If any values were taken from an unmapped tile, **CheckAccessFullyMapped** returns **FALSE**.

</dd> </dl>

## Return value

Type: **[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format)**

The texture format, which is one of the typed values listed in [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format).

## See also

<dl> <dt>

[SampleCmpLevelZero methods](texture1d-samplecmplevelzero.md)
</dt> </dl>

 

 
