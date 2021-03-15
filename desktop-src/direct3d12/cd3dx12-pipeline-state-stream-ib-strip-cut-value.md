---
title: CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE structure (D3dx12.h)
description: A helper structure used to describe the index buffer strip cut value as a single object suitable for a stream description.
ms.assetid: AF8F0919-4601-4A95-832A-5E1DA0304939
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_IB\_STRIP\_CUT\_VALUE structure

A helper structure used to describe the index buffer strip cut value as a single object suitable for a stream description.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE {
                                                   CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE;
                                                   CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE(D3D12_INDEX_BUFFER_STRIP_CUT_VALUE const &i);
  CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE operator=(D3D12_INDEX_BUFFER_STRIP_CUT_VALUE const& i);
                                                   operator D3D12_INDEX_BUFFER_STRIP_CUT_VALUE() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_IB\_STRIP\_CUT\_VALUE**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_IB\_STRIP\_CUT\_VALUE.

</dd> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_IB\_STRIP\_CUT\_VALUE(D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE const &i)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_IB\_STRIP\_CUT\_VALUE, initialized with a subobject type of **D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE\_IB\_STRIP\_CUT\_VALUE** and subobject data copied from *i*, a [**D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_index_buffer_strip_cut_value) structure.

</dd> <dt>

**operator=(D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE const& i)**
</dt> <dd>

Copy-assignment operator.

</dd> <dt>

**operator D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE() const**
</dt> <dd>

Implicit conversion to a [**D3D12\_INDEX\_BUFFER\_STRIP\_CUT\_VALUE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_index_buffer_strip_cut_value) structure.

</dd> </dl>

## Remarks

CD3DX12\_PIPELINE\_STATE\_STREAM\_IB\_STRIP\_CUT\_VALUE is a typedef specialization of the [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md) template, and is defined as follows:


```C++
typedef CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT<D3D12_INDEX_BUFFER_STRIP_CUT_VALUE, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_IB_STRIP_CUT_VALUE>
    CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE;
          
```



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> <dt>

[**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md)
</dt> <dt>

[**D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_pipeline_state_subobject_type)
</dt> </dl>

 

