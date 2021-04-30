---
title: dcl_usage input (sm1, sm2, sm3 - vs asm)
description: Declare the association between a vertex element usage and a usage index for a vertex shader input register.
ms.assetid: e0360f4d-1250-4dc5-b790-372b303a37a8
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# dcl\_usage input (sm1, sm2, sm3 - vs asm)

Declare the association between a vertex element usage and a usage index for a vertex shader input register.

## Syntax



|                                |
|--------------------------------|
| dcl\_usage\[usage\_index\] v\# |



 

Where:

-   dcl\_usage identifies how the register data will be used. This is the same value as the members of [**D3DDECLUSAGE**](/windows/desktop/direct3d9/d3ddeclusage) without the D3DDECLUSAGE prefix.
-   usage\_index is an optional integer index between 0 and 15. It modifies the usage data. The index matches the usage index in a vertex declaration. See [Vertex Declaration (Direct3D 9)](/windows/desktop/direct3d9/vertex-declaration). The index is appended to the usage value (dcl\_usage ) with no space. If it is not supplied, it is assumed to be 0.
-   v\# is a [Input Register](dx9-graphics-reference-asm-vs-registers-input.md).

## Remarks



| Vertex shader versions | 1\_1 | 2\_0 | 2\_x | 2\_sw | 3\_0 | 3\_sw |
|------------------------|------|------|------|-------|------|-------|
| dcl\_usage             | x    | x    | x    | x     | x    | x     |



 

All dcl\_usage instructions must appear before the first executable instruction.

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 
