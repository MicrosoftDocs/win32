---
Description: Note  Instead of using this legacy function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use the D3DCompile API. Compile a shader or an effect from a resource.
ms.assetid: d291e47d-e04f-4e2d-9d05-9aef8e4fcf7e
title: D3DX10CompileFromResource function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX10CompileFromResource function

> [!Note]  
> Instead of using this legacy function, we recommend that you compile offline by using the Fxc.exe command-line compiler or use the [**D3DCompile**](direct3dhlsl.d3dcompile) API.

 

Compile a shader or an effect from a resource.

## Syntax


```C++
HRESULT D3DX10CompileFromResource(
  _In_        HMODULE            hSrcModule,
  _In_        LPCTSTR            pSrcResource,
  _In_        LPCTSTR            pSrcFileName,
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

*hSrcModule* \[in\]
</dt> <dd>

Type: **[**HMODULE**](winprog.windows_data_types)**

Handle to the resource module containing the shader. HMODULE can be obtained with [GetModuleHandle Function](http://msdn.microsoft.com/en-us/library/ms683199.aspx).

</dd> <dt>

*pSrcResource* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Name of the resource containing the shader. If the compiler settings require Unicode, the data type LPCTSTR resolves to LPCWSTR. Otherwise, the data type resolves to LPCSTR.

</dd> <dt>

*pSrcFileName* \[in\]
</dt> <dd>

Type: **[**LPCTSTR**](winprog.windows_data_types)**

Optional. Effect file name, which is used for error messages only. Can be **NULL**.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const [**D3D10\_SHADER\_MACRO**](/windows/win32/D3D10Shader/?branch=master)\***

Optional. Pointer to an array of macro definitions (see [**D3D10\_SHADER\_MACRO**](/windows/win32/D3D10Shader/?branch=master)). The last structure in the array serves as a terminator and must have all members set to 0. If not used, set *pDefines* to **NULL**.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3D10INCLUDE**](/windows/win32/D3D10Shader/?branch=master)**

Optional. Pointer to an [**ID3D10Include Interface**](/windows/win32/D3D10Shader/?branch=master) interface for handling include files. Setting this to **NULL** will cause a compile error if a shader contains a \#include.

</dd> <dt>

*pFunctionName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Name of the shader-entry point function where shader execution begins. When you compile an effect, **D3DX10CompileFromResource** ignores *pFunctionName*; we recommend that you set *pFunctionName* to **NULL** because it is good programming practice to set a pointer parameter to **NULL** if the called function will not use it.

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

[Effect compile flags](d3d10-graphics-reference-effect-constants.md). When you compile a shader and not an effect file, **D3DX10CompileFromResource** ignores *Flags2*; we recommend that you set *Flags2* to zero because it is good programming practice to set a nonpointer parameter to zero if the called function will not use it.

</dd> <dt>

*pPump* \[in\]
</dt> <dd>

Type: **[**ID3DX10ThreadPump**](id3dx10threadpump.md)\***

A pointer to a thread pump interface (see [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md)). Use **NULL** to specify that this function should not return until it is completed.

</dd> <dt>

*ppShader* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master)\*\***

A pointer to an [**ID3D10Blob Interface**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master) which contains the compiled shader, as well as any embedded debug and symbol-table information.

</dd> <dt>

*ppErrorMsgs* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master)\*\***

A pointer to an [**ID3D10Blob Interface**](/windows/win32/D3DCommon/nn-d3dcommon-id3d10blob?branch=master) which contains a listing of errors and warnings that occurred during compilation. These errors and warnings are identical to the debug output from a debugger.

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

 

 




