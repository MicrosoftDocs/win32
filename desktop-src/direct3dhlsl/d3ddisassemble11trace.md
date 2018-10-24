---
title: D3DDisassemble11Trace function
description: Disassembles a section of compiled Microsoft High Level Shader Language (HLSL) code that is specified by shader trace steps.
ms.assetid: 983D5530-E220-42BE-9210-16E5A789CEE1
keywords:
- D3DDisassemble11Trace function HLSL
topic_type:
- apiref
api_name:
- D3DDisassemble11Trace
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DDisassemble11Trace function

Disassembles a section of compiled Microsoft High Level Shader Language (HLSL) code that is specified by shader trace steps.

## Syntax

``` syntax
HRESULT WINAPI D3DDisassemble11Trace(
  in  LPCVOID pSrcData,
  in  SIZE_T SrcDataSize,
  in  ID3D11ShaderTrace pTrace,
  in  UINT StartStep,
  in  UINT NumSteps,
  in  UINT Flags,
  out ID3DBlob ppDisassembly
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to compiled shader data.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The size, in bytes, of the block of memory that *pSrcData* points to.

</dd> <dt>

*pTrace* \[in\]
</dt> <dd>

Type: **[**ID3D11ShaderTrace**](https://msdn.microsoft.com/library/windows/desktop/hh446840)\***

A pointer to the [**ID3D11ShaderTrace**](https://msdn.microsoft.com/library/windows/desktop/hh446840) interface for the shader trace information object.

</dd> <dt>

*StartStep* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of the step in the trace from which **D3DDisassemble11Trace** starts the disassembly.

</dd> <dt>

*NumSteps* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of trace steps to disassemble.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A combination of zero or more of the following flags that are combined by using a bitwise **OR** operation. The resulting value specifies how **D3DDisassemble11Trace** disassembles the compiled shader data.



| Flag                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D\_DISASM\_ENABLE\_COLOR\_CODE (0x01)            | Enable the output of color codes.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| D3D\_DISASM\_ENABLE\_DEFAULT\_VALUE\_PRINTS (0x02) | Enable the output of default values.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| D3D\_DISASM\_ENABLE\_INSTRUCTION\_NUMBERING (0x04) | Enable instruction numbering.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| D3D\_DISASM\_ENABLE\_INSTRUCTION\_CYCLE (0x08)     | No effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| D3D\_DISASM\_DISABLE\_DEBUG\_INFO (0x10)           | Disable the output of debug information.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| D3D\_DISASM\_ENABLE\_INSTRUCTION\_OFFSET (0x20)    | Enable the output of instruction offsets.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| D3D\_DISASM\_INSTRUCTION\_ONLY (0x40)              | Enable the output of the instruction cycle per step in **D3DDisassemble11Trace**. <br/> This flag is similar to the D3D\_DISASM\_ENABLE\_INSTRUCTION\_NUMBERING and D3D\_DISASM\_ENABLE\_INSTRUCTION\_OFFSET flags.<br/> This flag has no effect in the [**D3DDisassembleRegion**](d3ddisassembleregion.md) function. Cycle information comes from the trace; therefore, cycle information is available only in the trace disassembly.<br/> |



 

</dd> <dt>

*ppDisassembly* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a buffer that receives the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that accesses the disassembled HLSL code.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

**D3DDisassemble11Trace** walks the steps of a shader trace and outputs appropriate disassembly for each step that is based on the step's instruction index. The disassembly is annotated with register-value information from the trace. The behavior of **D3DDisassemble11Trace** differs from [**D3DDisassemble**](d3ddisassemble.md) in that instead of the static disassembly of a compiled shader that **D3DDisassemble** performs, **D3DDisassemble11Trace** provides an execution trace that is based on the shader trace information.

> [!Note]  
> The D3dcompiler\_44.dll or later version of the file contains the **D3DDisassemble11Trace** compiler function.

 

## Requirements



|                    |                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3D11ShaderTracing.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DCompiler.lib</dt> </dl>      |
| DLL<br/>     | <dl> <dt>D3DCompiler\_47.dll</dt> </dl>  |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> </dl>

 

 





