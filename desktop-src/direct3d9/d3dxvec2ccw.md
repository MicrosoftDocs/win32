---
Description: Returns the z-component by taking the cross product of two 2D vectors.
ms.assetid: daec19f2-cd0f-4a68-affc-9a42bda8912c
title: D3DXVec2CCW function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXVec2CCW function

Returns the z-component by taking the cross product of two 2D vectors.

## Syntax


```C++
FLOAT D3DXVec2CCW(
  _In_ const D3DXVECTOR2 *pV1,
  _In_ const D3DXVECTOR2 *pV2
);
```



## Parameters

<dl> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The z-component.

## Remarks

This function determines the z-component by determining the cross-product based on the following formula: ((x1,y1,0) cross (x2,y2,0)). Or as shown in the following example.


```
pV1->x * pV2->y - pV1->y * pV2->x
```



If the value of the z-component is positive, the vector V2 is counterclockwise from the vector V1. This information is useful for back-face culling.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec2Dot**](d3dxvec2dot.md)
</dt> </dl>

 

 




