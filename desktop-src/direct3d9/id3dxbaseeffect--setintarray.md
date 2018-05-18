---
Description: 'Sets an array of integers.'
ms.assetid: '4491bffd-ce5e-4f84-ac11-0314a1b16d63'
title: 'ID3DXBaseEffect::SetIntArray method'
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

Type: **const [**INT**](winprog.windows_data_types)\***

Array of integers.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of integers in the array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**GetIntArray**](id3dxbaseeffect--getintarray.md)
</dt> </dl>

 

 




