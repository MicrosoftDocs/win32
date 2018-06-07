---
title: D3DCompile function
description: Compile HLSL code or an effect file into bytecode for a given target.
ms.assetid: feb3d4d1-06ce-4141-9267-c6c771659aa7
keywords:
- D3DCompile function HLSL
topic_type:
- apiref
api_name:
- D3DCompile
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DCompile function

Compile HLSL code or an effect file into bytecode for a given target.

## Syntax

``` syntax
HRESULT WINAPI D3DCompile(
  in      LPCVOID pSrcData,
  in      SIZE_T SrcDataSize,
  in_opt  LPCSTR pSourceName,
  in_opt  const D3D_SHADER_MACRO pDefines,
  in_opt  ID3DInclude pInclude,
  in_opt  LPCSTR pEntrypoint,
  in      LPCSTR pTarget,
  in      UINT Flags1,
  in      UINT Flags2,
  out     ID3DBlob ppCode,
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

You can use this parameter for strings that specify error messages. If not used, set to **NULL**.

</dd> <dt>

*pDefines* \[in, optional\]
</dt> <dd>

Type: **const [**D3D\_SHADER\_MACRO**](https://msdn.microsoft.com/library/windows/desktop/ff728732)\***

An array of NULL-terminated macro definitions (see [**D3D\_SHADER\_MACRO**](https://msdn.microsoft.com/library/windows/desktop/ff728732)).

</dd> <dt>

*pInclude* \[in, optional\]
</dt> <dd>

Type: **[**ID3DInclude**](https://msdn.microsoft.com/library/windows/desktop/ff728746)\***

Optional. A pointer to an [**ID3DInclude**](https://msdn.microsoft.com/library/windows/desktop/ff728746) for handling include files. Setting this to **NULL** will cause a compile error if a shader contains a \#include. You can pass the **D3D\_COMPILE\_STANDARD\_FILE\_INCLUDE** macro, which is a pointer to a default include handler. This default include handler includes files that are relative to the current directory and files that are relative to the directory of the initial source file. When you use **D3D\_COMPILE\_STANDARD\_FILE\_INCLUDE**, you must specify the source file name in the *pSourceName* parameter; the compiler will derive the initial relative directory from *pSourceName*.


```C++
#define D3D_COMPILE_STANDARD_FILE_INCLUDE ((ID3DInclude*)(UINT_PTR)1)
```



</dd> <dt>

*pEntrypoint* \[in, optional\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The name of the shader entry point function where shader execution begins. When you compile using a fx profile (for example, fx\_4\_0, fx\_5\_0, and so on), **D3DCompile** ignores *pEntrypoint*. In this case, we recommend that you set *pEntrypoint* to **NULL** because it is good programming practice to set a pointer parameter to **NULL** if the called function will not use it. For all other shader profiles, a valid *pEntrypoint* is required.

</dd> <dt>

*pTarget* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A string that specifies the shader target or set of shader features to compile against. The shader target can be shader model 2, shader model 3, shader model 4, or shader model 5. The target can also be an effect type (for example, fx\_4\_1). For info about the targets that various profiles support, see [Specifying Compiler Targets](specifying-compiler-targets.md).

</dd> <dt>

*Flags1* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags defined by [**D3D compile constants**](d3dcompile-constants.md).

</dd> <dt>

*Flags2* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags defined by [**D3D compile effect constants**](d3dcompile-effect-constants.md). When you compile a shader and not an effect file, **D3DCompile** ignores *Flags2*; we recommend that you set *Flags2* to zero because it is good programming practice to set a nonpointer parameter to zero if the called function will not use it.

</dd> <dt>

*ppCode* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that you can use to access the compiled code.

</dd> <dt>

*ppErrorMsgs* \[out, optional\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that you can use to access compiler error messages, or **NULL** if there are no errors.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

The difference between **D3DCompile** and [**D3DCompile2**](d3dcompile2.md) is that the latter method takes some optional parameters that can be used to control some aspects of how bytecode is generated. If this extra flexibility is not required, there is no performance gain from using **D3DCompile2**.

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

 

 





