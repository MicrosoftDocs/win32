---
title: CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE structure (D3dx12.h)
description: A helper structure used to describe the root signature as a single object suitable for a stream description.
ms.assetid: 351A78DC-9BDE-43B4-9A72-D65EE15CA441
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_ROOT\_SIGNATURE structure

A helper structure used to describe the root signature as a single object suitable for a stream description.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE {
                                               CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE;
                                               CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE(ID3D12RootSignature* const &i);
  CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE operator=(ID3D12RootSignature* const& i);
                                               operator ID3D12RootSignature*() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_ROOT\_SIGNATURE**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_ROOT\_SIGNATURE.

</dd> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_ROOT\_SIGNATURE(ID3D12RootSignature\* const &i)**
</dt> <dd>

Creates a new instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_ROOT\_SIGNATURE, initialized with a subobject type of **D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE\_ROOT\_SIGNATURE** and subobject data copied from *i*, a [**ID3D12RootSignature**](/windows/desktop/api/d3d12/nn-d3d12-id3d12rootsignature) structure.

</dd> <dt>

**operator=(ID3D12RootSignature\* const& i)**
</dt> <dd>

Copy-assignment operator.

</dd> <dt>

**operator ID3D12RootSignature\*() const**
</dt> <dd>

Implicit conversion to a [**ID3D12RootSignature**](/windows/desktop/api/d3d12/nn-d3d12-id3d12rootsignature) structure pointer.

</dd> </dl>

## Remarks

CD3DX12\_PIPELINE\_STATE\_STREAM\_ROOT\_SIGNATURE is a typedef specialization of the [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md) template, and is defined as follows:


```C++
typedef CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT<ID3D12RootSignature*, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_ROOT_SIGNATURE>
    CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE;
          
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

 

