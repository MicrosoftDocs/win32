---
description: Direct3D 12 Attributes
title: Direct3D 12 Attributes
ms.topic: article
ms.date: 08/13/2021
---

# Direct3D 12 Attributes

The following attributes can be used to configure Direct3D 12 Media Foundation resources.



| Attribute                                                                                                         | Description                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [MF_MT_D3D_RESOURCE_VERSION](mf-mt-d3d-resource-version.md) | Specifies the Direct3D version of the resources stored in the data stream associated with the media type. |
| [MF_MT_D3D12_CPU_READBACK](mf-mt-d3d12-cpu-readback.md) | Indicates whether CPU access is required for the associated Direct3D resources. |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_CROSS_ADAPTER](mf-mt-d3d12-resource-flag-allow-cross-adapter.md) | Indicates whether the resources in the stream can be used for cross-adapter data.  |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_DEPTH_STENCIL](mf-mt-d3d12-resource-flag-allow-depth-stencil.md) | Indicates whether depth stencil view can be created for the Direct3D resources in the stream associated with the media type. |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_RENDER_TARGET](mf-mt-d3d12-resource-flag-allow-render-target.md) | Indicates whether a render target view can be created for the Direct3D resources in the stream associated with the media type.  |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_SIMULTANEOUS_ACCESS](mf-mt-d3d12-resource-flag-allow-simultaneous-access.md) | Indicates whether the Direct3D resources in the stream can be simultaneously accessed by multiple different command queues.  |
| [MF_MT_D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS](mf-mt-d3d12-resource-flag-allow-unordered-access.md) | Indicates whether an unordered access view can be created for the Direct3D resources in the stream associated with the media type. |
| [MF_MT_D3D12_RESOURCE_FLAG_DENY_SHADER_RESOURCE](mf-mt-d3d12-resource-flag-deny-shader-resource.md) | Indicates whether shader resource view creation is disallowed for the Direct3D resources in the stream associated with the media type.  |
| [MF_MT_D3D12_TEXTURE_LAYOUT](mf-mt-d3d12-texture-layout.md) | Indicates the texture layout options that were used to create the associated Direct3D resources.  |
| [MF_SA_D3D12_CLEAR_VALUE](mf-sa-d3d12-clear-value.md) | Contains a blob with the information used to optimize clear operations for the Direct3D resources in the stream. |
| [MF_SA_D3D12_HEAP_FLAGS](mf-sa-d3d12-heap-flags.md) | Contains a value specifying the heap options used for the Direct3D resources in the stream. |
| [MF_SA_D3D12_HEAP_TYPE](mf-sa-d3d12-heap-type.md)  | Contains a value specifying the type of heap used for the Direct3D resources in the stream. |




 

## Related topics

<dl> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



