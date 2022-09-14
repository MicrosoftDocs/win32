---
description: Defines the supported blend operations. See Remarks for definitions of terms.
ms.assetid: ae750d84-ed7d-4a76-bf64-eae8828c66c7
title: D3DBLENDOP enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DBLENDOP
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DBLENDOP enumeration

Defines the supported blend operations. See Remarks for definitions of terms.

## Syntax


```C++
typedef enum D3DBLENDOP { 
  D3DBLENDOP_ADD          = 1,
  D3DBLENDOP_SUBTRACT     = 2,
  D3DBLENDOP_REVSUBTRACT  = 3,
  D3DBLENDOP_MIN          = 4,
  D3DBLENDOP_MAX          = 5,
  D3DBLENDOP_FORCE_DWORD  = 0x7fffffff
} D3DBLENDOP, *LPD3DBLENDOP;
```



## Constants

<dl> <dt>

<span id="D3DBLENDOP_ADD"></span><span id="d3dblendop_add"></span>**D3DBLENDOP\_ADD**
</dt> <dd>

The result is the destination added to the source. Result = Source + Destination

</dd> <dt>

<span id="D3DBLENDOP_SUBTRACT"></span><span id="d3dblendop_subtract"></span>**D3DBLENDOP\_SUBTRACT**
</dt> <dd>

The result is the destination subtracted from to the source. Result = Source - Destination

</dd> <dt>

<span id="D3DBLENDOP_REVSUBTRACT"></span><span id="d3dblendop_revsubtract"></span>**D3DBLENDOP\_REVSUBTRACT**
</dt> <dd>

The result is the source subtracted from the destination. Result = Destination - Source

</dd> <dt>

<span id="D3DBLENDOP_MIN"></span><span id="d3dblendop_min"></span>**D3DBLENDOP\_MIN**
</dt> <dd>

The result is the minimum of the source and destination. Result = MIN(Source, Destination)

</dd> <dt>

<span id="D3DBLENDOP_MAX"></span><span id="d3dblendop_max"></span>**D3DBLENDOP\_MAX**
</dt> <dd>

The result is the maximum of the source and destination. Result = MAX(Source, Destination)

</dd> <dt>

<span id="D3DBLENDOP_FORCE_DWORD"></span><span id="d3dblendop_force_dword"></span>**D3DBLENDOP\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Source, Destination, and Result are defined as:



| Term        | Type   | Description                                                            |
|-------------|--------|------------------------------------------------------------------------|
| Source      | Input  | Color of the source pixel before the operation.                        |
| Destination | Input  | Color of the pixel in the destination buffer before the operation.     |
| Result      | Output | Returned value that is the blended color resulting from the operation. |



 

This enumerated type defines values used by the following render states:

-   D3DRS\_BLENDOP
-   D3DRS\_BLENDOPALPHA

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

 

 
