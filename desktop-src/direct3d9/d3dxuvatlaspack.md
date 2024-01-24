---
description: Pack mesh partitioning data into an atlas.
ms.assetid: 4da85626-c36c-44d9-990b-0db80ed04423
title: D3DXUVAtlasPack function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXUVAtlasPack
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXUVAtlasPack function

Pack mesh partitioning data into an atlas.

## Syntax


```C++
HRESULT D3DXUVAtlasPack(
  _In_       LPD3DXMESH      pMesh,
  _In_       UINT            dwWidth,
  _In_       UINT            dwHeight,
  _In_       FLOAT           fGutter,
  _In_       DWORD           dwTextureIndex,
       const DWORD           *pdwPartitionResultAdjacency,
  _In_       LPD3DXUVATLASCB pCallback,
  _In_       FLOAT           fCallbackFrequency,
  _In_       LPVOID          pUserContent,
  _In_       DWORD           dwOptions,
  _In_       LPD3DXBUFFER    pFacePartitioning
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an input mesh (see [**ID3DXMesh**](id3dxmesh.md)) which contains the object geometry for calculating the atlas. At a minimum, the mesh must contain position data and 2D texture coordinates.

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

*pdwPartitionResultAdjacency* 
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh. It should be derived from the ppPartitionResultAdjacency returned from [**D3DXUVAtlasPartition**](d3dxuvatlaspartition.md). This value cannot be **NULL**, because Pack needs to know where charts were cut in the partition step in order to find the edges of each chart.

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

A void pointer to be passed back to the callback function.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

This options parameter is currently reserved.

</dd> <dt>

*pFacePartitioning* \[in\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)**

A pointer to an [**ID3DXBuffer**](id3dxbuffer.md) containing the array of the final face-partitioning. Each element contains one DWORD per face.

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
</dt> </dl>

 

 
