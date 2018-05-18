---
Description: 'Set the value of an arbitrary parameter or annotation, including simple types, structs, arrays, strings, shaders and textures.'
ms.assetid: 'ab71f1a1-3e10-4883-99b4-607e0b5751c2'
title: 'ID3DXBaseEffect::SetValue method'
---

# ID3DXBaseEffect::SetValue method

Set the value of an arbitrary parameter or annotation, including simple types, structs, arrays, strings, shaders and textures.

## Syntax


```C++
HRESULT SetValue(
  [in] D3DXHANDLE hParameter,
  [in] LPCVOID    pData,
  [in] UINT       Bytes
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)**

Pointer to a buffer containing data.

</dd> <dt>

*Bytes* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

\[in\] Number of bytes in the buffer. Pass in D3DX\_DEFAULT if you know your buffer is large enough to contain the entire parameter, and you want to skip size validation.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This method can be used in place of nearly all the effect set API calls.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> <dt>

[**GetValue**](id3dxbaseeffect--getvalue.md)
</dt> </dl>

 

 




