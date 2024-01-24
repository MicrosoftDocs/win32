---
description: Defines a volume.
ms.assetid: 415a96bc-1621-4691-b87a-98ca22f0bf07
title: D3DBOX structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DBOX
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DBOX structure

Defines a volume.

## Syntax


```C++
typedef struct D3DBOX {
  UINT Left;
  UINT Top;
  UINT Right;
  UINT Bottom;
  UINT Front;
  UINT Back;
} D3DBOX, *LPD3DBOX;
```



## Members

<dl> <dt>

**Left**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Position of the left side of the box on the x-axis.

</dd> <dt>

**Top**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Position of the top of the box on the y-axis.

</dd> <dt>

**Right**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Position of the right side of the box on the x-axis.

</dd> <dt>

**Bottom**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Position of the bottom of the box on the y-axis.

</dd> <dt>

**Front**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Position of the front of the box on the z-axis.

</dd> <dt>

**Back**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Position of the back of the box on the z-axis.

</dd> </dl>

## Remarks

**D3DBOX** includes the left, top, and front edges; however, the right, bottom, and back edges are not included. For example, a box that is 100 units wide and begins at 0 (thus, including the points up to and including 99) would be expressed with a value of 0 for the Left member and a value of 100 for the Right member. Note that a value of 99 is not used for the Right member.

The restrictions on side ordering observed for **D3DBOX** are left to right, top to bottom, and front to back.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
