---
title: CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC structure (D3dx12.h)
description: A helper structure used to describe a sample description as a single object suitable for a stream description.
ms.assetid: D84C5373-AC0F-430A-97A1-6125611869B2
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_DESC structure

A helper structure used to describe a sample description as a single object suitable for a stream description.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC {
                                            CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC;
                                            CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC(DXGI_SAMPLE_DESC const &i);
  CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC operator=(DXGI_SAMPLE_DESC const& i);
                                            operator DXGI_SAMPLE_DESC() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_DESC**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_DESC.

</dd> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_DESC(DXGI\_SAMPLE\_DESC const &i)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_DESC, initialized with a subobject type of **D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE\_SAMPLE\_DESC** and subobject data copied from *i*, a [**DXGI\_SAMPLE\_DESC**](https://www.bing.com/search?q=**DXGI\_SAMPLE\_DESC**) structure.

</dd> <dt>

**operator=(DXGI\_SAMPLE\_DESC const& i)**
</dt> <dd>

Copy-assignment operator.

</dd> <dt>

**operator DXGI\_SAMPLE\_DESC() const**
</dt> <dd>

Implicit conversion to a [**DXGI\_SAMPLE\_DESC**](https://www.bing.com/search?q=**DXGI\_SAMPLE\_DESC**) structure.

</dd> </dl>

## Remarks

CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_DESC is a typedef specialization of the [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md) template, and is defined as follows:


```C++
typedef CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT<DXGI_SAMPLE_DESC, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_SAMPLE_DESC>
    CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC;
          
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

 

