---
description: A 4x4 row-major matrix.
ms.assetid: 2253f486-7bb6-4966-b3ec-dba47e53e372
title: D3DMATRIX structure (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DMATRIX
api_type: 
- HeaderDef
api_location: 
- D3DX10Math.h
---

# D3DMATRIX structure

A 4x4 row-major matrix.

## Syntax


```C++
typedef struct D3DMATRIX {
  float m[4][4];
} D3DMATRIX, *LPD3DMATRIX;
```



## Members

<dl> <dt>

**m\[4\]\[4\]**
</dt> <dd>

Type: **float**

</dd> <dd>

The 4x4 row-major matrix.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](d3d10-graphics-reference-d3dx10-structures.md)
</dt> </dl>

 

 




