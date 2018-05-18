---
Description: 'Gets a BOOL value.'
ms.assetid: '9d61efcd-f267-4c45-b685-d363588796f7'
title: 'ID3DXBaseEffect::GetBool method'
---

# ID3DXBaseEffect::GetBool method

Gets a BOOL value.

## Syntax


```C++
HRESULT GetBool(
  [in]  D3DXHANDLE hParameter,
  [out] BOOL       *pb
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pb* \[out\]
</dt> <dd>

Type: **[**BOOL**](winprog.windows_data_types)\***

Returns a Boolean value.

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

[**SetBool**](id3dxbaseeffect--setbool.md)
</dt> </dl>

 

 




