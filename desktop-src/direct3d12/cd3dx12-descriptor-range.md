---
title: CD3DX12_DESCRIPTOR_RANGE structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_DESCRIPTOR\_RANGE structure.
ms.assetid: F066ECA5-5E52-4483-B773-B43C5F12809B
keywords:
- CD3DX12_DESCRIPTOR_RANGE structure
topic_type:
- apiref
api_name:
- CD3DX12_DESCRIPTOR_RANGE
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_DESCRIPTOR\_RANGE structure

A helper structure to enable easy initialization of a [**D3D12\_DESCRIPTOR\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range) structure.

## Syntax


```C++
struct CD3DX12_DESCRIPTOR_RANGE  : public D3D12_DESCRIPTOR_RANGE{
       CD3DX12_DESCRIPTOR_RANGE();
       explicit CD3DX12_DESCRIPTOR_RANGE(const D3D12_DESCRIPTOR_RANGE &o);
       CD3DX12_DESCRIPTOR_RANGE(D3D12_DESCRIPTOR_RANGE_TYPE rangeType, UINT numDescriptors, UINT baseShaderRegister, UINT registerSpace = 0, UINT offsetInDescriptorsFromTableStart = D3D12_DESCRIPTOR_RANGE_OFFSET_APPEND);
  void inline Init(D3D12_DESCRIPTOR_RANGE_TYPE rangeType, UINT numDescriptors, UINT baseShaderRegister, UINT registerSpace = 0, UINT offsetInDescriptorsFromTableStart = D3D12_DESCRIPTOR_RANGE_OFFSET_APPEND);
  void static inline Init(D3D12_DESCRIPTOR_RANGE &range, D3D12_DESCRIPTOR_RANGE_TYPE rangeType, UINT numDescriptors, UINT baseShaderRegister, UINT registerSpace = 0, UINT offsetInDescriptorsFromTableStart = D3D12_DESCRIPTOR_RANGE_OFFSET_APPEND);
};
```



## Members

<dl> <dt>

**CD3DX12\_DESCRIPTOR\_RANGE()**
</dt> <dd>

Creates a new, uninitialized, instance of a D3DX12\_DESCRIPTOR\_RANGE.

</dd> <dt>

**explicit CD3DX12\_DESCRIPTOR\_RANGE(const D3D12\_DESCRIPTOR\_RANGE &o)**
</dt> <dd>

Creates a new instance of a D3DX12\_DESCRIPTOR\_RANGE, initialized with the contents of another [**D3D12\_DESCRIPTOR\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range) structure.

</dd> <dt>

**CD3DX12\_DESCRIPTOR\_RANGE(D3D12\_DESCRIPTOR\_RANGE\_TYPE rangeType, UINT numDescriptors, UINT baseShaderRegister, UINT registerSpace = 0, UINT offsetInDescriptorsFromTableStart = D3D12\_DESCRIPTOR\_RANGE\_OFFSET\_APPEND)**
</dt> <dd>

Creates a new instance of a D3DX12\_DESCRIPTOR\_RANGE, initializing the following parameters:

[**D3D12\_DESCRIPTOR\_RANGE\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_descriptor_range_type) rangeType

UINT numDescriptors

UINT baseShaderRegister

UINT registerSpace = 0

UINT offsetInDescriptorsFromTableStart = D3D12\_DESCRIPTOR\_RANGE\_OFFSET\_APPEND

</dd> <dt>

**inline Init(D3D12\_DESCRIPTOR\_RANGE\_TYPE rangeType, UINT numDescriptors, UINT baseShaderRegister, UINT registerSpace = 0, UINT offsetInDescriptorsFromTableStart = D3D12\_DESCRIPTOR\_RANGE\_OFFSET\_APPEND)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_DESCRIPTOR\_RANGE\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_descriptor_range_type) rangeType

UINT numDescriptors

UINT baseShaderRegister

UINT registerSpace = 0

UINT offsetInDescriptorsFromTableStart = D3D12\_DESCRIPTOR\_RANGE\_OFFSET\_APPEND

</dd> <dt>

**static inline Init(D3D12\_DESCRIPTOR\_RANGE &range, D3D12\_DESCRIPTOR\_RANGE\_TYPE rangeType, UINT numDescriptors, UINT baseShaderRegister, UINT registerSpace = 0, UINT offsetInDescriptorsFromTableStart = D3D12\_DESCRIPTOR\_RANGE\_OFFSET\_APPEND)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_DESCRIPTOR\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range) &range

[**D3D12\_DESCRIPTOR\_RANGE\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_descriptor_range_type) rangeType

UINT numDescriptors

UINT baseShaderRegister

UINT registerSpace = 0

UINT offsetInDescriptorsFromTableStart = D3D12\_DESCRIPTOR\_RANGE\_OFFSET\_APPEND

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_DESCRIPTOR\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_range)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





