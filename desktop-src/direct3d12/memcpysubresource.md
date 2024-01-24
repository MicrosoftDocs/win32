---
title: MemcpySubresource function (D3dx12.h)
description: Copies a subresource row by row.
ms.assetid: 33A9F99D-FD85-4FD6-AFD6-7A10F16C3D9B
keywords:
- MemcpySubresource function
topic_type:
- apiref
api_name:
- MemcpySubresource
api_location:
- D3D12.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MemcpySubresource function

Copies a subresource row by row.

## Syntax


```C++
void inline MemcpySubresource(
  _In_ const D3D12_MEMCPY_DEST      *pDest,
  _In_ const D3D12_SUBRESOURCE_DATA *pSrc,
             SIZE_T                 RowSizeInBytes,
             UINT                   NumRows,
             UINT                   NumSlices
);
```



## Parameters

<dl> <dt>

*pDest* \[in\]
</dt> <dd>

Type: **const [**D3D12\_MEMCPY\_DEST**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_memcpy_dest)\***

A pointer to a [**D3D12\_MEMCPY\_DEST**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_memcpy_dest) structure that describes the destination of the memory copy operation.

</dd> <dt>

*pSrc* \[in\]
</dt> <dd>

Type: **const [**D3D12\_SUBRESOURCE\_DATA**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_subresource_data)\***

A pointer to a [**D3D12\_SUBRESOURCE\_DATA**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_subresource_data) structure that describes the source of the memory copy operation.

</dd> <dt>

*RowSizeInBytes* 
</dt> <dd>

Type: **[**SIZE\_T**](/windows/desktop/WinProg/windows-data-types)**

The size, in bytes, of each row.

</dd> <dt>

*NumRows* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of rows.

</dd> <dt>

*NumSlices* 
</dt> <dd>

Type: **[**UINT**](/windows/desktop/WinProg/windows-data-types)**

The number of slices.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Also consider the following methods:

-   [**ID3D12Resource::WriteToSubresource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12resource-writetosubresource)
-   [**ID3D12Resource::ReadFromSubresource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12resource-readfromsubresource)
-   [**ID3D12GraphicsCommandList::CopyResource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copyresource)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx12.h</dt> </dl>  |
| Library<br/> | <dl> <dt>D3D12.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D3D12.dll</dt> </dl> |



## See also

<dl> <dt>

[Helper Functions for D3D12](helper-functions-for-d3d12.md)
</dt> <dt>

[Subresources](subresources.md)
</dt> </dl>

 

