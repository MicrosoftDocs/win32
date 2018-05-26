---
Description: Tessellates a rectangular higher-order surface patch into a triangle mesh.
ms.assetid: d941d994-8a13-49ff-a0b1-b21a3f84ed78
title: D3DXTessellateRectPatch function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXTessellateRectPatch function

Tessellates a rectangular higher-order surface patch into a triangle mesh.

## Syntax


```C++
HRESULT D3DXTessellateRectPatch(
  _In_          LPDIRECT3DVERTEXBUFFER9 pVB,
  _In_    const FLOAT                   *pNumSegs,
  _In_    const D3DVERTEXELEMENT9       *pInDecl,
  _In_    const D3DRECTPATCH_INFO       *pRectPatchInfo,
  _Inout_       LPD3DXMESH              pMesh
);
```



## Parameters

<dl> <dt>

*pVB* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DVERTEXBUFFER9**](/windows/win32/d3d9helper/nn-d3d9-idirect3dvertexbuffer9?branch=master)**

Vertex buffer containing the patch data.

</dd> <dt>

*pNumSegs* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](winprog.windows_data_types)\***

Pointer to an array of four floating-point values that identify the number of segments into which each edge of the rectangle patch should be divided when tessellated. See [**D3DRECTPATCH\_INFO**](d3drectpatch-info.md).

</dd> <dt>

*pInDecl* \[in\]
</dt> <dd>

Type: **const [**D3DVERTEXELEMENT9**](d3dvertexelement9.md)\***

Vertex declaration structure that defines the vertex data. See [**D3DVERTEXELEMENT9**](d3dvertexelement9.md).

</dd> <dt>

*pRectPatchInfo* \[in\]
</dt> <dd>

Type: **const [**D3DRECTPATCH\_INFO**](d3drectpatch-info.md)\***

Describes a rectangular patch. See [**D3DRECTPATCH\_INFO**](d3drectpatch-info.md).

</dd> <dt>

*pMesh* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to the created mesh. See [**ID3DXMesh**](id3dxmesh.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Use [**D3DXRectPatchSize**](d3dxrectpatchsize.md) to get the number of output vertices and indices that the tessellation function needs.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> <dt>

[**D3DXTessellateTriPatch**](d3dxtessellatetripatch.md)
</dt> </dl>

 

 




