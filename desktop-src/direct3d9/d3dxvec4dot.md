---
Description: Determines the dot product of two 4D vectors.
ms.assetid: 565dede8-6cc8-4313-9480-2f252cac94f2
title: D3DXVec4Dot function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXVec4Dot function

Determines the dot product of two 4D vectors.

## Syntax


```C++
FLOAT D3DXVec4Dot(
  _In_ const D3DXVECTOR4 *pV1,
  _In_ const D3DXVECTOR4 *pV2
);
```



## Parameters

<dl> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](winprog.windows_data_types)**

The dot product.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec4Cross**](d3dxvec4cross.md)
</dt> </dl>

 

 




