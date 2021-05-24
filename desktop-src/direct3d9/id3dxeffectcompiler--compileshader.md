---
description: Compiles a shader from an effect that contains one or more functions.
ms.assetid: f34a2975-dcd5-4917-9b11-ed40583272f9
title: ID3DXEffectCompiler::CompileShader method (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXEffectCompiler.CompileShader
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXEffectCompiler::CompileShader method

Compiles a shader from an effect that contains one or more functions.

## Syntax


```C++
HRESULT CompileShader(
  [in]          D3DXHANDLE          hFunction,
  [in]          LPCSTR              pTarget,
  [in]          DWORD               Flags,
  [out, retval] LPD3DXBUFFER        *ppShader,
  [out, retval] LPD3DXBUFFER        *ppErrorMsgs,
  [out]         LPD3DXCONSTANTTABLE *ppConstantTable
);
```



## Parameters

<dl> <dt>

*hFunction* \[in\]
</dt> <dd>

Type: **[D3DXHANDLE](dx9-graphics-reference-effects-constants.md)**

Unique identifier to the function to be compiled. This value must not be **NULL**. See [Handles (Direct3D 9)](handles.md).

</dd> <dt>

*pTarget* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

Pointer to a shader profile which determines the shader instruction set. See [**D3DXGetVertexShaderProfile**](d3dxgetvertexshaderprofile.md) or [**D3DXGetPixelShaderProfile**](d3dxgetpixelshaderprofile.md) for a list of the profiles available.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Compile options identified by various flags. The Direct3D 10 HLSL compiler is now the default. See [D3DXSHADER Flags](d3dxshader-flags.md) for details.

</dd> <dt>

*ppShader* \[out, retval\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing the compiled shader. The compiler shader is an array of DWORDs. For more information about accessing the buffer, see [**ID3DXBuffer**](id3dxbuffer.md).

</dd> <dt>

*ppErrorMsgs* \[out, retval\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing at least the first compile error message that occurred. This includes effect compiler errors and high-level language compile errors. For more information about accessing the buffer, see [**ID3DXBuffer**](id3dxbuffer.md).

</dd> <dt>

*ppConstantTable* \[out\]
</dt> <dd>

Type: **[**LPD3DXCONSTANTTABLE**](id3dxconstanttable.md)\***

Returns an [**ID3DXConstantTable**](id3dxconstanttable.md) interface, which can be used to access shader constants. This value can be **NULL**. If you compile your application as large address aware (that is, you use the /LARGEADDRESSAWARE linker option to handle addresses larger than 2 GB), you cannot use this parameter and must set it to **NULL**. Instead, you must use the [**D3DXGetShaderConstantTableEx**](d3dxgetshaderconstanttableex.md) function to retrieve the shader-constant table that is embedded inside the shader. In this **D3DXGetShaderConstantTableEx** call, you must pass the **D3DXCONSTTABLE\_LARGEADDRESSAWARE** flag to the *Flags* parameter to specify to access up to 4 GB of virtual address space.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK.

If the arguments are invalid, the method will return D3DERR\_INVALIDCALL.

If the method fails, the return value will be E\_FAIL.

## Remarks

Targets can be specified for vertex shaders, pixel shaders, and texture fill functions.



| Targets                      | Functions                                                                      |
|-----------------------|-----------------------------------------------------------------------|
| Vertex shader targets | vs\_1\_1, vs\_2\_0, vs\_2\_sw, vs\_3\_0                               |
| Pixel shader targets  | ps\_1\_1, ps\_1\_2, ps\_1\_3, ps\_1\_4, ps\_2\_0, ps\_2\_sw, ps\_3\_0 |
| Texture fill targets  | tx\_0, tx\_1                                                          |



 

This method compiles a shader from a function that is written in a C-like language. For more information, see [HLSL](../direct3dhlsl/dx-graphics-hlsl.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[ID3DXEffectCompiler](id3dxeffectcompiler.md)
</dt> <dt>

[**D3DXGetShaderConstantTable**](d3dxgetshaderconstanttable.md)
</dt> </dl>

 

 
