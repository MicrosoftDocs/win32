---
title: Core Enumerations
description: This section contains information about the core enumerations.
ms.assetid: 1641713a-5ac8-4597-900b-1bba54f9f522
keywords:
- enumerations, Direct3D 11 Core
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Core Enumerations

This section contains information about the core enumerations.

## 

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>D3D11_ASYNC_GETDATA_FLAG</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_async_getdata_flag)<br/></td>
<td>Optional flags that control the behavior of [<strong>ID3D11DeviceContext::GetData</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-getdata).<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_BLEND</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_blend)<br/></td>
<td>Blend factors, which modulate values for the pixel shader and render target.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_BLEND_OP</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_blend_op)<br/></td>
<td>RGB or alpha blending operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_CLEAR_FLAG</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_clear_flag)<br/></td>
<td>Specifies the parts of the depth stencil to clear. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_COLOR_WRITE_ENABLE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_color_write_enable)<br/></td>
<td>Identify which components of each pixel of a render target are writable during blending.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_COMPARISON_FUNC</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_comparison_func)<br/></td>
<td>Comparison options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CONSERVATIVE_RASTERIZATION_MODE</strong>](/windows/desktop/api/D3D11_3/ne-d3d11_3-d3d11_conservative_rasterization_mode)<br/></td>
<td>Identifies whether conservative rasterization is on or off.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_CONSERVATIVE_RASTERIZATION_TIER</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_conservative_rasterization_tier)<br/></td>
<td>Specifies if the hardware and driver support conservative rasterization and at what tier level.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CONTEXT_TYPE</strong>](/windows/desktop/api/D3D11_3/ne-d3d11_3-d3d11_context_type)<br/></td>
<td>Specifies the context in which a query occurs.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_COPY_FLAGS</strong>](/windows/desktop/api/D3D11_1/ne-d3d11_1-d3d11_copy_flags)<br/></td>
<td><blockquote>
[!Note]<br />
This enumeration is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_COUNTER</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_counter)<br/></td>
<td>Options for performance counters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_COUNTER_TYPE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_counter_type)<br/></td>
<td>Data type of a performance counter.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CREATE_DEVICE_FLAG</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_create_device_flag)<br/></td>
<td>Describes parameters that are used to create a device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_1_CREATE_DEVICE_CONTEXT_STATE_FLAG</strong>](/windows/desktop/api/D3D11_1/ne-d3d11_1-d3d11_1_create_device_context_state_flag)<br/></td>
<td>Describes flags that are used to create a device context state object ([<strong>ID3DDeviceContextState</strong>](/windows/desktop/api/D3D11_1/)) with the [<strong>ID3D11Device1::CreateDeviceContextState</strong>](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11device1-createdevicecontextstate) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CULL_MODE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_cull_mode)<br/></td>
<td>Indicates triangles facing a particular direction are not drawn.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_DEPTH_WRITE_MASK</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_depth_write_mask)<br/></td>
<td>Identify the portion of a depth-stencil buffer for writing depth data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_DEVICE_CONTEXT_TYPE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_device_context_type)<br/></td>
<td>Device context options.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_feature)<br/></td>
<td>Direct3D 11 feature options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FENCE_FLAG</strong>](/windows/desktop/api/d3d11_3/ne-d3d11_3-d3d11_fence_flag)<br/></td>
<td>Specifies fence options. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FILL_MODE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_fill_mode)<br/></td>
<td>Determines the fill mode to use when rendering triangles.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FILTER</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_filter)<br/></td>
<td>Filtering options during texture sampling.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FILTER_TYPE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_filter_type)<br/></td>
<td>Types of magnification or minification sampler filters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FILTER_REDUCTION_TYPE</strong>](/windows/desktop/api/d3d11/ne-d3d11-d3d11_filter_reduction_type)<br/></td>
<td>Specifies the type of sampler filter reduction. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FORMAT_SUPPORT</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_format_support)<br/></td>
<td>Which resources are supported for a given format and given device (see [<strong>ID3D11Device::CheckFormatSupport</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkformatsupport) and [<strong>ID3D11Device::CheckFeatureSupport</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport)).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FORMAT_SUPPORT2</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_format_support2)<br/></td>
<td>Unordered resource support options for a compute shader resource (see [<strong>ID3D11Device::CheckFeatureSupport</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport)). <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_INPUT_CLASSIFICATION</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_input_classification)<br/></td>
<td>Type of data contained in an input slot.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_LOGIC_OP</strong>](/windows/desktop/api/D3D11_1/ne-d3d11_1-d3d11_logic_op)<br/></td>
<td><blockquote>
[!Note]<br />
This enumeration is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Specifies logical operations to configure for a render target.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_PRIMITIVE</strong>](/windows/desktop/api/d3d11/)<br/></td>
<td>Indicates how the pipeline interprets geometry or hull shader input primitives. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_PRIMITIVE_TOPOLOGY</strong>](/windows/desktop/api/D3D11/)<br/></td>
<td>How the pipeline interprets vertex data that is bound to the input-assembler stage. These primitive topology values determine how the vertex data is rendered on screen.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_QUERY</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_query)<br/></td>
<td>Query types.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_QUERY_MISC_FLAG</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_query_misc_flag)<br/></td>
<td>Flags that describe miscellaneous query behavior.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_RAISE_FLAG</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_raise_flag)<br/></td>
<td>Option(s) for raising an error to a non-continuable exception.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_SHADER_CACHE_SUPPORT_FLAGS</strong>](https://www.bing.com/search?q=<strong>D3D11_SHADER_CACHE_SUPPORT_FLAGS</strong>)<br/></td>
<td>Describes the level of support for shader caching in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_SHADER_MIN_PRECISION_SUPPORT</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_shader_min_precision_support)<br/></td>
<td><blockquote>
[!Note]<br />
This enumeration is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Values that specify minimum precision levels at shader stages.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_STENCIL_OP</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_stencil_op)<br/></td>
<td>The stencil operations that can be performed during depth-stencil testing.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_TEXTURE_ADDRESS_MODE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_texture_address_mode)<br/></td>
<td>Identify a technique for resolving texture coordinates that are outside of the boundaries of a texture.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_TEXTURECUBE_FACE</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_texturecube_face)<br/></td>
<td>The different faces of a cube texture.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_TILED_RESOURCES_TIER</strong>](/windows/desktop/api/D3D11/ne-d3d11-d3d11_tiled_resources_tier)<br/></td>
<td>Indicates the tier level at which tiled resources are supported.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Core Reference](d3d11-graphics-reference-d3d11-core.md)
</dt> </dl>

 

 





