---
description: Calculate per-triangle IMT's from from per-vertex data. This function allows you to calculate the IMT based off of any value in a mesh (color, normal, etc).
ms.assetid: a417a8ad-77b1-49ae-aea0-6a32a154499f
title: D3DXComputeIMTFromPerVertexSignal function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXComputeIMTFromPerVertexSignal
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXComputeIMTFromPerVertexSignal function

Calculate per-triangle IMT's from from per-vertex data. This function allows you to calculate the IMT based off of any value in a mesh (color, normal, etc).

## Syntax


```C++
HRESULT D3DXComputeIMTFromPerVertexSignal(
  _In_        LPD3DXMESH      pMesh,
  _In_  const FLOAT           *pfVertexSignal,
  _In_        UINT            uSignalDimension,
  _In_        UINT            uSignalStride,
  _In_        DWORD           dwOptions,
              LPD3DXUVATLASCB pStatusCallback,
              LPVOID          pUserContext,
  _Out_       LPD3DXBUFFER    *ppIMTData
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

A pointer to an input mesh (see [**ID3DXMesh**](id3dxmesh.md)) which contains the object geometry for calculating the IMT.

</dd> <dt>

*pfVertexSignal* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

A pointer to an array of per-vertex data from which IMT will be computed. The array size is uSignalStride \* v, where v is the number of vertices in the mesh.

</dd> <dt>

*uSignalDimension* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of floats per vertex.

</dd> <dt>

*uSignalStride* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of bytes per vertex in the array. This must be a multiple of sizeof(float)

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Texture wrap options. This is a combination of one or more [**D3DXIMT FLAGS**](./d3dximt-flags.md).

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

 

 
