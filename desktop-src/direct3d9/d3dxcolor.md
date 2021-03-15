---
description: Describes color values.
ms.assetid: 53d3176a-f727-498e-8bea-0e30e0a1c66e
title: D3DXCOLOR structure (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCOLOR
api_type: 
- HeaderDef
api_location: 
- d3dx9math.h
---

# D3DXCOLOR structure (D3dx9math.h)

Describes color values.

## Syntax


```C++
typedef struct D3DXCOLOR {
  FLOAT r;
  FLOAT g;
  FLOAT b;
  FLOAT a;
} D3DXCOLOR, *LPD3DXCOLOR;
```



## Members

<dl> <dt>

**r**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Red component of the color.

</dd> <dt>

**g**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Green component of the color.

</dd> <dt>

**b**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Blue component of the color.

</dd> <dt>

**a**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Alpha component of the color.

</dd> </dl>

## Remarks

C++ programmers can take advantage of operator overloading and type casting with the [**D3DXCOLOR Extensions**](d3dxcolor-extensions.md), which implement overloaded constructors, as well as assignment, unary, and binary (including equality) operators.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 
