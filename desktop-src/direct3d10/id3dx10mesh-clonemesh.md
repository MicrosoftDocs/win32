---
Description: Creates a new mesh and fills it with the data of a previously loaded mesh.
ms.assetid: 2ce39982-abc0-444b-bc6f-24508f76fe31
title: ID3DX10MeshCloneMesh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**UINT**](winprog.windows_data_types)**

Creation flags to be applied to the new mesh. See [**D3DX10\_MESH**](d3dx10-mesh.md).

</dd> <dt>

*pPosSemantic* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

The semantic name for the position data.

</dd> <dt>

*pDesc* \[in\]
</dt> <dd>

Type: **const [**D3D10\_INPUT\_ELEMENT\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_input_element_desc?branch=master)\***

Array of D3D10\_INPUT\_ELEMENT\_DESC structures, describing the vertex format for the returned mesh. See [**D3D10\_INPUT\_ELEMENT\_DESC**](/windows/win32/D3D10/ns-d3d10-d3d10_input_element_desc?branch=master).

</dd> <dt>

*DeclCount* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The number of elements in the pDesc array.

</dd> <dt>

*ppCloneMesh* \[out\]
</dt> <dd>

Type: **[**ID3DX10Mesh**](id3dx10mesh.md)\*\***

The new mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




