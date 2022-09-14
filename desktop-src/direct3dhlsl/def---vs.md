---
title: def - vs
description: Defines vertex shader constants.
ms.assetid: 13274e16-990f-4de8-9c99-6c268c7c06ef
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# def - vs

Defines vertex shader constants.

## Syntax



| def dst, float1, float2, float3, float4 |
|-----------------------------------------|



 

where

-   dst is the destination register.
-   float1, float2, float3, float4 are four floating point numbers.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| def                    | x    | x    | x    | x     | x    | x     |



 

The def instruction defines a shader constant whose value is loaded anytime a shader is set to a device. These are called immediate constants. Immediate constants take precedence over constants set by API methods SetVertexShaderConstantF.

There are two ways to set a constant in a shader.

1.  Use def - vs to define the constant directly inside a shader.

    def - vs can only define floating-point constants.

2.  Use the API methods to set a constant.
    -   Use [**SetVertexShaderConstantF**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshaderconstantf) to set a floating-point constant.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> <dt>

[defi - vs](defi---vs.md)
</dt> <dt>

[defb - vs](defb---vs.md)
</dt> </dl>

 

 