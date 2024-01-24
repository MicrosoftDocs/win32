---
description: Welds together replicated vertices that have equal attributes. This method uses specified epsilon values for equality comparisons.
ms.assetid: bddf6e0c-55a1-40d2-8681-e7f0f9002bfa
title: D3DXWeldVertices function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXWeldVertices
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXWeldVertices function

Welds together replicated vertices that have equal attributes. This method uses specified epsilon values for equality comparisons.

## Syntax


```C++
HRESULT D3DXWeldVertices(
  _In_          LPD3DXMESH       pMesh,
  _In_          DWORD            Flags,
  _In_    const D3DXWeldEpsilons *pEpsilons,
  _In_    const DWORD            *pAdjacencyIn,
  _Inout_       DWORD            *pAdjacencyOut,
  _Out_         DWORD            *pFaceRemap,
  _Out_         LPD3DXBUFFER     *ppVertexRemap
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) object, the mesh from which to weld vertices.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more flags from [**D3DXWELDEPSILONSFLAGS**](./d3dxweldepsilonsflags.md).

</dd> <dt>

*pEpsilons* \[in\]
</dt> <dd>

Type: **const [**D3DXWeldEpsilons**](d3dxweldepsilons.md)\***

Pointer to a [**D3DXWeldEpsilons**](d3dxweldepsilons.md) structure, specifying the epsilon values to be used for this method. Use **NULL** to initialize all structure members to a default value of 1.0e-6f.

</dd> <dt>

*pAdjacencyIn* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the source mesh. If the edge has no adjacent faces, the value is 0xffffffff. If this parameter is set to **NULL**, [**ID3DXBaseMesh::GenerateAdjacency**](id3dxbasemesh--generateadjacency.md) will be called to create logical adjacency information.

</dd> <dt>

*pAdjacencyOut* \[in, out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the optimized mesh. If the edge has no adjacent faces, the value is 0xffffffff.

</dd> <dt>

*pFaceRemap* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

An array of DWORDs, one per face, that identifies the original mesh face that corresponds to each face in the welded mesh.

</dd> <dt>

*ppVertexRemap* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) interface, which contains a DWORD for each vertex that specifies how the new vertices map to the old vertices. This remap is useful if you need to alter external data based on the new vertex mapping.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This function uses supplied adjacency information to determine the points that are replicated. Vertices are merged based on an epsilon comparison. Vertices with equal position must already have been calculated and represented by point-representative data.

This function combines logically-welded vertices that have similar components, such as normals or texture coordinates within pEpsilons.

The following example code calls this function with welding enabled. Vertices are compared using epsilon values for normal vector and vertex position. A pointer is returned to a face remapping array (*pFaceRemap*).


```
TCHAR            strMediaPath[512];       // X-file path 
LPD3DXBUFFER     pAdjacencyBuffer = NULL; // adjacency data buffer
LPD3DXBUFFER     pD3DXMtrlBuffer  = NULL; // material buffer
LPD3DXMESH       pMesh            = NULL; // mesh object
DWORD            m_dwNumMaterials;        // number of materials
D3DXWELDEPSILONS Epsilons;                // structure with epsilon values
DWORD            *pFaceRemap[65536];      // face remapping array
DWORD            i;                       // internal variable
    
    // Load the mesh from the specified file
    hr = D3DXLoadMeshFromX ( strMediaPath,
                         D3DXMESH_MANAGED,
                         m_pd3dDevice,
                         &pAdjacencyBuffer,
                         &pD3DXMtrlBuffer,
                         NULL,
                         &m_dwNumMaterials,
                         &pMesh ) )
                             
    if( FAILED( hr ) ) 
      goto End;              // Go to error handling
    
    // Set epsilon values
    Epsilons.Normal = 0.001;
    Epsilons.Position = 0.1;
    
    // Weld the vertices
    for( i=0; i < 65536; i++ )
    { 
        pFaceRemap[i] = 0; 
    }
    
    hr = D3DXWeldVertices ( pMesh,
                            D3DXWELDEPSILONS_WELDPARTIALMATCHES,
                            &Epsilons,
                            (DWORD*)pAdjacencyBuffer->GetBufferPointer(),
                            (DWORD*)pAdjacencyBuffer->GetBufferPointer(),
                            (DWORD*)pFaceRemap,
                            NULL )
                            
    if( FAILED( hr ) ) 
      goto End;              // Go to error handling
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
