---
title: CD3DX12_PIPELINE_STATE_STREAM_FLAGS structure (D3dx12.h)
description: A helper structure used to describe pipeline state flags as a single object suitable for a stream description.
ms.assetid: EF67936B-315A-4B3F-9E07-7CF4C5EE47CF
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_FLAGS structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_FLAGS
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_FLAGS structure

A helper structure used to describe pipeline state flags as a single object suitable for a stream description.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_FLAGS {
                                      CD3DX12_PIPELINE_STATE_STREAM_FLAGS;
                                      CD3DX12_PIPELINE_STATE_STREAM_FLAGS(D3D12_PIPELINE_STATE_FLAGS const &i);
  CD3DX12_PIPELINE_STATE_STREAM_FLAGS operator=(D3D12_PIPELINE_STATE_FLAGS const& i);
                                      operator D3D12_PIPELINE_STATE_FLAGS() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_FLAGS**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_FLAGS.

</dd> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_FLAGS(D3D12\_PIPELINE\_STATE\_FLAGS const &i)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_FLAGS, initialized with a subobject type of **D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE\_FLAGS** and subobject data copied from *i*, a [**D3D12\_PIPELINE\_STATE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_pipeline_state_flags) structure.

</dd> <dt>

**operator=(D3D12\_PIPELINE\_STATE\_FLAGS const& i)**
</dt> <dd>

Copy-assignment operator.

</dd> <dt>

**operator D3D12\_PIPELINE\_STATE\_FLAGS() const**
</dt> <dd>

Implicit conversion to a [**D3D12\_PIPELINE\_STATE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_pipeline_state_flags) structure.

</dd> </dl>

## Remarks

CD3DX12\_PIPELINE\_STATE\_STREAM\_FLAGS is a typedef specialization of the [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md) template, and is defined as follows:


```C++
typedef CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT<D3D12_PIPELINE_STATE_FLAGS, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_FLAGS>
    CD3DX12_PIPELINE_STATE_STREAM_FLAGS;
          
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

 

