---
title: Core Enumerations
description: This section contains information about the core enumerations.
ms.assetid: '1641713a-5ac8-4597-900b-1bba54f9f522'
keywords: ["enumerations, Direct3D 11 Core"]
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
<td>[<strong>D3D11_ASYNC_GETDATA_FLAG</strong>](d3d11-async-getdata-flag.md)<br/></td>
<td>Optional flags that control the behavior of [<strong>ID3D11DeviceContext::GetData</strong>](id3d11devicecontext-getdata.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_BLEND</strong>](d3d11-blend.md)<br/></td>
<td>Blend factors, which modulate values for the pixel shader and render target.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_BLEND_OP</strong>](d3d11-blend-op.md)<br/></td>
<td>RGB or alpha blending operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_CLEAR_FLAG</strong>](d3d11-clear-flag.md)<br/></td>
<td>Specifies the parts of the depth stencil to clear. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_COLOR_WRITE_ENABLE</strong>](d3d11-color-write-enable.md)<br/></td>
<td>Identify which components of each pixel of a render target are writable during blending.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_COMPARISON_FUNC</strong>](d3d11-comparison-func.md)<br/></td>
<td>Comparison options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CONSERVATIVE_RASTERIZATION_MODE</strong>](d3d11-conservative-rasterization-mode.md)<br/></td>
<td>Identifies whether conservative rasterization is on or off.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_CONSERVATIVE_RASTERIZATION_TIER</strong>](d3d11-conservative-rasterization-tier.md)<br/></td>
<td>Specifies if the hardware and driver support conservative rasterization and at what tier level.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CONTEXT_TYPE</strong>](d3d11-context-type.md)<br/></td>
<td>Specifies the context in which a query occurs.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_COPY_FLAGS</strong>](d3d11-copy-flags.md)<br/></td>
<td><blockquote>
[!Note]<br />
This enumeration is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Specifies how to handle the existing contents of a resource during a copy or update operation of a region within that resource.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_COUNTER</strong>](d3d11-counter.md)<br/></td>
<td>Options for performance counters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_COUNTER_TYPE</strong>](d3d11-counter-type.md)<br/></td>
<td>Data type of a performance counter.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CREATE_DEVICE_FLAG</strong>](d3d11-create-device-flag.md)<br/></td>
<td>Describes parameters that are used to create a device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_1_CREATE_DEVICE_CONTEXT_STATE_FLAG</strong>](d3d11-1-create-device-context-state-flag.md)<br/></td>
<td>Describes flags that are used to create a device context state object ([<strong>ID3DDeviceContextState</strong>](id3ddevicecontextstate.md)) with the [<strong>ID3D11Device1::CreateDeviceContextState</strong>](id3d11device1-createdevicecontextstate.md) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_CULL_MODE</strong>](d3d11-cull-mode.md)<br/></td>
<td>Indicates triangles facing a particular direction are not drawn.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_DEPTH_WRITE_MASK</strong>](d3d11-depth-write-mask.md)<br/></td>
<td>Identify the portion of a depth-stencil buffer for writing depth data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_DEVICE_CONTEXT_TYPE</strong>](d3d11-device-context-type.md)<br/></td>
<td>Device context options.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE</strong>](d3d11-feature.md)<br/></td>
<td>Direct3D 11 feature options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FENCE_FLAG</strong>](d3d11-fence-flag.md)<br/></td>
<td>Specifies fence options. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FILL_MODE</strong>](d3d11-fill-mode.md)<br/></td>
<td>Determines the fill mode to use when rendering triangles.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FILTER</strong>](d3d11-filter.md)<br/></td>
<td>Filtering options during texture sampling.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FILTER_TYPE</strong>](d3d11-filter-type.md)<br/></td>
<td>Types of magnification or minification sampler filters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FILTER_REDUCTION_TYPE</strong>](d3d11-filter-reduction-type.md)<br/></td>
<td>Specifies the type of sampler filter reduction. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FORMAT_SUPPORT</strong>](d3d11-format-support.md)<br/></td>
<td>Which resources are supported for a given format and given device (see [<strong>ID3D11Device::CheckFormatSupport</strong>](id3d11device-checkformatsupport.md) and [<strong>ID3D11Device::CheckFeatureSupport</strong>](id3d11device-checkfeaturesupport.md)).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FORMAT_SUPPORT2</strong>](d3d11-format-support2.md)<br/></td>
<td>Unordered resource support options for a compute shader resource (see [<strong>ID3D11Device::CheckFeatureSupport</strong>](id3d11device-checkfeaturesupport.md)). <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_INPUT_CLASSIFICATION</strong>](d3d11-input-classification.md)<br/></td>
<td>Type of data contained in an input slot.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_LOGIC_OP</strong>](d3d11-logic-op.md)<br/></td>
<td><blockquote>
[!Note]<br />
This enumeration is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Specifies logical operations to configure for a render target.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_PRIMITIVE</strong>](d3d11-primitive.md)<br/></td>
<td>Indicates how the pipeline interprets geometry or hull shader input primitives. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_PRIMITIVE_TOPOLOGY</strong>](d3d11-primitive-topology.md)<br/></td>
<td>How the pipeline interprets vertex data that is bound to the input-assembler stage. These primitive topology values determine how the vertex data is rendered on screen.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_QUERY</strong>](d3d11-query.md)<br/></td>
<td>Query types.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_QUERY_MISC_FLAG</strong>](d3d11-query-misc-flag.md)<br/></td>
<td>Flags that describe miscellaneous query behavior.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_RAISE_FLAG</strong>](d3d11-raise-flag.md)<br/></td>
<td>Option(s) for raising an error to a non-continuable exception.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_SHADER_CACHE_SUPPORT_FLAGS</strong>](direct3d11d3d11_shader_cache_support_flags)<br/></td>
<td>Describes the level of support for shader caching in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_SHADER_MIN_PRECISION_SUPPORT</strong>](d3d11-shader-min-precision-support.md)<br/></td>
<td><blockquote>
[!Note]<br />
This enumeration is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Values that specify minimum precision levels at shader stages.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_STENCIL_OP</strong>](d3d11-stencil-op.md)<br/></td>
<td>The stencil operations that can be performed during depth-stencil testing.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_TEXTURE_ADDRESS_MODE</strong>](d3d11-texture-address-mode.md)<br/></td>
<td>Identify a technique for resolving texture coordinates that are outside of the boundaries of a texture.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_TEXTURECUBE_FACE</strong>](d3d11-texturecube-face.md)<br/></td>
<td>The different faces of a cube texture.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_TILED_RESOURCES_TIER</strong>](d3d11-tiled-resources-tier.md)<br/></td>
<td>Indicates the tier level at which tiled resources are supported.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Core Reference](d3d11-graphics-reference-d3d11-core.md)
</dt> </dl>

 

 





