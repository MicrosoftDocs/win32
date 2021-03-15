---
description: Locks an index buffer and obtains a pointer to the index buffer memory.
ms.assetid: c8941164-1f2a-4aed-b0bd-8130aac61da4
title: ID3DXBaseMesh::LockIndexBuffer method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseMesh.LockIndexBuffer
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXBaseMesh::LockIndexBuffer method

Locks an index buffer and obtains a pointer to the index buffer memory.

## Syntax


```C++
HRESULT LockIndexBuffer(
  [in]          DWORD  Flags,
  [out, retval] LPVOID *ppData
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of zero or more locking flags that describe the type of lock to perform. For this method, the valid flags are:

-   D3DLOCK\_DISCARD
-   D3DLOCK\_NO\_DIRTY\_UPDATE
-   D3DLOCK\_NOSYSLOCK
-   D3DLOCK\_READONLY

For a description of the flags, see [D3DLOCK](d3dlock.md).

</dd> <dt>

*ppData* \[out, retval\]
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)\***

VOID\* pointer to a buffer containing the index data. The count of indices in this buffer will be equal to [**ID3DXBaseMesh::GetNumFaces**](id3dxbasemesh--getnumfaces.md) \* 3.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

When working with index buffers, you are allowed to make multiple lock calls. However, you must ensure that the number of lock calls match the number of unlock calls. DrawPrimitive calls will not succeed with any outstanding lock count on any currently set index buffer.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 
