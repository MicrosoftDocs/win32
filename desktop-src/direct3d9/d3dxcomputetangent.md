---
description: Computes the tangent vectors for the texture coordinates given in the texture stage. Provided to support legacy applications. Use D3DXComputeTangentFrameEx for better results.
ms.assetid: 39748459-3f9b-4b48-ae13-7143eb29c292
title: D3DXComputeTangent function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXComputeTangent
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXComputeTangent function

Computes the tangent vectors for the texture coordinates given in the texture stage. Provided to support legacy applications. Use [**D3DXComputeTangentFrameEx**](d3dxcomputetangentframeex.md) for better results.

## Syntax


```C++
HRESULT D3DXComputeTangent(
  _In_       LPD3DXMESH Mesh,
  _In_       DWORD      TexStageIndex,
  _In_       DWORD      TangentIndex,
  _In_       DWORD      BinormIndex,
  _In_       DWORD      Wrap,
  _In_ const DWORD      *pAdjacency
);
```



## Parameters

<dl> <dt>

*Mesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) interface that represent the input mesh.

</dd> <dt>

*TexStageIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Index that represents the texture stage.

</dd> <dt>

*TangentIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Index that provides the usage index for the tangent data. The vertex declaration implies the usage; this index modifies the usage with the usage index. For more information about a vertex declaration, see [Vertex Declaration (Direct3D 9)](vertex-declaration.md).

</dd> <dt>

*BinormIndex* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Index that provides the usage index for the binormal data. The vertex declaration implies the usage; this index modifies the usage with the usage index. For more information about a vertex declaration, see [Vertex Declaration (Direct3D 9)](vertex-declaration.md).

</dd> <dt>

*Wrap* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Set this value to 0 for no wrapping, or to 1 for wrapping in the U and V directions.

</dd> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face to be filled with adjacent face indices. The number of bytes in this array must be at least ((3 \* [**GetNumFaces**](id3dxbasemesh--getnumfaces.md)) \* sizeof(DWORD)).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is S\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

If the mesh vertex declaration specifies tangent or binormal fields, **D3DXComputeTangent** will update any user-supplied tangent or binormal data. Alternatively, set TangentIndex to [D3DX\_DEFAULT](other-d3dx-constants.md) to not update the user-supplied tangent data, or set BinormIndex to D3DX\_DEFAULT to not update the user-supplied binormal data. TexStageIndex cannot be set to D3DX\_DEFAULT.

**D3DXComputeTangent** depends on the mesh vertex declaration containing either the binormal field (BinormIndex), the tangent field (TangentIndex), or both. If both are missing, this function will fail.

This function simply calls [**D3DXComputeTangentFrameEx**](d3dxcomputetangentframeex.md) with the following input parameters:


```
D3DXComputeTangentFrameEx( Mesh,
                           D3DDECLUSAGE_TEXCOORD,
                           TexStageIndex,
                           ( BinormIndex == D3DX_DEFAULT ) ?
                               D3DX_DEFAULT : D3DDECLUSAGE_BINORMAL,
                               // provides backward function compatibility
                           BinormIndex,
                           ( TangentIndex == D3DX_DEFAULT ) ?
                               D3DX_DEFAULT : D3DDECLUSAGE_TANGENT,
                           TangentIndex,
                           D3DX_DEFAULT, // do not store normals
                           0,
                           ( Wrap ? D3DXTANGENT_WRAP_UV : 0 )
                               | D3DXTANGENT_GENERATE_IN_PLACE
                               | D3DXTANGENT_ORTHOGONALIZE_FROM_U,
                           pAdjacency,
                           -1.01f,
                           -0.01f,
                           -1.01f,
                           NULL,
                           NULL);
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

 

 
