---
Description: Describes a 16-bit floating point vector.
ms.assetid: f823a327-f07a-44e9-b58a-7865e11e80eb
title: D3DXFLOAT16 structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXFLOAT16 structure

Describes a 16-bit floating point vector.

## Syntax


```C++
typedef struct D3DXFLOAT16 {
  WORD Value;
} D3DXFLOAT16, *LPD3DXFLOAT16;
```



## Members

<dl> <dt>

**Value**
</dt> <dd>

Type: **[**WORD**](winprog.windows_data_types)**

</dd> <dd>

The 16-bit data.

</dd> </dl>

## Remarks

C++ programmers can take advantage of operator overloading and type casting with the [**D3DXFLOAT16 Extensions**](d3dxfloat16-extensions.md), which implement overloaded constructors and assignment, unary, and binary (including equality) operators.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




