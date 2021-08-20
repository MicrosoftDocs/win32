---
title: Texture Object
description: In Direct3D 10, you specify the samplers and textures independently; texture sampling is implemented by using a templated-texture object. This templated-texture object has a specific format, returns a specific type, and implements several methods.
ms.assetid: e8cb483a-d831-4942-b6fe-61dd5edb1813
keywords:
- Texture Object HLSL
topic_type:
- apiref
api_name:
- Texture Object
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Texture Object

In Direct3D 10, you specify the samplers and textures independently; texture sampling is implemented by using a templated-texture object. This templated-texture object has a specific format, returns a specific type, and implements several methods.

Differences between Direct3D9 and Direct3D10:

- In Direct3D 9, samplers are bound to specific textures.
- In Direct3D 10, textures and samplers are independent objects. Each templated-texture object implements texture sampling methods that take both the texture and the sampler as input parameters.



 

Here is the syntax for creating all texture objects (except multisampled objects).



| Object1 \[<*Type*>\] *Name*; |
|------------------------------------|



 

Multisampled objects (Texture2DMS and Texture2DMSArray) require the texture size to be explicitly stated and expressed as the number of samples.



| Object2 \[<*Type, Samples*>\] *Name*; |
|---------------------------------------------|



 

## Parameters



<table>
<colgroup>
<col  />
<col  />
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
<td>A texture object. Must be one of the following types. <br/> 
<table>
<thead>
<tr class="header">
<th>Object1 Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Buffer</td>
<td>Buffer </td>
</tr>
<tr class="even">
<td>Texture1D</td>
<td>1D texture</td>
</tr>
<tr class="odd">
<td>Texture1DArray</td>
<td>Array of 1D textures</td>
</tr>
<tr class="even">
<td>Texture2D</td>
<td>2D texture</td>
</tr>
<tr class="odd">
<td>Texture2DArray</td>
<td>Array of 2D textures</td>
</tr>
<tr class="even">
<td>Texture3D</td>
<td>3D texture</td>
</tr>
<tr class="odd">
<td>TextureCube</td>
<td>Cube texture</td>
</tr>
<tr class="even">
<td>TextureCubeArray  </td>
<td>Array of cube textures</td>
</tr>
<tr class="odd">
<td>Object2 Type</td>
<td>Description</td>
</tr>
<tr class="even">
<td>Texture2DMS</td>
<td>2D multisampled texture</td>
</tr>
<tr class="odd">
<td>Texture2DMSArray</td>
<td>Array of 2D multisampled textures</td>
</tr>
</tbody>
</table>

<p> </p>
<ol>
<li>The Buffer type supports most texture object methods except GetDimensions.</li>
<li>TextureCubeArray is available in shader model 4.1 or higher.</li>
<li>Shader model 4.1 is available in Direct3D 10.1 or higher.</li>
</ol></td>
</tr>
<tr class="even">
<td><p><span id="Type"></span><span id="type"></span><span id="TYPE"></span><em>Type</em></p></td>
<td><p>Optional. Any <a href="dx-graphics-hlsl-scalar.md">scalar HLSL type</a> or <a href="dx-graphics-hlsl-vector.md"><strong>vector HLSL type</strong></a>, surrounded by angle brackets. The default type is <strong>float4</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Name"></span><span id="name"></span><span id="NAME"></span><em>Name</em></p></td>
<td><p>An ASCII string that specifies the texture object name.</p></td>
</tr>
<tr class="even">
<td><p><span id="Samples"></span><span id="samples"></span><span id="SAMPLES"></span><em>Samples</em></p></td>
<td><p>The number of samples (ranges between 1 and 128).</p></td>
</tr>
</tbody>
</table>



 

## Example 1

Here is an example of declaring a texture object.


```
Texture2D <float4> MyTex;

Texture2DMS <float4, 128> MyMSTex;
```



## Texture Object Methods

Each texture object implements certain methods; here's the table that lists all of the methods. See the reference page for each method to see what objects can use that method.



| Texture Method                                                                     | Description                                                                                                       | vs\_4\_0 | vs\_4\_1  | ps\_4\_0 | ps\_4\_1  | gs\_4\_0 | gs\_4\_1  |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------|-----------|----------|-----------|----------|-----------|
| [CalculateLevelOfDetail](dx-graphics-hlsl-to-calculate-lod.md)                    | Calculate the LOD, return a clamped result.                                                                       |          |           |          | x         |          |           |
| [CalculateLevelOfDetailUnclamped](dx-graphics-hlsl-to-calculate-lod-unclamped.md) | Calculate the LOD, return an unclamped result.                                                                    |          |           |          | x         |          |           |
| [Gather](dx-graphics-hlsl-to-gather.md)                                           | Gets the four samples (red component only) that would be used for bilinear interpolation when sampling a texture. |          | x         |          | x         |          | x         |
| [GetDimensions](dx-graphics-hlsl-to-getdimensions.md)                             | Get the texture dimension for a specified mipmap level.                                                           | x        | x         | x        | x         | x        | x         |
| [GetDimensions (MultiSample)](dx-graphics-hlsl-to-getdimensions.md)               | Get the texture dimension for a specified mipmap level.                                                           |          | x         |          | x         |          | x         |
| [GetSamplePosition](dx-graphics-hlsl-to-get-sample-position.md)                   | Get the position of the specified sample.                                                                         |          | x         |          | x         |          | x         |
| [Load](dx-graphics-hlsl-to-load.md)                                               | Load data without any filtering or sampling.                                                                      | x        | x         | x        | x         | x        | x         |
| [Load (Multisample)](dx-graphics-hlsl-to-load.md)                                 | Load data without any filtering or sampling.                                                                      |          | x         | x        | x         |          | x         |
| [Sample](dx-graphics-hlsl-to-sample.md)                                           | Sample a texture.                                                                                                 |          |           | x        | x         |          |           |
| [SampleBias](dx-graphics-hlsl-to-samplebias.md)                                   | Sample a texture, after applying the bias value to the mipmap level.                                              |          |           | x        | x         |          |           |
| [SampleCmp](dx-graphics-hlsl-to-samplecmp.md)                                     | Sample a texture, using a comparison value to reject samples.                                                     |          |           | x        | x         |          |           |
| [SampleCmpLevelZero](dx-graphics-hlsl-to-samplecmplevelzero.md)                   | Sample a texture (mipmap level 0 only), using a comparison value to reject samples.                               | x        | x         | x        | x         | x        | x         |
| [SampleGrad](dx-graphics-hlsl-to-samplegrad.md)                                   | Sample a texture using a gradient to influence the way the sample location is calculated.                         | x        | x         | x        | x         | x        | x         |
| [SampleLevel](dx-graphics-hlsl-to-samplelevel.md)                                 | Sample a texture on the specified mipmap level.                                                                   | x        | x         | x        | x         | x        | x         |



 

### Return Type

The return type of a texture object method is float4 unless specified otherwise, with the exception of the multisampled anti-aliased texture objects that always need the type and sample count specified. The return type is the same as the texture resource type ([**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format)). In other words, it can be any of the following types.



| Type                       | Description                                                                                                                                                             |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| float                      | 32-bit float (see [Floating-Point Rules](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-resources-float-rules) for differences from IEEE float)                            |
| int                        | 32-bit signed integer                                                                                                                                                   |
| unsigned int               | 32-bit unsigned integer                                                                                                                                                 |
| snorm                      | 32-bit float in range -1 to 1 inclusive (see [Floating-Point Rules](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-resources-float-rules) for differences from IEEE float) |
| unorm                      | 32-bit float in range 0 to 1 inclusive (see [Floating-Point Rules](/windows/desktop/direct3d10/d3d10-graphics-programming-guide-resources-float-rules) for differences from IEEE float)  |
| any texture type or struct | The number of components returned must be between 1 and 3 inclusive.                                                                                                    |



 

In addition, the return type can be any texture type including a structure but, it must be less than 4 components such as a float1 type which returns one component.

## Default Values for Missing Components in a Texture

The default value for missing components in a texture resource type is zero for any component except the alpha component (A); the default value for the missing A is one. The way that this one appears to the shader depends on the texture resource type. It takes the form of the first typed component that is actually present in the texture resource type (starting from the left in RGBA order). If this form is UNORM or FLOAT, the default value for the missing A is 1.0f. If the form is SINT or UINT, the default value for the missing A is 0x1.

For example, when a shader reads the [**DXGI\_FORMAT\_R24\_UNORM\_X8\_TYPELESS**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) texture resource type, the default values for G and B are zero and the default value for A is 1.0f; when a shader reads the [**DXGI\_FORMAT\_R16G16\_UINT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) texture resource type, the default value for B is zero and the default value for A is 0x00000001; when a shader reads the [**DXGI\_FORMAT\_R16\_SINT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) texture resource type, the default values for G and B are zero and the default value for A is 0x00000001.

## Example 2

Here is an example of texture sampling using a texture method.


```
sampler MySamp;
Texture2D <float4> MyTex;
 
float4 main( float2 TexCoords[2] : TEXCOORD ) : SV_Target
{
    return MyTex.Sample( MySamp, TexCoords[0] ));
}
```



## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                        | Supported |
|---------------------------------------------------------------------|-----------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md) and higher shader models | yes       |



 

## See also

<dl> <dt>

[Shader Model 4](dx-graphics-hlsl-sm4.md)
</dt> </dl>

 

