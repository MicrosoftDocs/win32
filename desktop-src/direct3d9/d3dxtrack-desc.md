---
Description: Describes an animation track and specifies blending weight, speed, and position for the track at a given time.
ms.assetid: f1469b6f-861f-4b7d-a187-933092a5d257
title: D3DXTRACK\_DESC structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

Type: **[**D3DXPRIORITY\_TYPE**](https://msdn.microsoft.com/windows/desktop/7bd83e31-09c4-4376-a22d-ed8023b78e84)**

</dd> <dd>

Priority type, as defined in [**D3DXPRIORITY\_TYPE**](https://msdn.microsoft.com/windows/desktop/7bd83e31-09c4-4376-a22d-ed8023b78e84).

</dd> <dt>

**Weight**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Weight value. The weight determines the proportion of this track to blend with other tracks.

</dd> <dt>

**Speed**
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Speed value. This is used similarly to a multiplier to scale the period of the track.

</dd> <dt>

**Position**
</dt> <dd>

Type: **[**DOUBLE**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Time position of the track, in the local timeframe of its current animation set.

</dd> <dt>

**Enable**
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Track enable/disable. To enable, set to **TRUE**. To disable, set to **FALSE**.

</dd> </dl>

## Remarks

Tracks with the same priority are blended together, and the two resulting values are then blended using the priority blend factor. A track must have an animation set (stored separately) associated with it.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




