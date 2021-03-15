---
description: Determines the product of the current matrix and the given matrix.
ms.assetid: a673ce82-6fed-4a3f-8c37-d0db11195f06
title: ID3DXMATRIXStack::MultMatrix method (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMATRIXStack.MultMatrix
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack::MultMatrix method (D3dx9math.h)

Determines the product of the current matrix and the given matrix.

## Syntax


```C++
HRESULT MultMatrix(
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

This method right-multiplies the given matrix to the current matrix (transformation is about the current world origin).


```
m_pstack[m_currentPos] = m_pstack[m_currentPos] * (*pMat);
```



This method does not add an item to the stack, it replaces the current matrix with the product of the current matrix and the given matrix.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::MultMatrixLocal**](id3dxmatrixstack--multmatrixlocal.md)
</dt> </dl>

 

 




