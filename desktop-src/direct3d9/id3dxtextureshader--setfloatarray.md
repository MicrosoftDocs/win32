---
description: Sets an array of floating-point numbers.
ms.assetid: 8e64b569-a6bf-4925-9d21-4df0b6661ee2
title: ID3DXTextureShader::SetFloatArray method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXTextureShader.SetFloatArray
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXTextureShader::SetFloatArray method

Sets an array of floating-point numbers.

## Syntax


```C++
HRESULT SetFloatArray(
  [in]       D3DXHANDLE hConstant,
  [in] const FLOAT      *pf,
  [in]       UINT       Count
);
```



## Parameters

<dl> <dt>

*hConstant* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the array of constants. See [D3DXHANDLE](d3dxfx.md).

</dd> <dt>

*pf* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

Array of floating-point numbers.

</dd> <dt>

*Count* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of floating-point values in the array.

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

[ID3DXTextureShader](id3dxtextureshader.md)
</dt> </dl>

 

 
