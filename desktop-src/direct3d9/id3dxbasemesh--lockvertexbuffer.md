---
Description: 'Locks a vertex buffer and obtains a pointer to the vertex buffer memory.'
ms.assetid: 'afcd479c-b268-4720-b26c-88b82f1aab08'
title: 'ID3DXBaseMesh::LockVertexBuffer method'
---

# ID3DXBaseMesh::LockVertexBuffer method

Locks a vertex buffer and obtains a pointer to the vertex buffer memory.

## Syntax


```C++
HRESULT LockVertexBuffer(
  [in]          DWORD  Flags,
  [out, retval] LPVOID *ppData
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
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

VOID\* pointer to a buffer containing the vertex data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be D3DERR\_INVALIDCALL.

## Remarks

When working with vertex buffers, you are allowed to make multiple lock calls; however, you must ensure that the number of lock calls match the number of unlock calls. DrawPrimitive calls will not succeed with any outstanding lock count on any currently set vertex buffer.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> </dl>

 

 




