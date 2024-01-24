---
description: Defines the location at which a color or color component must be accessed for lighting calculations.
ms.assetid: 76061d47-a31c-4008-aa8d-a0464dd3423f
title: D3DMATERIALCOLORSOURCE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DMATERIALCOLORSOURCE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DMATERIALCOLORSOURCE enumeration

Defines the location at which a color or color component must be accessed for lighting calculations.

## Syntax


```C++
typedef enum D3DMATERIALCOLORSOURCE { 
  D3DMCS_MATERIAL     = 0,
  D3DMCS_COLOR1       = 1,
  D3DMCS_COLOR2       = 2,
  D3DMCS_FORCE_DWORD  = 0x7fffffff
} D3DMATERIALCOLORSOURCE, *LPD3DMATERIALCOLORSOURCE;
```



## Constants

<dl> <dt>

<span id="D3DMCS_MATERIAL"></span><span id="d3dmcs_material"></span>**D3DMCS\_MATERIAL**
</dt> <dd>

Use the color from the current material.

</dd> <dt>

<span id="D3DMCS_COLOR1"></span><span id="d3dmcs_color1"></span>**D3DMCS\_COLOR1**
</dt> <dd>

Use the diffuse vertex color.

</dd> <dt>

<span id="D3DMCS_COLOR2"></span><span id="d3dmcs_color2"></span>**D3DMCS\_COLOR2**
</dt> <dd>

Use the specular vertex color.

</dd> <dt>

<span id="D3DMCS_FORCE_DWORD"></span><span id="d3dmcs_force_dword"></span>**D3DMCS\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

These flags are used to set the value of the following render states in the [**D3DRENDERSTATETYPE**](./d3drenderstatetype.md) enumerated type.

-   D3DRS\_AMBIENTMATERIALSOURCE
-   D3DRS\_DIFFUSEMATERIALSOURCE
-   D3DRS\_EMISSIVEMATERIALSOURCE
-   D3DRS\_SPECULARMATERIALSOURCE

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

 

 
