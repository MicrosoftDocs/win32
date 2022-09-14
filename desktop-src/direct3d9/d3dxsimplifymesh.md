---
description: Generates a simplified mesh using the provided weights that come as close as possible to the given MinValue.
ms.assetid: 589356a9-f272-4851-92ae-54dbecc0b234
title: D3DXSimplifyMesh function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSimplifyMesh
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXSimplifyMesh function

Generates a simplified mesh using the provided weights that come as close as possible to the given MinValue.

## Syntax


```C++
HRESULT D3DXSimplifyMesh(
  _In_        LPD3DXMESH           pMesh,
  _In_  const DWORD                *pAdjacency,
  _In_  const D3DXATTRIBUTEWEIGHTS *pVertexAttributeWeights,
  _In_  const FLOAT                *pVertexWeights,
  _In_        DWORD                MinValue,
  _In_        DWORD                Options,
  _Out_       LPD3DXMESH           *ppMesh
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the source mesh.

</dd> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specify the three neighbors for each face in the mesh to be simplified.

</dd> <dt>

*pVertexAttributeWeights* \[in\]
</dt> <dd>

Type: **const [**D3DXATTRIBUTEWEIGHTS**](d3dxattributeweights.md)\***

Pointer to a [**D3DXATTRIBUTEWEIGHTS**](d3dxattributeweights.md) structure, containing the weight for each vertex component. If this parameter is set to **NULL**, a default structure is used. See Remarks.

</dd> <dt>

*pVertexWeights* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to an array of vertex weights. If this parameter is set to **NULL**, all vertex weights are set to 1.0.

</dd> <dt>

*MinValue* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Number of vertices or faces, depending on the flag set in the *Options* parameter, by which to simplify the source mesh.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Specifies simplification options for the mesh. One of the flags in [**D3DXMESHSIMP**](./d3dxmeshsimp.md) can be set.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Address of a pointer to an [**ID3DXMesh**](id3dxmesh.md) interface, representing the returned simplification mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_INVALIDDATA, E\_OUTOFMEMORY.

## Remarks

This function generates a mesh that has *MinValue* vertices or faces.

If the simplification process cannot reduce the mesh to *MinValue*, the call still succeeds because *MinValue* is a desired minimum, not an absolute minimum.

If *pVertexAttributeWeights* is set to **NULL**, the following values are assigned to the default [**D3DXATTRIBUTEWEIGHTS**](d3dxattributeweights.md) structure.


```
D3DXATTRIBUTEWEIGHTS AttributeWeights;
    
AttributeWeights.Position  = 1.0;
AttributeWeights.Boundary =  1.0;
AttributeWeights.Normal   =  1.0;
AttributeWeights.Diffuse  =  0.0;
AttributeWeights.Specular =  0.0;
AttributeWeights.Tex[8]   =  {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
```



This default structure is what most applications should use because it considers only geometric and normal adjustment. Only in special cases will the other member fields need to be modified.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
