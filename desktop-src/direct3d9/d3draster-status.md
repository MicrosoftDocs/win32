---
Description: Describes the raster status.
ms.assetid: f7b5b714-8fc8-47b8-adec-1089b8d07081
title: D3DRASTER_STATUS structure
ms.author: windowssdkdev
ms.topic: structure
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

Type: **[**BOOL**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

**TRUE** if the raster is in the vertical blank period. **FALSE** if the raster is not in the vertical blank period.

</dd> <dt>

**ScanLine**
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

If InVBlank is **FALSE**, then this value is an integer roughly corresponding to the current scan line painted by the raster. Scan lines are numbered in the same way as Direct3D surface coordinates: 0 is the top of the primary surface, extending to the value (height of the surface - 1) at the bottom of the display.

If InVBlank is **TRUE**, then this value is set to zero and can be ignored.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetRasterStatus**](https://msdn.microsoft.com/library/Bb174402(v=VS.85).aspx)
</dt> </dl>

 

 




