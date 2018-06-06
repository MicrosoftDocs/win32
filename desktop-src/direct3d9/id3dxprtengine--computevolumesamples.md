---
Description: Computes a projection of the direct lighting from the previous light bounce into spherical harmonic (SH) basis vectors that represent incident radiance at specified locations.
ms.assetid: ccde7c59-cb82-4d61-822a-e1e9ecea0a28
title: ID3DXPRTEngine::ComputeVolumeSamples method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXPRTEngine::ComputeVolumeSamples method

Computes a projection of the direct lighting from the previous light bounce into spherical harmonic (SH) basis vectors that represent incident radiance at specified locations.

## Syntax


```C++
HRESULT ComputeVolumeSamples(
  [in]            LPD3DXPRTBUFFER pSurfDataIn,
  [in]            UINT            Order,
  [in]            UINT            NumVolSamples.xml,
  [in]      const D3DXVECTOR3     *pSampleLocs,
  [in, out]       LPD3DXPRTBUFFER pDataOut
);
```



## Parameters

<dl> <dt>

*pSurfDataIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an input [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that represents the 3D object from the previous light bounce.

</dd> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Order of the SH evaluation. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*NumVolSamples.xml* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Number of sample locations.

</dd> <dt>

*pSampleLocs* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Position for each sample. If pSampleLocs is **NULL**, ComputeVolumeSamples will compute transfer matrices at every mesh vertex. However, if pSampleLocs is not **NULL**, you must sample over a sphere (set UseSphere = **TRUE** and UseCosine = **FALSE** in [**ID3DXPRTEngine::SetSamplingInfo**](id3dxprtengine--setsamplinginfo.md)); otherwise, ComputeVolumeSamples will return D3DERR\_INVALIDCALL.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an output [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that projects the direct lighting from the previous light bounce into SH basis vectors. This buffer must have the proper number of color channels allocated for the simulation.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This method computes how the light from the source radiance function is reflected off the surface that represents the scene (pSurfDataIn) and arrives at each point in space specified by pSampleLocs. The SH coefficients represent the mapping, at each pSampleLocs point, of source radiance to transferred incident radiance.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> <dt>

[**ID3DXPRTEngine::ComputeVolumeSamplesDirectSH**](id3dxprtengine--computevolumesamplesdirectsh.md)
</dt> </dl>

 

 




