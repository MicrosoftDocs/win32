---
title: CD3DX12\_RESOURCE\_BARRIER structure
description: A helper structure to enable easy initialization of a D3D12\_RESOURCE\_BARRIER structure.
ms.assetid: '89E0F38C-8802-46E6-9583-95C5D853CD99'
keywords: ["CD3DX12_RESOURCE_BARRIER structure"]
topic_type:
- apiref
api_name:
- CD3DX12_RESOURCE_BARRIER
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_RESOURCE\_BARRIER structure

A helper structure to enable easy initialization of a [**D3D12\_RESOURCE\_BARRIER**](d3d12-resource-barrier.md) structure.

## Syntax


```C++
struct CD3DX12_RESOURCE_BARRIER  : public D3D12_RESOURCE_BARRIER{
                           CD3DX12_RESOURCE_BARRIER();
                           explicit CD3DX12_RESOURCE_BARRIER(const D3D12_RESOURCE_BARRIER &amp;o);
  CD3DX12_RESOURCE_BARRIER static inline Transition(ID3D12Resource* pResource, D3D12_RESOURCE_STATES stateBefore, D3D12_RESOURCE_STATES stateAfter, UINT subresource = D3D12_RESOURCE_BARRIER_ALL_SUBRESOURCES, D3D12_RESOURCE_BARRIER_FLAGS flags = D3D12_RESOURCE_BARRIER_FLAG_NONE);
  CD3DX12_RESOURCE_BARRIER static inline Aliasing(ID3D12Resource* pResourceBefore, ID3D12Resource* pResourceAfter);
  CD3DX12_RESOURCE_BARRIER static inline UAV(ID3D12Resource* pResource);
                           operator const D3D12_RESOURCE_BARRIER&amp;() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_RESOURCE\_BARRIER()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_RESOURCE\_BARRIER.

</dd> <dt>

**explicit CD3DX12\_RESOURCE\_BARRIER(const D3D12\_RESOURCE\_BARRIER &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RESOURCE\_BARRIER, initialized with the contents of another [**D3D12\_RESOURCE\_BARRIER**](d3d12-resource-barrier.md).

</dd> <dt>

**static inline Transition(ID3D12Resource\* pResource, D3D12\_RESOURCE\_STATES stateBefore, D3D12\_RESOURCE\_STATES stateAfter, UINT subresource = D3D12\_RESOURCE\_BARRIER\_ALL\_SUBRESOURCES, D3D12\_RESOURCE\_BARRIER\_FLAGS flags = D3D12\_RESOURCE\_BARRIER\_FLAG\_NONE)**
</dt> <dd>

Transitions between resource states, using the following parameters:

[**ID3D12Resource**](id3d12resource.md)\* pResource

[**D3D12\_RESOURCE\_STATES**](d3d12-resource-states.md) stateBefore

[**D3D12\_RESOURCE\_STATES**](d3d12-resource-states.md) stateAfter

(opt) UINT subresource = [**D3D12\_RESOURCE\_BARRIER\_ALL\_SUBRESOURCES**](constants.md)

(opt) [**D3D12\_RESOURCE\_BARRIER\_FLAGS**](d3d12-resource-barrier-flags.md) flags = D3D12\_RESOURCE\_BARRIER\_FLAG\_NONE

</dd> <dt>

**static inline Aliasing(ID3D12Resource\* pResourceBefore, ID3D12Resource\* pResourceAfter)**
</dt> <dd>

Creates aliases for the resource before and after the barrier transition. Parameters:

[**ID3D12Resource**](id3d12resource.md)\* pResourceBefore

[**ID3D12Resource**](id3d12resource.md)\* pResourceAfter

</dd> <dt>

**static inline UAV(ID3D12Resource\* pResource)**
</dt> <dd>

Creates an unordered-access-view (UAV) for the resource. Parameters:

[**ID3D12Resource**](id3d12resource.md)\* pResource

</dd> <dt>

**operator const D3D12\_RESOURCE\_BARRIER&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_RESOURCE\_BARRIER**](d3d12-resource-barrier.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





