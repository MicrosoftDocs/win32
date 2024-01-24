---
description: Gets a literal status of a parameter. A literal parameter has a value that doesn't change during the lifetime of an effect.
ms.assetid: 417abbee-5193-462e-b0d1-b4928ad0a041
title: ID3DXEffectCompiler::GetLiteral method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffectCompiler.GetLiteral
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffectCompiler::GetLiteral method

Gets a literal status of a parameter. A literal parameter has a value that doesn't change during the lifetime of an effect.

## Syntax


```C++
HRESULT GetLiteral(
  [in]  D3DXHANDLE hParameter,
  [out] BOOL       *pLiteral
);
```



## Parameters

<dl> <dt>

*hParameter* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to a parameter. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pLiteral* \[out\]
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)\***

Returns True if the parameter is a literal, and False otherwise.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

This methods only changes whether the parameter is a literal or not. To change the value of a parameter, use a method like [**ID3DXBaseEffect::SetBool**](id3dxbaseeffect--setbool.md) or [**ID3DXBaseEffect::SetValue**](id3dxbaseeffect--setvalue.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectCompiler](id3dxeffectcompiler.md)
</dt> <dt>

[Usages and Literals (Direct3D 9)](usages-and-literals.md)
</dt> <dt>

[**ID3DXEffectCompiler::SetLiteral**](id3dxeffectcompiler--setliteral.md)
</dt> </dl>

 

 
