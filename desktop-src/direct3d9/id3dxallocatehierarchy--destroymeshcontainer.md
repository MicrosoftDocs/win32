---
description: Requests deallocation of a mesh container object.
ms.assetid: 7a976ba8-6972-4857-b0a9-4ea7a88dc8ac
title: ID3DXAllocateHierarchy::DestroyMeshContainer method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAllocateHierarchy.DestroyMeshContainer
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAllocateHierarchy::DestroyMeshContainer method

Requests deallocation of a mesh container object.

## Syntax


```C++
HRESULT DestroyMeshContainer(
  [in] LPD3DXMESHCONTAINER pMeshContainerToFree
);
```



## Parameters

<dl> <dt>

*pMeshContainerToFree* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESHCONTAINER**](d3dxmeshcontainer.md)**

Pointer to the mesh container object to be deallocated.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from D3DERR or D3DXERR, as this will cause [**D3DXLoadMeshHierarchyFromX**](d3dxloadmeshhierarchyfromx.md) to fail also, and return the error.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAllocateHierarchy](id3dxallocatehierarchy.md)
</dt> </dl>

 

 




