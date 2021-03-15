---
description: Compile a shader file.
ms.assetid: 9b19ab67-d5d5-482d-b3fe-ce20b64d7ad8
title: D3DXCompileShader function (D3DX9Shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCompileShader
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXCompileShader function

Compile a shader file.

> [!Note]  
> Instead of using this legacy function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use the [**D3DCompile**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile) API.

 

## Syntax


```C++
HRESULT D3DXCompileShader(
  _In_        LPCSTR              pSrcData,
  _In_        UINT                srcDataLen,
  _In_  const D3DXMACRO           *pDefines,
  _In_        LPD3DXINCLUDE       pInclude,
  _In_        LPCSTR              pFunctionName,
  _In_        LPCSTR              pProfile,
  _In_        DWORD               Flags,
  _Out_       LPD3DXBUFFER        *ppShader,
  _Out_       LPD3DXBUFFER        *ppErrorMsgs,
  _Out_       LPD3DXCONSTANTTABLE *ppConstantTable
);
```



## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to a string that contains the shader.

</dd> <dt>

*srcDataLen* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Length of the data in bytes.

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

*pFunctionName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to a string that contains the name of the shader entry point function where execution begins.

</dd> <dt>

*pProfile* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to a shader profile which determines the shader instruction set. See [**D3DXGetVertexShaderProfile**](d3dxgetvertexshaderprofile.md) or [**D3DXGetPixelShaderProfile**](d3dxgetpixelshaderprofile.md) for a list of the profiles available.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Compile options identified by various flags. The Direct3D 10 HLSL compiler is now the default. See [D3DXSHADER Flags](d3dxshader-flags.md) for details.

</dd> <dt>

*ppShader* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing the created shader. This buffer contains the compiled shader code, as well as any embedded debug and symbol table information.

</dd> <dt>

*ppErrorMsgs* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Returns a buffer containing a listing of errors and warnings that were encountered during the compile. These are the same messages the debugger displays when running in debug mode. This value may be **NULL**.

</dd> <dt>

*ppConstantTable* \[out\]
</dt> <dd>

Type: **[**LPD3DXCONSTANTTABLE**](id3dxconstanttable.md)\***

Returns an [**ID3DXConstantTable**](id3dxconstanttable.md) interface, which can be used to access shader constants. This value can be **NULL**. If you compile your application as large address aware (that is, you use the /LARGEADDRESSAWARE linker option to handle addresses larger than 2 GB), you cannot use this parameter and must set it to **NULL**. Instead, you must use the [**D3DXGetShaderConstantTableEx**](d3dxgetshaderconstanttableex.md) function to retrieve the shader-constant table that is embedded inside the shader. In this **D3DXGetShaderConstantTableEx** call, you must pass the **D3DXCONSTTABLE\_LARGEADDRESSAWARE** flag to the *Flags* parameter to specify to access up to 4 GB of virtual address space.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Shader.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Shader Functions](dx9-graphics-reference-d3dx-functions-shader.md)
</dt> <dt>

[**D3DXCompileShaderFromFile**](d3dxcompileshaderfromfile.md)
</dt> <dt>

[**D3DXCompileShaderFromResource**](d3dxcompileshaderfromresource.md)
</dt> </dl>

 

 
