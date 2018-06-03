---
Description: Returns the square of the length of a 2D vector.
ms.assetid: 0ecc40bb-7613-463a-a8a0-5e184feb441f
title: D3DXVec2LengthSq function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXVec2LengthSq function

Returns the square of the length of a 2D vector.

## Syntax


```C++
FLOAT D3DXVec2LengthSq(
  _In_ const D3DXVECTOR2 *pV
);
```



## Parameters

<dl> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to the source [**D3DXVECTOR2**](d3dxvector2.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](https://msdn.microsoft.com/windows/desktop/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The vector's squared length.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec2Length**](d3dxvec2length.md)
</dt> </dl>

 

 




