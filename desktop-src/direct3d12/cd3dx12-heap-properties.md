---
title: CD3DX12_HEAP_PROPERTIES structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_HEAP\_PROPERTIES structure.
ms.assetid: AC759F25-D643-412D-AA83-3A2C040BE64B
keywords:
- CD3DX12_HEAP_PROPERTIES structure
topic_type:
- apiref
api_name:
- CD3DX12_HEAP_PROPERTIES
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_HEAP\_PROPERTIES structure

A helper structure to enable easy initialization of a [**D3D12\_HEAP\_PROPERTIES**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_properties) structure.

## Syntax


```C++
struct CD3DX12_HEAP_PROPERTIES  : public D3D12_HEAP_PROPERTIES{
       CD3DX12_HEAP_PROPERTIES();
       explicit CD3DX12_HEAP_PROPERTIES(const D3D12_HEAP_PROPERTIES &o);
       CD3DX12_HEAP_PROPERTIES(D3D12_CPU_PAGE_PROPERTY cpuPageProperty, D3D12_MEMORY_POOL memoryPoolPreference, UINT creationNodeMask = 1, UINT nodeMask = 1);
       explicit CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE type, UINT creationNodeMask = 1, UINT nodeMask = 1);
       operator const D3D12_HEAP_PROPERTIES&() const;
  bool inline operator==( const D3D12_HEAP_PROPERTIES& l, const D3D12_HEAP_PROPERTIES& r );
  bool inline operator!=( const D3D12_HEAP_PROPERTIES& l, const D3D12_HEAP_PROPERTIES& r );
};
```



## Members

<dl> <dt>

**CD3DX12\_HEAP\_PROPERTIES()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_HEAP\_PROPERTIES.

</dd> <dt>

**explicit CD3DX12\_HEAP\_PROPERTIES(const D3D12\_HEAP\_PROPERTIES &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_PROPERTIES, initialized with the contents of another [**D3D12\_HEAP\_PROPERTIES**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_properties) structure.

</dd> <dt>

**CD3DX12\_HEAP\_PROPERTIES(D3D12\_CPU\_PAGE\_PROPERTY cpuPageProperty, D3D12\_MEMORY\_POOL memoryPoolPreference, UINT creationNodeMask = 1, UINT nodeMask = 1)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_PROPERTIES, initializing the following parameters:

[**D3D12\_CPU\_PAGE\_PROPERTY**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_cpu_page_property) cpuPageProperty

[**D3D12\_MEMORY\_POOL**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_memory_pool) memoryPoolPreference

(opt) UINT creationNodeMask = 1

(opt) UINT nodeMask = 1

</dd> <dt>

**explicit CD3DX12\_HEAP\_PROPERTIES(D3D12\_HEAP\_TYPE type, UINT creationNodeMask = 1, UINT nodeMask = 1)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_PROPERTIES, initializing the following parameters:

[**D3D12\_HEAP\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_type) type

(opt) UINT creationNodeMask = 1

(opt) UINT nodeMask = 1

</dd> <dt>

**operator const D3D12\_HEAP\_PROPERTIES&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> <dt>

**inline operator==( const D3D12\_HEAP\_PROPERTIES& l, const D3D12\_HEAP\_PROPERTIES& r )**
</dt> <dd>

Tests for equality between the specified D3D12\_HEAP\_PROPERTIES instances, based on equality of all member fields.

</dd> <dt>

**inline operator!=( const D3D12\_HEAP\_PROPERTIES& l, const D3D12\_HEAP\_PROPERTIES& r )**
</dt> <dd>

Tests for inequality between the specified D3D12\_HEAP\_PROPERTIES instances. Implemented by taking the inverse of the **operator==** value.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_HEAP\_PROPERTIES**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_properties)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





