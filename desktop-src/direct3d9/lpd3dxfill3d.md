---
description: LPD3DXFILL3D - Function type used by the texture fill functions.
ms.assetid: ab2f3005-150f-46e1-b75b-75c39e7feed1
title: LPD3DXFILL3D
ms.topic: reference
ms.date: 05/31/2018
---

# LPD3DXFILL3D

Function type used by the texture fill functions.

## Syntax


```
typedef VOID (WINAPI *LPD3DXFILL2D)(
    D3DXVECTOR4* pOut, 
    CONST D3DXVECTOR3* pTexCoord, 
    CONST D3DXVECTOR3* pTexelSize, 
    LPVOID pData,  
);
```



## Parameters

pOut - Pointer to a vector, which the function uses to return its result. X, Y, Z, and W will be mapped to R, G, B, and A, respectively.

pTexCoord - Pointer to a vector containing the coordinates of the texel currently being evaluated. Texture coordinate components for texture and volume textures range from 0 to 1. Texture coordinate components for cube textures range from -1 to 1.

pTexelSize - Pointer to a vector containing the dimensions of the current texel.

pData - Pointer to user data.

## Return Value

No return value.

## Remarks

Be sure to specify the [**Windows Data Types**](../winprog/windows-data-types.md) calling convention when declaring the callback function. Otherwise, stack overflows can occur.



| Requirement                         | Value           |
|--------------------------|------------|
| Header                   | d3dx9tex.h |
| Import Library           | d3dx9.lib  |
| Minimum Operating System | Windows 98 |



 

## Related topics

<dl> <dt>

[Callback Functions](dx9-graphics-reference-d3dx-callback-functions.md)
</dt> <dt>

[LPD3DXFILL2D](lpd3dxfill2d.md)
</dt> </dl>

 

 
