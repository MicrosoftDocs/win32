---
Description: Describes a locked rectangular region.
ms.assetid: ee5d2ea6-bf98-4b09-bc67-b808ffcb23c6
title: D3DLOCKED_RECT structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DLOCKED_RECT
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DLOCKED\_RECT structure

Describes a locked rectangular region.

## Syntax


```C++
typedef struct D3DLOCKED_RECT {
  INT  Pitch;
  void *pBits;
} D3DLOCKED_RECT, *LPD3DLOCKED_RECT;
```



## Members

<dl> <dt>

**Pitch**
</dt> <dd>

Type: **[**INT**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Number of bytes in one row of the surface.

</dd> <dt>

**pBits**
</dt> <dd>

Type: **void\***

</dd> <dd>

Pointer to the locked bits. If a [**RECT**](https://msdn.microsoft.com/library/Dd162897(v=VS.85).aspx) was provided to the [**LockRect**](https://msdn.microsoft.com/library/Bb205896(v=VS.85).aspx) call, pBits will be appropriately offset from the start of the surface.

</dd> </dl>

## Remarks

The pitch for DXTn formats is different from what was returned in DirectX 7. It now refers to the number of bytes in a row of blocks. For example, if you have a width of 16, then you will have a pitch of 4 blocks (4\*8 for DXT1, 4\*16 for DXT2-5.)

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**IDirect3DCubeTexture9::LockRect**](https://msdn.microsoft.com/library/Bb174334(v=VS.85).aspx)
</dt> <dt>

[**IDirect3DSurface9::LockRect**](https://msdn.microsoft.com/library/Bb205896(v=VS.85).aspx)
</dt> <dt>

[**IDirect3DTexture9::LockRect**](https://msdn.microsoft.com/library/Bb205913(v=VS.85).aspx)
</dt> </dl>

 

 




