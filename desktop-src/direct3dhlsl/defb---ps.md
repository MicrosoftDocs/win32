---
title: defb - ps
description: Defines a boolean constant value, which should be loaded any time a shader is set to a device.
ms.assetid: bb0b87cb-08a4-4790-88da-e398cea62911
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# defb - ps

Defines a boolean constant value, which should be loaded any time a shader is set to a device.

## Syntax



| defb dest, booleanValue |
|-------------------------|



 

where

-   dst is the destination register.
-   booleanValue is a single boolean value, either true or false.

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| defb                  |      |      |      |      |      | x    | x     | x    | x     |



 

The defb instruction defines a boolean shader constant whose value is loaded anytime a shader is set to a device. These are called immediate constants. Immediate constants take precedence over constants set by the API method SetPixelShaderConstantB.

There are two ways to set a booleanconstant in a shader.

1.  Use defb to define the constant directly inside a shader.
2.  Use the API methods to set a constant.
    -   Use [**SetPixelShaderConstantB**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstantb) to set a Boolean constant.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> <dt>

[def - ps](def---ps.md)
</dt> <dt>

[defi - ps](defi---ps.md)
</dt> </dl>

 

 