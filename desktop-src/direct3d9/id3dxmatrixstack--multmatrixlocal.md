---
description: ID3DXMATRIXStack::MultMatrixLocal method (D3dx9math.h) - Determines the product of the given matrix and the current matrix.
ms.assetid: 6f909b38-821c-4173-aba9-fd4392f70551
title: ID3DXMATRIXStack::MultMatrixLocal method (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMATRIXStack.MultMatrixLocal
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack::MultMatrixLocal method (D3dx9math.h)

Determines the product of the given matrix and the current matrix.

## Syntax


```C++
HRESULT MultMatrixLocal(
  [in] const D3DXMATRIX *pMat
);
```



## Parameters

<dl> <dt>

*pMat* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure to be multiplied with the current matrix.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method left-multiplies the given matrix to the current matrix (transformation is about the local origin of the object).


```
m_pstack[m_currentPos] = (*pMat) * m_pstack[m_currentPos];
```



This method does not add an item to the stack, it replaces the current matrix with the product of the given matrix and the current matrix.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::MultMatrix**](id3dxmatrixstack--multmatrix.md)
</dt> </dl>

 

 




