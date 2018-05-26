---
Description: Searches through a shader for a particular comment. The comment is identified by a four-character code (FOURCC) in the first DWORD of the comment.
ms.assetid: 86ab8330-fd48-4d14-835c-92399c6c8a38
title: D3DXFindShaderComment function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **const [**DWORD**](winprog.windows_data_types)\***

Pointer to the shader function DWORD stream.

</dd> <dt>

*FourCC* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

FOURCC code that identifies the comment block. See [FourCC Formats](d3dformat.md).

</dd> <dt>

*ppData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](winprog.windows_data_types)\***

Returns a pointer to the comment data (not including the comment token and FOURCC code). This value can be **NULL**.

</dd> <dt>

*pSizeInBytes* \[out\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)\***

Returns the size of the comment data in bytes. This value can be **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the comment is not found, and no other error has occurred, S\_FALSE is returned.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> </dl>

 

 




