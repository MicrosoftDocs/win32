---
description: Calculates per-triangle IMT's from a custom application-specified signal that varies over the surface of the mesh (generally at a higher frequency than vertex data). The signal is evaluated via a user-specified callback function.
ms.assetid: f1d96021-0b7d-43e6-b51b-71a90d2f5ad8
title: D3DXComputeIMTFromSignal function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXComputeIMTFromSignal
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXComputeIMTFromSignal function

Calculates per-triangle IMT's from a custom application-specified signal that varies over the surface of the mesh (generally at a higher frequency than vertex data). The signal is evaluated via a user-specified callback function.

## Syntax


```C++
HRESULT D3DXComputeIMTFromSignal(
  _In_  LPD3DXMESH              pMesh,
  _In_  DWORD                   dwTextureIndex,
  _In_  UINT                    uSignalDimension,
  _In_  FLOAT                   fMaxUVDistance,
  _In_  DWORD                   dwOptions,
  _In_  LPD3DXIMTSIGNALCALLBACK pSignalCallback,
  _In_  VOID                    *pUserData,
        LPD3DXUVATLASCB         pStatusCallback,
        LPVOID                  pUserContext,
  _Out_ LPD3DXBUFFER            *ppIMTData
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

A pointer to an input mesh (see [**ID3DXMesh**](id3dxmesh.md)) which contains the object geometry for calculating the IMT.

</dd> <dt>

*dwTextureIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Zero-based texture coordinate index that identifies which set of texture coordinates to use.

</dd> <dt>

*uSignalDimension* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of components in each data point in the signal.

</dd> <dt>

*fMaxUVDistance* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The maximum distance between vertices; the algorithm continues subdividing until the distance between all vertices is less than or equal to fMaxUVDistance.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Texture wrap options. This is a combination of one or more [**D3DXIMT FLAGS**](./d3dximt-flags.md).

</dd> <dt>

*pSignalCallback* \[in\]
</dt> <dd>

Type: **[LPD3DXIMTSIGNALCALLBACK](lpd3dximtsignalcallback.md)**

A pointer to a user-provided evaluator function, which will be used to compute the signal value at arbitrary U,V coordinates. The function follows the prototype of [LPD3DXIMTSIGNALCALLBACK](lpd3dximtsignalcallback.md).

</dd> <dt>

*pUserData* \[in\]
</dt> <dd>

Type: **VOID\***

A pointer to a user-defined value which is passed to the signal callback function. Typically used by an application to pass a pointer to a data structure that provides context information for the callback function.

</dd> <dt>

*pStatusCallback* 
</dt> <dd>

Type: **[LPD3DXUVATLASCB](lpd3dxuvatlascb.md)**

A pointer to a callback function to monitor IMT computation progress.

</dd> <dt>

*pUserContext* 
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

A pointer to a user-defined variable which is passed to the status callback function. Typically used by an application to pass a pointer to a data structure that provides context information for the callback function.

</dd> <dt>

*ppIMTData* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

A pointer to the buffer (see [**ID3DXBuffer**](id3dxbuffer.md)) containing the returned IMT array. This array can be provided as input to the D3DX [UVAtlas Functions](dx9-graphics-reference-d3dx-functions-uvatlas.md) to prioritize texture-space allocation in the texture parameterization.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK; otherwise, the value is D3DERR\_INVALIDCALL.

## Remarks

This function requires that the input mesh contain a signal-to-mesh texture mapping (ie. texture coordinates). It allows the user to define a signal arbitrarily over the surface of the mesh.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[UVAtlas Functions](dx9-graphics-reference-d3dx-functions-uvatlas.md)
</dt> <dt>

[Using UVAtlas (Direct3D 9)](using-uvatlas.md)
</dt> </dl>

 

 
