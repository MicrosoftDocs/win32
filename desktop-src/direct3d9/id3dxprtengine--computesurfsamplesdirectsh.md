---
description: Computes, at an arbitrary point not on a mesh, a transfer vector that maps source radiance (represented by a spherical harmonic (SH) approximation) to exit radiance.
ms.assetid: 44790465-440d-4426-b780-ed872fbf8efb
title: ID3DXPRTEngine::ComputeSurfSamplesDirectSH method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.ComputeSurfSamplesDirectSH
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::ComputeSurfSamplesDirectSH method

Computes, at an arbitrary point not on a mesh, a transfer vector that maps source radiance (represented by a spherical harmonic (SH) approximation) to exit radiance.

## Syntax


```C++
HRESULT ComputeSurfSamplesDirectSH(
  [in]            UINT            SHOrder,
  [in]            UINT            NumSamples,
  [in]      const D3DXVECTOR3     *pSampleLocs,
  [in]      const D3DXVECTOR3     *pSampleNorms,
  [in, out]       LPD3DXPRTBUFFER pDataOut
);
```



## Parameters

<dl> <dt>

*SHOrder* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Order of the SH approximation to use.

</dd> <dt>

*NumSamples* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of sample locations.

</dd> <dt>

*pSampleLocs* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Position for each sample.

</dd> <dt>

*pSampleNorms* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Normal vector for each sample location.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an output [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that models the direct lighting contribution to the point, using the SH approximation.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Do not use a texture buffer when calling this method.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> <dt>

[**ID3DXPRTEngine::ComputeDirectLightingSH**](id3dxprtengine--computedirectlightingsh.md)
</dt> <dt>

[**ID3DXPRTEngine::ComputeSurfSamplesBounce**](id3dxprtengine--computesurfsamplesbounce.md)
</dt> </dl>

 

 
