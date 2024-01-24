---
description: Computes a projection of distant lighting into spherical harmonic (SH) basis vectors that represent incident radiance at specified locations.
ms.assetid: 4d07b288-aec1-48eb-8d27-f3d7d8cfb69e
title: ID3DXPRTEngine::ComputeVolumeSamplesDirectSH method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.ComputeVolumeSamplesDirectSH
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::ComputeVolumeSamplesDirectSH method

Computes a projection of distant lighting into spherical harmonic (SH) basis vectors that represent incident radiance at specified locations.

## Syntax


```C++
HRESULT ComputeVolumeSamplesDirectSH(
  [in]            UINT            OrderIn,
  [in]            UINT            OrderOut,
  [in]            UINT            NumVolSamples.xml,
  [in]      const D3DXVECTOR3     *pSampleLocs,
  [in, out]       LPD3DXPRTBUFFER pDataOut
);
```



## Parameters

<dl> <dt>

*OrderIn* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Order of the SH representation of distant lighting. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The degree of the evaluation is OrderIn - 1.

</dd> <dt>

*OrderOut* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Order of the SH representation of local lighting. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The degree of the evaluation is OrderOut - 1.

</dd> <dt>

*NumVolSamples.xml* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of sample locations.

</dd> <dt>

*pSampleLocs* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Position for each sample.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an output [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that projects the distant lighting into SH basis vectors. This buffer must have the proper number of color channels allocated for the simulation. This method generates OrderIn² \* OrderOut"² scalars per channel at each sample location.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This method computes how light from a distant source arrives at each point in space specified by pSampleLocs. The SH coefficients represent the mapping, at each pSampleLocs point, of source radiance to transferred incident radiance.

To use this method successfully, you must set sampling over a sphere with UseSphere = **TRUE** and UseCosine = **FALSE** in [**ID3DXPRTEngine::SetSamplingInfo**](id3dxprtengine--setsamplinginfo.md); otherwise, this method will return an error with D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> <dt>

[**ID3DXPRTEngine::ComputeVolumeSamples**](id3dxprtengine--computevolumesamples.md)
</dt> </dl>

 

 
