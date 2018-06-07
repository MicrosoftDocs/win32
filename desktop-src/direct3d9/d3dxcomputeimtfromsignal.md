---
Description: Calculates per-triangle IMT's from a custom application-specified signal that varies over the surface of the mesh (generally at a higher frequency than vertex data). The signal is evaluated via a user-specified callback function.
ms.assetid: f1d96021-0b7d-43e6-b51b-71a90d2f5ad8
title: D3DXComputeIMTFromSignal function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Zero-based texture coordinate index that identifies which set of texture coordinates to use.

</dd> <dt>

*uSignalDimension* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The number of components in each data point in the signal.

</dd> <dt>

*fMaxUVDistance* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

The maximum distance between vertices; the algorithm continues subdividing until the distance between all vertices is less than or equal to fMaxUVDistance.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Texture wrap options. This is a combination of one or more [**D3DXIMT FLAGS**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dximt_flags.htm).

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

Type: **[**LPVOID**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

A pointer to a user-defined variable which is passed to the status callback function. Typically used by an application to pass a pointer to a data structure that provides context information for the callback function.

</dd> <dt>

*ppIMTData* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

A pointer to the buffer (see [**ID3DXBuffer**](id3dxbuffer.md)) containing the returned IMT array. This array can be provided as input to the D3DX [UVAtlas Functions](dx9-graphics-reference-d3dx-functions-uvatlas.md) to prioritize texture-space allocation in the texture parameterization.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK; otherwise, the value is D3DERR\_INVALIDCALL.

## Remarks

This function requires that the input mesh contain a signal-to-mesh texture mapping (ie. texture coordinates). It allows the user to define a signal arbitrarily over the surface of the mesh.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[UVAtlas Functions](dx9-graphics-reference-d3dx-functions-uvatlas.md)
</dt> <dt>

[Using UVAtlas (Direct3D 9)](using-uvatlas.md)
</dt> </dl>

 

 




