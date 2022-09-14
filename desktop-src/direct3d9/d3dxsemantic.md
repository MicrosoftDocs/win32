---
description: Semantics map a parameter to vertex or pixel shader registers. They can also be optional descriptive strings attached to non-register parameters.
ms.assetid: 547a6ff3-be24-4299-9119-6719ad09b4ef
title: D3DXSEMANTIC structure (D3dx9shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSEMANTIC
api_type: 
- HeaderDef
api_location: 
- d3dx9shader.h
---

# D3DXSEMANTIC structure

Semantics map a parameter to vertex or pixel shader registers. They can also be optional descriptive strings attached to non-register parameters.

## Syntax


```C++
typedef struct D3DXSEMANTIC {
  UINT Usage;
  UINT UsageIndex;
} D3DXSEMANTIC, *LPD3DXSEMANTIC;
```



## Members

<dl> <dt>

**Usage**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Options that identify how resources are used. See [**D3DDECLUSAGE**](./d3ddeclusage.md).

</dd> <dt>

**UsageIndex**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Options that modify how the usage is interpreted. The usage and usage index make up a vertex declaration. See [Vertex Declaration (Direct3D 9)](vertex-declaration.md).

</dd> </dl>

## Remarks

Semantics are required for vertex and pixel shader, input and output registers.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[Effect Structures](dx9-graphics-reference-effects-structures.md)
</dt> </dl>

 

 
