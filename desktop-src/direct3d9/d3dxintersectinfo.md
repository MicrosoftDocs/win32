---
Description: Describes a ray-triangle intersection.
ms.assetid: b6f50fc0-2c8a-4efa-a144-bd0851f8b0ca
title: D3DXINTERSECTINFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXINTERSECTINFO structure

Describes a ray-triangle intersection.

## Syntax


```C++
typedef struct D3DXINTERSECTINFO {
  DWORD FaceIndex;
  FLOAT U;
  FLOAT V;
  FLOAT Dist;
} D3DXINTERSECTINFO, *LPD3DXINTERSECTINFO;
```



## Members

<dl> <dt>

**FaceIndex**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Index of the triangle that hit the ray.

</dd> <dt>

**U**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Barycentric coordinate within the triangle where the ray intersects.

</dd> <dt>

**V**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Barycentric coordinate within the triangle where the ray intersects.

</dd> <dt>

**Dist**
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

</dd> <dd>

Distance along the ray where the intersection occurred.

</dd> </dl>

## Remarks

Barycentric coordinates define a point inside a triangle in terms of the triangle's vertices. For a more in-depth description of barycentric coordinates, see [Mathworld's Barycentric Coordinates Description](http://go.microsoft.com/?linkid=9742311).

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




