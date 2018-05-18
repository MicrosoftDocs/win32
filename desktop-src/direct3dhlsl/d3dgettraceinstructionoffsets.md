---
title: D3DGetTraceInstructionOffsets function
description: Retrieves the byte offsets for instructions within a section of shader code.
ms.assetid: '9E27C70C-C266-48A6-81C7-E9A5E430B48B'
keywords: ["D3DGetTraceInstructionOffsets function HLSL"]
topic_type:
- apiref
api_name:
- D3DGetTraceInstructionOffsets
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
---

# D3DGetTraceInstructionOffsets function

Retrieves the byte offsets for instructions within a section of shader code.

## Syntax

``` syntax
HRESULT WINAPI D3DGetTraceInstructionOffsets(
  in      LPCVOID pSrcData,
  in      SIZE_T SrcDataSize,
  in      UINT Flags,
  in      SIZE_T StartInstIndex,
  in      SIZE_T NumInsts,
  out_opt SIZE_T pOffsets,
  out_opt SIZE_T pTotalInsts
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

A pointer to the compiled shader data.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

The size, in bytes, of the block of memory that *pSrcData* points to.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

A combination of the following flags that are combined by using a bitwise **OR** operation. The resulting value specifies how **D3DGetTraceInstructionOffsets** retrieves the instruction offsets.



| Flag                                                     | Description                                               |
|----------------------------------------------------------|-----------------------------------------------------------|
| D3D\_GET\_INST\_OFFSETS\_INCLUDE\_NON\_EXECUTABLE (0x01) | Include non-executable code in the retrieved information. |



 

</dd> <dt>

*StartInstIndex* \[in\]
</dt> <dd>

The index of the instruction in the compiled shader data for which **D3DGetTraceInstructionOffsets** starts to retrieve the byte offsets.

</dd> <dt>

*NumInsts* \[in\]
</dt> <dd>

The number of instructions for which **D3DGetTraceInstructionOffsets** retrieves the byte offsets.

</dd> <dt>

*pOffsets* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives the actual number of offsets.

</dd> <dt>

*pTotalInsts* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives the total number of instructions in the section of shader code.

</dd> </dl>

## Return value

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

A new kind of Microsoft High Level Shader Language (HLSL) debugging information from a program database (PDB) file uses instruction-byte offsets within a shader blob (arbitrary-length data buffer). You use **D3DGetTraceInstructionOffsets** to translate to and from instruction indexes.

> [!Note]  
> The D3dcompiler\_44.dll or later version of the file contains the **D3DGetTraceInstructionOffsets** compiler function.

 

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

 

 





