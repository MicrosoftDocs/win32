---
title: defi - vs
description: Defines an integer constant value, which should be loaded anytime a shader is set to a device.
ms.assetid: d6067a7d-58fb-4553-a42f-192c29bf78b7
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# defi - vs

Defines an integer constant value, which should be loaded anytime a shader is set to a device.

## Syntax



| defi dst, integerValue0, integerValue1, integerValue2, integerValue3 |
|----------------------------------------------------------------------|



 

-   dst is the destination register.
-   integerValue\# is a constant integer value.

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| defi                   |      | x    | x    | x     | x    | x     |



 

The defi instruction defines an integer shader constant whose value is loaded anytime a shader is set to a device. These are called immediate constants. Immediate constants take precedence over constants set by the API method SetVertexShaderConstantI.

There are two ways to set an integer constant in a shader.

1.  Use defi to define the integer constant vector directly inside a shader.
2.  Use the API methods to set a constant.
    -   Use [**SetVertexShaderConstantI**](/windows/desktop/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshaderconstanti) to set an integer constant.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> <dt>

[def - vs](def---vs.md)
</dt> <dt>

[defb - vs](defb---vs.md)
</dt> </dl>

 

 