---
title: Core Structures
description: This section contains information about the core structures.
ms.assetid: 2a45182a-7114-4075-b8b8-147f52fe7aa9
keywords:
- structures, Direct3D 11 Core
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Core Structures

This section contains information about the core structures.

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
<td>[<strong>D3D11_BLEND_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_blend_desc)<br/></td>
<td>Describes the blend state that you use in a call to [<strong>ID3D11Device::CreateBlendState</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createblendstate) to create a blend-state object. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_BLEND_DESC1</strong>](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_blend_desc1)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes the blend state that you use in a call to [<strong>ID3D11Device1::CreateBlendState1</strong>](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11device1-createblendstate1) to create a blend-state object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_BOX</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_box)<br/></td>
<td>Defines a 3D box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_COUNTER_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_counter_desc)<br/></td>
<td>Describes a counter.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_COUNTER_INFO</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_counter_info)<br/></td>
<td>Information about the video card's performance counter capabilities.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_DEPTH_STENCIL_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_depth_stencil_desc)<br/></td>
<td>Describes depth-stencil state.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_DEPTH_STENCILOP_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_depth_stencilop_desc)<br/></td>
<td>Stencil operations that can be performed based on the results of stencil test.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_DRAW_INDEXED_INSTANCED_INDIRECT_ARGS</strong>](/windows/desktop/api/d3d11/ns-d3d11-d3d11_draw_indexed_instanced_indirect_args)<br/></td>
<td>Arguments for draw indexed instanced indirect. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_DRAW_INSTANCED_INDIRECT_ARGS</strong>](/windows/desktop/api/d3d11/ns-d3d11-d3d11_draw_instanced_indirect_args)<br/></td>
<td>Arguments for draw instanced indirect. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_ARCHITECTURE_INFO</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_architecture_info)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes information about Direct3D 11.1 adapter architecture.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_D3D9_OPTIONS</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d9_options)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes Direct3D 9 feature options in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_D3D9_OPTIONS1</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d9_options1)<br/></td>
<td>Describes Direct3D 9 feature options in the current graphics driver.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_D3D9_SHADOW_SUPPORT</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d9_shadow_support)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes Direct3D 9 shadow support in the current graphics driver. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_D3D9_SIMPLE_INSTANCING_SUPPORT</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d9_simple_instancing_support)<br/></td>
<td>Describes whether simple instancing is supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d10_x_hardware_options)<br/></td>
<td>Describes compute shader and raw and structured buffer support in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_D3D11_OPTIONS</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes Direct3D 11.1 feature options in the current graphics driver.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_D3D11_OPTIONS1</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options1)<br/></td>
<td>Describes Direct3D 11.2 feature options in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_D3D11_OPTIONS2</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options2)<br/></td>
<td>Describes Direct3D 11.3 feature options in the current graphics driver.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_D3D11_OPTIONS3</strong>](/windows/desktop/api/d3d11/ns-d3d11-d3d11_feature_data_d3d11_options3)<br/></td>
<td>Describes Direct3D 11.3 feature options in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_D3D11_OPTIONS4</strong>](/windows/desktop/api/d3d11_4/ns-d3d11_4-d3d11_feature_data_d3d11_options4)<br/></td>
<td>Describes Direct3D 11.4 feature options in the current graphics driver.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_DOUBLES</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_doubles)<br/></td>
<td>Describes double data type support in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_FORMAT_SUPPORT</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_format_support)<br/></td>
<td>Describes which resources are supported by the current graphics driver for a given format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_FORMAT_SUPPORT2</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_format_support2)<br/></td>
<td>Describes which unordered resource options are supported by the current graphics driver for a given format.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_GPU_VIRTUAL_ADDRESS_SUPPORT</strong>](/windows/desktop/api/d3d11/ns-d3d11-d3d11_feature_data_gpu_virtual_address_support)<br/></td>
<td>Describes feature data GPU virtual address support, including maximum address bits per resource and per process. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_MARKER_SUPPORT</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_marker_support)<br/></td>
<td>Describes whether a GPU profiling technique is supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_SHADER_CACHE</strong>](/windows/desktop/api/d3d11/ns-d3d11-d3d11_feature_data_shader_cache)<br/></td>
<td>Describes the level of shader caching supported in the current graphics driver.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_FEATURE_DATA_SHADER_MIN_PRECISION_SUPPORT</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_shader_min_precision_support)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes precision support options for shaders in the current graphics driver.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_FEATURE_DATA_THREADING</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_threading)<br/></td>
<td>Describes the multi-threading features that are supported by the current graphics driver.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_INPUT_ELEMENT_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_input_element_desc)<br/></td>
<td>A description of a single element for the input-assembler stage.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_QUERY_DATA_PIPELINE_STATISTICS</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_query_data_pipeline_statistics)<br/></td>
<td>Query information about graphics-pipeline activity in between calls to [<strong>ID3D11DeviceContext::Begin</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-begin) and [<strong>ID3D11DeviceContext::End</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-end).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_QUERY_DATA_SO_STATISTICS</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_query_data_so_statistics)<br/></td>
<td>Query information about the amount of data streamed out to the stream-output buffers in between [<strong>ID3D11DeviceContext::Begin</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-begin) and [<strong>ID3D11DeviceContext::End</strong>](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-end).<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_QUERY_DATA_TIMESTAMP_DISJOINT</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_query_data_timestamp_disjoint)<br/></td>
<td>Query information about the reliability of a timestamp query.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_QUERY_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_query_desc)<br/></td>
<td>Describes a query.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_QUERY_DESC1</strong>](/windows/desktop/api/D3D11_3/ns-d3d11_3-cd3d11_query_desc1)<br/></td>
<td>Describes a query.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_RASTERIZER_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_rasterizer_desc)<br/></td>
<td>Describes rasterizer state.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_RASTERIZER_DESC1</strong>](/windows/desktop/api/D3D11_1/ns-d3d11_1-cd3d11_rasterizer_desc1)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes rasterizer state.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_RASTERIZER_DESC2</strong>](/windows/desktop/api/D3D11_3/ns-d3d11_3-cd3d11_rasterizer_desc2)<br/></td>
<td>Describes rasterizer state.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_RECT</strong>](d3d11-rect.md)<br/></td>
<td>D3D11_RECT is declared as follows:<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_RENDER_TARGET_BLEND_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_render_target_blend_desc)<br/></td>
<td>Describes the blend state for a render target.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_RENDER_TARGET_BLEND_DESC1</strong>](/windows/desktop/api/D3D11_1/ns-d3d11_1-d3d11_render_target_blend_desc1)<br/></td>
<td><blockquote>
[!Note]<br />
This structure is supported by the Direct3D 11.1 runtime, which is available on Windows 8 and later operating systems.
</blockquote>
<br/> Describes the blend state for a render target.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_SAMPLER_DESC</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_sampler_desc)<br/></td>
<td>Describes a sampler state.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3D11_SO_DECLARATION_ENTRY</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_so_declaration_entry)<br/></td>
<td>Description of a vertex element in a vertex buffer in an output slot.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3D11_VIEWPORT</strong>](/windows/desktop/api/D3D11/ns-d3d11-d3d11_viewport)<br/></td>
<td>Defines the dimensions of a viewport.<br/></td>
</tr>
</tbody>
</table>



 

In addition, there is a 2D rectangle structure defined in D3D11.h.


```
typedef RECT D3D11_RECT;
```



For documentation, see [RECT](http://msdn.microsoft.com/library/ms536136.aspx) in [Windows GDI](http://msdn.microsoft.com/library/ms536795.aspx) on [MSDN](http://msdn.microsoft.com/).

## Related topics

<dl> <dt>

[Core Reference](d3d11-graphics-reference-d3d11-core.md)
</dt> </dl>

 

 





