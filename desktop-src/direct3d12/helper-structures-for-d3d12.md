---
title: Helper structures for Direct3D 12
description: These helper structures help initialize many of the Direct3D 12 structures. They're declared in `d3dx12.h`.
ms.assetid: 822CACCE-4A45-4104-91BD-4968A657662E
keywords:
- Helper structures
- d3dx12.h
ms.localizationpriority: low
ms.topic: article
ms.date: 07/28/2021
---

# Helper structures for Direct3D 12

These helper structures help initialize many of the Direct3D 12 structures. They're declared in `d3dx12.h`.

`d3dx12.h` is available separately from the Direct3D 12 headers. You can download `d3dx12.h` from [The D3D12 Helper Library](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Libraries/D3DX12).

## In this section

| Topic | Description |
|-|-|
| [**CD3DX12_BLEND_DESC**](cd3dx12-blend-desc.md) | A helper structure to enable easy initialization of a [**D3D12_BLEND_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_blend_desc) structure. |
| [**CD3DX12_BOX**](cd3dx12-box.md) | A helper structure to enable easy initialization of a [**D3D12_BOX**](/windows/win32/api/d3d12/ns-d3d12-d3d12_box) structure. |
| [**CD3DX12_CLEAR_VALUE**](cd3dx12-clear-value.md) | A helper structure to enable easy initialization of a [**D3D12_CLEAR_VALUE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_clear_value) structure. |
| [**CD3DX12_CPU_DESCRIPTOR_HANDLE**](cd3dx12-cpu-descriptor-handle.md) | A helper structure to enable easy initialization of a [**D3D12_CPU_DESCRIPTOR_HANDLE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_cpu_descriptor_handle) structure. |
| [**CD3DX12_DEFAULT**](cd3dx12-default.md) | Passes **D3D12_DEFAULT** into a constructor for each helper structure. This structure is simply used as a mechanism to set default parameters on the other helper structures. |
| [**CD3DX12_DEPTH_STENCIL_DESC**](cd3dx12-depth-stencil-desc.md) | A helper structure to enable easy initialization of a [**D3D12_DEPTH_STENCIL_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_depth_stencil_desc) structure. |
| [**CD3DX12_DEPTH_STENCIL_DESC1**](cd3dx12-depth-stencil-desc1.md) | A helper structure to enable easy initialization of a [**D3D12_DEPTH_STENCIL_DESC1**](/windows/win32/api/d3d12/ns-d3d12-d3d12_depth_stencil_desc1) structure. |
| [**CD3DX12_DESCRIPTOR_RANGE**](cd3dx12-descriptor-range.md) | A helper structure to enable easy initialization of a [**D3D12_DESCRIPTOR_RANGE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_descriptor_range) structure. |
| [**CD3DX12_DESCRIPTOR_RANGE1**](cd3dx12-descriptor-range1.md) | A helper structure to enable easy initialization of a [**D3D12_DESCRIPTOR_RANGE1**](/windows/win32/api/d3d12/ns-d3d12-d3d12_descriptor_range1) structure. |
| [**CD3DX12_GPU_DESCRIPTOR_HANDLE**](cd3dx12-gpu-descriptor-handle.md) | A helper structure to enable easy initialization of a [**D3D12_GPU_DESCRIPTOR_HANDLE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_gpu_descriptor_handle) structure. |
| [**CD3DX12_HEAP_DESC**](cd3dx12-heap-desc.md) | A helper structure to enable easy initialization of a [**D3D12_HEAP_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_heap_desc) structure. |
| [**CD3DX12_HEAP_PROPERTIES**](cd3dx12-heap-properties.md) | A helper structure to enable easy initialization of a [**D3D12_HEAP_PROPERTIES**](/windows/win32/api/d3d12/ns-d3d12-d3d12_heap_properties) structure. |
| [**CD3DX12_PACKED_MIP_INFO**](cd3dx12-packed-mip-info.md) | A helper structure to enable easy initialization of a [**D3D12_PACKED_MIP_INFO**](/windows/win32/api/d3d12/ns-d3d12-d3d12_packed_mip_info) structure. |
| [**CD3DX12_PIPELINE_STATE_STREAM**](cd3dx12-pipeline-state-stream.md) | A helper structure for creating and working with graphics and compute pipeline states through a combined interface. See [**D3D12_GRAPHICS_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) and [**D3D12_COMPUTE_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc). |
| [**CD3DX12_PIPELINE_STATE_STREAM1**](cd3dx12-pipeline-state-stream1.md) | A helper structure for creating and working with graphics and compute pipeline states through a combined interface. See [**D3D12_GRAPHICS_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc) and [**D3D12_COMPUTE_PIPELINE_STATE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_compute_pipeline_state_desc). |
| [**CD3DX12_PIPELINE_STATE_STREAM2**](cd3dx12-pipeline-state-stream2.md) | A helper structure for creating and working with graphics and compute pipeline states through a combined interface. |
| [**CD3DX12_PIPELINE_STATE_STREAM_BLEND_DESC**](cd3dx12-pipeline-state-stream-blend-desc.md) | A helper structure used to describe a blend description as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_CACHED_PSO**](cd3dx12-pipeline-state-stream-cached-pso.md) | A helper structure used to describe a cached PSO as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_CS**](cd3dx12-pipeline-state-stream-cs.md) | A helper structure used to describe a compute shader as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL**](cd3dx12-pipeline-state-stream-depth-stencil.md) | A helper structure used to describe a depth stencil description as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL1**](cd3dx12-pipeline-state-stream-depth-stencil1.md) | A helper structure used to describe a depth stencil description as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_DEPTH_STENCIL_FORMAT**](cd3dx12-pipeline-state-stream-depth-stencil-format.md) | A helper structure used to describe the depth stencil format as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_DS**](cd3dx12-pipeline-state-stream-ds.md) | A helper structure used to describe a domain shader as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_FLAGS**](cd3dx12-pipeline-state-stream-flags.md) | A helper structure used to describe pipeline state flags as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_GS**](cd3dx12-pipeline-state-stream-gs.md) | A helper structure used to describe a geometry shader as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_HS**](cd3dx12-pipeline-state-stream-hs.md) | A helper structure used to describe a hull shader as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_IB_STRIP_CUT_VALUE**](cd3dx12-pipeline-state-stream-ib-strip-cut-value.md) | A helper structure used to describe the index buffer strip cut value as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_INPUT_LAYOUT**](cd3dx12-pipeline-state-stream-input-layout.md) | A helper structure used to describe an input layout as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_NODE_MASK**](cd3dx12-pipeline-state-stream-node-mask.md) | A helper structure used to describe a node mask as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_PARSE_HELPER**](cd3dx12-pipeline-state-stream-parse-helper.md) | Builds an internal CD3DX12_PIPELINE_STATE_STREAM object from subobject details passed into the corresponding member functions. This struct implements the [**ID3DX12PipelineParserCallbacks**](id3dx12pipelineparsercallbacks.md) interface. |
| [**CD3DX12_PIPELINE_STATE_STREAM_PRIMITIVE_TOPOLOGY**](cd3dx12-pipeline-state-stream-primitive-topology.md) | A helper structure used to describe the primitive topology as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_PS**](cd3dx12-pipeline-state-stream-ps.md) | A helper structure used to describe a pixel shader as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_RASTERIZER**](cd3dx12-pipeline-state-stream-rasterizer.md) | A helper structure used to describe a rasterizer description as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_RENDER_TARGET_FORMATS**](cd3dx12-pipeline-state-stream-render-target-formats.md) | A helper structure used to describe the render target formats as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_ROOT_SIGNATURE**](cd3dx12-pipeline-state-stream-root-signature.md) | A helper structure used to describe the root signature as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_DESC**](cd3dx12-pipeline-state-stream-sample-desc.md) | A helper structure used to describe a sample description as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_SAMPLE_MASK**](cd3dx12-pipeline-state-stream-sample-mask.md) | A helper structure used to describe a sample mask as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_STREAM_OUTPUT**](cd3dx12-pipeline-state-stream-stream-output.md) | A helper structure used to describe the stream output description as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_SUBOBJECT**](cd3dx12-pipeline-state-stream-subobject.md) | A templated helper structure used to encapsulate subobject type and subobject data pairs as a single object suitable for a stream description. |
| [**CD3DX12_PIPELINE_STATE_STREAM_VS**](cd3dx12-pipeline-state-stream-vs.md) | A helper structure used to describe a vertex shader as a single object suitable for a stream description. |
| [**CD3DX12_RANGE**](cd3dx12-range.md) | A helper structure to enable easy initialization of a [**D3D12_RANGE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_range) structure. |
| [**CD3DX12_RANGE_UINT64**](cd3dx12-range-uint64.md) | A helper structure to enable easy initialization of a [**D3D12_RANGE_UINT64**](/windows/win32/api/d3d12/ns-d3d12-d3d12_range_uint64) structure. |
| [**CD3DX12_RASTERIZER_DESC**](cd3dx12-rasterizer-desc.md) | A helper structure to enable easy initialization of a [**D3D12_RASTERIZER_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_rasterizer_desc) structure. |
| [**CD3DX12_RECT**](cd3dx12-rect.md) | A helper structure to enable easy initialization of a [**D3D12_RECT**](d3d12-rect.md) structure. |
| [**CD3DX12_RESOURCE_ALLOCATION_INFO**](cd3dx12-resource-allocation-info.md) | A helper structure to enable easy initialization of a [**D3D12_RESOURCE_ALLOCATION_INFO**](/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_allocation_info) structure. |
| [**CD3DX12_RESOURCE_BARRIER**](cd3dx12-resource-barrier.md) | A helper structure to enable easy initialization of a [**D3D12_RESOURCE_BARRIER**](/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_barrier) structure. |
| [**CD3DX12_RESOURCE_DESC**](cd3dx12-resource-desc.md) | A helper structure to enable easy initialization of a [**D3D12_RESOURCE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_desc) structure. |
| [**CD3DX12_RESOURCE_DESC1**](cd3dx12-resource-desc1.md) | A helper structure to enable easy initialization of a [**D3D12_RESOURCE_DESC1**](/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_desc1) structure. |
| [**CD3DX12_ROOT_CONSTANTS**](cd3dx12-root-constants.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_CONSTANTS**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_constants) structure. |
| [**CD3DX12_ROOT_DESCRIPTOR**](cd3dx12-root-descriptor.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_DESCRIPTOR**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_descriptor) structure. |
| [**CD3DX12_ROOT_DESCRIPTOR1**](cd3dx12-root-descriptor1.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_DESCRIPTOR1**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_descriptor1) structure. |
| [**CD3DX12_ROOT_DESCRIPTOR_TABLE**](cd3dx12-root-descriptor-table.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_DESCRIPTOR_TABLE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_descriptor_table) structure. |
| [**CD3DX12_ROOT_DESCRIPTOR_TABLE1**](cd3dx12-root-descriptor-table1.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_DESCRIPTOR_TABLE1**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_descriptor_table1) structure. |
| [**CD3DX12_ROOT_PARAMETER**](cd3dx12-root-parameter.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_PARAMETER**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_parameter) structure. |
| [**CD3DX12_ROOT_PARAMETER1**](cd3dx12-root-parameter1.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_PARAMETER1**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_parameter1) structure. |
| [**CD3DX12_ROOT_SIGNATURE_DESC**](cd3dx12-root-signature-desc.md) | A helper structure to enable easy initialization of a [**D3D12_ROOT_SIGNATURE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_root_signature_desc) structure. |
| [**CD3DX12_RT_FORMAT_ARRAY**](cd3dx12-rt-format-array.md) | A helper structure to enable easy initialization of a [**D3D12_RT_FORMAT_ARRAY**](/windows/win32/api/d3d12/ns-d3d12-d3d12_rt_format_array) structure. |
| [**CD3DX12_SHADER_BYTECODE**](cd3dx12-shader-bytecode.md) | A helper structure to enable easy initialization of a [**D3D12_SHADER_BYTECODE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_shader_bytecode) structure. |
| [**CD3DX12_STATE_OBJECT_DESC**](cd3dx12-state-object-desc.md) | The central class of the D3DX12 State Object Creation Helpers, which are helper classes for creating state objects out of an arbitrary set of subobjects. |
| [**CD3DX12_STATIC_SAMPLER_DESC**](cd3dx12-static-sampler-desc.md) | A helper structure to enable easy initialization of a [**D3D12_STATIC_SAMPLER_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_static_sampler_desc) structure. |
| [**CD3DX12_SUBRESOURCE_FOOTPRINT**](cd3dx12-subresource-footprint.md) | A helper structure to enable easy initialization of a [**D3D12_SUBRESOURCE_FOOTPRINT**](/windows/win32/api/d3d12/ns-d3d12-d3d12_subresource_footprint) structure. |
| [**CD3DX12_SUBRESOURCE_RANGE_UINT64**](cd3dx12-subresource-range-uint64.md) | A helper structure to enable easy initialization of a [**D3D12_SUBRESOURCE_RANGE_UINT64**](/windows/win32/api/d3d12/ns-d3d12-d3d12_subresource_range_uint64) structure. |
| [**CD3DX12_SUBRESOURCE_TILING**](cd3dx12-subresource-tiling.md) | A helper structure to enable easy initialization of a [**D3D12_SUBRESOURCE_TILING**](/windows/win32/api/d3d12/ns-d3d12-d3d12_subresource_tiling) structure. |
| [**CD3DX12_TEXTURE_COPY_LOCATION**](cd3dx12-texture-copy-location.md) | A helper structure to enable easy initialization of a [**D3D12_TEXTURE_COPY_LOCATION**](/windows/win32/api/d3d12/ns-d3d12-d3d12_texture_copy_location) structure. |
| [**CD3DX12_TILE_REGION_SIZE**](cd3dx12-tile-region-size.md) | A helper structure to enable easy initialization of a [**D3D12_TILE_REGION_SIZE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tile_region_size) structure. |
| [**CD3DX12_TILE_SHAPE**](cd3dx12-tile-shape.md) | A helper structure to enable easy initialization of a [**D3D12_TILE_SHAPE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tile_shape) structure. |
| [**CD3DX12_TILED_RESOURCE_COORDINATE**](cd3dx12-tiled-resource-coordinate.md) | A helper structure to enable easy initialization of a [**D3D12_TILED_RESOURCE_COORDINATE**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tiled_resource_coordinate) structure. |
| [**CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC**](cd3dx12-versioned-root-signature-desc.md) | A helper structure to enable easy initialization of a [**D3D12_VERSIONED_ROOT_SIGNATURE_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) structure. |
| [**CD3DX12_VIEW_INSTANCING_DESC**](cd3dx12-view-instancing-desc.md) | A helper structure to enable easy initialization of a [**D3DX12_VIEW_INSTANCING_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_view_instancing_desc) structure. |
| [**CD3DX12_VIEWPORT**](cd3dx12-viewport.md) | A helper structure to enable easy initialization of a [**D3D12_VIEWPORT**](/windows/win32/api/d3d12/ns-d3d12-d3d12_viewport) structure. |
| [**D3DX12_MESH_SHADER_PIPELINE_STATE_DESC**](d3dx12-mesh-shader-pipeline-state-desc.md) | For [mesh/amplifications shaders](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html), you can use the data from an [EffectPipelineStateDescription](https://github.com/Microsoft/DirectXTK12/wiki/EffectPipelineStateDescription), with **D3DX12_MESH_SHADER_PIPELINE_STATE_DESC**, to provide all the state. |

## Related topics

* [Helper structures and functions for D3D12](helper-structures-and-functions-for-d3d12.md)
* [Direct3D 12 reference](direct3d-12-reference.md)
