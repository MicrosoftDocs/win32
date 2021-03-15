---
description: Convert the specified mesh subset into a series of strips.
ms.assetid: 4f005383-6a5a-4393-ac88-202e45946d3d
title: D3DXConvertMeshSubsetToStrips function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXConvertMeshSubsetToStrips
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXConvertMeshSubsetToStrips function

Convert the specified mesh subset into a series of strips.

## Syntax


```C++
HRESULT D3DXConvertMeshSubsetToStrips(
  _In_  LPD3DXBASEMESH         MeshIn,
  _In_  DWORD                  AttribId,
  _In_  DWORD                  IBOptions,
  _Out_ LPDIRECT3DINDEXBUFFER9 *ppIndexBuffer,
  _Out_ DWORD                  *pNumIndices,
  _Out_ LPD3DXBUFFER           *ppStripLengths,
  _Out_ DWORD                  *pNumStrips
);
```



## Parameters

<dl> <dt>

*MeshIn* \[in\]
</dt> <dd>

Type: **[**LPD3DXBASEMESH**](id3dxbasemesh.md)**

Pointer to an [**ID3DXBaseMesh**](id3dxbasemesh.md) interface, representing the mesh to convert to a strip.

</dd> <dt>

*AttribId* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Attribute ID of the mesh subset to convert to strips.

</dd> <dt>

*IBOptions* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more flags from the [**D3DXMESH**](./d3dxmesh.md) enumeration, specifying options for creating the index buffer. Cannot be D3DXMESH\_32BIT. The index buffer will be created with 32-bit or 16-bit indices depending on the format of the index buffer of the mesh specified by the *MeshIn* parameter.

</dd> <dt>

*ppIndexBuffer* \[out\]
</dt> <dd>

Type: **[**LPDIRECT3DINDEXBUFFER9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dindexbuffer9)\***

Pointer to an [**IDirect3DIndexBuffer9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dindexbuffer9) interface, representing index buffer containing the strip.

</dd> <dt>

*pNumIndices* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Number of indices in the buffer returned in the *ppIndexBuffer* parameter.

</dd> <dt>

*ppStripLengths* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Buffer containing an array of one DWORD per strip, which specifies the number of triangles in the that strip.

</dd> <dt>

*pNumStrips* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Number of individual strips in the index buffer and corresponding strip length array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

Before running this function, call [**Optimize**](id3dxmesh--optimize.md) or [**D3DXOptimizeFaces**](d3dxoptimizefaces.md), with the D3DXMESHOPT\_ATTRSORT flag set.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
