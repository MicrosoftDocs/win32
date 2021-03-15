---
description: Defines a rectangle.
ms.assetid: a8590411-fd34-4048-a41f-b4155d955573
title: D3DRECT structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DRECT
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DRECT structure

Defines a rectangle.

## Syntax


```C++
typedef struct D3DRECT {
  LONG x1;
  LONG y1;
  LONG x2;
  LONG y2;
} D3DRECT;
```



## Members

<dl> <dt>

**x1**
</dt> <dd>

Type: **[**LONG**](../winprog/windows-data-types.md)**

</dd> <dd>

The x-coordinate of the upper-left corner of the rectangle.

</dd> <dt>

**y1**
</dt> <dd>

Type: **[**LONG**](../winprog/windows-data-types.md)**

</dd> <dd>

The y-coordinate of the upper-left corner of the rectangle.

</dd> <dt>

**x2**
</dt> <dd>

Type: **[**LONG**](../winprog/windows-data-types.md)**

</dd> <dd>

The x-coordinate of the lower-right corner of the rectangle.

</dd> <dt>

**y2**
</dt> <dd>

Type: **[**LONG**](../winprog/windows-data-types.md)**

</dd> <dd>

The y-coordinate of the lower-right corner of the rectangle.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**Clear**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-clear)
</dt> </dl>

 

 
