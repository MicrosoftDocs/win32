---
Description: Transforms a 4D vector by a given matrix.
ms.assetid: ccbf33bc-1f94-4cf8-b048-220d54516e00
title: D3DXVec4Transform function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec4Transform
api_type: 
- HeaderDef
api_location: 
- D3DX10Math.h
---

# D3DXVec4Transform function

Transforms a 4D vector by a given matrix.

## Syntax


```C++
D3DXVECTOR4* D3DXVec4Transform(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_    const D3DXVECTOR4 *pV,
  _In_    const D3DXMATRIX  *pM
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](https://msdn.microsoft.com/en-us/library/Bb205548(v=VS.85).aspx)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](https://msdn.microsoft.com/en-us/library/Bb205548(v=VS.85).aspx)\***

Pointer to the source D3DXVECTOR4 structure.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](https://msdn.microsoft.com/en-us/library/Bb172912(v=VS.85).aspx)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](https://msdn.microsoft.com/en-us/library/Bb205548(v=VS.85).aspx)\***

Pointer to a D3DXVECTOR4 structure that is the transformed 4D vector.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec4Transform function can be used as a parameter for another function.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




