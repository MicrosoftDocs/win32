---
title: CD3DX12_HEAP_DESC structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_HEAP\_DESC structure.
ms.assetid: 38E0BA60-2BB0-4AC1-870A-10AB16E4C6E6
keywords:
- CD3DX12_HEAP_DESC structure
topic_type:
- apiref
api_name:
- CD3DX12_HEAP_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_HEAP\_DESC structure

A helper structure to enable easy initialization of a [**D3D12\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_desc) structure.

## Syntax


```C++
struct CD3DX12_HEAP_DESC  : public D3D12_HEAP_DESC{
   CD3DX12_HEAP_DESC();
   explicit CD3DX12_HEAP_DESC(const D3D12_HEAP_DESC &o);
   CD3DX12_HEAP_DESC(UINT64 size, D3D12_HEAP_PROPERTIES properties, UINT64 alignment = 0, D3D12_HEAP_FLAGS flags = D3D12_HEAP_FLAG_NONE);
   CD3DX12_HEAP_DESC(UINT64 size, D3D12_HEAP_TYPE type, UINT64 alignment = 0, D3D12_HEAP_FLAGS flags = D3D12_HEAP_FLAG_NONE);
   CD3DX12_HEAP_DESC(UINT64 size, D3D12_CPU_PAGE_PROPERTY cpuPageProperty, D3D12_MEMORY_POOL memoryPoolPreference, UINT64 alignment = 0, D3D12_HEAP_FLAGS flags = D3D12_HEAP_FLAG_NONE);
   CD3DX12_HEAP_DESC(const D3D12_RESOURCE_ALLOCATION_INFO& resAllocInfo, D3D12_HEAP_PROPERTIES properties, D3D12_HEAP_FLAGS flags = D3D12_HEAP_FLAG_NONE);
   CD3DX12_HEAP_DESC(const D3D12_RESOURCE_ALLOCATION_INFO& resAllocInfo, D3D12_HEAP_TYPE type, D3D12_HEAP_FLAGS flags = D3D12_HEAP_FLAG_NONE);
   CD3DX12_HEAP_DESC(const D3D12_RESOURCE_ALLOCATION_INFO& resAllocInfo, D3D12_CPU_PAGE_PROPERTY cpuPageProperty, D3D12_MEMORY_POOL memoryPoolPreference, D3D12_HEAP_FLAGS flags = D3D12_HEAP_FLAG_NONE);
   operator const D3D12_HEAP_DESC&() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_HEAP\_DESC()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_HEAP\_DESC.

</dd> <dt>

**explicit CD3DX12\_HEAP\_DESC(const D3D12\_HEAP\_DESC &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_DESC, initialized with the contents of another [**D3D12\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_desc) structure.

</dd> <dt>

**CD3DX12\_HEAP\_DESC(UINT64 size, D3D12\_HEAP\_PROPERTIES properties, UINT64 alignment = 0, D3D12\_HEAP\_FLAGS flags = D3D12\_HEAP\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_DESC, initializing the following parameters:

UINT64 size

[**D3D12\_HEAP\_PROPERTIES**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_properties) properties

(opt) UINT64 alignment = 0

(opt) [**D3D12\_HEAP\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_flags) flags = D3D12\_HEAP\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_HEAP\_DESC(UINT64 size, D3D12\_HEAP\_TYPE type, UINT64 alignment = 0, D3D12\_HEAP\_FLAGS flags = D3D12\_HEAP\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_DESC, initializing the following parameters:

UINT64 size

[**D3D12\_HEAP\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_type) type

(opt) UINT64 alignment = 0

(opt) [**D3D12\_HEAP\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_flags) flags = D3D12\_HEAP\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_HEAP\_DESC(UINT64 size, D3D12\_CPU\_PAGE\_PROPERTY cpuPageProperty, D3D12\_MEMORY\_POOL memoryPoolPreference, UINT64 alignment = 0, D3D12\_HEAP\_FLAGS flags = D3D12\_HEAP\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_DESC, initializing the following parameters:

UINT64 size

[**D3D12\_CPU\_PAGE\_PROPERTY**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_cpu_page_property) cpuPageProperty

[**D3D12\_MEMORY\_POOL**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_memory_pool) memoryPoolPreference

(opt) UINT64 alignment = 0

(opt) [**D3D12\_HEAP\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_flags) flags = D3D12\_HEAP\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_HEAP\_DESC(const D3D12\_RESOURCE\_ALLOCATION\_INFO& resAllocInfo, D3D12\_HEAP\_PROPERTIES properties, D3D12\_HEAP\_FLAGS flags = D3D12\_HEAP\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_DESC, initializing the following parameters:

[**D3D12\_RESOURCE\_ALLOCATION\_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_allocation_info)& resAllocInfo

[**D3D12\_HEAP\_PROPERTIES**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_properties) properties

(opt) [**D3D12\_HEAP\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_flags) flags = D3D12\_HEAP\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_HEAP\_DESC(const D3D12\_RESOURCE\_ALLOCATION\_INFO& resAllocInfo, D3D12\_HEAP\_TYPE type, D3D12\_HEAP\_FLAGS flags = D3D12\_HEAP\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_DESC, initializing the following parameters:

[**D3D12\_RESOURCE\_ALLOCATION\_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_allocation_info)& resAllocInfo

[**D3D12\_HEAP\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_type) type

(opt) [**D3D12\_HEAP\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_flags) flags = D3D12\_HEAP\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_HEAP\_DESC(const D3D12\_RESOURCE\_ALLOCATION\_INFO& resAllocInfo, D3D12\_CPU\_PAGE\_PROPERTY cpuPageProperty, D3D12\_MEMORY\_POOL memoryPoolPreference, D3D12\_HEAP\_FLAGS flags = D3D12\_HEAP\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_HEAP\_DESC, initializing the following parameters:

[**D3D12\_RESOURCE\_ALLOCATION\_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_allocation_info)& resAllocInfo

[**D3D12\_CPU\_PAGE\_PROPERTY**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_cpu_page_property) cpuPageProperty

[**D3D12\_MEMORY\_POOL**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_memory_pool) memoryPoolPreference

(opt) [**D3D12\_HEAP\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_heap_flags) flags = D3D12\_HEAP\_FLAG\_NONE

</dd> <dt>

**operator const D3D12\_HEAP\_DESC&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the CD3DX12\_HEAP\_DESC structure type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_HEAP\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_heap_desc)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





