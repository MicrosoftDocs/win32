---
title: CD3DX12_TEXTURE_COPY_LOCATION structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_TEXTURE\_COPY\_LOCATION structure.
ms.assetid: 8BA93729-2FFB-4C09-88B0-779049BAF385
keywords:
- CD3DX12_TEXTURE_COPY_LOCATION structure
topic_type:
- apiref
api_name:
- CD3DX12_TEXTURE_COPY_LOCATION
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_TEXTURE\_COPY\_LOCATION structure

A helper structure to enable easy initialization of a [**D3D12\_TEXTURE\_COPY\_LOCATION**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_texture_copy_location) structure.

## Syntax


```C++
struct CD3DX12_TEXTURE_COPY_LOCATION  : public D3D12_TEXTURE_COPY_LOCATION{
   CD3DX12_TEXTURE_COPY_LOCATION();
   explicit CD3DX12_TEXTURE_COPY_LOCATION(const D3D12_TEXTURE_COPY_LOCATION &o);
   CD3DX12_TEXTURE_COPY_LOCATION(ID3D12Resource* pRes);
   CD3DX12_TEXTURE_COPY_LOCATION(ID3D12Resource* pRes, D3D12_PLACED_SUBRESOURCE_FOOTPRINT const& Footprint);
   CD3DX12_TEXTURE_COPY_LOCATION(ID3D12Resource* pRes, UINT Sub);
};
```



## Members

<dl> <dt>

**CD3DX12\_TEXTURE\_COPY\_LOCATION()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_TEXTURE\_COPY\_LOCATION.

</dd> <dt>

**explicit CD3DX12\_TEXTURE\_COPY\_LOCATION(const D3D12\_TEXTURE\_COPY\_LOCATION &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_TEXTURE\_COPY\_LOCATION, initialized with the contents of another [**D3D12\_TEXTURE\_COPY\_LOCATION**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_texture_copy_location) structure.

</dd> <dt>

**CD3DX12\_TEXTURE\_COPY\_LOCATION(ID3D12Resource\* pRes)**
</dt> <dd>

Creates a new instance of a CD3DX12\_TEXTURE\_COPY\_LOCATION, initializing the following parameters:

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)\* pRes

</dd> <dt>

**CD3DX12\_TEXTURE\_COPY\_LOCATION(ID3D12Resource\* pRes, D3D12\_PLACED\_SUBRESOURCE\_FOOTPRINT const& Footprint)**
</dt> <dd>

Creates a new instance of a CD3DX12\_TEXTURE\_COPY\_LOCATION, initializing the following parameters:

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)\* pRes

[**D3D12\_PLACED\_SUBRESOURCE\_FOOTPRINT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_placed_subresource_footprint) const& Footprint

</dd> <dt>

**CD3DX12\_TEXTURE\_COPY\_LOCATION(ID3D12Resource\* pRes, UINT Sub)**
</dt> <dd>

Creates a new instance of a CD3DX12\_TEXTURE\_COPY\_LOCATION, initializing the following parameters:

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)\* pRes

UINT Sub

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_TEXTURE\_COPY\_LOCATION**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_texture_copy_location)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





