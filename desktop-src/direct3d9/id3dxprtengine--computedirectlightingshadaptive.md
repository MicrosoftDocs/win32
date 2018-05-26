---
Description: Computes the direct lighting contribution to 3D objects where the source radiance is represented by a spherical harmonic (SH) approximation, using adaptive sampling.
ms.assetid: 792d8460-d608-4384-ac1c-556435074580
title: ID3DXPRTEngineComputeDirectLightingSHAdaptive method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPRTEngine::ComputeDirectLightingSHAdaptive method

Computes the direct lighting contribution to 3D objects where the source radiance is represented by a spherical harmonic (SH) approximation, using adaptive sampling. This method generates new vertices and faces on the mesh to more accurately approximate the precomputed radiance transfer (PRT) signal.

## Syntax


```C++
HRESULT ComputeDirectLightingSHAdaptive(
  [in]      UINT            Order,
  [in]      FLOAT           AdaptiveThresh,
  [in]      FLOAT           MinEdgeLength,
  [in]      UINT            MaxSubdiv,
  [in, out] LPD3DXPRTBUFFER pDataOut
);
```



## Parameters

<dl> <dt>

*Order* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Order of the SH evaluation. Must be in the range of [D3DXSH\_MINORDER](other-d3dx-constants.md) to D3DXSH\_MAXORDER, inclusive. The evaluation generates Order² coefficients. The degree of the evaluation is Order - 1.

</dd> <dt>

*AdaptiveThresh* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Threshold on the PRT vector to use for subdividing mesh vertices and faces. If less than 1e-6f, a default value of 1e-6f is specified.

</dd> <dt>

*MinEdgeLength* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Minimum face edge length that will be generated in adaptive sampling. If the method determines that the value is too small, a model-dependent value is specified. If zero, a default value of 4 is specified.

</dd> <dt>

*MaxSubdiv* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Maximum level of subdivision of a face that will be used in adaptive sampling.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an output [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object. This buffer must have the proper number of color channels allocated for the simulation.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> <dt>

[**ID3DXPRTEngine::RobustMeshRefine**](id3dxprtengine--robustmeshrefine.md)
</dt> </dl>

 

 




