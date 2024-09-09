---
title: Load (DirectX HLSL Texture Object)
description: Reads texel data without any filtering or sampling.
ms.assetid: a2fbda88-29c7-4d28-bd3e-df1d9aa36ee8
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Load (DirectX HLSL Texture Object)

Reads texel data without any filtering or sampling.



<table>
<tbody>
<tr class="odd">
<td>ret Object.Load(<dl> typeX Location,<br />
[typeX SampleIndex, ]<br />
[typeX Offset ]<br />
</dl>);</td>
</tr>
</tbody>
</table>

typeX denotes that there are four possible types: **int**, **int2**, **int3** or **int4**.

 

## Parameters

<dl> <dt>

<span id="Object"></span><span id="object"></span><span id="OBJECT"></span>*Object*
</dt> <dd>

A [texture-object](dx-graphics-hlsl-to-type.md) type (except TextureCube or TextureCubeArray).

</dd> <dt>

<span id="Location"></span><span id="location"></span><span id="LOCATION"></span>*Location*
</dt> <dd>

\[in\] The texture coordinates; the last component specifies the mipmap level. This method uses a 0-based coordinate system and not a 0.0-1.0 UV system. The argument type is dependent on the texture-object type.



| Object Type                                  | Parameter Type |
|----------------------------------------------|----------------|
| Buffer                                       | int            |
| Texture1D, Texture2DMS                       | int2           |
| Texture1DArray, Texture2D, Texture2DMSArray  | int3           |
| Texture2DArray, Texture3D                    | int4           |



 

For example, to access a 2D texture, supply integer texel coordinates for the first two components and a mipmap level for the third component.

> [!Note]  
> When one or more of the coordinates in *Location* exceed the u, v, or w mipmap level dimensions of the texture, **Load** returns zero in all components. Direct3D guarantees to return zero for any resource that is accessed out of bounds.

 

</dd> <dt>

<span id="SampleIndex"></span><span id="sampleindex"></span><span id="SAMPLEINDEX"></span>*SampleIndex*
</dt> <dd>

\[in\] A sampling index. Required for multi-sample textures. Not supported for other textures.



| Texture Type                                                                                                   | Parameter Type |
|----------------------------------------------------------------------------------------------------------------|----------------|
| Texture1D, Texture1DArray, Texture2D, Texture2DArray, Texture3D, Texture2DArray, TextureCube, TextureCubeArray | not supported  |
| Texture2DMS, Texture2DMSArray¹                                                                                 | int            |

</dd> <dt>

<span id="Offset"></span><span id="offset"></span><span id="OFFSET"></span>*Offset*
</dt> <dd>

\[in\] An optional offset applied to the texture coordinates before sampling. The offset type is dependent on the texture-object type, and needs to be static.



| Texture Type                                             | Parameter Type |
|----------------------------------------------------------|----------------|
| Texture1D, Texture1DArray                                | int            |
| Texture2D, Texture2DArray, Texture2DMS, Texture2DMSArray | int2           |
| Texture3D                                                | int3           |



 

> [!Note]  
> *SampleIndex* must always be specified first with multi-sample textures.

 

</dd> </dl>

## Return Value

The return type matches the type in the *Object* declaration. For example, a Texture2D object that was declared as "Texture2d&lt;uint4&gt; myTexture;" has a return value of type **uint4**.

## Minimum Shader Model

This function is supported in the following shader models.



| vs\_4\_0 | vs\_4\_1¹ | ps\_4\_0 | ps\_4\_1¹ | gs\_4\_0 | gs\_4\_1¹ |
|----------|-----------|----------|-----------|----------|-----------|
| x        | x         | x        | x         | x        | x         |



 

-   Shader Model 4.1 is available in Direct3D 10.1 or higher.

## Example

This partial code example is from the Paint.fx file in the [AdvancedParticles Sample](https://msdn.microsoft.com/library/Ee416394(v=VS.85).aspx).


```
// Object Declarations
Buffer<float4> g_ParticleBuffer;

// Shader body calling the intrinsic function
float4 PSPaint(PSQuadIn input) : SV_Target
{       
    ... 
    for( int i=g_ParticleStart; i<g_NumParticles; i+=g_ParticleStep )
    {
        ... 
        // load the particle
        float4 particlePos = g_ParticleBuffer.Load( i*4 );
        float4 particleColor = g_ParticleBuffer.Load( (i*4) + 2 );
        ...     
    }
    ...
}   
```



## Related topics

<dl> <dt>

[Texture-Object](dx-graphics-hlsl-to-type.md)
</dt> </dl>

 

 




