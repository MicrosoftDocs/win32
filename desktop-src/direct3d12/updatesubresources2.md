---
title: UpdateSubresources (heap-allocating) function
description: Updates subresources with a heap-allocating implementation.
ms.assetid: '328D8755-D328-471D-AAF4-9771CBFF7539'
keywords: ["UpdateSubresources function"]
topic_type:
- apiref
api_name:
- UpdateSubresources
api_location:
- D3D12.dll
api_type:
- DllExport
---

# UpdateSubresources (heap-allocating) function

Updates subresources with a heap-allocating implementation.

## Syntax


```C++
UINT64 inline UpdateSubresources(
  _In_ ID3D12GraphicsCommandList *pCmdList,
  _In_ ID3D12Resource            *pDestinationResource,
  _In_ ID3D12Resource            *pIntermediate,
       UINT64                    IntermediateOffset,
  _In_ UINT                      FirstSubresource,
  _In_ UINT                      NumSubresources,
  _In_ D3D12_SUBRESOURCE_DATA    *pSrcData
);
```



## Parameters

<dl> <dt>

*pCmdList* \[in\]
</dt> <dd>

Type: **[**ID3D12GraphicsCommandList**](id3d12graphicscommandlist.md)\***

A pointer to the [**ID3D12GraphicsCommandList**](id3d12graphicscommandlist.md) interface for the command list.

</dd> <dt>

*pDestinationResource* \[in\]
</dt> <dd>

Type: **[**ID3D12Resource**](id3d12resource.md)\***

A pointer to the [**ID3D12Resource**](id3d12resource.md) interface that represents the destination resource.

</dd> <dt>

*pIntermediate* \[in\]
</dt> <dd>

Type: **[**ID3D12Resource**](id3d12resource.md)\***

A pointer to the [**ID3D12Resource**](id3d12resource.md) interface that represents the intermediate resource.

</dd> <dt>

*IntermediateOffset* 
</dt> <dd>

Type: **[**UINT64**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The offset, in bytes, to the intermediate resource.

</dd> <dt>

*FirstSubresource* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The index of the first subresource in the resource. The range of valid values is 0 to D3D12\_REQ\_SUBRESOURCES.

</dd> <dt>

*NumSubresources* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The number of subresources in the resource. The range of valid values is 0 to (D3D12\_REQ\_SUBRESOURCES - *FirstSubresource*).

</dd> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**D3D12\_SUBRESOURCE\_DATA**](d3d12-subresource-data.md)\***

Pointer to an array (of length *NumSubresources*) of pointers to [**D3D12\_SUBRESOURCE\_DATA**](d3d12-subresource-data.md) structures containing descriptions of the subresource data used for the update.

</dd> </dl>

## Return value

Type: **[**UINT64**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The size, in bytes, of the buffer.

## Requirements



|                    |                                                                                      |
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

 

 





