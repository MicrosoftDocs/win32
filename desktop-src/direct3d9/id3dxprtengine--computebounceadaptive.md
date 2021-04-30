---
description: Computes the source radiance resulting from a single bounce of interreflected light, using adaptive sampling.
ms.assetid: 61f8cecd-d95a-4f02-929e-02f2bce5bde9
title: ID3DXPRTEngine::ComputeBounceAdaptive method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine.ComputeBounceAdaptive
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::ComputeBounceAdaptive method

Computes the source radiance resulting from a single bounce of interreflected light, using adaptive sampling. This method generates new vertices and faces on the mesh to more accurately approximate the precomputed radiance transfer (PRT) signal. This method can be used for any lit scene, including a spherical harmonic (SH)-based PRT model.

## Syntax


```C++
HRESULT ComputeBounceAdaptive(
  [in]      LPD3DXPRTBUFFER pDataIn,
  [in]      FLOAT           AdaptiveThresh,
  [in]      FLOAT           MinEdgeLength,
  [in]      UINT            MaxSubdiv,
  [in, out] LPD3DXPRTBUFFER pDataOut,
  [in, out] LPD3DXPRTBUFFER pDataTotal
);
```



## Parameters

<dl> <dt>

*pDataIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an input [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that represents the 3D object from the previous light bounce. This input buffer must have the proper number of color channels allocated for the simulation.

</dd> <dt>

*AdaptiveThresh* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Threshold on the PRT vector to use for subdividing mesh vertices and faces. If less than 1e-6f, a default value of 1e-6f is specified.

</dd> <dt>

*MinEdgeLength* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Minimum face edge length that will be generated in adaptive sampling. If the method determines that the value is too small, a model-dependent value is specified. If zero, a default value of 4 is specified.

</dd> <dt>

*MaxSubdiv* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Maximum level of subdivision of a face that will be used in adaptive sampling.

</dd> <dt>

*pDataOut* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an output [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object. This output buffer must have the proper number of color channels allocated for the simulation.

</dd> <dt>

*pDataTotal* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTBUFFER**](id3dxprtbuffer.md)**

Pointer to an optional [**ID3DXPRTBuffer**](id3dxprtbuffer.md) object that keeps a running sum of pDataOut with each light bounce computation. May be **NULL**.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> <dt>

[**ID3DXPRTEngine::RobustMeshRefine**](id3dxprtengine--robustmeshrefine.md)
</dt> </dl>

 

 
