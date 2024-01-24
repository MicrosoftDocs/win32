---
description: Describes an animation track and specifies blending weight, speed, and position for the track at a given time.
ms.assetid: f1469b6f-861f-4b7d-a187-933092a5d257
title: D3DXTRACK_DESC structure (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXTRACK_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXTRACK\_DESC structure

Describes an animation track and specifies blending weight, speed, and position for the track at a given time.

## Syntax


```C++
typedef struct D3DXTRACK_DESC {
  D3DXPRIORITY_TYPE Priority;
  FLOAT             Weight;
  FLOAT             Speed;
  DOUBLE            Position;
  BOOL              Enable;
} D3DXTRACK_DESC, *LPD3DXTRACK_DESC;
```



## Members

<dl> <dt>

**Priority**
</dt> <dd>

Type: **[**D3DXPRIORITY\_TYPE**](./d3dxpriority-type.md)**

</dd> <dd>

Priority type, as defined in [**D3DXPRIORITY\_TYPE**](./d3dxpriority-type.md).

</dd> <dt>

**Weight**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Weight value. The weight determines the proportion of this track to blend with other tracks.

</dd> <dt>

**Speed**
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

</dd> <dd>

Speed value. This is used similarly to a multiplier to scale the period of the track.

</dd> <dt>

**Position**
</dt> <dd>

Type: **[**DOUBLE**](../winprog/windows-data-types.md)**

</dd> <dd>

Time position of the track, in the local timeframe of its current animation set.

</dd> <dt>

**Enable**
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

</dd> <dd>

Track enable/disable. To enable, set to **TRUE**. To disable, set to **FALSE**.

</dd> </dl>

## Remarks

Tracks with the same priority are blended together, and the two resulting values are then blended using the priority blend factor. A track must have an animation set (stored separately) associated with it.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 
