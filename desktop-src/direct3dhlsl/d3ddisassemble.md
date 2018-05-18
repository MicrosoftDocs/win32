---
title: D3DDisassemble function
description: Disassembles compiled HLSL code.
ms.assetid: '0b5cfe31-1277-4923-a6e2-7e020019b74c'
keywords: ["D3DDisassemble function HLSL"]
topic_type:
- apiref
api_name:
- D3DDisassemble
api_location:
- d3dcompiler_47.dll
api_type:
- DllExport
---

# D3DDisassemble function

Disassembles compiled HLSL code.

## Syntax

``` syntax
HRESULT WINAPI D3DDisassemble(
  in     LPCVOID pSrcData,
  in     SIZE_T SrcDataSize,
  in     UINT Flags,
  in_opt LPCSTR szComments,
  out    ID3DBlob ppDisassembly
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to source data as compiled HLSL code.

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Length of *pSrcData*.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

Flags affecting the behavior of **D3DDisassemble**. *Flags* can be a combination of zero or more of the following values.



| Flag                                            | Description                          |
|-------------------------------------------------|--------------------------------------|
| **D3D\_DISASM\_ENABLE\_COLOR\_CODE**            | Enable the output of color codes.    |
| **D3D\_DISASM\_ENABLE\_DEFAULT\_VALUE\_PRINTS** | Enable the output of default values. |
| **D3D\_DISASM\_ENABLE\_INSTRUCTION\_NUMBERING** | Enable instruction numbering.        |
| **D3D\_DISASM\_ENABLE\_INSTRUCTION\_CYCLE**     | No effect.                           |
| **D3D\_DISASM\_DISABLE\_DEBUG\_INFO**           | Disable debug information.           |
| **D3D\_DISASM\_ENABLE\_INSTRUCTION\_OFFSET**    | Enable instruction offsets.          |
| **D3D\_DISASM\_INSTRUCTION\_ONLY**              | Disassemble instructions only.       |
| **D3D\_DISASM\_PRINT\_HEX\_LITERALS**           | Use hex symbols in disassemblies.    |



 

</dd> <dt>

*szComments* \[in, optional\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The comment string at the top of the shader that identifies the shader constants and variables.

</dd> <dt>

*ppDisassembly* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a buffer that receives the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that accesses assembly text.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

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

 

 





