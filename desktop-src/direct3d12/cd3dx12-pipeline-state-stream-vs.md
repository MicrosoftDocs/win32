---
title: CD3DX12_PIPELINE_STATE_STREAM_VS structure (D3dx12.h)
description: A helper structure used to describe a vertex shader as a single object suitable for a stream description.
ms.assetid: 27EAB08C-D3B9-4920-B7D2-754AA3562A94
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_VS structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_VS
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_VS structure

A helper structure used to describe a vertex shader as a single object suitable for a stream description.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_VS {
                                   CD3DX12_PIPELINE_STATE_STREAM_VS;
                                   CD3DX12_PIPELINE_STATE_STREAM_VS(D3D12_SHADER_BYTECODE const &i);
  CD3DX12_PIPELINE_STATE_STREAM_VS operator=(D3D12_SHADER_BYTECODE const& i);
                                   operator D3D12_SHADER_BYTECODE() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_VS**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_VS.

</dd> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_VS(D3D12\_SHADER\_BYTECODE const &i)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_VS, initialized with a subobject type of **D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE\_VS** and subobject data copied from *i*, a [**D3D12\_SHADER\_BYTECODE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_shader_bytecode) structure.

</dd> <dt>

**operator=(D3D12\_SHADER\_BYTECODE const& i)**
</dt> <dd>

Copy-assignment operator.

</dd> <dt>

**operator D3D12\_SHADER\_BYTECODE() const**
</dt> <dd>

Implicit conversion to a [**D3D12\_SHADER\_BYTECODE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_shader_bytecode) structure.

</dd> </dl>

## Remarks

CD3DX12\_PIPELINE\_STATE\_STREAM\_VS is a typedef specialization of the [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md) template, and is defined as follows:


```C++
typedef CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT<D3D12_SHADER_BYTECODE, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_VS>
    CD3DX12_PIPELINE_STATE_STREAM_VS;
          
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

 

