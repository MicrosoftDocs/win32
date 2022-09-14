---
title: CD3DX12_ROOT_DESCRIPTOR_TABLE structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_ROOT\_DESCRIPTOR\_TABLE structure.
ms.assetid: 154B4C50-4E94-471C-A44E-F120A84F007C
keywords:
- CD3DX12_ROOT_DESCRIPTOR_TABLE structure
topic_type:
- apiref
api_name:
- CD3DX12_ROOT_DESCRIPTOR_TABLE
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_ROOT\_DESCRIPTOR\_TABLE structure

A helper structure to enable easy initialization of a [**D3D12\_ROOT\_DESCRIPTOR\_TABLE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table) structure.

## Syntax


```C++
struct CD3DX12_ROOT_DESCRIPTOR_TABLE  : public D3D12_ROOT_DESCRIPTOR_TABLE{
       CD3DX12_ROOT_DESCRIPTOR_TABLE();
       explicit CD3DX12_ROOT_DESCRIPTOR_TABLE(const D3D12_ROOT_DESCRIPTOR_TABLE &o);
       CD3DX12_ROOT_DESCRIPTOR_TABLE(UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE* _pDescriptorRanges);
  void inline Init(UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE* _pDescriptorRanges);
  void static inline Init(D3D12_ROOT_DESCRIPTOR_TABLE &rootDescriptorTable, UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE* _pDescriptorRanges);
};
```



## Members

<dl> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR\_TABLE()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_ROOT\_DESCRIPTOR\_TABLE.

</dd> <dt>

**explicit CD3DX12\_ROOT\_DESCRIPTOR\_TABLE(const D3D12\_ROOT\_DESCRIPTOR\_TABLE &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR\_TABLE, initialized with the contents of another [**D3D12\_ROOT\_DESCRIPTOR\_TABLE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table) structure.

</dd> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR\_TABLE(UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE\* \_pDescriptorRanges)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR\_TABLE, initializing the following parameters:

UINT numDescriptorRanges

[**D3D12\_DESCRIPTOR\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range)\* \_pDescriptorRanges

</dd> <dt>

**inline Init(UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE\* \_pDescriptorRanges)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT numDescriptorRanges

[**D3D12\_DESCRIPTOR\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range)\* \_pDescriptorRanges

</dd> <dt>

**static inline Init(D3D12\_ROOT\_DESCRIPTOR\_TABLE &rootDescriptorTable, UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE\* \_pDescriptorRanges)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_DESCRIPTOR\_TABLE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table) &rootDescriptorTable

UINT numDescriptorRanges

[**D3D12\_DESCRIPTOR\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range)\* \_pDescriptorRanges

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_ROOT\_DESCRIPTOR\_TABLE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





