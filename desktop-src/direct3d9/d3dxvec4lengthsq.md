---
Description: Returns the square of the length of a 4D vector.
ms.assetid: 73091179-4acb-408b-8c91-766052999f26
title: D3DXVec4LengthSq function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXVec4LengthSq function

Returns the square of the length of a 4D vector.

## Syntax


```C++
FLOAT D3DXVec4LengthSq(
  _In_ const D3DXVECTOR4 *pV
);
```



## Parameters

<dl> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to the source [**D3DXVECTOR4**](d3dxvector4.md) structure.

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

[**D3DXVec4Length**](d3dxvec4length.md)
</dt> </dl>

 

 




