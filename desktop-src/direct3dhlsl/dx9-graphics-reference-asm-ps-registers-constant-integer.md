---
title: Constant integer register (HLSL PS reference)
description: Constant integer registers are used only by loop - ps and rep - ps.
ms.assetid: 85720ec0-b6aa-4a24-910c-3ad0468300dc
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Constant integer register (HLSL PS reference)

Constant integer registers are used only by [loop - ps](loop---ps.md) and [rep - ps](rep---ps.md).

They can be set using [defi - ps](defi---ps.md) or [**SetPixelShaderConstantI**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstanti).

When used as an argument to the [loop - ps](loop---ps.md) instruction:

-   .x is the iteration count. ([rep - ps](rep---ps.md) uses only this component).
-   .y is the initial value for the loop counter.
-   .z is the increment step for the loop counter.



| Pixel shader versions     | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|---------------------------|------|------|------|------|------|-------|------|------|-------|
| Constant Integer Register |      |      |      |      |      |       | x    | x    | x     |



 

The behavior of shader constants has changed between Direct3D 8 and Direct3D 9.

-   For Direct3D 9, constants set with defx assign values to the shader constant space. The lifetime of a constant declared with defx is confined to the execution of that shader only. Conversely, constants set using the APIs SetXXXShaderConstantX initialize constants in global space. Constants in global space are not copied to local space (visible to the shader) until SetxxxShaderConstants is called.
-   For Direct3D 8, constants set with defx or the APIs both assign values to the shader constant space. Each time the shader is executed, the constants are used by the current shader regardless of the technique used to set them.

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 