---
description: Loads the given matrix into the current matrix.
ms.assetid: c4c5ac50-238f-4b41-8ea9-7e48ffd03fc5
title: ID3DXMATRIXStack::LoadMatrix method (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMATRIXStack.LoadMatrix
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMATRIXStack::LoadMatrix method (D3dx9math.h)

Loads the given matrix into the current matrix.

## Syntax


```C++
HRESULT LoadMatrix(
  [in] const D3DXMATRIX *pMat
);
```



## Parameters

<dl> <dt>

*pMat* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure loaded into the current matrix.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

Note that this method does not add an item to the stack; rather, it replaces the current matrix with the supplied matrix.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMATRIXStack](id3dxmatrixstack.md)
</dt> <dt>

[**ID3DXMATRIXStack::LoadIdentity**](id3dxmatrixstack--loadidentity.md)
</dt> </dl>

 

 




