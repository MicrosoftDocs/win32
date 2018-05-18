---
Description: 'Gets an array of floating point values.'
ms.assetid: 'ba839129-c332-4ce8-b7c1-ea0ef4697ade'
title: 'ID3DXBaseEffect::GetFloatArray method'
---

# ID3DXBaseEffect::GetFloatArray method

Gets an array of floating point values.

## Syntax


```C++
HRESULT GetFloatArray(
  [in]  D3DXHANDLE hParameter,
  [out] FLOAT      *pf,
  [in]  UINT       Count
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pf* \[out\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Returns an array of floating point values.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of floating point values in the array.

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

[**SetFloatArray**](id3dxbaseeffect--setfloatarray.md)
</dt> </dl>

 

 




