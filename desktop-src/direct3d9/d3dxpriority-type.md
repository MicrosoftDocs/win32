---
description: Defines the priority type to which an animation track is assigned.
ms.assetid: 7bd83e31-09c4-4376-a22d-ed8023b78e84
title: D3DXPRIORITY_TYPE enumeration (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPRIORITY_TYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXPRIORITY\_TYPE enumeration

Defines the priority type to which an animation track is assigned.

## Syntax


```C++
typedef enum D3DXPRIORITY_TYPE { 
  D3DXPRIORITY_LOW          = 0,
  D3DXPRIORITY_HIGH         = 1,
  D3DXPRIORITY_FORCE_DWORD  = 0x7fffffff
} D3DXPRIORITY_TYPE, *LPD3DXPRIORITY_TYPE;
```



## Constants

<dl> <dt>

<span id="D3DXPRIORITY_LOW"></span><span id="d3dxpriority_low"></span>**D3DXPRIORITY\_LOW**
</dt> <dd>

Track should be blended with all the low-priority tracks before the low-priority blend is mixed with the high-priority blend.

</dd> <dt>

<span id="D3DXPRIORITY_HIGH"></span><span id="d3dxpriority_high"></span>**D3DXPRIORITY\_HIGH**
</dt> <dd>

Track should be blended with all the high-priority tracks before the high-priority blend is mixed with the low-priority blend.

</dd> <dt>

<span id="D3DXPRIORITY_FORCE_DWORD"></span><span id="d3dxpriority_force_dword"></span>**D3DXPRIORITY\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Tracks with the same priority are blended together, and the two resulting values are then blended using the priority blend factor.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




