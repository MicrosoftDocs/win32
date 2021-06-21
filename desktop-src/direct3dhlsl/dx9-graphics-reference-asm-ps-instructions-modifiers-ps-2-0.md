---
title: Modifiers for ps_2_0 and Above
description: Instruction modifiers affect the result of the instruction before it is written into the destination register. Learn about modifiers for ps_2_0 and above.
ms.assetid: eb2a8a1f-51bc-4516-b679-a8fb25b0dda0
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Modifiers for ps\_2\_0 and Above

Instruction modifiers affect the result of the instruction before it is written into the destination register.

This section contains reference information for the instruction modifiers implemented by pixel shader version 2\_0 and above.



| Name                                     | Syntax     | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------------------------|------------|------|------|-------|------|-------|
| [Centroid](#centroid)                    | \_centroid | x    | x    | x     | x    | x     |
| [Partial\_Precision](#partial-precision) | \_pp       | x    | x    | x     | x    | x     |
| [Saturate](#saturate)                    | \_sat      | x    | x    | x     | x    | x     |



 

## Centroid

The centroid modifier is an optional modifier that clamps attribute interpolation within the range of the primitive when a multisample pixel center is not covered by the primitive. This can be seen in [Centroid Sampling](https://msdn.microsoft.com/library/ee415231(VS.85).aspx).

You can apply the centroid modifier to an assembly instruction as shown here:


```
dcl_texcoord0_centroid v0
```



You can also apply the centroid modifier to a semantic as shown here:


```
float4 TexturePointCentroidPS( float4 TexCoord : TEXCOORD0_centroid ) : COLOR0
{
    return tex2D( PointSampler, TexCoord );
}
```



In addition, any [Input Color Register](dx9-graphics-reference-asm-ps-registers-input-color.md) (v\#) declared with a color semantic will automatically have centroid applied. Gradients computed from attributes that are centroid sampled are not guaranteed to be accurate.

## Partial Precision

The partial precision instruction modifier (\_pp) indicates areas where partial precision is acceptable, provided that the underlying implementation supports it. Implementations are always free to ignore the modifier and perform the affected operations in full precision.

The \_pp modifier can occur in two contexts:

-   On a texture coordinate declaration to enable passing texture coordinates to the pixel shader in partial-precision form. This allows, for example, the use of texture coordinates to relay color data to the pixel shader, which may be faster with partial precision than with full precision in some implementations. In the absence of this modifier, texture coordinates must be passed in full precision.
-   On any instruction including texture load instructions. This indicates that the implementation is allowed to execute the instruction with partial precision and store a partial precision result. In the absence of an explicit modifier, the instruction must be performed at full precision (regardless of the input precision).

Examples:


```
dcl_texcoord0_pp t1
cmp_pp r0, r1, r2, r3
```



## Saturate

The saturate instruction modifier (\_sat) saturates (or clamps) the instruction result to the range \[0, 1\] before writing to the destination register.

The \_sat instruction modifier can be used with any instruction except [frc - ps](frc---ps.md), [sincos - ps](sincos---ps.md), and any tex\* instructions.

For ps\_2\_0, ps\_2\_x, and ps\_2\_sw, the \_sat instruction modifier cannot be used with instructions writing to any output registers ([Output Color Register](dx9-graphics-reference-asm-ps-registers-output-color.md) or [Output Depth Register](dx9-graphics-reference-asm-ps-registers-output-depth.md)). This restriction does not apply to ps\_3\_0 and above.

Example:


```
dp3_sat r0, v0, c1
```



## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 




