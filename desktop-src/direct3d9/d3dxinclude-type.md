---
description: Describes the location for the include file.
ms.assetid: a15d363e-0d82-44a9-816b-edf2f60540b3
title: D3DXINCLUDE_TYPE enumeration (D3dx9shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXINCLUDE_TYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9shader.h
---

# D3DXINCLUDE\_TYPE enumeration

Describes the location for the include file.

## Syntax


```C++
typedef enum D3DXINCLUDE_TYPE { 
  D3DXINC_LOCAL        = 0,
  D3DXINC_SYSTEM       = 1,
  D3DXINC_FORCE_DWORD  = 0x7fffffff
} D3DXINCLUDE_TYPE, *LPD3DXINCLUDE_TYPE;
```



## Constants

<dl> <dt>

<span id="D3DXINC_LOCAL"></span><span id="d3dxinc_local"></span>**D3DXINC\_LOCAL**
</dt> <dd>

Look in the local project for the include file.

</dd> <dt>

<span id="D3DXINC_SYSTEM"></span><span id="d3dxinc_system"></span>**D3DXINC\_SYSTEM**
</dt> <dd>

Look in the system path for the include file.

</dd> <dt>

<span id="D3DXINC_FORCE_DWORD"></span><span id="d3dxinc_force_dword"></span>**D3DXINC\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




