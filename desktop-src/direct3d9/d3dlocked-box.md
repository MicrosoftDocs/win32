---
Description: Describes a locked box (volume).
ms.assetid: b371fb5e-2d65-453c-acd7-214de8aaa78a
title: D3DLOCKED\_BOX structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**int**](winprog.windows_data_types)**

</dd> <dd>

Byte offset from the left edge of one row to the left edge of the next row.

</dd> <dt>

**SlicePitch**
</dt> <dd>

Type: **[**int**](winprog.windows_data_types)**

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

[**IDirect3DVolume9::LockBox**](/windows/win32/d3d9helper/nf-d3d9-idirect3dvolume9-lockbox?branch=master)
</dt> <dt>

[**IDirect3DVolumeTexture9::LockBox**](/windows/win32/d3d9helper/nf-d3d9-idirect3dvolumetexture9-lockbox?branch=master)
</dt> </dl>

 

 




