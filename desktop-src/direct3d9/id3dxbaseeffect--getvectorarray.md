---
description: Gets an array of vectors.
ms.assetid: 75fe454c-75f7-4f03-acd2-dd9cbf94fb96
title: ID3DXBaseEffect::GetVectorArray method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetVectorArray
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetVectorArray method

Gets an array of vectors.

## Syntax


```C++
HRESULT GetVectorArray(
  [in]  D3DXHANDLE  hParameter,
  [out] D3DXVECTOR4 *pVector,
  [in]  UINT        Count
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pVector* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](d3dxvector4.md)\***

Returns an array of 4D floating point vectors.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of vectors in the array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

If the destination vectors are larger than the source vectors, only the initial components of each destination vector will be filled, and the remaining destination vector components will be set to zero.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**SetVectorArray**](id3dxbaseeffect--setvectorarray.md)
</dt> </dl>

 

 
