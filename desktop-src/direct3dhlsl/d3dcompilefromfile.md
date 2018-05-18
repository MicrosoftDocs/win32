---
title: D3DCompileFromFile function
description: Compiles Microsoft High Level Shader Language (HLSL) code into bytecode for a given target.
ms.assetid: '09F1DB4F-C279-4E25-8A1C-34272EB62C07'
keywords: ["D3DCompileFromFile function HLSL"]
topic_type:
- apiref
api_name:
- D3DCompileFromFile
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
---

# D3DCompileFromFile function

> [!Note]  
> You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store. Refer to the section, "Compiling shaders for UWP", in the remarks for [**D3DCompile2**](d3dcompile2.md).

 

Compiles Microsoft High Level Shader Language (HLSL) code into bytecode for a given target.

## Syntax

``` syntax
HRESULT WINAPI D3DCompileFromFile(
  in      LPCWSTR pFileName,
  in_opt  const D3D_SHADER_MACRO pDefines,
  in_opt  ID3DInclude pInclude,
  in      LPCSTR pEntrypoint,
  in      LPCSTR pTarget,
  in      UINT Flags1,
  in      UINT Flags2,
  out     ID3DBlob ppCode,
  out_opt ID3DBlob ppErrorMsgs
);
```

## Parameters

<dl> <dt>

*pFileName* \[in\]
</dt> <dd>

A pointer to a constant null-terminated string that contains the name of the file that contains the shader code.

</dd> <dt>

*pDefines* \[in, optional\]
</dt> <dd>

An optional array of [**D3D\_SHADER\_MACRO**](https://msdn.microsoft.com/library/windows/desktop/ff728732) structures that define shader macros. Each macro definition contains a name and a NULL-terminated definition. If not used, set to **NULL**.

</dd> <dt>

*pInclude* \[in, optional\]
</dt> <dd>

An optional pointer to an [**ID3DInclude**](https://msdn.microsoft.com/library/windows/desktop/ff728746) interface that the compiler uses to handle include files. If you set this parameter to **NULL** and the shader contains a \#include, a compile error occurs. You can pass the **D3D\_COMPILE\_STANDARD\_FILE\_INCLUDE** macro, which is a pointer to a default include handler. This default include handler includes files that are relative to the current directory.


```
#define D3D_COMPILE_STANDARD_FILE_INCLUDE ((ID3DInclude*)(UINT_PTR)1)
```



</dd> <dt>

*pEntrypoint* \[in\]
</dt> <dd>

A pointer to a constant null-terminated string that contains the name of the shader entry point function where shader execution begins. When you compile an effect, **D3DCompileFromFile** ignores *pEntrypoint*; we recommend that you set *pEntrypoint* to **NULL** because it is good programming practice to set a pointer parameter to **NULL** if the called function will not use it.

</dd> <dt>

*pTarget* \[in\]
</dt> <dd>

A pointer to a constant null-terminated string that specifies the shader target or set of shader features to compile against. The shader target can be a shader model (for example, shader model 2, shader model 3, shader model 4, or shader model 5 and later). The target can also be an effect type (for example, fx\_4\_1). For info about the targets that various profiles support, see [Specifying Compiler Targets](specifying-compiler-targets.md).

</dd> <dt>

*Flags1* \[in\]
</dt> <dd>

A combination of shader [**compile options**](d3dcompile-constants.md) that are combined by using a bitwise **OR** operation. The resulting value specifies how the compiler compiles the HLSL code.

</dd> <dt>

*Flags2* \[in\]
</dt> <dd>

A combination of effect [**compile options**](d3dcompile-effect-constants.md) that are combined by using a bitwise **OR** operation. The resulting value specifies how the compiler compiles the effect. When you compile a shader and not an effect file, **D3DCompileFromFile** ignores *Flags2*; we recommend that you set *Flags2* to zero because it is good programming practice to set a nonpointer parameter to zero if the called function will not use it.

</dd> <dt>

*ppCode* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that you can use to access the compiled code.

</dd> <dt>

*ppErrorMsgs* \[out, optional\]
</dt> <dd>

An optional pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that you can use to access compiler error messages, or **NULL** if there are no errors.

</dd> </dl>

## Return value

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

> [!Note]  
> The D3dcompiler\_44.dll or later version of the file contains the **D3DCompileFromFile** compiler function.

 

## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3DCompiler.lib</dt> </dl>     |
| DLL<br/>     | <dl> <dt>D3DCompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





