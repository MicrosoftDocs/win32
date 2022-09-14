---
description: Gets the handle of a technique.
ms.assetid: da139706-734b-4d5e-896d-52f045942218
title: ID3DXBaseEffect::GetTechnique method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseEffect.GetTechnique
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXBaseEffect::GetTechnique method

Gets the handle of a technique.

## Syntax


```C++
D3DXHANDLE GetTechnique(
  [in] UINT Index
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Technique index.

</dd> </dl>

## Return value

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Returns the handle of the specified technique, or **NULL** if the index was invalid. See [Handles (Direct3D 9)](handles.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXBaseEffect](id3dxbaseeffect.md)
</dt> </dl>

 

 
