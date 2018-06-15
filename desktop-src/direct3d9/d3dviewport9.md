---
Description: Defines the window dimensions of a render-target surface onto which a 3D volume projects.
ms.assetid: fb2c6048-f837-497d-8e4f-e18942d37899
title: D3DVIEWPORT9 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DVIEWPORT9 structure

Defines the window dimensions of a render-target surface onto which a 3D volume projects.

## Syntax


```C++
typedef struct D3DVIEWPORT9 {
  DWORD X;
  DWORD Y;
  DWORD Width;
  DWORD Height;
  float MinZ;
  float MaxZ;
} D3DVIEWPORT9, *LPD3DVIEWPORT9;
```



## Members

<dl> <dt>

**X**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Pixel coordinate of the upper-left corner of the viewport on the render-target surface. Unless you want to render to a subset of the surface, this member can be set to 0.

</dd> <dt>

**Y**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Pixel coordinate of the upper-left corner of the viewport on the render-target surface. Unless you want to render to a subset of the surface, this member can be set to 0.

</dd> <dt>

**Width**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Width dimension of the clip volume, in pixels. Unless you are rendering only to a subset of the surface, this member should be set to the width dimension of the render-target surface.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Height dimension of the clip volume, in pixels. Unless you are rendering only to a subset of the surface, this member should be set to the height dimension of the render-target surface.

</dd> <dt>

**MinZ**
</dt> <dd>

Type: **float**

</dd> <dd>

Together with MaxZ, value describing the range of depth values into which a scene is to be rendered, the minimum and maximum values of the clip volume. Most applications set this value to 0.0. Clipping is performed after applying the projection matrix.

</dd> <dt>

**MaxZ**
</dt> <dd>

Type: **float**

</dd> <dd>

Together with MinZ, value describing the range of depth values into which a scene is to be rendered, the minimum and maximum values of the clip volume. Most applications set this value to 1.0. Clipping is performed after applying the projection matrix.

</dd> </dl>

## Remarks

The X, Y, Width, and Height members describe the position and dimensions of the viewport on the render-target surface. Usually, applications render to the entire target surface; when rendering on a 640 x 480 surface, these members should be 0, 0, 640, and 480, respectively. The MinZ and MaxZ are typically set to 0.0 and 1.0 but can be set to other values to achieve specific effects. For example, you might set them both to 0.0 to force the system to render objects to the foreground of a scene, or both to 1.0 to force the objects into the background.

When the viewport parameters for a device change (because of a call to the [**SetViewport**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-setviewport) method), the driver builds a new transformation matrix.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[**GetViewport**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-getviewport)
</dt> <dt>

[**SetViewport**](/windows/desktop/api/d3d9helper/nf-d3d9-idirect3ddevice9-setviewport)
</dt> </dl>

 

 




