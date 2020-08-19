---
title: Constant Integer Register (HLSL VS reference)
description: Constant integer registers are used only by loop - vs and rep - vs.
ms.assetid: da9916d4-655b-4c98-99a4-1abfa66459b5
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Constant Integer Register (HLSL VS reference)

Constant integer registers are used only by [loop - vs](loop---vs.md) and [rep - vs](rep---vs.md).

They can be set using [defi - vs](defi---vs.md) or [**SetVertexShaderConstantI**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshaderconstanti).

When used as an argument to the [loop - vs](loop---vs.md) instruction:

-   .x is the iteration count. ([rep - vs](rep---vs.md) uses only this component).
-   .y is the initial value for the loop counter.
-   .z is the increment step for the loop counter.

The behavior of shader constants has changed between Direct3D 8 and Direct3D 9.

-   For Direct3D 9, constants set with defx assign values to the shader constant space. The lifetime of a constant declared with defx is confined to the execution of that shader only. Conversely, constants set using the APIs SetXXXShaderConstantX initialize constants in global space. Constants in global space are not copied to local space (visible to the shader) until SetxxxShaderConstants is called.
-   For Direct3D 8, constants set with defx or the APIs both assign values to the shader constant space. Each time the shader is executed, the constants are used by the current shader regardless of the technique used to set them.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 