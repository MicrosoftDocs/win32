---
title: SampleLevel (DirectX HLSL Texture Object)
description: Samples a texture using a mipmap-level offset.
ms.assetid: d61426c8-e09f-4e88-99f6-fa96c4a2b58d
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# SampleLevel (DirectX HLSL Texture Object)

Samples a texture using a mipmap-level offset.

&lt;Template Type&gt; Object.SampleLevel( sampler\_state S, float Location, float LOD \[, int Offset\] );



 

This function is similar to [Sample](dx-graphics-hlsl-to-sample.md) except that it uses the LOD level (in the last component of the location parameter) to choose the mipmap level. For example, a 2D texture uses the first two components for uv coordinates and the third component for the mipmap level.

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

<p> </p>
<p>If the texture object is an array, the last component is the array index.</p></td>
</tr>
<tr class="even">
<td><p><span id="LOD"></span><span id="lod"></span><em>LOD</em></p></td>
<td><p>[in] A number that specifies the mipmap level. If the value is = 0, the zero'th (biggest map) is used. The fractional value (if supplied) is used to interpolate between two mipmap levels.</p></td>
</tr>
<tr class="odd">
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

This partial code example is from the Instancing.fx file in the [Instancing10 Sample](https://msdn.microsoft.com/library/Ee416415(v=VS.85).aspx).


```
// Object Declarations
Texture1D g_txRandom;

SamplerState g_samPoint
{
    Filter = MIN_MAG_MIP_POINT;
    AddressU = Wrap;
    AddressV = Wrap;
};

    
// Shader body calling the intrinsic function
float3 RandomDir(float fOffset)
{   
    float tCoord = (fOffset) / 300.0;
    return g_txRandom.SampleLevel( g_samPoint, tCoord, 0 );
   ...

```



## Related topics

<dl> <dt>

[Texture-Object](dx-graphics-hlsl-to-type.md)
</dt> </dl>

 

