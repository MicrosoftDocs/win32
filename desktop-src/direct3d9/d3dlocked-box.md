---
Description: Describes a locked box (volume).
ms.assetid: b371fb5e-2d65-453c-acd7-214de8aaa78a
title: D3DLOCKED_BOX structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DLOCKED_BOX
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DLOCKED\_BOX structure

Describes a locked box (volume).

## Syntax


```C++
typedef struct D3DLOCKED_BOX {
  int  RowPitch;
  int  SlicePitch;
  void *pBits;
} D3DLOCKED_BOX, *LPD3DLOCKED_BOX;
```



## Members

<dl> <dt>

**RowPitch**
</dt> <dd>

Type: **[**int**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Byte offset from the left edge of one row to the left edge of the next row.

</dd> <dt>

**SlicePitch**
</dt> <dd>

Type: **[**int**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Byte offset from the top-left of one slice to the top-left of the next deepest slice.

</dd> <dt>

**pBits**
</dt> <dd>

Type: **void\***

</dd> <dd>

Pointer to the beginning of the volume box. If a [**D3DBOX**](d3dbox.md) was provided to the LockBox call, pBits will be appropriately offset from the start of the volume.

</dd> </dl>

## Remarks

Volumes can be visualized as being organized into slices of width x height 2D surfaces stacked up to make a width x height x depth volume. For more information, see [Volume Texture Resources (Direct3D 9)](volume-texture-resources.md).

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**IDirect3DVolume9::LockBox**](https://msdn.microsoft.com/library/Bb205938(v=VS.85).aspx)
</dt> <dt>

[**IDirect3DVolumeTexture9::LockBox**](https://msdn.microsoft.com/library/Bb205945(v=VS.85).aspx)
</dt> </dl>

 

 




