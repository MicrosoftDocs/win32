---
title: TextureCube::Sample(S,float,float) function
description: Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to. | TextureCube::Sample(S,float,float) function
ms.assetid: 7DB25135-46B5-48E2-91D0-A45D355179D6
keywords:
- Sample function HLSL
topic_type:
- apiref
api_name:
- Sample
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TextureCube::Sample(S,float,float) function

Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to.

## Syntax


``` syntax
DXGI_FORMAT Sample(
  in SamplerState S,
  in float        Location,
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

[Sample methods](texturecube-sample.md)
</dt> <dt>

[**TextureCube**](texturecube.md)
</dt> </dl>

 

 
