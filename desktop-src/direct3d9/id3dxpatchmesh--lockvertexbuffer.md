---
Description: Lock the vertex buffer.
ms.assetid: f7e4f27d-1b40-4b0d-8173-48a0b15cfc95
title: ID3DXPatchMeshLockVertexBuffer method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXPatchMesh::LockVertexBuffer method

Lock the vertex buffer.

## Syntax


```C++
HRESULT LockVertexBuffer(
  [in]          DWORD  flags,
  [out, retval] LPVOID *ppData
);
```



## Parameters

<dl> <dt>

*flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Combination of zero or more locking flags that describe the type of lock to perform. For this method, the valid flags are:

-   D3DLOCK\_DISCARD
-   D3DLOCK\_NO\_DIRTY\_UPDATE
-   D3DLOCK\_NOSYSLOCK
-   D3DLOCK\_READONLY
-   D3DLOCK\_NOOVERWRITE

For a description of the flags, see [D3DLOCK](d3dlock.md).

</dd> <dt>

*ppData* \[out, retval\]
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)\***

VOID\* pointer to a memory buffer containing the returned vertex data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

The vertex buffer is usually locked, written to, and then unlocked for reading.

Patch meshes use 16-bit index buffers.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 




