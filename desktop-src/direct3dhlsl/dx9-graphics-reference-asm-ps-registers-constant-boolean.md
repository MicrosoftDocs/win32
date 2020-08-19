---
title: Constant Boolean register (HLSL PS reference)
description: This register is a collection of bits used in static flow control instructions (for example, if bool - ps - else - ps - endif - ps).
ms.assetid: fb4abe19-d0cf-48ac-866e-4be60cc86bd6
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Constant Boolean register (HLSL PS reference)

This register is a collection of bits used in static flow control instructions (for example, [if bool - ps](if-bool---ps.md) - [else - ps](else---ps.md) - [endif - ps](endif---ps.md)). There are 16 of them, therefore, a shader can have 16 independent branch conditions. They can be set using [defb - ps](defb---ps.md) or [**SetPixelShaderConstantB**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstantb).

The behavior of shader constants has changed between Direct3D 8 and Direct3D 9.

-   For Direct3D 9, constants set with defx assign values to the shader constant space. The lifetime of a constant declared with defx is confined to the execution of that shader only. Conversely, constants set using the APIs SetXXXShaderConstantX initialize constants in global space. Constants in global space are not copied to local space (visible to the shader) until SetxxxShaderConstants is called.
-   For Direct3D 8, constants set with defx or the APIs both assign values to the shader constant space. Each time the shader is executed, the constants are used by the current shader regardless of the technique used to set them.



| Pixel shader versions     | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_sw | 2\_x | 3\_0 | 3\_sw |
|---------------------------|------|------|------|------|------|-------|------|------|-------|
| Constant Boolean register |      |      |      |      |      |       | x    | x    | x     |



 

## Related topics

<dl> <dt>

[Registers](dx9-graphics-reference-asm-ps-registers.md)
</dt> </dl>

 

 