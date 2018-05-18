---
Description: 'Note  Instead of using this legacy function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use the D3DCompile API. Compile a shader or an effect that is loaded in memory.'
ms.assetid: 'c6458d82-a649-402c-8180-5b7320f9fdb0'
title: D3DX10CompileFromMemory function
---

# D3DX10CompileFromMemory function

> [!Note]  
> Instead of using this legacy function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use the [**D3DCompile**](direct3dhlsl.d3dcompile) API.

 

Compile a shader or an effect that is loaded in memory.

## Syntax


```C++
HRESULT D3DX10CompileFromMemory(
  _In_        LPCSTR             pSrcData,
  _In_        SIZE_T             SrcDataLen,
  _In_        LPCSTR             pFileName,
  _In_  const D3D10_SHADER_MACRO *pDefines,
  _In_        LPD3D10INCLUDE     pInclude,
  _In_        LPCSTR             pFunctionName,
  _In_        LPCSTR             pProfile,
  _In_        UINT               Flags1,
  _In_        UINT               Flags2,
  _In_        ID3DX10ThreadPump  *pPump,
  _Out_       ID3D10Blob         **ppShader,
  _Out_       ID3D10Blob         **ppErrorMsgs,
  _Out_       HRESULT            *pHResult
);
```



## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Pointer to the shader in memory.

</dd> <dt>

*SrcDataLen* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](winprog.windows_data_types)**

Size of the shader in memory.

</dd> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

The name of the file that contains the shader code.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3D10\_SHADER\_MACRO**](d3d10-shader-macro.md)\***

Optional. Pointer to an array of macro definitions (see [**D3D10\_SHADER\_MACRO**](d3d10-shader-macro.md)). The last structure in the array serves as a terminator and must have all members set to 0. If not used, set *pDefines* to **NULL**.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3D10INCLUDE**](id3d10include.md)**

Optional. Pointer to an [**ID3D10Include Interface**](id3d10include.md) interface for handling include files. Setting this to **NULL** will cause a compile error if a shader contains a \#include.

</dd> <dt>

*pFunctionName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Name of the shader-entry point function where shader execution begins. When you compile an effect, **D3DX10CompileFromMemory** ignores *pFunctionName*; we recommend that you set *pFunctionName* to **NULL** because it is good programming practice to set a pointer parameter to **NULL** if the called function will not use it.

</dd> <dt>

*pProfile* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

A string that specifies the shader model; can be any profile in [shader model 2](direct3dhlsl.dx_graphics_hlsl_sm2), [shader model 3](direct3dhlsl.dx_graphics_hlsl_sm3), or [shader model 4](direct3dhlsl.dx_graphics_hlsl_sm4).

</dd> <dt>

*Flags1* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

[Shader compile flags](d3d10-shader.md).

</dd> <dt>

*Flags2* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

[Effect compile flags](d3d10-graphics-reference-effect-constants.md). When you compile a shader and not an effect file, **D3DX10CompileFromMemory** ignores *Flags2*; we recommend that you set *Flags2* to zero because it is good programming practice to set a nonpointer parameter to zero if the called function will not use it.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\***

A pointer to a thread pump interface (see [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md)). Use **NULL** to specify that this function should not return until it is completed.

</dd> <dt>

*ppShader* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](id3d10blob.md)\*\***

A pointer to an [**ID3D10Blob Interface**](id3d10blob.md) which contains the compiled shader, as well as any embedded debug and symbol-table information.

</dd> <dt>

*ppErrorMsgs* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](id3d10blob.md)\*\***

A pointer to an [**ID3D10Blob Interface**](id3d10blob.md) which contains a listing of errors and warnings that occurred during compilation. These errors and warnings are identical to the debug output from a debugger.

</dd> <dt>

*pHResult* \[out\]
</dt> <dd>

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)\***

A pointer to the return value. May be **NULL**. If *pPump* is not **NULL**, then *pHResult* must be a valid memory location until the asynchronous execution completes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Async.h</dt> </dl> |



## See also

<dl> <dt>

[General Purpose Functions](d3d10-graphics-reference-d3dx10-functions-general-purpose.md)
</dt> </dl>

 

 




