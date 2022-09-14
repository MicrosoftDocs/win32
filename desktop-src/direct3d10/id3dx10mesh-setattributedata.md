---
description: Set the mesh's attribute data.
ms.assetid: bcf7b1b3-b923-400a-8d12-5094f3844d8f
title: ID3DX10Mesh::SetAttributeData method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.SetAttributeData
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh::SetAttributeData method

Set the mesh's attribute data.

## Syntax


```C++
HRESULT SetAttributeData(
  [in] const UINT *pData
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Type: **const [**UINT**](../winprog/windows-data-types.md)\***

The attribute data to set.

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

 

 
