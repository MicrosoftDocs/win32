---
title: SampleGrad (DirectX HLSL Texture Object)
description: Samples a texture using a gradient to influence the way the sample location is calculated. | SampleGrad (DirectX HLSL Texture Object)
ms.assetid: f3d73296-23c4-4178-b89e-6f84cfcb48a5
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# SampleGrad (DirectX HLSL Texture Object)

Samples a texture using a gradient to influence the way the sample location is calculated.

&lt;Template Type&gt; Object.SampleGrad( sampler\_state S, float Location, float DDX, float DDY \[, int Offset\] );



 

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
<td>Any <a href="dx-graphics-hlsl-to-type.md">texture-object</a> type (except Texture2DMS and Texture2DMSArray).<br/></td>
</tr>
<tr class="even">
<td><span id="S"></span><span id="s"></span><em>S</em><br/></td>
<td>[in] A <a href="dx-graphics-hlsl-sampler.md">Sampler state</a>. This is an object declared in an effect file that contains state assignments.<br/></td>
</tr>
<tr class="odd">
<td><span id="Location"></span><span id="location"></span><span id="LOCATION"></span><em>Location</em><br/></td>
<td>[in] The Texture coordinates. The argument type is dependent on the texture-object type. <br/> 
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
<tr class="odd">
<td>Texture2DMS, Texture2DMSArray</td>
<td>not supported</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td><p><span id="DDX"></span><span id="ddx"></span><em>DDX</em></p></td>
<td><p>[in] The rate of change of the surface geometry in the x direction. The argument type is dependent on the texture-object type.</p>

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
<td>float</td>
</tr>
<tr class="even">
<td>Texture2D, Texture2DArray</td>
<td>float2</td>
</tr>
<tr class="odd">
<td>Texture3D, TextureCube, TextureCubeArray </td>
<td>float3</td>
</tr>
<tr class="even">
<td>Texture2DMS, Texture2DMSArray</td>
<td>not supported</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td><p><span id="DDY"></span><span id="ddy"></span><em>DDY</em></p></td>
<td><p>[in] The rate of change of the surface geometry in the y direction. The argument type is dependent on the texture-object type.</p>

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
<td>float</td>
</tr>
<tr class="even">
<td>Texture2D, Texture2DArray</td>
<td>float2</td>
</tr>
<tr class="odd">
<td>Texture3D, TextureCube, TextureCubeArray </td>
<td>float3</td>
</tr>
<tr class="even">
<td>Texture2DMS, Texture2DMSArray</td>
<td>not supported</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td><p><span id="Offset"></span><span id="offset"></span><span id="OFFSET"></span><em>Offset</em></p></td>
<td><p>[in] An optional texture coordinate offset, which can be used for any texture-object types. The offset is applied to the location before sampling. Use an offset only at an integer miplevel; otherwise, you may get results that do not translate well to hardware. The argument type is dependent on the texture-object type. For more info, see<a href="dx-graphics-hlsl-to-sample.md">Applying Integer Offsets</a>.</p>

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
<tr class="odd">
<td>Texture2DMS, Texture2DMSArray</td>
<td>not supported</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

## Return Value

The texture's template type, which may be a single- or multi-component vector. The format is based on the texture's [**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format).

## Minimum Shader Model

This function is supported in the following shader models.



| vs\_4\_0 | vs\_4\_1  | ps\_4\_0 | ps\_4\_1  | gs\_4\_0 | gs\_4\_1  |
|----------|-----------|----------|-----------|----------|-----------|
| x        | x         | x        | x         | x        | x         |



 

1.  TextureCubeArray is available in Shader Model 4.1 or higher.
2.  Shader Model 4.1 is available in Direct3D 10.1 or higher.

## Example

This partial code example is from the MotionBlur.fx file in the [MotionBlur10 Sample](https://msdn.microsoft.com/library/Ee416417(v=VS.85).aspx).


```
// Object Declarations
Texture2D g_txDiffuse;

SamplerState g_samLinear
{
    Filter = ANISOTROPIC;
    MaxAnisotropy = 8;
    AddressU = Wrap;
    AddressV = Wrap;
};

struct VSSceneOut
{
    float4 Pos : SV_POSITION;
    float4 Color : COLOR0;
    float2 Tex : TEXCOORD;
    float2 Aniso : ANISOTROPY;
};

float4 PSSceneMain( VSSceneOut Input ) : SV_TARGET
{
    float2 ddx = Input.Aniso;
    float2 ddy = Input.Aniso;
    
    // Shader body calling the intrinsic function
    float4 diff = g_txDiffuse.SampleGrad( g_samLinear, Input.Tex, ddx, ddy);
    
    ...
}
```



## Related topics

<dl> <dt>

[Texture-Object](dx-graphics-hlsl-to-type.md)
</dt> </dl>

 

