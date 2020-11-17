---
title: Sample(S,float,int,float) function (HLSL reference)
description: Samples a Texture2D with an optional value to clamp sample level-of-detail (LOD) values to.
ms.assetid: 899FACB6-40BB-471B-82A7-BDBBC63B206E
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

# Sample(S,float,int,float) function (HLSL reference)

Samples a [**Texture2D**](sm5-object-texture2d.md) with an optional value to clamp sample level-of-detail (LOD) values to.

> [!Note]  
> Requires [shader model 5](d3d11-graphics-reference-sm5.md) or higher.

 

## Syntax

``` syntax
DXGI_FORMAT Sample(
  in SamplerState S,
  in float Location,
  in int Offset,
  in float Clamp
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

An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the location before sampling. The texture offsets need to be static. The argument type is dependent on the texture-object type. For more info, see [Applying texture coordinate offsets](dx-graphics-hlsl-to-sample.md).



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

## Remarks

Texture sampling uses the texel position to look up a texel value. An offset can be applied to the position before lookup. The sampler state contains the sampling and filtering options. This method can be invoked within a pixel shader, but it is not supported in a vertex shader or a geometry shader.

Use an offset only at an integer miplevel; otherwise, you may get different results depending on hardware implementation or driver settings.

### Calculating Texel Positions

Texture coordinates are floating-point values that reference texture data, which is also known as normalized texture space. Address wrapping modes are applied in this order (texture coordinates + offsets + wrap mode) to modify texture coordinates outside the \[0...1\] range.

For texture arrays, an additional value in the location parameter specifies an index into a texture array. This index is treated as a scaled float value (instead of the normalized space for standard texture coordinates). The conversion to an integer index is done in the following order (float + round-to-nearest-even integer + clamp to the array range).

### Applying Texture Coordinate Offsets

The offset parameter modifies the texture coordinates, in texel space. Even though texture coordinates are normalized floating-point numbers, the offset applies an integer offset. Also note that the texture offsets need to be static.

The data format returned is determined by the texture format. For example, if the texture resource was defined with the DXGI\_FORMAT\_A8B8G8R8\_UNORM\_SRGB format, the sampling operation converts sampled texels from gamma 2.0 to 1.0, filter, and writes the result as a floating-point value in the range \[0..1\].

Use an offset only at an integer miplevel; otherwise, you may get results that do not translate well to hardware.

## See also

<dl> <dt>

[Sample methods](texture-sample-overload.md)
</dt> <dt>

[Texture-Object](dx-graphics-hlsl-to-type.md)
</dt> </dl>

 

 
