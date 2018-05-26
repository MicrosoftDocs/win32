---
title: D3DX11CreateAsyncCompilerProcessor function
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks. Create an asynchronous-data processor for a shader.
ms.assetid: 90756ac3-946d-49fa-9f97-70dc5da812c6
keywords:
- D3DX11CreateAsyncCompilerProcessor function Direct3D 11
topic_type:
- apiref
api_name:
- D3DX11CreateAsyncCompilerProcessor
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DX11CreateAsyncCompilerProcessor function

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. See Remarks.

 

Create an asynchronous-data processor for a shader.

## Syntax


```C++
HRESULT D3DX11CreateAsyncCompilerProcessor(
  _In_        LPCSTR               pFileName,
  _In_  const D3D11_SHADER_MACRO   *pDefines,
  _In_        LPD3D10INCLUDE       pInclude,
  _In_        LPCSTR               pFunctionName,
  _In_        LPCSTR               pProfile,
  _In_        UINT                 Flags1,
  _In_        UINT                 Flags2,
  _Out_       ID3D10Blob           **ppCompiledShader,
  _Out_       ID3D10Blob           **ppErrorBuffer,
  _Out_       ID3DX11DataProcessor **ppDataProcessor
);
```



## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A string that contains the shader filename.

</dd> <dt>

*pDefines* \[in\]
</dt> <dd>

Type: **const D3D11\_SHADER\_MACRO\***

A NULL-terminated array of shader macros; set this to **NULL** to specify no macros.

</dd> <dt>

*pInclude* \[in\]
</dt> <dd>

Type: **[**LPD3D10INCLUDE**](https://msdn.microsoft.com/library/windows/desktop/bb173775)**

A pointer to an include interface. This parameter can be **NULL**.

</dd> <dt>

*pFunctionName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Name of the shader-entry point function where shader execution begins. When you compile an effect, **D3DX11CreateAsyncCompilerProcessor** ignores *pFunctionName*; we recommend that you set *pFunctionName* to **NULL** because it is good programming practice to set a pointer parameter to **NULL** if the called function will not use it..

</dd> <dt>

*pProfile* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A string that specifies the shader profile or shader model; can be any profile in shader model 2, shader model 3, shader model 4, or shader model 5. The profile can also be for effect type (for example, fx\_4\_1).

</dd> <dt>

*Flags1* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Shader compile flags.

</dd> <dt>

*Flags2* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Effect compile flags. When you compile a shader and not an effect file, **D3DX11CreateAsyncCompilerProcessor** ignores *Flags2*; we recommend that you set *Flags2* to zero because it is good programming practice to set a nonpointer parameter to zero if the called function will not use it.

</dd> <dt>

*ppCompiledShader* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](https://msdn.microsoft.com/library/windows/desktop/bb173507)\*\***

Address of a pointer to the compiled effect.

</dd> <dt>

*ppErrorBuffer* \[out\]
</dt> <dd>

Type: **[**ID3D10Blob**](https://msdn.microsoft.com/library/windows/desktop/bb173507)\*\***

Address of a pointer to compile errors.

</dd> <dt>

*ppDataProcessor* \[out\]
</dt> <dd>

Type: **[**ID3DX11DataProcessor**](id3dx11dataprocessor.md)\*\***

Address of a pointer to a buffer that contains the data processor created (see [**ID3DX11DataProcessor Interface**](id3dx11dataprocessor.md)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 11 Return Codes](d3d11-graphics-reference-returnvalues.md).

## Remarks

There s no implementation of the  async loader  outside of D3DX 10, and D3DX 11.

For Windows Store apps, the DirectX samples (for example, the [Direct3D tutorial sample](http://go.microsoft.com/fwlink/p/?linkid=255263)) include the **BasicLoader** module that uses the Windows Runtime asynchronous programming model ([**AsyncBase**](64259b9b-f427-4ffd-a611-e7a2f82362b2)).

For Win32 desktop apps, you can use the [Concurrency Runtime](56237d96-10b0-494a-9cb4-f5c5090436c5) to implement something similar to the Windows Runtime asynchronous programming model.

## Requirements



|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX11async.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX11.lib</dt> </dl>    |



## See also

<dl> <dt>

[D3DX Functions](d3d11-graphics-reference-d3dx11-functions.md)
</dt> </dl>

 

 





