---
description: Set the point rep data for the mesh.
ms.assetid: 451a1ff0-68fa-48c4-b3f1-d41d7583cb3f
title: ID3DX10Mesh::SetPointRepData method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.SetPointRepData
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh::SetPointRepData method

Set the point rep data for the mesh.

## Syntax


```C++
HRESULT SetPointRepData(
  [in] const UINT *pPointReps
);
```



## Parameters

<dl> <dt>

*pPointReps* \[in\]
</dt> <dd>

Type: **const [**UINT**](../winprog/windows-data-types.md)\***

The point rep data to set.

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

 

 
