---
Description: Removes mesh data from the device that has been committed to the device (with ID3DX10MeshCommitToDevice).
ms.assetid: 60eee1f8-f04b-4f33-8f86-0564d0334f97
title: ID3DX10MeshDiscard method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10Mesh::Discard method

Removes mesh data from the device that has been committed to the device (with [**ID3DX10Mesh::CommitToDevice**](id3dx10mesh-committodevice.md)).

## Syntax


```C++
HRESULT Discard(
  [in] D3DX10_MESH_DISCARD_FLAGS dwDiscard
);
```



## Parameters

<dl> <dt>

*dwDiscard* \[in\]
</dt> <dd>

Type: **[**D3DX10\_MESH\_DISCARD\_FLAGS**](d3dx10-mesh-discard-flags.md)**

Specifies which pieces of mesh data to discard from the device. See [**D3DX10\_MESH\_DISCARD\_FLAGS**](d3dx10-mesh-discard-flags.md).

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

 

 




