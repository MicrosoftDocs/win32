---
title: texldl - vs
description: Sample a texture with a particular sampler. The particular mipmap level-of-detail being sampled has to be specified as the fourth component of the texture coordinate. | texldl - vs
ms.assetid: 774c058d-7b3e-46a9-adce-c9a44efefd78
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# texldl - vs

Sample a texture with a particular sampler. The particular mipmap level-of-detail being sampled has to be specified as the fourth component of the texture coordinate.

## Syntax



| texldl dst, src0, src1 |
|------------------------|



 

Where:

-   dst is a destination register.
-   src0 is a source register that provides the texture coordinates for the texture sample.
-   src1 identifies the source sampler register (s\#), where \# specifies which texture sampler number to sample. The sampler has associated with it a texture and a control state defined by the [**D3DSAMPLERSTATETYPE**](/windows/desktop/direct3d9/d3dsamplerstatetype) enumeration (for example, D3DSAMP\_MINFILTER).

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| texldl                 |      |      |      |       | x    | x     |



 

texldl looks up the texture set at the sampler stage referenced by src1. The level-of-detail is selected from src0.w. This value can be negative, in which case the level-of-detail selected is the "zeroth one" (biggest map) with the MAGFILTER. Because src0.w is a floating point value, the fractional value is used to interpolate (if MIPFILTER is LINEAR) between two mip levels. Sampler states MIPMAPLODBIAS and MAXMIPLEVEL are honored. For more information about sampler states, see [**D3DSAMPLERSTATETYPE**](/windows/desktop/direct3d9/d3dsamplerstatetype).

If a shader program samples from a sampler that does not have a texture set, 0001 is obtained in the destination register.

This is an approximation to the reference device algorithm.


```
LOD = src0.w + LODBIAS;
if (LOD <= 0 )
{
   LOD = 0;
   Filter = MagFilter;
   tex = Lookup( MAX(MAXMIPLEVEL, LOD), Filter );
}
else
{
   Filter = MinFilter;
   LOD = MAX( MAXMIPLEVEL, LOD);
   tex = Lookup( Floor(LOD), Filter );
   if( MipFilter == LINEAR )
   {
      tex1 = Lookup( Ceil(LOD), Filter );                        
      tex = (1 - frac(src0.w))*tex + frac(src0.w)*tex1;
   }
}
```



Restrictions:

-   The texture coordinates should not be scaled by texture size.
-   dst must be a [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md) (r\#).
-   dst can accept a write mask. See [Destination Register Masking](dx9-graphics-reference-asm-vs-registers-modifiers-masking.md).
-   Defaults for missing components are either 0 or 1, and depend on the texture format.
-   src1 must be a [Sampler (Direct3D 9 asm-vs)](dx9-graphics-reference-asm-vs-registers-sampler.md) (s\#). src1 may not use a negate modifier. src1 may use swizzle, which is applied after sampling before the write mask is honored. The sampler must have been declared (using [dcl\_samplerType (sm3 - vs asm)](dcl-samplertype---vs.md)) at the beginning of the shader.
-   The number of coordinates required to perform the texture sample depends on how the sampler was declared. If it was declared as a cube, a three-component texture coordinate is required (.rgb). Validation enforces that coordinates provided to texldl Are sufficient for the texture dimension declared for the sampler. However, it is not guaranteed that the application actually set a texture (through the API) with dimensions equal to the dimension declared for the sampler. In such a case, the runtime will attempt to detect mismatches (possibly in debug only). Sampling a texture with fewer dimensions than are present in the texture coordinate will be allowed, and will be assumed to ignore the extra texture coordinate components. Conversely, sampling a texture with more dimensions than are present in the texture coordinate is not allowed.
-   If the src0 (texture coordinate) is a [Temporary Register](dx9-graphics-reference-asm-vs-registers-temporary.md) (r\#), the components required for the lookup (described above) must have been previously written.
-   Sampling unsigned RGB textures will result in float values between 0.0 and 1.0.
-   Sampling signed textures will result in float values between -1.0 to 1.0.
-   When sampling floating point textures, Float16 means that the data will range within MAX\_FLOAT16. Float32 means the maximum range of the pipeline will be used. Sampling outside of either range is undefined.
-   There is no dependent read limit.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 
