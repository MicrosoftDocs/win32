---
title: CD3DX12_ROOT_DESCRIPTOR_TABLE1 structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_ROOT\_DESCRIPTOR\_TABLE1 structure.
ms.assetid: 82AC1948-92AA-4A4D-B443-717E9BF3046D
keywords:
- CD3DX12_ROOT_DESCRIPTOR_TABLE1 structure
topic_type:
- apiref
api_name:
- CD3DX12_ROOT_DESCRIPTOR_TABLE1
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_ROOT\_DESCRIPTOR\_TABLE1 structure

A helper structure to enable easy initialization of a [**D3D12\_ROOT\_DESCRIPTOR\_TABLE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table1) structure.

## Syntax


```C++
struct CD3DX12_ROOT_DESCRIPTOR_TABLE1  : public D3D12_ROOT_DESCRIPTOR_TABLE1{
       CD3DX12_ROOT_DESCRIPTOR_TABLE1();
       explicit CD3DX12_ROOT_DESCRIPTOR_TABLE1(const D3D12_ROOT_DESCRIPTOR_TABLE1 &o);
       CD3DX12_ROOT_DESCRIPTOR_TABLE1(UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE1* _pDescriptorRanges);
  void inline Init(UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE1* _pDescriptorRanges);
  void static inline Init(D3D12_ROOT_DESCRIPTOR_TABLE1 &rootDescriptorTable, UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE1* _pDescriptorRanges);
};
```



## Members

<dl> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR\_TABLE1()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_ROOT\_DESCRIPTOR\_TABLE1.

</dd> <dt>

**explicit CD3DX12\_ROOT\_DESCRIPTOR\_TABLE1(const D3D12\_ROOT\_DESCRIPTOR\_TABLE1 &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR\_TABLE1, initialized with the contents of another [**D3D12\_ROOT\_DESCRIPTOR\_TABLE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table1) structure.

</dd> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR\_TABLE1(UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE1\* \_pDescriptorRanges)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR\_TABLE1, initializing the following parameters:

UINT numDescriptorRanges

const [**D3D12\_DESCRIPTOR\_RANGE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range1)\* \_pDescriptorRanges

</dd> <dt>

**inline Init(UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE1\* \_pDescriptorRanges)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT numDescriptorRanges

const [**D3D12\_DESCRIPTOR\_RANGE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range1)\* \_pDescriptorRanges

</dd> <dt>

**static inline Init(D3D12\_ROOT\_DESCRIPTOR\_TABLE1 &rootDescriptorTable, UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE1\* \_pDescriptorRanges)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_DESCRIPTOR\_TABLE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table1) &rootDescriptorTable

UINT numDescriptorRanges

const [**D3D12\_DESCRIPTOR\_RANGE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range1)\* \_pDescriptorRanges

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_ROOT\_DESCRIPTOR\_TABLE1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor_table1)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





