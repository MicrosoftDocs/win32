---
title: CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT class (D3dx12.h)
description: A helper class for creating a raytracing pipeline configuration state subobject, with flags.
keywords:
- CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT class
topic_type:
- apiref
api_name:
- CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 08/05/2021
---

# CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT class

A helper class for creating a raytracing pipeline configuration state subobject, with flags.

For more info about the D3DX12 State Object Creation Helpers, see [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md).

## Syntax

```cpp
class CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT
{
public:
    CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT() noexcept;
    CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT(CD3DX12_STATE_OBJECT_DESC& ContainingStateObject);
    void Config(UINT MaxTraceRecursionDepth, D3D12_RAYTRACING_PIPELINE_FLAGS Flags) noexcept;
    D3D12_STATE_SUBOBJECT_TYPE Type() const noexcept override;
    operator const D3D12_STATE_SUBOBJECT& () const noexcept;
    operator const D3D12_RAYTRACING_PIPELINE_CONFIG1& () const noexcept;
};
```

## Members

`CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT`

Default constructor. Creates a new, default-initialized, instance of a **CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT**.

`CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT(CD3DX12_STATE_OBJECT_DESC&)`

Constructor that creates a new instance of a **CD3DX12_RAYTRACING_PIPELINE_CONFIG1_SUBOBJECT** initialized with the contents of a [**CD3DX12_STATE_OBJECT_DESC**](cd3dx12-state-object-desc.md) object.

`Config(UINT, D3D12_RAYTRACING_PIPELINE_FLAGS)`

Function for configuring the limit on ray recursion for the raytracing pipeline. Also takes a [D3D12_RAYTRACING_PIPELINE_FLAGS](/windows/win32/api/d3d12/ns-d3d12-d3d12_raytracing_pipeline_flags) parameter.

`Type`

Retrieves the type of the subobject, represented by the [D3D12_STATE_SUBOBJECT_TYPE_RAYTRACING_PIPELINE_CONFIG](/windows/win32/api/d3d12/ne-d3d12-d3d12_state_subobject_type) constant.

`operator const D3D12_STATE_SUBOBJECT&`

Conversion operator that returns a reference to a constant [D3D12_STATE_SUBOBJECT](/windows/win32/api/d3d12/ns-d3d12-d3d12_state_subobject) object describing the state object.

`operator const D3D12_RAYTRACING_PIPELINE_CONFIG&`

Conversion operator that returns a reference to a constant [D3D12_RAYTRACING_PIPELINE_CONFIG](/windows/win32/api/d3d12/ns-d3d12-d3d12_raytracing_pipeline_config) object describing the state object.

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
* [CD3DX12_STATE_OBJECT_DESC](cd3dx12-state-object-desc.md)
