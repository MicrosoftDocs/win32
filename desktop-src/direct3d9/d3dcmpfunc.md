---
description: Defines the supported compare functions.
ms.assetid: 999af3eb-a208-4312-acee-373192ea69e4
title: D3DCMPFUNC enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DCMPFUNC
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DCMPFUNC enumeration

Defines the supported compare functions.

## Syntax


```C++
typedef enum D3DCMPFUNC { 
  D3DCMP_NEVER         = 1,
  D3DCMP_LESS          = 2,
  D3DCMP_EQUAL         = 3,
  D3DCMP_LESSEQUAL     = 4,
  D3DCMP_GREATER       = 5,
  D3DCMP_NOTEQUAL      = 6,
  D3DCMP_GREATEREQUAL  = 7,
  D3DCMP_ALWAYS        = 8,
  D3DCMP_FORCE_DWORD   = 0x7fffffff
} D3DCMPFUNC, *LPD3DCMPFUNC;
```



## Constants

<dl> <dt>

<span id="D3DCMP_NEVER"></span><span id="d3dcmp_never"></span>**D3DCMP\_NEVER**
</dt> <dd>

Always fail the test.

</dd> <dt>

<span id="D3DCMP_LESS"></span><span id="d3dcmp_less"></span>**D3DCMP\_LESS**
</dt> <dd>

Accept the new pixel if its value is less than the value of the current pixel.

</dd> <dt>

<span id="D3DCMP_EQUAL"></span><span id="d3dcmp_equal"></span>**D3DCMP\_EQUAL**
</dt> <dd>

Accept the new pixel if its value equals the value of the current pixel.

</dd> <dt>

<span id="D3DCMP_LESSEQUAL"></span><span id="d3dcmp_lessequal"></span>**D3DCMP\_LESSEQUAL**
</dt> <dd>

Accept the new pixel if its value is less than or equal to the value of the current pixel.

</dd> <dt>

<span id="D3DCMP_GREATER"></span><span id="d3dcmp_greater"></span>**D3DCMP\_GREATER**
</dt> <dd>

Accept the new pixel if its value is greater than the value of the current pixel.

</dd> <dt>

<span id="D3DCMP_NOTEQUAL"></span><span id="d3dcmp_notequal"></span>**D3DCMP\_NOTEQUAL**
</dt> <dd>

Accept the new pixel if its value does not equal the value of the current pixel.

</dd> <dt>

<span id="D3DCMP_GREATEREQUAL"></span><span id="d3dcmp_greaterequal"></span>**D3DCMP\_GREATEREQUAL**
</dt> <dd>

Accept the new pixel if its value is greater than or equal to the value of the current pixel.

</dd> <dt>

<span id="D3DCMP_ALWAYS"></span><span id="d3dcmp_always"></span>**D3DCMP\_ALWAYS**
</dt> <dd>

Always pass the test.

</dd> <dt>

<span id="D3DCMP_FORCE_DWORD"></span><span id="d3dcmp_force_dword"></span>**D3DCMP\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The values in this enumerated type define the supported compare functions for the D3DRS\_ZFUNC, D3DRS\_ALPHAFUNC, and D3DRS\_STENCILFUNC render states.

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

 

 
