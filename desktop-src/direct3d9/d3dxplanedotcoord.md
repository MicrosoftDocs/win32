---
Description: Computes the dot product of a plane and a 3D vector. The w parameter of the vector is assumed to be 1.
ms.assetid: 634de6bc-b631-493d-a7a6-292a3c3253d6
title: D3DXPlaneDotCoord function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXPlaneDotCoord function

Computes the dot product of a plane and a 3D vector. The w parameter of the vector is assumed to be 1.

## Syntax


```C++
FLOAT D3DXPlaneDotCoord(
  _In_ const D3DXPLANE   *pP,
  _In_ const D3DXVECTOR3 *pV
);
```



## Parameters

<dl> <dt>

*pP* \[in\]
</dt> <dd>

Type: **const [**D3DXPLANE**](d3dxplane.md)\***

Pointer to a source [**D3DXPLANE**](d3dxplane.md) structure.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a source [**D3DXVECTOR3**](d3dxvector3.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The dot product of the plane and 3D vector.

## Remarks

Given a plane (a, b, c, d) and a 3D vector (x, y, z) the return value of this function is a\*x + b\*y + c\*z + d\*1. The **D3DXPlaneDotCoord** function is useful for determining the plane's relationship with a coordinate in 3D space.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXPlaneDot**](d3dxplanedot.md)
</dt> <dt>

[**D3DXPlaneDotNormal**](d3dxplanedotnormal.md)
</dt> </dl>

 

 




