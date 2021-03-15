---
description: Describes the raster status.
ms.assetid: f7b5b714-8fc8-47b8-adec-1089b8d07081
title: D3DRASTER_STATUS structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DRASTER_STATUS
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DRASTER\_STATUS structure

Describes the raster status.

## Syntax


```C++
typedef struct D3DRASTER_STATUS {
  BOOL InVBlank;
  UINT ScanLine;
} D3DRASTER_STATUS, *LPD3DRASTER_STATUS;
```



## Members

<dl> <dt>

**InVBlank**
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

</dd> <dd>

**TRUE** if the raster is in the vertical blank period. **FALSE** if the raster is not in the vertical blank period.

</dd> <dt>

**ScanLine**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

If InVBlank is **FALSE**, then this value is an integer roughly corresponding to the current scan line painted by the raster. Scan lines are numbered in the same way as Direct3D surface coordinates: 0 is the top of the primary surface, extending to the value (height of the surface - 1) at the bottom of the display.

If InVBlank is **TRUE**, then this value is set to zero and can be ignored.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetRasterStatus**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getrasterstatus)
</dt> </dl>

 

 
