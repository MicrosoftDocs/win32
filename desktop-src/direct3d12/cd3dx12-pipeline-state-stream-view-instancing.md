---
title: CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING structure (D3dx12.h)
description: A helper structure used to wrap a [CD3DX12_VIEW_INSTANCING_DESC](cd3dx12-view-instancing-desc.md) structure. Allows shaders to render to multiple views with a single draw call; useful for stereo vision or cubemap generation.
keywords:
- CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING structure
topic_type:
- apiref
api_name:
- CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 08/05/2021
---

# CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING structure

A helper structure used to wrap a [CD3DX12_VIEW_INSTANCING_DESC](cd3dx12-view-instancing-desc.md) structure. Allows shaders to render to multiple views with a single draw call; useful for stereo vision or cubemap generation.

## Syntax

```cpp
typedef CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT<CD3DX12_VIEW_INSTANCING_DESC, D3D12_PIPELINE_STATE_SUBOBJECT_TYPE_VIEW_INSTANCING, CD3DX12_DEFAULT> CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING;
```

**CD3DX12_PIPELINE_STATE_STREAM_VIEW_INSTANCING** is a `typedef` specialization of the [CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT](cd3dx12-pipeline-state-stream-subobject.md) template.

## Members

See [CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT](cd3dx12-pipeline-state-stream-subobject.md) and [CD3DX12_VIEW_INSTANCING_DESC](cd3dx12-view-instancing-desc.md).

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h) |

## See also

* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
* [CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT](cd3dx12-pipeline-state-stream-subobject.md)
* [D3D12_PIPELINE_STATE_SUBOBJECT_TYPE](/windows/win32/api/d3d12/ne-d3d12-d3d12_pipeline_state_subobject_type)
* [D3DX12_VIEW_INSTANCING_DESC](/windows/win32/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc)
