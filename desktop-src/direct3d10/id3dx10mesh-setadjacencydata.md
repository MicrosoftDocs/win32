---
Description: Set the mesh's adjacency data.
ms.assetid: 67d51ce0-7fe2-484d-9874-f1fa59632d59
title: ID3DX10Mesh::SetAdjacencyData method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DX10Mesh::SetAdjacencyData method

Set the mesh's adjacency data.

## Syntax


```C++
HRESULT SetAdjacencyData(
  [in] const UINT *pAdjacency
);
```



## Parameters

<dl> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **const [**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

The adjacency data to set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 




