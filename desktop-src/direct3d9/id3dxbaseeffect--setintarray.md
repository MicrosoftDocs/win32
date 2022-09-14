---
description: ID3DXBaseEffect::SetIntArray method - Sets an array of integers.
ms.assetid: 4491bffd-ce5e-4f84-ac11-0314a1b16d63
title: ID3DXBaseEffect::SetIntArray method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.SetIntArray
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::SetIntArray method

Sets an array of integers.

## Syntax


```C++
HRESULT SetIntArray(
  [in]       D3DXHANDLE hParameter,
  [in] const INT        *pn,
  [in]       UINT       Count
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pn* \[in\]
</dt> <dd>

Type: **const [**INT**](../winprog/windows-data-types.md)\***

Array of integers.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of integers in the array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**GetIntArray**](id3dxbaseeffect--getintarray.md)
</dt> </dl>

 

 
