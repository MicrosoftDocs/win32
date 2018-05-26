---
Description: Describes a plane.
ms.assetid: ffca4650-9788-4559-8f6b-a4e5db29ce55
title: D3DXPLANE structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXPLANE structure

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

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The a coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> <dt>

**b**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The b coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> <dt>

**c**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The c coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> <dt>

**d**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

The d coefficient of the clipping plane in the general plane equation. See Remarks.

</dd> </dl>

## Remarks

The members of the **D3DXPLANE** structure take the form of the general plane equation. They fit into the general plane equation so that **a**x + **b**y + **c**z + **d**w = 0.

C++ programmers can take advantage of operator overloading and type casting with the [**D3DXPLANE Extensions**](d3dxplane-extensions.md) which implement overloaded constructors and assignment, unary, and binary (including equality) operators.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9math.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




