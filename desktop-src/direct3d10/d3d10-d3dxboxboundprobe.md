---
Description: Determines whether a ray intersects the volume of a box's bounding box.
ms.assetid: d3cdcf89-461b-44b0-b5d0-ca2e3869a5ad
title: D3DXBoxBoundProbe function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXBoxBoundProbe function

Determines whether a ray intersects the volume of a box's bounding box.

## Syntax


```C++
BOOL D3DXBoxBoundProbe(
  _In_ const D3DXVECTOR3 *pMin,
  _In_ const D3DXVECTOR3 *pMax,
  _In_ const D3DXVECTOR3 *pRayPosition,
  _In_ const D3DXVECTOR3 *pRayDirection
);
```



## Parameters

<dl> <dt>

*pMin* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxvector3.htm)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md), describing the lower-left corner of the bounding box. See Remarks.

</dd> <dt>

*pMax* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxvector3.htm)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, describing the upper-right corner of the bounding box. See Remarks.

</dd> <dt>

*pRayPosition* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxvector3.htm)\***

Pointer to a D3DXVECTOR3 structure, specifying the origin coordinate of the ray.

</dd> <dt>

*pRayDirection* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxvector3.htm)\***

Pointer to a D3DXVECTOR3 structure, specifying the direction of the ray. This vector should not be (0,0,0) but does not need to be normalized.

</dd> </dl>

## Return value

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Returns **TRUE** if the ray intersects the volume of the box's bounding box. Otherwise, returns **FALSE**.

## Remarks

**D3DXBoxBoundProbe** determines if the ray intersects the volume of the box's bounding box, not just the surface of the box.

The values passed to **D3DXBoxBoundProbe** are xmin, xmax, ymin, ymax, zmin, and zmax. Thus, the following defines the corners of the bounding box.


```
xmax, ymax, zmax
xmax, ymax, zmin
xmax, ymin, zmax
xmax, ymin, zmin
xmin, ymax, zmax
xmin, ymax, zmin
xmin, ymin, zmax
xmin, ymin, zmin
```



The depth of the bounding box in the z direction is zmax - zmin, in the y direction is ymax - ymin, and in the x direction is xmax - xmin. For example, with the following minimum and maximum vectors, min (-1, -1, -1) and max (1, 1, 1), the bounding box is defined in the following manner.


```
 1,  1,  1
 1,  1, -1
 1, -1,  1
 1, -1, -1
-1,  1,  1
-1,  1, -1
-1, -1,  1
-1, -1, -l
```



## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](d3d10-graphics-reference-d3dx10-functions-mesh.md)
</dt> </dl>

 

 




