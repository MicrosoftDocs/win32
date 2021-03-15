---
description: Used with compressed results of the vertex version of the precomputed radiance transfer (PRT) simulator.
ms.assetid: 10d81920-2a1b-42fa-aabe-7d6b504f4d36
title: D3DXSHPRTCompSplitMeshSC function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHPRTCompSplitMeshSC
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSHPRTCompSplitMeshSC function

Used with compressed results of the vertex version of the precomputed radiance transfer (PRT) simulator. After [**D3DXSHPRTCompSuperCluster**](d3dxshprtcompsupercluster.md) has been called, this function can be used to split the mesh into a group of faces/vertices per super cluster. Each super cluster contains all of the faces that contain any vertex classified in one of its clusters. All of the vertices connected to this set of faces are also included with the returned array ppVertStatus indicating whether or not the vertex belongs to the super cluster.

## Syntax


```C++
HRESULT D3DXSHPRTCompSplitMeshSC(
  _In_    UINT                          *pClusterIDs,
  _In_    UINT                          NumVertices,
  _In_    UINT                          NumCs,
  _In_    UINT                          *pSClusterIDs,
  _In_    UINT                          NumSCs,
  _In_    LPVOID                        pInputIB,
  _In_    BOOL                          InputIBIs32Bit,
  _In_    UINT                          NumFaces,
  _Inout_ LPD3DXBUFFER                  *ppIBData,
  _Inout_ UINT                          *pIBDataLength,
  _Inout_ BOOL                          OutputIBIs32Bit,
  _Inout_ LPD3DXBUFFER                  *ppFaceRemap,
  _Inout_ LPD3DXBUFFER                  *ppVertData,
  _Inout_ UINT                          *pVertDataLength,
  _Inout_ UINT                          *pSCClusterList,
  _Inout_ D3DXSHPRTSPLITMESHCLUSTERDATA *pSCData
);
```



## Parameters

<dl> <dt>

*pClusterIDs* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

*NumVertices* cluster IDs (extracted from a compressed buffer.)

</dd> <dt>

*NumVertices* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of vertices in original mesh.

</dd> <dt>

*NumCs* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of clusters (input parameter to compression.)

</dd> <dt>

*pSClusterIDs* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Array of size *NumCs* that will contain super cluster IDs.

</dd> <dt>

*NumSCs* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of super clusters allocated in [**D3DXSHPRTCompSuperCluster**](d3dxshprtcompsupercluster.md).

</dd> <dt>

*pInputIB* \[in\]
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

Raw index buffer for mesh. The format depends on *InputIBIs32Bit*.

</dd> <dt>

*InputIBIs32Bit* \[in\]
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

If **TRUE**, the index buffer is set to 32 bit; otherwise, 16 bit.

</dd> <dt>

*NumFaces* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of faces in the original mesh (*pInputIB* is 3 times this length.)

</dd> <dt>

*ppIBData* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Raw index buffer that will contain the resulting split faces. Format determined by *InputIBIs32Bit*. Allocated by function.

</dd> <dt>

*pIBDataLength* \[in, out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Length of *ppIBData*, assigned in function.

</dd> <dt>

*OutputIBIs32Bit* \[in, out\]
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

If **TRUE**, allocates an unsigned integer array; otherwise, allocates an unsigned short array.

</dd> <dt>

*ppFaceRemap* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Mapping of each face in *ppIBData* to original faces. Length is \**pIBDataLength*/3.

</dd> <dt>

*ppVertData* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

New vertex data structure. Size of *pVertDataLength*.

</dd> <dt>

*pVertDataLength* \[in, out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Number of new vertices in split mesh. Assigned in function.

</dd> <dt>

*pSCClusterList* \[in, out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Array of length *NumCs* which *pSCData* indexes into (*pClusterIDs*\* fields) for each supercluster, contains clusters sorted by supercluster.

</dd> <dt>

*pSCData* \[in, out\]
</dt> <dd>

Type: **[**D3DXSHPRTSPLITMESHCLUSTERDATA**](d3dxshprtsplitmeshclusterdata.md)\***

Structure per super cluster. Contains indices into *ppIBData*, *pSCClusterList*, and *ppVertData*.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> </dl>

 

 
