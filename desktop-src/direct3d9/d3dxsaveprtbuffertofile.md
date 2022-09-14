---
description: Saves a precomputed radiance transfer (PRT) buffer to disk.
ms.assetid: 1fca69bd-6729-45af-981f-b7480c741bc2
title: D3DXSavePRTBufferToFile function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSavePRTBufferToFile
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSavePRTBufferToFile function

Saves a precomputed radiance transfer (PRT) buffer to disk.

## Syntax

```cpp
HRESULT D3DXSavePRTBufferToFile(
  _In_ LPCSTR          pFileName,
  _In_ LPD3DXPRTBUFFER pBuffer
);
```

## Parameters

*pFileName* \[in\]

Type: **[LPCSTR](../winprog/windows-data-types.md)**

Name of the file to which the buffer is to be saved.

*pBuffer* \[in\]

Type: **[LPD3DXPRTBUFFER](id3dxprtbuffer.md)**

Address of a pointer to the input [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object.

## Return value

Type: **[HRESULT](../com/structure-of-com-error-codes.md)**

If the method succeeds, the return value is **D3D\_OK**. If the method fails, the return value can be **D3DERR\_INVALIDCALL**.

## Remarks

The compiler setting also determines the function version. If Unicode is defined, then the function call resolves to [D3DXSavePRTBufferToFileW](). Otherwise, the function call resolves to **D3DXSavePRTBufferToFileA**.

The PRT file format is a binary file in the form of a header and then a data block.

```cpp
struct PRTHeader
{
    UINT NumSamples;
    UINT NumCoeffs;
    UINT NumChannels;
    UINT TexWidth;
    UINT TexHeight;
    UINT bIsTex;
};
```

For the case of *bIsTex* being non-zero, *NumSamples* should equal `TexWidth * TexHeight`.

The data block that follows the header is `NumSamples * NumCoeffs * NumChannels * sizeof(float)` bytes.

## Requirements

| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |

## See also

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
