---
title: Texture3D::Sample(S,float,int,float) function
description: Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to. | Texture3D::Sample(S,float,int,float) function
ms.assetid: A1114A4A-16B9-4A5D-9A9D-262D6BAA9F2E
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

# Texture3D::Sample(S,float,int,float) function

Samples a texture with an optional value to clamp sample level-of-detail (LOD) values to.

## Syntax


``` syntax
DXGI_FORMAT Sample(
  in SamplerState S,
  in float        Location,
  in int          Offset,
  in float        Clamp
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

*Offset* \[in\]
</dt> <dd>

An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the location before sampling. Use an offset only at an integer miplevel; otherwise, you may get results that do not translate well to hardware. The argument type is dependent on the texture-object type. For more info, see [Applying Integer Offsets](dx-graphics-hlsl-to-sample.md).



| Texture-Object Type           | Parameter Type |
|-------------------------------|----------------|
| Texture1D, Texture1DArray     | int            |
| Texture2D, Texture2DArray     | int2           |
| Texture3D                     | int3           |
| TextureCube, TextureCubeArray | not supported  |



 

</dd> <dt>

*Clamp* \[in\]
</dt> <dd>

An optional value to clamp sample LOD values to. For example, if you pass 2.0f for the clamp value, you ensure that no individual sample accesses a mip level less than 2.0f.

</dd> </dl>

## Return value

The texture format, which is one of the typed values listed in [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format).

## See also

<dl> <dt>

[Sample methods](texture3d-sample.md)
</dt> <dt>

[**Texture3D**](sm5-object-texture3d.md)
</dt> </dl>

 

 
