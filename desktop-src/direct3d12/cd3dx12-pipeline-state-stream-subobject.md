---
title: CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT structure (D3dx12.h)
description: A templated helper structure used to encapsulate subobject type and subobject data pairs as a single object suitable for a stream description.
ms.assetid: 4C59D483-6ED8-49BD-B91B-2A912AFE2409
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT structure

A templated helper structure used to encapsulate subobject type and subobject data pairs as a single object suitable for a stream description.

## Syntax


```C++
struct CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT {
                                          CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT;
                                          CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT(InnerStructType const &i);
  CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT operator=(InnerStructType const& i);
                                          operator InnerStructType() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT.

</dd> <dt>

**CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT(**InnerStructType** const &i)**
</dt> <dd>

Creates a new CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT template instance, initialized with a subobject type of [**D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_pipeline_state_subobject_type) and subobject data copied from *i*. Both the subobject type and subobject data type are given as template parameters, **Type** and **InnerStructType**, respectively. For more information, see Remarks below.

</dd> <dt>

**operator=(**InnerStructType** const& i)**
</dt> <dd>

Copy-assignment operator.

</dd> <dt>

**operator **InnerStructType**() const**
</dt> <dd>

Implicit conversion to the subobject data type given by the **InnerStructType** template parameter.

</dd> </dl>

## Remarks

CD3DX12\_PIPELINE\_STATE\_STREAM\_SUBOBJECT is a template defined as follows:


```C++
template <typename InnerStructType, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE Type, typename DefaultArg = InnerStructType>
class alignas(void*) CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT
{
private:
    D3D12_PIPELINE_STATE_SUBOBJECT_TYPE _Type;
    InnerStructType _Inner;
public:
    CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT() : _Type(Type), _Inner(DefaultArg()) {}
    CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT(InnerStructType const& i) : _Type(Type), _Inner(i) {}
    CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT& operator=(InnerStructType const& i) { _Inner = i; return *this; }
    operator InnerStructType() const { return _Inner; }
};  
          
```



The template parameter **InnerStructType** specifies the subobject data type; that is, the subobject details to be encoded into a stream. The template parameter **Type** specifies the subobject type; that is, the type of the structure specified by the template parameter **InnerStructType**. The template parameter **DefaultArg** specifies an optional value that the subobject data will be initialized to when an instance of the corresponding template instantiation is default-constructed; for example, to default-construct a [**CD3DX12\_PIPELINE\_STATE\_STREAM\_BLEND\_DESC**](cd3dx12-pipeline-state-stream-blend-desc.md) initialized with common blend-state defaults using [**CD3DX12\_DEFAULT**](cd3dx12-default.md).

Here are the template instantiations that are defined:

-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_FLAGS**](cd3dx12-pipeline-state-stream-flags.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_NODE\_MASK**](cd3dx12-pipeline-state-stream-node-mask.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_ROOT\_SIGNATURE**](cd3dx12-pipeline-state-stream-root-signature.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_INPUT\_LAYOUT**](cd3dx12-pipeline-state-stream-input-layout.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_IB\_STRIP\_CUT\_VALUE**](cd3dx12-pipeline-state-stream-ib-strip-cut-value.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_PRIMITIVE\_TOPOLOGY**](cd3dx12-pipeline-state-stream-primitive-topology.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_VS**](cd3dx12-pipeline-state-stream-vs.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_GS**](cd3dx12-pipeline-state-stream-gs.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_STREAM\_OUTPUT**](cd3dx12-pipeline-state-stream-stream-output.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_HS**](cd3dx12-pipeline-state-stream-hs.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_DS**](cd3dx12-pipeline-state-stream-ds.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_PS**](cd3dx12-pipeline-state-stream-ps.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_CS**](cd3dx12-pipeline-state-stream-cs.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_BLEND\_DESC**](cd3dx12-pipeline-state-stream-blend-desc.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL**](cd3dx12-pipeline-state-stream-depth-stencil.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1**](cd3dx12-pipeline-state-stream-depth-stencil1.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL\_FORMAT**](cd3dx12-pipeline-state-stream-depth-stencil-format.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_RASTERIZER**](cd3dx12-pipeline-state-stream-rasterizer.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_RENDER\_TARGET\_FORMATS**](cd3dx12-pipeline-state-stream-render-target-formats.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_DESC**](cd3dx12-pipeline-state-stream-sample-desc.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_SAMPLE\_MASK**](cd3dx12-pipeline-state-stream-sample-mask.md)
-   [**CD3DX12\_PIPELINE\_STATE\_STREAM\_CACHED\_PSO**](cd3dx12-pipeline-state-stream-cached-pso.md)

The [**CD3DX12\_PIPELINE\_STATE\_STREAM\_BLEND\_DESC**](cd3dx12-pipeline-state-stream-blend-desc.md), [**CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL**](cd3dx12-pipeline-state-stream-depth-stencil.md), [**CD3DX12\_PIPELINE\_STATE\_STREAM\_DEPTH\_STENCIL1**](cd3dx12-pipeline-state-stream-depth-stencil1.md), and [**CD3DX12\_PIPELINE\_STATE\_STREAM\_RASTERIZER**](cd3dx12-pipeline-state-stream-rasterizer.md) structures are defined to initialize their subobject data with common defaults using [**CD3DX12\_DEFAULT**](cd3dx12-default.md).

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> <dt>

[**D3D12\_PIPELINE\_STATE\_SUBOBJECT\_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_pipeline_state_subobject_type)
</dt> </dl>

 

