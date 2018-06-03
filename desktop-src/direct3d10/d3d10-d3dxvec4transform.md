---
Description: Transforms a 4D vector by a given matrix.
ms.assetid: ccbf33bc-1f94-4cf8-b048-220d54516e00
title: D3DXVec4Transform function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**D3DXVECTOR4**](https://msdn.microsoft.com/windows/desktop/fbfe7851-7bec-4fa0-b4dc-52f5cb83d0a4)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](https://msdn.microsoft.com/windows/desktop/fbfe7851-7bec-4fa0-b4dc-52f5cb83d0a4)\***

Pointer to the source D3DXVECTOR4 structure.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](https://msdn.microsoft.com/windows/desktop/0911088b-50cf-4c4a-996e-351386fc359b)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](https://msdn.microsoft.com/windows/desktop/fbfe7851-7bec-4fa0-b4dc-52f5cb83d0a4)\***

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

 

 




