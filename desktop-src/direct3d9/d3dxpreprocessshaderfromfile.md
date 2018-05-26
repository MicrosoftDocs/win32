---
Description: Preprocesses a shader file without performing compilation. This resolves all \#defines and \#includes, providing a self-contained shader for subsequent compilation.
ms.assetid: 1be68cc0-b4a3-41b4-b956-b96ed439be9e
title: D3DXPreprocessShaderFromFile function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXPreprocessShaderFromFile function

Preprocesses a shader file without performing compilation. This resolves all \#defines and \#includes, providing a self-contained shader for subsequent compilation.

> [!Note]  
> Instead of using this legacy function, we recommend that you use the [**D3DPreprocess**](direct3dhlsl.d3dpreprocess) API.

 

## Syntax


```C++
HRESULT D3DXPreprocessShaderFromFile(
  _In_        LPCSTR        pSrcFile,
  _In_  const D3DXMACRO     *pDefines,
  _In_        LPD3DXINCLUDE pInclude,
  _Out_       LPD3DXBUFFER  *ppShaderText,
  _Out_       LPD3DXBUFFER  *ppErrorMsgs
);
```



## Parameters

<dl> <dt>

*pSrcFile* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Pointer to a string that specifies the filename of the shader.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3DXMACRO**](d3dxmacro.md)\***

An optional **NULL** terminated array of [**D3DXMACRO**](d3dxmacro.md) structures. This value may be **NULL**.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3DXINCLUDE**](id3dxinclude.md)**

Optional interface pointer, [**ID3DXInclude**](id3dxinclude.md), to use for handling \#include directives. If this value is **NULL**, \#includes will either be honored when compiling from a file or will cause an error when compiled from a resource or memory.

</dd> <dt>

*ppShaderText* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing a single large string that represents the resulting formatted token stream.

</dd> <dt>

*ppErrorMsgs* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing a listing of errors and warnings that were encountered during the compile. These are the same messages the debugger displays when running in debug mode. This value may be **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> <dt>

[**D3DXPreprocessShader**](d3dxpreprocessshader.md)
</dt> <dt>

[**D3DXPreprocessShaderFromResource**](d3dxpreprocessshaderfromresource.md)
</dt> </dl>

 

 




