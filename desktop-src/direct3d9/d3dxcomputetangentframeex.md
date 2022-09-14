---
description: Performs tangent frame computations on a mesh. Tangent, binormal, and optionally normal vectors are generated. Singularities are handled as required by grouping edges and splitting vertices.
ms.assetid: 15cc46bc-6db6-4e1d-a95e-cd60d2666600
title: D3DXComputeTangentFrameEx function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXComputeTangentFrameEx
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXComputeTangentFrameEx function

Performs tangent frame computations on a mesh. Tangent, binormal, and optionally normal vectors are generated. Singularities are handled as required by grouping edges and splitting vertices.

## Syntax


```C++
HRESULT D3DXComputeTangentFrameEx(
  _In_        ID3DXMesh   *pMesh,
  _In_        DWORD       dwTextureInSemantic,
  _In_        DWORD       dwTextureInIndex,
  _In_        DWORD       dwUPartialOutSemantic,
  _In_        DWORD       dwUPartialOutIndex,
  _In_        DWORD       dwVPartialOutSemantic,
  _In_        DWORD       dwVPartialOutIndex,
  _In_        DWORD       dwNormalOutSemantic,
  _In_        DWORD       dwNormalOutIndex,
  _In_        DWORD       dwOptions,
  _In_  const DWORD       *pdwAdjacency,
  _In_        FLOAT       fPartialEdgeThreshold,
  _In_        FLOAT       fSingularPointThreshold,
  _In_        FLOAT       fNormalEdgeThreshold,
  _Out_       ID3DXMesh   **ppMeshOut,
  _Out_       ID3DXBuffer **ppVertexMapping
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**ID3DXMesh**](id3dxmesh.md)\***

Pointer to an input [**ID3DXMesh**](id3dxmesh.md) mesh object.

</dd> <dt>

*dwTextureInSemantic* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the texture coordinate input semantic. If D3DX\_DEFAULT, the function assumes that there are no texture coordinates, and the function will fail unless normal vector calculation is specified.

</dd> <dt>

*dwTextureInIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

If a mesh has multiple texture coordinates, specifies the texture coordinate to use for the tangent frame computations. If zero, the mesh has only a single texture coordinate.

</dd> <dt>

*dwUPartialOutSemantic* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the output semantic for the type, typically D3DDECLUSAGE\_TANGENT, that describes where the partial derivative with respect to the U texture coordinate will be stored. If D3DX\_DEFAULT, then this partial derivative will not be stored.

</dd> <dt>

*dwUPartialOutIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the semantic index at which to store the partial derivative with respect to the U texture coordinate.

</dd> <dt>

*dwVPartialOutSemantic* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the [**D3DDECLUSAGE**](./d3ddeclusage.md) type, typically D3DDECLUSAGE\_BINORMAL, that describes where the partial derivative with respect to the V texture coordinate will be stored. If D3DX\_DEFAULT, then this partial derivative will not be stored.

</dd> <dt>

*dwVPartialOutIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the semantic index at which to store the partial derivative with respect to the V texture coordinate.

</dd> <dt>

*dwNormalOutSemantic* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the output normal semantic, typically D3DDECLUSAGE\_NORMAL, that describes where the normal vector at each vertex will be stored. If D3DX\_DEFAULT, then this normal vector will not be stored.

</dd> <dt>

*dwNormalOutIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies the semantic index at which to store the normal vector at each vertex.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more [**D3DXTANGENT**](./d3dxtangent.md) flags that specify tangent frame computation options. If **NULL**, the following options will be specified:



| Description                                                                                              | [**D3DXTANGENT**](./d3dxtangent.md) Flag Value                               |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Weight the normal vector length by the angle, in radians, subtended by the two edges leaving the vertex. | & !( D3DXTANGENT\_WEIGHT\_BY\_AREA \| D3DXTANGENT\_WEIGHT\_EQUAL )                |
| Compute orthogonal Cartesian coordinates from texture coordinates (u, v). See Remarks.                   | & !( D3DXTANGENT\_ORTHOGONALIZE\_FROM\_U \| D3DXTANGENT\_ORTHOGONALIZE\_FROM\_V ) |
| Textures are not wrapped in either u or v directions                                                     | & !( D3DXTANGENT\_WRAP\_UV )                                                      |
| Partial derivatives with respect to texture coordinates are normalized.                                  | & !( D3DXTANGENT\_DONT\_NORMALIZE\_PARTIALS )                                     |
| Vertices are ordered in a counterclockwise direction around each triangle.                               | & !( D3DXTANGENT\_WIND\_CW )                                                      |
| Use per-vertex normal vectors already present in the input mesh.                                         | & !( D3DXTANGENT\_CALCULATE\_NORMALS )                                            |



 

If D3DXTANGENT\_GENERATE\_IN\_PLACE is not set, the input mesh is cloned. The original mesh must therefore have sufficient space to store the computed normal vector and partial derivative data.

</dd> <dt>

*pdwAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh. The number of bytes in this array must be at least 3 \* [**GetNumFaces**](id3dxbasemesh--getnumfaces.md) \* sizeof(DWORD).

</dd> <dt>

*fPartialEdgeThreshold* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Specifies the maximum cosine of the angle at which two partial derivatives are deemed to be incompatible with each other. If the dot product of the direction of the two partial derivatives in adjacent triangles is less than or equal to this threshold, then the vertices shared between these triangles will be split.

</dd> <dt>

*fSingularPointThreshold* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Specifies the maximum magnitude of a partial derivative at which a vertex will be deemed singular. As multiple triangles are incident on a point that have nearby tangent frames, but altogether cancel each other out (such as at the top of a sphere), the magnitude of the partial derivative will decrease. If the magnitude is less than or equal to this threshold, then the vertex will be split for every triangle that contains it.

</dd> <dt>

*fNormalEdgeThreshold* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Similar to fPartialEdgeThreshold, specifies the maximum cosine of the angle between two normals that is a threshold beyond which vertices shared between triangles will be split. If the dot product of the two normals is less than the threshold, the shared vertices will be split, forming a hard edge between neighboring triangles. If the dot product is more than the threshold, neighboring triangles will have their normals interpolated.

</dd> <dt>

*ppMeshOut* \[out\]
</dt> <dd>

Type: **[**ID3DXMesh**](id3dxmesh.md)\*\***

Address of a pointer to an output [**ID3DXMesh**](id3dxmesh.md) mesh object that receives the computed tangent, binormal, and normal vector data.

</dd> <dt>

*ppVertexMapping* \[out\]
</dt> <dd>

Type: **[**ID3DXBuffer**](id3dxbuffer.md)\*\***

Address of a pointer to an output [**ID3DXBuffer**](id3dxbuffer.md) buffer object that receives a mapping of new vertices computed by this method to the original vertices. The buffer is an array of DWORDs, with the array size defined as the number of vertices in ppMeshOut.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

A simplified version of this function is available as [**D3DXComputeTangentFrame**](d3dxcomputetangentframe.md).

The computed normal vector at each vertex is always normalized to have unit length.

The most robust solution for computing orthogonal Cartesian coordinates is to not set flags D3DXTANGENT\_ORTHOGONALIZE\_FROM\_U and D3DXTANGENT\_ORTHOGONALIZE\_FROM\_V, so that orthogonal coordinates are computed from both texture coordinates u and v. However, in this case, if either u or v is zero, then the function will compute orthogonal coordinates using D3DXTANGENT\_ORTHOGONALIZE\_FROM\_V or D3DXTANGENT\_ORTHOGONALIZE\_FROM\_U, respectively.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**D3DXComputeTangentFrame**](d3dxcomputetangentframe.md)
</dt> </dl>

 

 
