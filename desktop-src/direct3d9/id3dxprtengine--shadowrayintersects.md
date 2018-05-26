---
Description: Uses efficient ray-tracing in precomputed radiance transfer (PRT) simulations to determine whether a ray intersects a mesh. Typically used to determine whether a given point is in shadow.
ms.assetid: fcd53a0f-80e8-4013-8efd-125e38f4ccd0
title: ID3DXPRTEngineShadowRayIntersects method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTEngine::ShadowRayIntersects method

Uses efficient ray-tracing in precomputed radiance transfer (PRT) simulations to determine whether a ray intersects a mesh. Typically used to determine whether a given point is in shadow.

## Syntax


```C++
BOOL ShadowRayIntersects(
  [in] const D3DXVECTOR3 *pRayPos,
  [in] const D3DXVECTOR3 *pRayDir
);
```



## Parameters

<dl> <dt>

*pRayPos* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure, specifying the point where the ray begins.

</dd> <dt>

*pRayDir* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure, specifying the normalized direction of the ray.

</dd> </dl>

## Return value

Type: **[**BOOL**](winprog.windows_data_types)**

Returns **TRUE** if the ray intersects the current mesh; otherwise, returns **FALSE**.

## Remarks

Use [**ID3DXPRTEngine::SetMinMaxIntersection**](id3dxprtengine--setminmaxintersection.md) to set minimum and maximum distances of intersection with the ray.

This method executes faster than [**ID3DXPRTEngine::ClosestRayIntersects**](id3dxprtengine--closestrayintersects.md).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> <dt>

[**ID3DXPRTEngine::ClosestRayIntersects**](id3dxprtengine--closestrayintersects.md)
</dt> <dt>

[**ID3DXPRTEngine::SetMinMaxIntersection**](id3dxprtengine--setminmaxintersection.md)
</dt> </dl>

 

 




