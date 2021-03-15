---
description: Defines the supported culling modes.
ms.assetid: b669307c-0d40-4ecb-8a2e-8bd1d9c65647
title: D3DCULL enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DCULL
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DCULL enumeration

Defines the supported culling modes.

## Syntax


```C++
typedef enum D3DCULL { 
  D3DCULL_NONE         = 1,
  D3DCULL_CW           = 2,
  D3DCULL_CCW          = 3,
  D3DCULL_FORCE_DWORD  = 0x7fffffff
} D3DCULL, *LPD3DCULL;
```



## Constants

<dl> <dt>

<span id="D3DCULL_NONE"></span><span id="d3dcull_none"></span>**D3DCULL\_NONE**
</dt> <dd>

Do not cull back faces.

</dd> <dt>

<span id="D3DCULL_CW"></span><span id="d3dcull_cw"></span>**D3DCULL\_CW**
</dt> <dd>

Cull back faces with clockwise vertices.

</dd> <dt>

<span id="D3DCULL_CCW"></span><span id="d3dcull_ccw"></span>**D3DCULL\_CCW**
</dt> <dd>

Cull back faces with counterclockwise vertices.

</dd> <dt>

<span id="D3DCULL_FORCE_DWORD"></span><span id="d3dcull_force_dword"></span>**D3DCULL\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The values in this enumerated type are used by the D3DRS\_CULLMODE render state. The culling modes define how back faces are culled when rendering a geometry.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9)
</dt> <dt>

[**D3DRENDERSTATETYPE**](./d3drenderstatetype.md)
</dt> </dl>

 

 
