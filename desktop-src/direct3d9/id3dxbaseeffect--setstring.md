---
Description: 'Sets a string.'
ms.assetid: '7e8eef70-85ee-461d-bf8c-44cda5f184cd'
title: 'ID3DXBaseEffect::SetString method'
---

# ID3DXBaseEffect::SetString method

Sets a string.

## Syntax


```C++
HRESULT SetString(
  [in] D3DXHANDLE hParameter,
  [in] LPCSTR     pString
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pString* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

String to set.

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

[**GetString**](id3dxbaseeffect--getstring.md)
</dt> </dl>

 

 




