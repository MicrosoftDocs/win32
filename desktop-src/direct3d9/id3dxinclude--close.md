---
description: A user-implemented method for closing a shader \#include file.
ms.assetid: de54ce56-3884-443a-9879-4e7290bcfb8d
title: ID3DXInclude::Close method (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXInclude.Close
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXInclude::Close method

A user-implemented method for closing a shader \#include file.

## Syntax


```C++
HRESULT Close(
  [in] LPCVOID pData
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](../winprog/windows-data-types.md)**

Pointer to the returned buffer that contains the include directives. This is the pointer that was returned by the corresponding [**ID3DXInclude::Open**](id3dxinclude--open.md) call.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The user-implemented method should return S\_OK. If the callback fails when reading the \#include file, the API that caused the callback to be called will fail. This is one of the following:

-   The HLSL shader will fail one of the D3DXCompileShader\*\*\* functions.
-   The assembly shader will fail one of the D3DXAssembleShader\*\*\* functions.
-   The effect will fail one of the D3DXCreateEffect\*\*\* or D3DXCreateEffectCompiler\*\*\* functions.

## Remarks

If [**ID3DXInclude::Open**](id3dxinclude--open.md) was successful, **ID3DXInclude::Close** is guaranteed to be called before the API using this interface returns.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXInclude](id3dxinclude.md)
</dt> <dt>

[**ID3DXInclude::Open**](id3dxinclude--open.md)
</dt> </dl>

 

 
