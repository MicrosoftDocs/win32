---
title: SampleCmp (DirectX HLSL Texture Object)
description: Samples a texture and compares a single component against the specified comparison value.
ms.assetid: e21894c4-e8c5-4c3d-92c1-727964f8fd94
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# SampleCmp (DirectX HLSL Texture Object)

Samples a texture and compares a single component against the specified comparison value.

<table>
<tbody>
<tr class="odd">
<td>float Object.SampleCmp( <dl> SamplerComparisonState S,<br />
float Location,<br />
float CompareValue,<br />
[int Offset]<br />
</dl>);</td>
</tr>
</tbody>
</table>
 

The comparison is a single-component comparison between the first component stored in the texture, and the comparison value passed into the method.

This method can be invoked only from a pixel shader; it isn't supported in a vertex or geometry shader.

## Parameters

<dl> <dt>

<span id="Object"></span><span id="object"></span><span id="OBJECT"></span>*Object*
</dt> <dd>

Any [texture-object](dx-graphics-hlsl-to-type.md) type (except Texture2DMS, Texture2DMSArray, or Texture3D).

</dd> <dt>

<span id="S"></span><span id="s"></span>*S*
</dt> <dd>

\[in\] A sampler-comparison state, which is the sampler state plus a comparison state (a comparison function and a comparison filter). See the [sampler type](dx-graphics-hlsl-sampler.md) for details and an example.

</dd> <dt>

<span id="Location"></span><span id="location"></span><span id="LOCATION"></span>*Location*
</dt> <dd>

\[in\] The texture coordinates. The argument type is dependent on the texture-object type.

| Texture-Object Type          | Parameter Type |
|------------------------------|----------------|
| Texture1D                    | float          |
| Texture1DArray, Texture2D    | float2         |
| Texture2DArray¹, TextureCube | float3         |
| TextureCubeArray¹            | float4         |

</dd> <dt>

<span id="CompareValue"></span><span id="comparevalue"></span><span id="COMPAREVALUE"></span>*CompareValue*
</dt> <dd>

A floating-point value to use as a comparison value.

</dd> <dt>

<span id="Offset"></span><span id="offset"></span><span id="OFFSET"></span>*Offset*
</dt> <dd>

\[in\] An optional texture coordinate offset, which can be used for any texture-object type; the offset is applied to the location before sampling. The texture offsets need to be static. The argument type is dependent on the texture-object type. For more info, see [Applying texture coordinate offsets](dx-graphics-hlsl-to-sample.md).

| Texture-Object Type            | Parameter Type |
|--------------------------------|----------------|
| Texture1D, Texture1DArray      | int            |
| Texture2D, Texture2DArray¹     | int2           |
| TextureCube, TextureCubeArray¹ | Not supported  |

</dd> </dl>

## Return Value

Returns a floating-point value in the range \[0..1\].

For each texel fetched (based on the sampler configuration of the filter mode), **SampleCmp** performs a comparison of the z value (3rd component of input) from the shader against the texel value (1 if the comparison passes; otherwise 0). **SampleCmp** then blends these 0 and 1 results for each texel together as in normal texture filtering (not an average) and returns the resulting \[0..1\] value to the shader.

## Remarks

Comparison filtering provides a basic filtering operation that is useful for percentage-closer-depth filtering.

When using this method on a floating-point resource (Instead of a signed-normalized or unsigned-normalized format), the comparison value is not automatically clamped between 0.0 and 1.0. Therefore, a manual clamp of the comparison value may be necessary for common shadowing techniques.

Use an offset only at an integer miplevel; otherwise, you may get different results depending on hardware implementation or driver settings.

## Minimum Shader Model

This function is supported in the following shader models.

| vs\_4\_0 | vs\_4\_1² | ps\_4\_0 | ps\_4\_1² | gs\_4\_0 | gs\_4\_1² |
|----------|-----------|----------|-----------|----------|-----------|
|          |           | x¹       | x         |          |           |

1.  Texture2DArray and TextureCubeArray are available in Shader Model 4.1 or higher.
2.  Shader Model 4.1 is available in Direct3D 10.1 or higher.

> [!NOTE]  
> **SampleCmp** is also available in ps 4\_0\_level\_9\_1 and 4\_0\_level\_9\_3 when you use the techniques that are described in [Implementing shadow buffers for Direct3D feature level 9](/previous-versions/windows/apps/jj262110(v=win.10)).

## Related topics

[Texture-Object](dx-graphics-hlsl-to-type.md)
