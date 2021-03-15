---
description: Access the vertex description passed into D3DX10CreateMesh. The vertex description describes the layout of the mesh's vertex buffers.
ms.assetid: e4a4a98a-e131-414c-ad98-21288ff0c61b
title: ID3DX10Mesh::GetVertexDescription method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.GetVertexDescription
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh::GetVertexDescription method

Access the vertex description passed into [**D3DX10CreateMesh**](d3d10-d3dx10createmesh.md). The vertex description describes the layout of the mesh's vertex buffers.

## Syntax


```C++
HRESULT GetVertexDescription(
  [out] const D3D10_INPUT_ELEMENT_DESC **ppDesc,
  [in]        UINT                     *pDeclCount
);
```



## Parameters

<dl> <dt>

*ppDesc* \[out\]
</dt> <dd>

Type: **const [**D3D10\_INPUT\_ELEMENT\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_input_element_desc)\*\***

Array of input elements that describe the layout of the mesh's vertex buffers. See [**D3D10\_INPUT\_ELEMENT\_DESC**](/windows/desktop/api/D3D10/ns-d3d10-d3d10_input_element_desc).

</dd> <dt>

*pDeclCount* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)\***

The number of input elements in ppDesc.

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

 

 
