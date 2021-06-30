---
title: Sample (DirectX HLSL Texture Object)
description: Samples a texture. | Sample (DirectX HLSL Texture Object)
ms.assetid: 788ba4b4-8013-411f-9a19-fb9983386fa0
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Sample (DirectX HLSL Texture Object)

Samples a texture.

&lt;Template Type&gt; Object.Sample( sampler\_state S, float Location \[, int Offset\] );

## Parameters

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="Object"></span><span id="object"></span><span id="OBJECT"></span><em>Object</em><br/></td>
<td>Any <a href="dx-graphics-hlsl-to-type.md">texture-object</a> type (except Texture2DMS and Texture2DMSArray).<br/></td>
</tr>
<tr class="even">
<td><span id="S"></span><span id="s"></span><em>S</em><br/></td>
<td>[in] A <a href="dx-graphics-hlsl-sampler.md">Sampler state</a>. This is an object declared in an effect file that contains state assignments.<br/></td>
</tr>
<tr class="odd">
<td><span id="Location"></span><span id="location"></span><span id="LOCATION"></span><em>Location</em><br/></td>
<td>[in] The texture coordinates. The argument type is dependent on the texture-object type. <br/> 
<table>
<thead>
<tr class="header">
<th>Texture-Object Type</th>
<th>Parameter Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Texture1D</td>
<td>float</td>
</tr>
<tr class="even">
<td>Texture1DArray, Texture2D</td>
<td>float2</td>
</tr>
<tr class="odd">
<td>Texture2DArray, Texture3D, TextureCube</td>
<td>float3</td>
</tr>
<tr class="even">
<td>TextureCubeArray </td>
<td>float4</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td><p><span id="Offset"></span><span id="offset"></span><span id="OFFSET"></span><em>Offset</em></p></td>
<td><p>[in] An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the location before sampling. The texture offsets need to be static. The argument type is dependent on the texture-object type. For more info, see <a href="/windows/win32/direct3dhlsl/dx-graphics-hlsl-to-sample#applying-texture-coordinate-offsets">Applying texture coordinate offsets</a>.</p>

<table>
<thead>
<tr class="header">
<th>Texture-Object Type</th>
<th>Parameter Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Texture1D, Texture1DArray</td>
<td>int</td>
</tr>
<tr class="even">
<td>Texture2D, Texture2DArray</td>
<td>int2</td>
</tr>
<tr class="odd">
<td>Texture3D</td>
<td>int3</td>
</tr>
<tr class="even">
<td>TextureCube, TextureCubeArray </td>
<td>not supported</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>

## Return value

The texture's template type, which may be a single- or multi-component vector. The format is based on the texture's [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format).

## Minimum Shader Model

This function is supported in the following shader models.

| vs\_4\_0 | vs\_4\_1  | ps\_4\_0 | ps\_4\_1  | gs\_4\_0 | gs\_4\_1  |
|----------|-----------|----------|-----------|----------|-----------|
|          |           | x        | x         |          |           |

1.  TextureCubeArray is available in Shader Model 4.1 or higher.
2.  Shader Model 4.1 is available in Direct3D 10.1 or higher.

## Example

This partial code example is based on the BasicHLSL11.fx file in the [BasicHLSL11 Sample](https://github.com/microsoftarchive/msdn-code-gallery-community-a-c/tree/master/Basic%20DXUT%20Win32%20Samples/%5BC%2B%2B%5D-Basic%20DXUT%20Win32%20Samples/C%2B%2B/BasicHLSL11).

```
// Object Declarations
Texture2D g_MeshTexture;            // Color texture for mesh

SamplerState MeshTextureSampler
{
    Filter = MIN_MAG_MIP_LINEAR;
    AddressU = Wrap;
    AddressV = Wrap;
};

struct VS_OUTPUT
{
    float4 Position   : SV_POSITION; // vertex position 
    float4 Diffuse    : COLOR0;      // vertex diffuse color (note that COLOR0 is clamped from 0..1)
    float2 TextureUV  : TEXCOORD0;   // vertex texture coords 
};

VS_OUTPUT In;

// Shader body calling the intrinsic function
   ...
        Output.RGBColor = g_MeshTexture.Sample(MeshTextureSampler, In.TextureUV) * In.Diffuse;
```

## Remarks

Texture sampling uses the texel position to look up a texel value. An offset can be applied to the position before lookup. The sampler state contains the sampling and filtering options. This method can be invoked within a pixel shader, but it is not supported in a vertex shader or a geometry shader.

Use an offset only at an integer miplevel; otherwise, you may get different results depending on hardware implementation or driver settings.

### Calculating texel positions

Texture coordinates are floating-point values that reference texture data, which is also known as normalized texture space. Address wrapping modes are applied in this order (texture coordinates + offsets + wrap mode) to modify texture coordinates outside the \[0...1\] range.

For texture arrays, an additional value in the location parameter specifies an index into a texture array. This index is treated as a scaled float value (instead of the normalized space for standard texture coordinates). The conversion to an integer index is done in the following order (float + round-to-nearest-even integer + clamp to the array range).

### Applying texture coordinate offsets

The offset parameter modifies the texture coordinates, in texel space. Even though texture coordinates are normalized floating-point numbers, the offset applies an integer offset. Also note that the texture offsets need to be static.

The data format returned is determined by the texture format. For example, if the texture resource was defined with the DXGI\_FORMAT\_A8B8G8R8\_UNORM\_SRGB format, the sampling operation converts sampled texels from gamma 2.0 to 1.0, filter, and writes the result as a floating-point value in the range \[0..1\].

## Related topics

[Texture-Object](dx-graphics-hlsl-to-type.md)
