---
Description: Sets a non-transposed matrix.
ms.assetid: 90329460-756e-4b3e-9ff3-be9dc556eb9f
title: ID3DXBaseEffectSetMatrix method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXBaseEffect::SetMatrix method

Sets a non-transposed matrix.

## Syntax


```C++
HRESULT SetMatrix(
  [in]       D3DXHANDLE hParameter,
  [in] const D3DXMATRIX *pMatrix
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pMatrix* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a nontransposed matrix. See [**D3DXMATRIX**](d3dxmatrix.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

A non-transposed matrix contains row-major data. In other words, each vector is contained in a row.

If the destination matrix is smaller than the source matrix, the additional components of the source matrix will be ignored.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**GetMatrix**](id3dxbaseeffect--getmatrix.md)
</dt> </dl>

 

 




