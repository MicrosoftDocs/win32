---
description: Contains red, green, and blue ramp data.
ms.assetid: c596f47a-6c09-4b97-ab2f-b1da3d851aa4
title: D3DGAMMARAMP structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DGAMMARAMP
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DGAMMARAMP structure

Contains red, green, and blue ramp data.

## Syntax


```C++
typedef struct D3DGAMMARAMP {
  WORD red[256];
  WORD green[256];
  WORD blue[256];
} D3DGAMMARAMP, *LPD3DGAMMARAMP;
```



## Members

<dl> <dt>

**red**
</dt> <dd>

Type: **[**WORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Array of 256 WORD element that describes the red gamma ramp.

</dd> <dt>

**green**
</dt> <dd>

Type: **[**WORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Array of 256 WORD element that describes the green gamma ramp.

</dd> <dt>

**blue**
</dt> <dd>

Type: **[**WORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Array of 256 WORD element that describes the blue gamma ramp.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetGammaRamp**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getgammaramp)
</dt> <dt>

[**SetGammaRamp**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setgammaramp)
</dt> </dl>

 

 
