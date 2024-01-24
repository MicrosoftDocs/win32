---
description: Searches through a shader for a particular comment. The comment is identified by a four-character code (FOURCC) in the first DWORD of the comment.
ms.assetid: 86ab8330-fd48-4d14-835c-92399c6c8a38
title: D3DXFindShaderComment function (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXFindShaderComment
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXFindShaderComment function

Searches through a shader for a particular comment. The comment is identified by a four-character code (FOURCC) in the first DWORD of the comment.

## Syntax


```C++
HRESULT D3DXFindShaderComment(
  _In_  const DWORD   *pFunction,
  _In_        DWORD   FourCC,
  _In_        LPCVOID *ppData,
  _Out_       UINT    *pSizeInBytes
);
```



## Parameters

<dl> <dt>

*pFunction* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to the shader function DWORD stream.

</dd> <dt>

*FourCC* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

FOURCC code that identifies the comment block. See [FourCC Formats](d3dformat.md).

</dd> <dt>

*ppData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](../winprog/windows-data-types.md)\***

Returns a pointer to the comment data (not including the comment token and FOURCC code). This value can be **NULL**.

</dd> <dt>

*pSizeInBytes* \[out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Returns the size of the comment data in bytes. This value can be **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the comment is not found, and no other error has occurred, S\_FALSE is returned.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 
