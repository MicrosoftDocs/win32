---
Description: Locks the mesh buffer that contains the mesh attribute data, and returns a pointer to it.
ms.assetid: 17a321b8-bfb4-4018-869f-6b09e0a811eb
title: ID3DXMesh::LockAttributeBuffer method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXMesh::LockAttributeBuffer method

Locks the mesh buffer that contains the mesh attribute data, and returns a pointer to it.

## Syntax


```C++
HRESULT LockAttributeBuffer(
  [in]  DWORD Flags,
  [out] DWORD **ppData
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Combination of zero or more locking flags that describe the type of lock to perform. For this method, the valid flags are:

-   D3DLOCK\_DISCARD
-   D3DLOCK\_NO\_DIRTY\_UPDATE
-   D3DLOCK\_NOSYSLOCK
-   D3DLOCK\_READONLY

For a description of the flags, see [D3DLOCK](d3dlock.md).

</dd> <dt>

*ppData* \[out\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\*\***

Address of a pointer to a buffer containing a DWORD for each face in the mesh.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

If [**ID3DXMesh::Optimize**](id3dxmesh--optimize.md) has been called, the mesh will also have an attribute table that can be accessed using the [**ID3DXBaseMesh::GetAttributeTable**](id3dxbasemesh--getattributetable.md) method.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMesh](id3dxmesh.md)
</dt> <dt>

[**ID3DXMesh::UnlockAttributeBuffer**](id3dxmesh--unlockattributebuffer.md)
</dt> <dt>

[**ID3DXBaseMesh::GetAttributeTable**](id3dxbasemesh--getattributetable.md)
</dt> <dt>

[**ID3DXMesh::SetAttributeTable**](id3dxmesh--setattributetable.md)
</dt> </dl>

 

 




