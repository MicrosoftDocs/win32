---
Description: 'Gets the handle of a top-level parameter or a structure member parameter by looking up its name.'
ms.assetid: 'fb03685e-e512-4293-80d7-6c2c0fc9ebfd'
title: 'ID3DXBaseEffect::GetParameterByName method'
---

# ID3DXBaseEffect::GetParameterByName method

Gets the handle of a top-level parameter or a structure member parameter by looking up its name.

## Syntax


```C++
D3DXHANDLE GetParameterByName(
  [in] D3DXHANDLE hParameter,
  [in] LPCSTR     pName
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Handle of the parameter, or **NULL** for top-level parameters. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

String containing the parameter name.

</dd> </dl>

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns the handle of the specified parameter, or **NULL** if the index was invalid. See [Handles (Direct3D 9)](handles.md).

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 




