---
title: D3DDisassembleRegion function
description: Disassembles a specific region of compiled Microsoft High Level Shader Language (HLSL) code.
ms.assetid: 4813FF62-42FA-425D-9C24-9E472F04E35B
keywords:
- D3DDisassembleRegion function HLSL
topic_type:
- apiref
api_name:
- D3DDisassembleRegion
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
ms.topic: article
ms.date: 05/31/2018
---

# D3DDisassembleRegion function

Disassembles a specific region of compiled Microsoft High Level Shader Language (HLSL) code.

## Syntax

``` syntax
HRESULT WINAPI D3DDisassembleRegion(
  in      LPCVOID pSrcData,
  in      SIZE_T SrcDataSize,
  in      UINT Flags,
  in_opt  LPCSTR szComments,
  in      SIZE_T StartByteOffset,
  in      SIZE_T NumInsts,
  out_opt SIZE_T pFinishByteOffset,
  out     ID3DBlob ppDisassembly
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

A pointer to compiled shader data.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

The size, in bytes, of the block of memory that *pSrcData* points to.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

A combination of zero or more of the following flags that are combined by using a bitwise **OR** operation. The resulting value specifies how **D3DDisassembleRegion** disassembles the compiled shader data.



| Flag                                               | Description                                                                                                                                                                                                                |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D\_DISASM\_ENABLE\_COLOR\_CODE (0x01)            | Enable the output of color codes.                                                                                                                                                                                          |
| D3D\_DISASM\_ENABLE\_DEFAULT\_VALUE\_PRINTS (0x02) | Enable the output of default values.                                                                                                                                                                                       |
| D3D\_DISASM\_ENABLE\_INSTRUCTION\_NUMBERING (0x04) | Enable instruction numbering.                                                                                                                                                                                              |
| D3D\_DISASM\_ENABLE\_INSTRUCTION\_CYCLE (0x08)     | No effect.                                                                                                                                                                                                                 |
| D3D\_DISASM\_DISABLE\_DEBUG\_INFO (0x10)           | Disable the output of debug information.                                                                                                                                                                                   |
| D3D\_DISASM\_ENABLE\_INSTRUCTION\_OFFSET (0x20)    | Enable the output of instruction offsets.                                                                                                                                                                                  |
| D3D\_DISASM\_INSTRUCTION\_ONLY (0x40)              | This flag has no effect in **D3DDisassembleRegion**. Cycle information comes from the trace; therefore, cycle information is available only in [**D3DDisassemble11Trace**](d3ddisassemble11trace.md)'s trace disassembly. |



 

</dd> <dt>

*szComments* \[in, optional\]
</dt> <dd>

A pointer to a constant null-terminated string at the top of the shader that identifies the shader constants and variables.

</dd> <dt>

*StartByteOffset* \[in\]
</dt> <dd>

The number of bytes offset into the compiled shader data where **D3DDisassembleRegion** starts the disassembly.

</dd> <dt>

*NumInsts* \[in\]
</dt> <dd>

The number of instructions to disassemble.

</dd> <dt>

*pFinishByteOffset* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives the number of bytes offset into the compiled shader data where **D3DDisassembleRegion** finishes the disassembly.

</dd> <dt>

*ppDisassembly* \[out\]
</dt> <dd>

A pointer to a buffer that receives the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that accesses the disassembled HLSL code.

</dd> </dl>

## Return value

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

> [!Note]  
> The D3dcompiler\_44.dll or later version of the file contains the **D3DDisassembleRegion** compiler function.

 

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

 

 





