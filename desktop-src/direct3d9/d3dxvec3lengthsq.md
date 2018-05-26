---
Description: Returns the square of the length of a 3D vector.
ms.assetid: 25dc50cc-542b-4989-a858-9b37603393a0
title: D3DXVec3LengthSq function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXVec3LengthSq function

Returns the square of the length of a 3D vector.

## Syntax


```C++
FLOAT D3DXVec3LengthSq(
  _In_ const D3DXVECTOR3 *pV
);
```



## Parameters

<dl> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the source [**D3DXVECTOR3**](d3dxvector3.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](winprog.windows_data_types)**

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

[**D3DXVec3Length**](d3dxvec3length.md)
</dt> </dl>

 

 




