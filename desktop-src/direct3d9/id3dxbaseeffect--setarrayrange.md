---
Description: 'Set the range of an array to pass to the device.'
ms.assetid: '43f1c258-770c-4756-9033-e5667b379fe6'
title: 'ID3DXBaseEffect::SetArrayRange method'
---

# ID3DXBaseEffect::SetArrayRange method

Set the range of an array to pass to the device.

## Syntax


```C++
HRESULT SetArrayRange(
  [in] D3DXHANDLE hParameter,
  [in] UINT       Start,
  [in] UINT       Stop
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*Start* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Start index.

</dd> <dt>

*Stop* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Stop index.

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
</dt> </dl>

 

 




