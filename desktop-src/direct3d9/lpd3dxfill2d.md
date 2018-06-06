---
Description: Function type used by the texture fill functions.
ms.assetid: faa2d610-cf85-42d0-833c-a46fb7fe3dbf
title: LPD3DXFILL2D
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LPD3DXFILL2D

Function type used by the texture fill functions.

## Syntax


```
typedef VOID (WINAPI *LPD3DXFILL2D)(
    D3DXVECTOR4* pOut, 
    CONST D3DXVECTOR2* pTexCoord, 
    CONST D3DXVECTOR2* pTexelSize, 
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

Be sure to specify the [**Windows Data Types**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46) calling convention when declaring the callback function. Otherwise, stack overflows can occur.



|                          |            |
|--------------------------|------------|
| Header                   | d3dx9tex.h |
| Import Library           | d3dx9.lib  |
| Minimum Operating System | Windows 98 |



 

## Related topics

<dl> <dt>

[Callback Functions](dx9-graphics-reference-d3dx-callback-functions.md)
</dt> <dt>

[LPD3DXFILL3D](lpd3dxfill3d.md)
</dt> </dl>

 

 



