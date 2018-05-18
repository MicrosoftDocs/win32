---
Description: 'Sets a floating point value.'
ms.assetid: 'f49fb4d2-6e3d-4452-8102-76200c55cf1f'
title: 'ID3DXBaseEffect::SetFloat method'
---

# ID3DXBaseEffect::SetFloat method

Sets a floating point value.

## Syntax


```C++
HRESULT SetFloat(
  [in] D3DXHANDLE hParameter,
  [in] FLOAT      f
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*f* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Floating point value.

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

[**GetFloat**](id3dxbaseeffect--getfloat.md)
</dt> </dl>

 

 




