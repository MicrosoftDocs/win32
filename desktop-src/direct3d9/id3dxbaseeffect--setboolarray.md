---
Description: 'Sets an array of Boolean values.'
ms.assetid: '920b3482-cc30-4ab2-bfce-59f03afe11da'
title: 'ID3DXBaseEffect::SetBoolArray method'
---

# ID3DXBaseEffect::SetBoolArray method

Sets an array of Boolean values.

## Syntax


```C++
HRESULT SetBoolArray(
  [in]       D3DXHANDLE hParameter,
  [in] const BOOL       *pB,
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

*pB* \[in\]
</dt> <dd>

Type: **const [**BOOL**](winprog.windows_data_types)\***

Array of Boolean values.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of Boolean values in the array.

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

[**GetBoolArray**](id3dxbaseeffect--getboolarray.md)
</dt> </dl>

 

 




