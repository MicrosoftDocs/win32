---
Description: Gets the attributes of the patch.
ms.assetid: 601a3275-25ea-4e16-8297-a9fc1f5fdd49
title: ID3DXPatchMeshGetPatchInfo method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPatchMesh::GetPatchInfo method

Gets the attributes of the patch.

## Syntax


```C++
HRESULT GetPatchInfo(
  [out, retval] LPD3DXPATCHINFO PatchInfo
);
```



## Parameters

<dl> <dt>

*PatchInfo* \[out, retval\]
</dt> <dd>

Type: **[**LPD3DXPATCHINFO**](d3dxpatchinfo.md)**

Pointer to the structures containing the patch attributes. For more information about patch attributes, see [**D3DXPATCHINFO**](d3dxpatchinfo.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 




