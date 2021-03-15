---
description: Computes locally-deformable precomputed radiance transfer (LDPRT) coefficients relative to per-sample normal vectors to minimize the least-squares error with respect to input ID3DXPRTBuffer data.
ms.assetid: 302c20cd-d495-4a23-9692-7456355471eb
title: ID3DXPRTEngine::ComputeLDPRTCoeffs method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.ComputeLDPRTCoeffs
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::ComputeLDPRTCoeffs method

Computes locally-deformable precomputed radiance transfer (LDPRT) coefficients relative to per-sample normal vectors to minimize the least-squares error with respect to input [**ID3DXPRTBuffer**](id3dxprtbuffer.md) data. These coefficients can be used with skinned or transformed normal vectors to model global effects on dynamic objects.

## Syntax


```C++
HRESULT ComputeLDPRTCoeffs(
  [in]      LPD3DXPRTBUFFER pDataIn,
  [in]      UINT            Order,
  [in, out] D3DXVECTOR3     *pNormOut,
  [in, out] LPD3DXPRTBUFFER pDataOut
);
```



## Parameters

<dl> <dt>

*pDataIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an input [**ID3DXPRTBuffer**](id3dxprtbuffer.md) spherical harmonic (SH) precomputed radiance transfer (PRT) data object.

</dd> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Order of the SH evaluation. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*pNormOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](d3dxvector3.md)\***

Optional vector array to be filled with shader-optimal normal vectors for which LDPRT coefficients are optimized. This array must be the same size as the number of samples in pDataIn. If **NULL**, surface normal vectors are used.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an output [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that contains Order zonal harmonic coefficients per color channel per sample.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Solutions for shading normal vectors can optionally be obtained with this method. These normal vectors, along with the LDPRT coefficients, can more accurately represent the PRT signal. In this case, the coefficients represent zonal harmonics oriented in the normal direction.

This method cannot be used with results from [**ID3DXPRTEngine::ComputeSurfSamplesBounce**](id3dxprtengine--computesurfsamplesbounce.md) or [**ID3DXPRTEngine::ComputeSurfSamplesDirectSH**](id3dxprtengine--computesurfsamplesdirectsh.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 
