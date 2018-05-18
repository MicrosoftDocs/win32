---
title: CD3DX12\_PACKED\_MIP\_INFO structure
description: A helper structure to enable easy initialization of a D3D12\_PACKED\_MIP\_INFO structure.
ms.assetid: 'B3549D78-C354-48FC-A012-1F835DBD585E'
keywords: ["CD3DX12_PACKED_MIP_INFO structure"]
topic_type:
- apiref
api_name:
- CD3DX12_PACKED_MIP_INFO
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_PACKED\_MIP\_INFO structure

A helper structure to enable easy initialization of a [**D3D12\_PACKED\_MIP\_INFO**](d3d12-packed-mip-info.md) structure.

## Syntax


```C++
struct CD3DX12_PACKED_MIP_INFO  : public D3D12_PACKED_MIP_INFO{
   CD3DX12_PACKED_MIP_INFO();
   explicit CD3DX12_PACKED_MIP_INFO(const D3D12_PACKED_MIP_INFO &amp;o);
   CD3DX12_PACKED_MIP_INFO(UINT8 numStandardMips, UINT8 numPackedMips, UINT numTilesForPackedMips, UINT startTileIndexInOverallResource);
   operator const D3D12_PACKED_MIP_INFO&amp;() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PACKED\_MIP\_INFO()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PACKED\_MIP\_INFO.

</dd> <dt>

**explicit CD3DX12\_PACKED\_MIP\_INFO(const D3D12\_PACKED\_MIP\_INFO &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PACKED\_MIP\_INFO, initialized with the contents of another [**D3D12\_PACKED\_MIP\_INFO**](d3d12-packed-mip-info.md) structure.

</dd> <dt>

**CD3DX12\_PACKED\_MIP\_INFO(UINT8 numStandardMips, UINT8 numPackedMips, UINT numTilesForPackedMips, UINT startTileIndexInOverallResource)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PACKED\_MIP\_INFO, initializing the following parameters:

UINT8 numStandardMips

UINT8 numPackedMips

UINT numTilesForPackedMips

UINT startTileIndexInOverallResource

</dd> <dt>

**operator const D3D12\_PACKED\_MIP\_INFO&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_PACKED\_MIP\_INFO**](d3d12-packed-mip-info.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





