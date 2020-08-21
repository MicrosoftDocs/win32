---
title: defb - vs
description: Defines a Boolean constant value, which should be loaded anytime a shader is set to a device.
ms.assetid: 1db41115-14aa-462e-a7ee-c0a53fee97d8
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# defb - vs

Defines a Boolean constant value, which should be loaded anytime a shader is set to a device.

## Syntax



| defb dest, booleanValue |
|-------------------------|



 

where

-   dst is the destination register.
-   booleanValue is a boolean value, either True or False.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| defb                   |      | x    | x    | x     | x    | x     |



 

The defb - vs instruction defines a boolean shader constant whose value is loaded anytime a shader is set to a device. These are called immediate constants. Immediate constants take precedence over constants set by the API method SetVertexShaderConstantB.

There are two ways to set a boolean constant in a shader.

1.  Use defb - vs to define the constant directly inside a shader.
2.  Use the API methods to set a constant.
    -   Use [**SetVertexShaderConstantB**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshaderconstantb) to set a Boolean constant.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> <dt>

[def - vs](def---vs.md)
</dt> <dt>

[defi - vs](defi---vs.md)
</dt> </dl>

 

 