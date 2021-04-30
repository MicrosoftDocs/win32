---
title: CD3DX12_RESOURCE_BARRIER structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_RESOURCE\_BARRIER structure.
ms.assetid: 89E0F38C-8802-46E6-9583-95C5D853CD99
keywords:
- CD3DX12_RESOURCE_BARRIER structure
topic_type:
- apiref
api_name:
- CD3DX12_RESOURCE_BARRIER
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_RESOURCE\_BARRIER structure

A helper structure to enable easy initialization of a [**D3D12\_RESOURCE\_BARRIER**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_barrier) structure.

## Syntax


```C++
struct CD3DX12_RESOURCE_BARRIER  : public D3D12_RESOURCE_BARRIER{
                           CD3DX12_RESOURCE_BARRIER();
                           explicit CD3DX12_RESOURCE_BARRIER(const D3D12_RESOURCE_BARRIER &o);
  CD3DX12_RESOURCE_BARRIER static inline Transition(ID3D12Resource* pResource, D3D12_RESOURCE_STATES stateBefore, D3D12_RESOURCE_STATES stateAfter, UINT subresource = D3D12_RESOURCE_BARRIER_ALL_SUBRESOURCES, D3D12_RESOURCE_BARRIER_FLAGS flags = D3D12_RESOURCE_BARRIER_FLAG_NONE);
  CD3DX12_RESOURCE_BARRIER static inline Aliasing(ID3D12Resource* pResourceBefore, ID3D12Resource* pResourceAfter);
  CD3DX12_RESOURCE_BARRIER static inline UAV(ID3D12Resource* pResource);
                           operator const D3D12_RESOURCE_BARRIER&() const;
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

Creates a new instance of a CD3DX12\_RESOURCE\_BARRIER, initialized with the contents of another [**D3D12\_RESOURCE\_BARRIER**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_barrier).

</dd> <dt>

**static inline Transition(ID3D12Resource\* pResource, D3D12\_RESOURCE\_STATES stateBefore, D3D12\_RESOURCE\_STATES stateAfter, UINT subresource = D3D12\_RESOURCE\_BARRIER\_ALL\_SUBRESOURCES, D3D12\_RESOURCE\_BARRIER\_FLAGS flags = D3D12\_RESOURCE\_BARRIER\_FLAG\_NONE)**
</dt> <dd>

Transitions between resource states, using the following parameters:

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)\* pResource

[**D3D12\_RESOURCE\_STATES**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_states) stateBefore

[**D3D12\_RESOURCE\_STATES**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_states) stateAfter

(opt) UINT subresource = [**D3D12\_RESOURCE\_BARRIER\_ALL\_SUBRESOURCES**](constants.md)

(opt) [**D3D12\_RESOURCE\_BARRIER\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_barrier_flags) flags = D3D12\_RESOURCE\_BARRIER\_FLAG\_NONE

</dd> <dt>

**static inline Aliasing(ID3D12Resource\* pResourceBefore, ID3D12Resource\* pResourceAfter)**
</dt> <dd>

Creates aliases for the resource before and after the barrier transition. Parameters:

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)\* pResourceBefore

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)\* pResourceAfter

</dd> <dt>

**static inline UAV(ID3D12Resource\* pResource)**
</dt> <dd>

Creates an unordered-access-view (UAV) for the resource. Parameters:

[**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource)\* pResource

</dd> <dt>

**operator const D3D12\_RESOURCE\_BARRIER&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_RESOURCE\_BARRIER**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_barrier)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





