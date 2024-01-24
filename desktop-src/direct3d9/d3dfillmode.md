---
description: Defines constants describing the fill mode.
ms.assetid: be835432-e8d5-4afb-a810-2dac25bdc9dc
title: D3DFILLMODE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DFILLMODE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DFILLMODE enumeration

Defines constants describing the fill mode.

## Syntax


```C++
typedef enum D3DFILLMODE { 
  D3DFILL_POINT        = 1,
  D3DFILL_WIREFRAME    = 2,
  D3DFILL_SOLID        = 3,
  D3DFILL_FORCE_DWORD  = 0x7fffffff
} D3DFILLMODE, *LPD3DFILLMODE;
```



## Constants

<dl> <dt>

<span id="D3DFILL_POINT"></span><span id="d3dfill_point"></span>**D3DFILL\_POINT**
</dt> <dd>

Fill points.

</dd> <dt>

<span id="D3DFILL_WIREFRAME"></span><span id="d3dfill_wireframe"></span>**D3DFILL\_WIREFRAME**
</dt> <dd>

Fill wireframes.

</dd> <dt>

<span id="D3DFILL_SOLID"></span><span id="d3dfill_solid"></span>**D3DFILL\_SOLID**
</dt> <dd>

Fill solids.

</dd> <dt>

<span id="D3DFILL_FORCE_DWORD"></span><span id="d3dfill_force_dword"></span>**D3DFILL\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The values in this enumerated type are used by the D3DRS\_FILLMODE render state.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DRENDERSTATETYPE**](./d3drenderstatetype.md)
</dt> </dl>

 

 
