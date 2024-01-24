---
description: Creates a precomputed radiance transfer (PRT) buffer that can be compressed or filled by a simulator. This function should be used to create per-vertex or volume buffers.
ms.assetid: f79a3691-ab5f-4404-aafd-f9635ff88e71
title: D3DXCreatePRTBuffer function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCreatePRTBuffer
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXCreatePRTBuffer function

Creates a precomputed radiance transfer (PRT) buffer that can be compressed or filled by a simulator. This function should be used to create per-vertex or volume buffers.

## Syntax


```C++
HRESULT D3DXCreatePRTBuffer(
  _In_    UINT            NumSamples,
  _In_    UINT            NumCoeffs,
  _In_    UINT            NumChannels,
  _Inout_ LPD3DXPRTBUFFER *ppBuffer
);
```



## Parameters

<dl> <dt>

*NumSamples* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of vertices (or texels) sampled.

</dd> <dt>

*NumCoeffs* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of coefficients per sample location. When using spherical harmonic (SH) PRT, the number of coefficients should be Order², where Order is the order of the SH evaluation. Order must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The degree of the evaluation is Order - 1.

</dd> <dt>

*NumChannels* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of color channels to set in the mesh. Set to 1 to specify gray materials (R = G = B), or 3 to enable color bleeding effects.

</dd> <dt>

*ppBuffer* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)\***

Address of a pointer to the created [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of these: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

When the buffer is created, all values are initialized to zero.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> <dt>

[**D3DXCreatePRTBufferTex**](d3dxcreateprtbuffertex.md)
</dt> </dl>

 

 
