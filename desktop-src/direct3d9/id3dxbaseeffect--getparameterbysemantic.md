---
description: Gets the handle of a top-level parameter or a structure member parameter by looking up its semantic with a case-insensitive search.
ms.assetid: 3de3791a-fe09-4a39-bd6f-0e20a641dd32
title: ID3DXBaseEffect::GetParameterBySemantic method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetParameterBySemantic
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetParameterBySemantic method

Gets the handle of a top-level parameter or a structure member parameter by looking up its semantic with a case-insensitive search.

## Syntax


```C++
D3DXHANDLE GetParameterBySemantic(
  [in] D3DXHANDLE hParameter,
  [in] LPCSTR     pSemantic
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Handle of the parameter, or **NULL** for top-level parameters. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pSemantic* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

String containing the semantic name.

</dd> </dl>

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns the handle of the first parameter that matches the specified semantic, or **NULL** if the semantic was not found. See [Handles (Direct3D 9)](handles.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 
