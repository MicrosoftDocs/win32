---
description: Creates a new mesh and fills it with the data of a previously loaded mesh.
ms.assetid: 2ce39982-abc0-444b-bc6f-24508f76fe31
title: ID3DX10Mesh::CloneMesh method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.CloneMesh
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh::CloneMesh method

Creates a new mesh and fills it with the data of a previously loaded mesh.

## Syntax


```C++
HRESULT CloneMesh(
  [in]        UINT                     Flags,
  [in]        LPCSTR                   pPosSemantic,
  [in]  const D3D10_INPUT_ELEMENT_DESC *pDesc,
  [in]        UINT                     DeclCount,
  [out]       ID3DX10Mesh              **ppCloneMesh
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Creation flags to be applied to the new mesh. See [**D3DX10\_MESH**](d3dx10-mesh.md).

</dd> <dt>

*pPosSemantic* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

The semantic name for the position data.

</dd> <dt>

*pDesc* \[in\]
</dt> <dd>

Type: **const [**D3D10\_INPUT\_ELEMENT\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_input_element_desc)\***

Array of D3D10\_INPUT\_ELEMENT\_DESC structures, describing the vertex format for the returned mesh. See [**D3D10\_INPUT\_ELEMENT\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_input_element_desc).

</dd> <dt>

*DeclCount* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of elements in the pDesc array.

</dd> <dt>

*ppCloneMesh* \[out\]
</dt> <dd>

Type: **[**ID3DX10Mesh**](id3dx10mesh.md)\*\***

The new mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
