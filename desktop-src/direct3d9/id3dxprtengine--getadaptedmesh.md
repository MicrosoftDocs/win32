---
description: Returns a mesh with modifications resulting from adaptive spatial sampling. The returned mesh contains only positions, normals, and texture coordinates (if defined).
ms.assetid: 21447733-b27b-4906-8c0e-7089dec71b5b
title: ID3DXPRTEngine::GetAdaptedMesh method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ID3DXPRTEngine.GetAdaptedMesh
api_type:
- COM
api_location:
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine::GetAdaptedMesh method

Returns a mesh with modifications resulting from adaptive spatial sampling. The returned mesh contains only positions, normals, and texture coordinates (if defined).

## Syntax


```C++
HRESULT GetAdaptedMesh(
  [in]      LPDIRECT3DDEVICE9 pDevice,
  [in, out] UINT              *pFaceRemap,
  [in, out] UINT              *pVertRemap,
  [in, out] FLOAT             *pfVertWeights,
  [out]     LPD3DXMESH        *ppMesh
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**LPDIRECT3DDEVICE9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9)**

Pointer to an [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) device that is used to create the output mesh.

</dd> <dt>

*pFaceRemap* \[in, out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Pointer to the original mesh face that was split to generate the current face.

</dd> <dt>

*pVertRemap* \[in, out\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

Pointer to a destination array containing the three original mesh vertices that are the parents of the current vertex.

</dd> <dt>

*pfVertWeights* \[in, out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to a destination array containing blending factors for the pVertRemap vertices.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)\***

Pointer to the output [**ID3DXMesh**](id3dxmesh.md) mesh object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned.D3DERR\_INVALIDCALL

## Remarks

pVertRemap and pfVertWeights can be used to interpolate any per-vertex value over the mesh.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPRTEngine](id3dxprtengine.md)
</dt> </dl>

 

 
