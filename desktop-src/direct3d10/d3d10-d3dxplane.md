---
description: Describes a plane.
ms.assetid: c6da7343-a4f3-4cac-855b-14bd70c0d3c2
title: D3DXPLANE structure (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPLANE
api_type: 
- HeaderDef
api_location: 
- D3DX10Math.h
---

# D3DXPLANE structure (D3DX10Math.h)

Describes a plane.

## Syntax


```C++
typedef struct D3DXPLANE {
  FLOAT a;
  FLOAT b;
  FLOAT c;
  FLOAT d;
} D3DXPLANE, *LPD3DXPLANE;
```



## Members

<dl> <dt>

**a**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

The a coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> <dt>

**b**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

The b coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> <dt>

**c**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

The c coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> <dt>

**d**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

The d coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> </dl>

## Remarks

The members of the **D3DXPLANE** structure take the form of the general plane equation. They fit into the general plane equation so that ax + by + cz + dw = 0.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](d3d10-graphics-reference-d3dx10-structures.md)
</dt> </dl>

 

 
