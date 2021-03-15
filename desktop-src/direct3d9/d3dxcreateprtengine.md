---
description: Creates an ID3DXPRTEngine object that can efficiently generate precomputed radiance transfer (PRT) simulations of a 3D scene.
ms.assetid: fdfe02b5-03fb-4bee-a53b-012ae3572644
title: D3DXCreatePRTEngine function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCreatePRTEngine
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXCreatePRTEngine function

Creates an [**ID3DXPRTEngine**](id3dxprtengine.md) object that can efficiently generate precomputed radiance transfer (PRT) simulations of a 3D scene.

## Syntax


```C++
HRESULT D3DXCreatePRTEngine(
  _In_    LPD3DXMESH      pMesh,
  _In_    DWORD           *pAdjacency,
  _In_    BOOL            ExtractUVs,
  _In_    LPD3DXMESH      pBlockerMesh,
  _Inout_ LPD3DXPRTENGINE ppEngine
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an input [**ID3DXMesh**](id3dxmesh.md) mesh object that models the 3D scene. This mesh must have an attribute table in which vertices are in a unique attribute.

</dd> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Optional pointer to an array of three DWORDs per face to be filled with adjacent face indices. The number of bytes in this array must be at least ((3 \* [**GetNumFaces**](id3dxbasemesh--getnumfaces.md)) \* sizeof(DWORD)). May be **NULL**.

</dd> <dt>

*ExtractUVs* \[in\]
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

If **TRUE**, textures will be used to store albedos or PRT vectors.

</dd> <dt>

*pBlockerMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Pointer to an optional [**ID3DXMesh**](id3dxmesh.md) mesh object that blocks the 3D scene. May be **NULL**.

</dd> <dt>

*ppEngine* \[in, out\]
</dt> <dd>

Type: **[**LPD3DXPRTENGINE**](id3dxprtengine.md)**

Pointer to an output [**ID3DXPRTEngine**](id3dxprtengine.md) object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Use [**D3DXConcatenateMeshes**](d3dxconcatenatemeshes.md) to combine multiple meshes into a single mesh interface.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Precomputed Radiance Transfer Functions](dx9-graphics-reference-d3dx-functions-prt.md)
</dt> </dl>

 

 
