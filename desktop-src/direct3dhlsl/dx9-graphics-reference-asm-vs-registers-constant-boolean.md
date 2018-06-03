---
title: Constant Boolean Register
description: This register is a collection of bits used in static flow control instructions (for example, if bool - vs - else - vs - endif - vs).
ms.assetid: bd02d03b-c228-481a-9c98-7442be4cdd07
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constant Boolean Register

This register is a collection of bits used in static flow control instructions (for example, [if bool - vs](if-bool---vs.md) - [else - vs](else---vs.md) - [endif - vs](endif---vs.md)). There are 16 of them, therefore, a shader can have 16 independent branch conditions. They can be set using [defb - vs](defb---vs.md) or [**SetVertexShaderConstantB**](https://msdn.microsoft.com/library/windows/desktop/bb174466).

The behavior of shader constants has changed between Direct3D 8 and Direct3D 9.

-   For Direct3D 9, constants set with defx assign values to the shader constant space. The lifetime of a constant declared with defx is confined to the execution of that shader only. Conversely, constants set using the APIs SetXXXShaderConstantX initialize constants in global space. Constants in global space are not copied to local space (visible to the shader) until SetxxxShaderConstants is called.
-   For Direct3D 8, constants set with defx or the APIs both assign values to the shader constant space. Each time the shader is executed, the constants are used by the current shader regardless of the technique used to set them.

## Related topics

<dl> <dt>

[Vertex Shader Registers](dx9-graphics-reference-asm-vs-registers.md)
</dt> </dl>

 

 




