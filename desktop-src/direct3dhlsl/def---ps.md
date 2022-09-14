---
title: def - ps
description: Defines pixel shader floating-point constants.
ms.assetid: 679b3074-73f3-48de-8c7a-f43bff76b25a
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# def - ps

Defines pixel shader floating-point constants.

## Syntax



| def dst, fVvalue1, fValue2, fValue3, fValue4 |
|----------------------------------------------|



 

Where:

-   dst is the destination register.
-   fValue1 to fValue4 are floating-point values..

## Remarks



| Pixel shader versions | 1\_1 | 1\_2 | 1\_3 | 1\_4 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|-----------------------|------|------|------|------|------|------|-------|------|-------|
| def                   | x    | x    | x    | x    | x    | x    | x     | x    | x     |



 

There are two ways to set a floating-point constant in a pixel shader.

1.  Use def to define the constant directly inside a shader.
2.  Use the API to set a constant with [**SetPixelShaderConstantF**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setpixelshaderconstantf).

def defines a shader constant whose value is loaded any time a shader is set to a device. These are called immediate constants. Immediate constants take precedence over constants set by the API method.

-   Must appear before the first arithmetic or addressing instruction in shader.
-   Can be intermixed with [dcl - (sm2, sm3 - ps asm)](dcl---ps.md) instructions (which are the other type of instruction that resides at the beginning of a shader).
-   dst register must be a [constant register](dx9-graphics-reference-asm-ps-registers-ps-1-x.md).
-   Write mask must be full (default).
-   If a [constant register](dx9-graphics-reference-asm-ps-registers-ps-1-x.md) is defined multiple times in a shader, the last one persists.

## Related topics

<dl> <dt>

[Pixel Shader Instructions](dx9-graphics-reference-asm-ps-instructions.md)
</dt> </dl>

 

 