---
Description: 'Creates a mesh object using a declarator.'
ms.assetid: '50e09378-2935-4b18-8fc9-5e58eaadae44'
title: D3DX10CreateMesh function
---

# D3DX10CreateMesh function

Creates a mesh object using a declarator.

## Syntax


```C++
HRESULT D3DX10CreateMesh(
  _In_        ID3D10Device             *pDevice,
  _In_  const D3D10_INPUT_ELEMENT_DESC *pDeclaration,
  _In_        UINT                     DeclCount,
  _In_        LPCSTR                   pPositionSemantic,
  _In_        UINT                     VertexCount,
  _In_        UINT                     FaceCount,
  _In_        UINT                     Options,
  _Out_       ID3DX10Mesh              **ppMesh
);
```



## Parameters

<dl> <dt>

*pDevice* \[in\]
</dt> <dd>

Type: **[**ID3D10Device**](id3d10device.md)\***

Pointer to an [**ID3D10Device Interface**](id3d10device.md), the device object to be associated with the mesh.

</dd> <dt>

*pDeclaration* \[in\]
</dt> <dd>

Type: **const [**D3D10\_INPUT\_ELEMENT\_DESC**](d3d10-input-element-desc.md)\***

Array of [**D3D10\_INPUT\_ELEMENT\_DESC**](d3d10-input-element-desc.md) elements, describing the vertex format for the returned mesh. This parameter must map directly to a flexible vertex format (FVF).

</dd> <dt>

*DeclCount* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of elements in pDeclaration.

</dd> <dt>

*pPositionSemantic* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Semantic that identifies which part of the vertex declaration contains position information.

</dd> <dt>

*VertexCount* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of vertices for the mesh. This parameter must be greater than 0.

</dd> <dt>

*FaceCount* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Number of faces for the mesh. The valid range for this number is greater than 0, and one less than the maximum DWORD (typically 65534), because the last index is reserved.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Combination of one or more flags from the [**D3DX10\_MESH**](d3dx10-mesh.md), specifying options for the mesh.

</dd> <dt>

*ppMesh* \[out\]
</dt> <dd>

Type: **[**ID3DX10Mesh**](id3dx10mesh.md)\*\***

Address of a pointer to an [**ID3DX10Mesh Interface**](id3dx10mesh.md), representing the created mesh object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](d3d10-graphics-reference-d3dx10-functions-mesh.md)
</dt> <dt>

[D3DX Functions](d3d10-graphics-reference-d3dx10-functions.md)
</dt> </dl>

 

 




