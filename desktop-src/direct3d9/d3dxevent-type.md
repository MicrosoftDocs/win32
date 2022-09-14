---
description: Describes the type of events that can be keyed by the animation controller.
ms.assetid: d98b398e-29e1-41b5-84eb-37983bac8d0a
title: D3DXEVENT_TYPE enumeration (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXEVENT_TYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXEVENT\_TYPE enumeration

Describes the type of events that can be keyed by the animation controller.

## Syntax


```C++
typedef enum D3DXEVENT_TYPE { 
  D3DXEVENT_TRACKSPEED     = 0,
  D3DXEVENT_TRACKWEIGHT    = 1,
  D3DXEVENT_TRACKPOSITION  = 2,
  D3DXEVENT_TRACKENABLE    = 3,
  D3DXEVENT_PRIORITYBLEND  = 4,
  D3DXEVENT_FORCE_DWORD    = 0x7fffffff
} D3DXEVENT_TYPE, *LPD3DXEVENT_TYPE;
```



## Constants

<dl> <dt>

<span id="D3DXEVENT_TRACKSPEED"></span><span id="d3dxevent_trackspeed"></span>**D3DXEVENT\_TRACKSPEED**
</dt> <dd>

Track speed.

</dd> <dt>

<span id="D3DXEVENT_TRACKWEIGHT"></span><span id="d3dxevent_trackweight"></span>**D3DXEVENT\_TRACKWEIGHT**
</dt> <dd>

Track weight.

</dd> <dt>

<span id="D3DXEVENT_TRACKPOSITION"></span><span id="d3dxevent_trackposition"></span>**D3DXEVENT\_TRACKPOSITION**
</dt> <dd>

Track position.

</dd> <dt>

<span id="D3DXEVENT_TRACKENABLE"></span><span id="d3dxevent_trackenable"></span>**D3DXEVENT\_TRACKENABLE**
</dt> <dd>

Enable flag.

</dd> <dt>

<span id="D3DXEVENT_PRIORITYBLEND"></span><span id="d3dxevent_priorityblend"></span>**D3DXEVENT\_PRIORITYBLEND**
</dt> <dd>

Priority blend value.

</dd> <dt>

<span id="D3DXEVENT_FORCE_DWORD"></span><span id="d3dxevent_force_dword"></span>**D3DXEVENT\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




