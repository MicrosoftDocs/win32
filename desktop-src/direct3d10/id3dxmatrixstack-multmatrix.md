---
description: ID3DXMATRIXStack::MultMatrix method (D3DX10.h) - Determines the product of the current matrix and the given matrix.
ms.assetid: 72388919-e474-4433-b219-41e2d312848e
title: ID3DXMATRIXStack::MultMatrix method (D3DX10.h)
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
- D3DX10.lib
- D3DX10.dll
---

# ID3DXMATRIXStack::MultMatrix method (D3DX10.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/directxmath-portal.md) instead along with this header from [GitHub](https://github.com/microsoft/DirectXMath/tree/main/MatrixStack).

Determines the product of the current matrix and the given matrix.

## Syntax


```C++
HRESULT MultMatrix(
  [in] const D3DXMATRIX *pM
);
```



## Parameters

<dl> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the D3DXMATRIX structure to be multiplied with the current matrix.

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
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DXMatrixStack](d3d10-id3dxmatrixstack.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
