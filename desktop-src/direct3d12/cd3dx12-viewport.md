---
title: CD3DX12_VIEWPORT structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_VIEWPORT structure.
ms.assetid: 1A824F54-596B-450E-A191-B60FBBBB60ED
keywords:
- CD3DX12_VIEWPORT structure
topic_type:
- apiref
api_name:
- CD3DX12_VIEWPORT
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_VIEWPORT structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

A helper structure to enable easy initialization of a [**D3D12\_VIEWPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_viewport) structure.

## Syntax


```C++
struct CD3DX12_VIEWPORT  : public D3D12_VIEWPORT{
   CD3DX12_VIEWPORT();
   explicit CD3DX12_VIEWPORT(const D3D12_VIEWPORT& o);
   explicit CD3DX12_VIEWPORT(FLOAT topLeftX, FLOAT topLeftY, FLOAT width, FLOAT height, FLOAT minDepth = D3D12_MIN_DEPTH, FLOAT maxDepth = D3D12_MAX_DEPTH);
   explicit CD3DX12_VIEWPORT(ID3D12Resource* pResource, UINT mipSlice = 0, FLOAT topLeftX = 0.0f, FLOAT topLeftY = 0.0f, FLOAT minDepth = D3D12_MIN_DEPTH, FLOAT maxDepth = D3D12_MAX_DEPTH);
   ~CD3DX12_VIEWPORT();
   operator const D3D12_VIEWPORT&() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_VIEWPORT()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_VIEWPORT.

</dd> <dt>

**explicit CD3DX12\_VIEWPORT(const D3D12\_VIEWPORT& o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VIEWPORT, initializing the following parameters:

const D3D12\_VIEWPORT& o

</dd> <dt>

**explicit CD3DX12\_VIEWPORT(FLOAT topLeftX, FLOAT topLeftY, FLOAT width, FLOAT height, FLOAT minDepth = D3D12\_MIN\_DEPTH, FLOAT maxDepth = D3D12\_MAX\_DEPTH)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VIEWPORT, initializing the following parameters:

FLOAT topLeftX

FLOAT topLeftY

FLOAT width

FLOAT height

FLOAT minDepth = D3D12\_MIN\_DEPTH

FLOAT maxDepth = D3D12\_MAX\_DEPTH

</dd> <dt>

**explicit CD3DX12\_VIEWPORT(ID3D12Resource\* pResource, UINT mipSlice = 0, FLOAT topLeftX = 0.0f, FLOAT topLeftY = 0.0f, FLOAT minDepth = D3D12\_MIN\_DEPTH, FLOAT maxDepth = D3D12\_MAX\_DEPTH)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VIEWPORT, initializing the following parameters:

ID3D12Resource\* pResource

UINT mipSlice = 0

FLOAT topLeftX = 0.0f

FLOAT topLeftY = 0.0f

FLOAT minDepth = D3D12\_MIN\_DEPTH

FLOAT maxDepth = D3D12\_MAX\_DEPTH

</dd> <dt>

**~CD3DX12\_VIEWPORT()**
</dt> <dd>

Destroys an instance of a D3DX12\_VIEWPORT.

</dd> <dt>

**operator const D3D12\_VIEWPORT&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_VIEWPORT**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_viewport)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





