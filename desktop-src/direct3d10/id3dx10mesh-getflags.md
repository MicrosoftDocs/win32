---
description: Access the mesh's creation flags.
ms.assetid: df21aa5d-d8c4-43ee-8b22-ca1ee75ecf64
title: ID3DX10Mesh::GetFlags method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.GetFlags
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh::GetFlags method

Access the mesh's creation flags.

## Syntax


```C++
UINT GetFlags();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**UINT**](../winprog/windows-data-types.md)**

The creation flags passed into the *options* parameter of [**D3DX10CreateMesh**](d3d10-d3dx10createmesh.md) when the mesh was created. See [**D3DX10\_MESH**](d3dx10-mesh.md).

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

 

 
