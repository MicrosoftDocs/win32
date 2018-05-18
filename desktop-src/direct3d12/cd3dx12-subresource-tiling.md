---
title: CD3DX12\_SUBRESOURCE\_TILING structure
description: A helper structure to enable easy initialization of a D3D12\_SUBRESOURCE\_TILING structure.
ms.assetid: '102E5E25-300B-40F2-A953-E40AD7EE61AD'
keywords: ["CD3DX12_SUBRESOURCE_TILING structure"]
topic_type:
- apiref
api_name:
- CD3DX12_SUBRESOURCE_TILING
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_SUBRESOURCE\_TILING structure

A helper structure to enable easy initialization of a [**D3D12\_SUBRESOURCE\_TILING**](d3d12-subresource-tiling.md) structure.

## Syntax


```C++
struct CD3DX12_SUBRESOURCE_TILING  : public D3D12_SUBRESOURCE_TILING{
   CD3DX12_SUBRESOURCE_TILING();
   explicit CD3DX12_SUBRESOURCE_TILING(const D3D12_SUBRESOURCE_TILING &amp;o);
   CD3DX12_SUBRESOURCE_TILING(UINT widthInTiles, UINT16 heightInTiles, UINT16 depthInTiles, UINT startTileIndexInOverallResource);
   operator const D3D12_SUBRESOURCE_TILING&amp;() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_SUBRESOURCE\_TILING()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_SUBRESOURCE\_TILING.

</dd> <dt>

**explicit CD3DX12\_SUBRESOURCE\_TILING(const D3D12\_SUBRESOURCE\_TILING &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_SUBRESOURCE\_TILING, initialized with the contents of another [**D3D12\_SUBRESOURCE\_TILING**](d3d12-subresource-tiling.md) structure.

</dd> <dt>

**CD3DX12\_SUBRESOURCE\_TILING(UINT widthInTiles, UINT16 heightInTiles, UINT16 depthInTiles, UINT startTileIndexInOverallResource)**
</dt> <dd>

Creates a new instance of a CD3DX12\_SUBRESOURCE\_TILING, initializing the following parameters:

UINT widthInTiles

UINT16 heightInTiles

UINT16 depthInTiles

UINT startTileIndexInOverallResource

</dd> <dt>

**operator const D3D12\_SUBRESOURCE\_TILING&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_SUBRESOURCE\_TILING**](d3d12-subresource-tiling.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





