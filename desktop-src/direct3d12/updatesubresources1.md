---
title: UpdateSubresources function
description: Updates subresources, all the subresource arrays should be populated, typically by calling ID3D12Device GetCopyableFootprints.
ms.assetid: 'D6885165-095E-452D-8D93-A2C43A215F48'
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

# UpdateSubresources function

Updates subresources, all the subresource arrays should be populated, typically by calling [**ID3D12Device::GetCopyableFootprints**](id3d12device-getcopyablefootprints.md).

## Syntax


```C++
UINT64 inline UpdateSubresources(
  _In_       ID3D12GraphicsCommandList          *pCmdList,
  _In_       ID3D12Resource                     *pDestinationResource,
  _In_       ID3D12Resource                     *pIntermediate,
  _In_       UINT                               FirstSubresource,
  _In_       UINT                               NumSubresources,
             UINT64                             RequiredSize,
  _In_ const D3D12_PLACED_SUBRESOURCE_FOOTPRINT *pLayouts,
  _In_ const UINT                               *pNumRows,
  _In_ const UINT64                             *pRowSizesInBytes,
  _In_ const D3D12_SUBRESOURCE_DATA             *pSrcData
);
```



## Parameters

<dl> <dt>

*pCmdList* \[in\]
</dt> <dd>

Type: **[**ID3D12GraphicsCommandList**](id3d12graphicscommandlist.md)\***

The command list, as a pointer to an [**ID3D12GraphicsCommandList**](id3d12graphicscommandlist.md).

</dd> <dt>

*pDestinationResource* \[in\]
</dt> <dd>

Type: **[**ID3D12Resource**](id3d12resource.md)\***

The destination resource, as a pointer to an [**ID3D12Resource**](id3d12resource.md).

</dd> <dt>

*pIntermediate* \[in\]
</dt> <dd>

Type: **[**ID3D12Resource**](id3d12resource.md)\***

The intermediate resource, as a pointer to an [**ID3D12Resource**](id3d12resource.md).

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

*RequiredSize* 
</dt> <dd>

Type: **[**UINT64**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The required size, in bytes, for the update.

</dd> <dt>

*pLayouts* \[in\]
</dt> <dd>

Type: **const [**D3D12\_PLACED\_SUBRESOURCE\_FOOTPRINT**](d3d12-placed-subresource-footprint.md)\***

Pointer to an array (of length *NumSubresources*) of pointers to the structures that contains the description and placement of the resource's subresources.

</dd> <dt>

*pNumRows* \[in\]
</dt> <dd>

Type: **const [**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)\***

Pointer to an array (of length *NumSubresources*) of UINTS containing the number of rows for each subresource.

</dd> <dt>

*pRowSizesInBytes* \[in\]
</dt> <dd>

Type: **const [**UINT64**](https://msdn.microsoft.com/library/windows/desktop/aa383751)\***

Pointer to an array (of length *NumSubresources*) of UINTS containing the size, in bytes, of each row.

</dd> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **const [**D3D12\_SUBRESOURCE\_DATA**](d3d12-subresource-data.md)\***

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

 

 





