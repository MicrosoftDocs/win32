---
title: SampleCmp::SampleCmp(S,float,float,float) function for TextureCube
description: Samples a texture, using a comparison value to reject samples, with an optional value to clamp sample level-of-detail (LOD) values to. | SampleCmp::SampleCmp(S,float,float,float) function for TextureCube
ms.assetid: FCCF12CF-3F0A-4468-9FC4-27CAAF0BEEE3
keywords:
- SampleCmp function HLSL
topic_type:
- apiref
api_name:
- SampleCmp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SampleCmp::SampleCmp(S,float,float,float) function for TextureCube

Samples a texture, using a comparison value to reject samples, with an optional value to clamp sample level-of-detail (LOD) values to.

## Syntax


``` syntax
DXGI_FORMAT SampleCmp(
  in SamplerState S,
  in float        Location,
  in float        CompareValue,
  in float        Clamp
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

*Clamp* \[in\]
</dt> <dd>

Type: **float**

An optional value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f.

</dd> </dl>

## Return value

Type: **[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format)**

The texture format, which is one of the typed values listed in [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format).

## See also

<dl> <dt>

[SampleCmp methods](texturecube-samplecmp.md)
</dt> <dt>

[**TextureCube**](texturecube.md)
</dt> </dl>

 

 
