---
title: CalculateLevelOfDetail (DirectX HLSL Texture Object)
description: Calculates the level of detail.
ms.assetid: 7c7c3754-45a9-49c6-8420-aac22f776b15
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# CalculateLevelOfDetail (DirectX HLSL Texture Object)

Calculates the level of detail.

ret Object.CalculateLevelOfDetail( sampler\_state S, float x );



 

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
<td>[in] A <a href="/windows/desktop/direct3d10/d3d10-effect-sampler-syntax">Sampler state</a>. This is an object declared in an effect file that contains state assignments.<br/></td>
</tr>
<tr class="odd">
<td><span id="x"></span><span id="X"></span><em>x</em><br/></td>
<td>[in] The linear interpolation value or values, which is a floating-point number between 0.0 and 1.0 inclusive. The number of components is dependent on the texture-object type. <br/> 
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
<td>float1</td>
</tr>
<tr class="even">
<td>Texture2D, Texture2DArray</td>
<td>float2</td>
</tr>
<tr class="odd">
<td>Texture3D, TextureCube, TextureCubeArray </td>
<td>float3</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

## Return Value

Returns the calculated LOD, a single floating-point value.

## Minimum Shader Model

This function is supported in the following shader models.



| vs\_4\_0 | vs\_4\_1  | ps\_4\_0 | ps\_4\_1  | gs\_4\_0 | gs\_4\_1  |
|----------|-----------|----------|-----------|----------|-----------|
|          |           |          | x         |          |           |



 

1.  TextureCubeArray is available in Shader Model 4.1 or higher.
2.  Shader Model 4.1 is available in Direct3D 10.1 or higher.

## Related topics

<dl> <dt>

[Texture-Object](dx-graphics-hlsl-to-type.md)
</dt> </dl>

 

