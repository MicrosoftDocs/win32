---
title: D3DPreprocess function
description: Preprocesses uncompiled HLSL code.
ms.assetid: cb49749f-d837-4a0c-8c6e-d67b0b6206a2
keywords:
- D3DPreprocess function HLSL
topic_type:
- apiref
api_name:
- D3DPreprocess
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
ms.topic: article
ms.date: 05/31/2018
---

# D3DPreprocess function

Preprocesses uncompiled HLSL code.

## Syntax

``` syntax
HRESULT WINAPI D3DPreprocess(
  in      LPCVOID pSrcData,
  in      SIZE_T SrcDataSize,
  in_opt  LPCSTR pSourceName,
  in_opt  const D3D_SHADER_MACRO pDefines,
  in_opt  ID3DInclude pInclude,
  out     ID3DBlob ppCodeText,
  out_opt ID3DBlob ppErrorMsgs
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to uncompiled shader data; either ASCII HLSL code or a compiled effect.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Length of *pSrcData*.

</dd> <dt>

*pSourceName* \[in, optional\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The name of the file that contains the uncompiled HLSL code.

</dd> <dt>

*pDefines* \[in, optional\]
</dt> <dd>

Type: **const [**D3D\_SHADER\_MACRO**](https://msdn.microsoft.com/library/windows/desktop/ff728732)\***

An array of NULL-terminated macro definitions (see [**D3D\_SHADER\_MACRO**](https://msdn.microsoft.com/library/windows/desktop/ff728732)).

</dd> <dt>

*pInclude* \[in, optional\]
</dt> <dd>

Type: **[**ID3DInclude**](https://msdn.microsoft.com/library/windows/desktop/ff728746)\***

A pointer to an [**ID3DInclude**](https://msdn.microsoft.com/library/windows/desktop/ff728746) for handling include files. Setting this to **NULL** will cause a compile error if a shader contains a \#include. You can pass the **D3D\_COMPILE\_STANDARD\_FILE\_INCLUDE** macro, which is a pointer to a default include handler. This default include handler includes files that are relative to the current directory and files that are relative to the directory of the initial source file. When you use **D3D\_COMPILE\_STANDARD\_FILE\_INCLUDE**, you must specify the source file name in the *pSourceName* parameter; the compiler will derive the initial relative directory from *pSourceName*.


```C++
#define D3D_COMPILE_STANDARD_FILE_INCLUDE ((ID3DInclude*)(UINT_PTR)1)
```



</dd> <dt>

*ppCodeText* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

The address of a [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) that contains the compiled code.

</dd> <dt>

*ppErrorMsgs* \[out, optional\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to an [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) that contains compiler error messages, or **NULL** if there were no errors.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

**D3DPreprocess** outputs [\#line](dx-graphics-hlsl-appendix-pre-line.md) directives and preserves line numbering of source input so that output line numbering can be properly related to the input source.

## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3dcompiler\_47.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3dcompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





