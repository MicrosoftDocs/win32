---
description: Create a UV atlas for a mesh.
ms.assetid: 70256990-b177-451e-b42a-84799fdc2a17
title: D3DXUVAtlasCreate function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXUVAtlasCreate
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXUVAtlasCreate function

Create a UV atlas for a mesh.

## Syntax


```C++
HRESULT D3DXUVAtlasCreate(
  _In_        LPD3DXMESH      pMesh,
  _In_        UINT            dwMaxChartNumber,
  _In_        FLOAT           fMaxStretch,
  _In_        UINT            dwWidth,
  _In_        UINT            dwHeight,
  _In_        FLOAT           fGutter,
  _In_        DWORD           dwTextureIndex,
  _In_  const DWORD           *pdwAdjacency,
        const DWORD           *pdwFalseEdges,
  _In_        FLOAT           *pfIMTArray,
  _In_        LPD3DXUVATLASCB pCallback,
  _In_        FLOAT           fCallbackFrequency,
  _In_        LPVOID          pUserContext,
  _In_        DWORD           dwOptions,
  _In_        LPD3DXMESH      *ppMeshOut,
  _Out_       LPD3DXBUFFER    *ppFacePartitioning,
  _Out_       LPD3DXBUFFER    *ppVertexRemapArray,
  _Out_       FLOAT           *pfMaxStretchOut,
  _Out_       UINT            *pdwNumChartsOut
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an input mesh (see [**ID3DXMesh**](id3dxmesh.md)) which contains the object geometry for calculating the atlas. At a minimum, the mesh must contain position data and 2D texture coordinates.

</dd> <dt>

*dwMaxChartNumber* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The maximum number of charts to partition the mesh into. See remarks about the partitioning modes. Use 0 to tell D3DX that the atlas should be parameterized based on stretch.

</dd> <dt>

*fMaxStretch* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The amount of stretching allowed. 0 means no stretching is allowed, 1 means any amount of stretching can be used.

</dd> <dt>

*dwWidth* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Texture width.

</dd> <dt>

*dwHeight* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Texture height.

</dd> <dt>

*fGutter* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The minimum distance, in texels, between two charts on the atlas. The gutter is always scaled by the width; so, if a gutter of 2.5 is used on a 512x512 texture, then the minimum distance between two charts is 2.5 / 512.0 texels.

</dd> <dt>

*dwTextureIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Zero-based texture coordinate index that identifies which set of texture coordinates to use.

</dd> <dt>

*pdwAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

A pointer to an array of adjacency data. with 3 DWORDs per face, indicating which triangles are adjacent to each other (see [**ID3DXBaseMesh::GenerateAdjacency**](id3dxbasemesh--generateadjacency.md)).

</dd> <dt>

*pdwFalseEdges* 
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

An array with 3 DWORDS per face. Each face indicates if an edge is false or not. A non-false edge is indicated by -1, a false edge is indicated by any other value. This enables the parameterization of a mesh of quads where the edges down the middle of each quad will not be cut.

</dd> <dt>

*pfIMTArray* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

A pointer to an array of integrated metric tensors that describes how to stretch a triangle (see [IntegratedMetricTensor](using-uvatlas.md)).

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Type: **[LPD3DXUVATLASCB](lpd3dxuvatlascb.md)**

A pointer to a callback function (see [LPD3DXUVATLASCB](lpd3dxuvatlascb.md)) that is useful for monitoring progress.

</dd> <dt>

*fCallbackFrequency* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Specify how often D3DX will call the callback; a reasonable default value is 0.0001f.

</dd> <dt>

*pUserContent* \[in\]
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

Pointer to a user-defined value which is passed to the callback function; typically used by an application to pass a pointer to a data structure that provides context information for the callback function.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specify the quality of the charts generated. See [**D3DXUVATLAS**](./d3dxuvatlas.md).

</dd> <dt>

*ppMeshOut* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Pointer to the created mesh with the atlas (see [**ID3DXMesh**](id3dxmesh.md)).

</dd> <dt>

*ppFacePartitioning* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

A pointer to an array of the final face-partitioning data. Each element contains one DWORD per face (see [**ID3DXBuffer**](id3dxbuffer.md)).

</dd> <dt>

*ppVertexRemapArray* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

A pointer to an array of remapped vertices. Each array element identifies the original vertex that each final vertex came from (if the vertex was split during remapping). Each array element contains one DWORD per vertex.

</dd> <dt>

*pfMaxStretchOut* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

A pointer to the maximum stretch value generated by the atlas algorithm. The range is between 0.0 and 1.0.

</dd> <dt>

*pdwNumChartsOut* \[out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

A pointer to the number of charts created by the atlas algorithm. If dwMaxChartNumber is too low, this parameter will return the minimum number of charts required to create an atlas.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK; otherwise, the value is D3DERR\_INVALIDCALL.

## Remarks

D3DXUVAtlasCreate can partition mesh geometry two ways:

-   Based on the number of charts
-   Based on the maximum allowed stretch. If the maximum allowed stretch is 0, each triangle will likely be in its own chart.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[UVAtlas Functions](dx9-graphics-reference-d3dx-functions-uvatlas.md)
</dt> <dt>

[UV Atlas Command-Line Tool (uvatlas.exe)](https://msdn.microsoft.com/library/Ee419017(v=VS.85).aspx)
</dt> </dl>

 

 
