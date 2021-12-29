---
title: CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1 structure (D3dx12.h)
description: A helper structure used to describe a depth stencil description as a single object suitable for a stream description. | CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1 structure (D3dx12.h)
ms.assetid: 7D3554D9-610D-43B5-94F0-68167E966A86
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1 structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1 structure

A helper structure used to describe a depth stencil description as a single object suitable for a stream description.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1 {
                                               CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1;
                                               CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1(CD3DX12_DEPTH_STENCIL_DESC1 const &i);
  CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1 operator=(CD3DX12_DEPTH_STENCIL_DESC1 const& i);
                                               operator CD3DX12_DEPTH_STENCIL_DESC1() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1.

</dd> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1(CD3DX12\_DEPTH\_STENCIL\_DESC1 const &i)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1, initialized with a subobject type of **D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE\_DEPTH\_STENCIL1** and subobject data copied from *i*, a [**CD3DX12\_DEPTH\_STENCIL\_DESC1**](cd3dx12-depth-stencil-desc1.md) structure.

</dd> <dt>

**operator=(CD3DX12\_DEPTH\_STENCIL\_DESC1 const& i)**
</dt> <dd>

Copy-assignment operator.

</dd> <dt>

**operator CD3DX12\_DEPTH\_STENCIL\_DESC1() const**
</dt> <dd>

Implicit conversion to a [**CD3DX12\_DEPTH\_STENCIL\_DESC1**](cd3dx12-depth-stencil-desc1.md) structure.

</dd> </dl>

## Remarks

CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1 is a typedef specialization of the [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md) template, and is defined as follows:


```C++
typedef CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT<CD3DX12_DEPTH_STENCIL_DESC1, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_DEPTH_STENCIL1, CD3DX12_DEFAULT>
    CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1;
          
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

 

