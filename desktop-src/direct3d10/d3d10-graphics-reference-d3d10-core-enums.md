---
description: 'This section contains information about the following core enumerations:'
ms.assetid: 3d1541bf-75d8-459d-a912-4068e9a0a9e4
title: Direct3D 10 core enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 10 core enumerations

This section contains information about the following core enumerations:



| Enumeration                                                               | Description                                                                                                                                         |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D10\_ASYNC\_GETDATA\_FLAG**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_async_getdata_flag)           | Optional flags that control what happens when data is retrieved by calling [**ID3D10Asynchronous::GetData**](/windows/desktop/api/D3D10/nf-d3d10-id3d10asynchronous-getdata).       |
| [**D3D10\_BLEND**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_blend)                                       | Blend options.                                                                                                                                      |
| [**D3D10\_BLEND\_OP**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_blend_op)                                | Blending operations between source and destination pixels.                                                                                          |
| [**D3D10\_CLEAR\_FLAG**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_clear_flag)                            | Specifies which parts of the depth stencil to clear.                                                                                                |
| [**D3D10\_COLOR\_WRITE\_ENABLE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_color_write_enable)           | Color writing masks.                                                                                                                                |
| [**D3D10\_COMPARISON\_FUNC**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_comparison_func)                  | Comparison functions.                                                                                                                               |
| [**D3D10\_COUNTER**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_counter)                                   | Types of performance counters.                                                                                                                      |
| [**D3D10\_COUNTER\_TYPE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_counter_type)                        | Data type of a counter.                                                                                                                             |
| [**D3D10\_CREATE\_DEVICE\_FLAG**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_create_device_flag)           | Device creation flags.                                                                                                                              |
| [**D3D10\_CULL\_MODE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_cull_mode)                              | Rasterizer cull modes.                                                                                                                              |
| [**D3D10\_DEPTH\_WRITE\_MASK**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_depth_write_mask)               | Determines which portion of the depth stencil is writable.                                                                                          |
| [**D3D10\_DEVICE\_STATE\_TYPES**](/windows/desktop/api/D3D10Effect/ne-d3d10effect-d3d10_device_state_types)           | Used in [**ID3D10StateBlock Interface**](/windows/desktop/api/d3d10effect/nn-d3d10effect-id3d10stateblock) function calls.                                                                      |
| [**D3D10\_DRIVER\_TYPE**](/windows/desktop/api/D3D10misc/ne-d3d10misc-d3d10_driver_type)                          | Type of device driver.                                                                                                                              |
| [**D3D10\_FEATURE\_LEVEL1**](/windows/desktop/api/D3D10_1/ne-d3d10_1-d3d10_feature_level1)                    | The version of hardware acceleration.                                                                                                               |
| [**D3D10\_FILL\_MODE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_fill_mode)                              | Rasterizer fill modes.                                                                                                                              |
| [**D3D10\_FILTER**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_filter)                                     | Types of sampler filters.                                                                                                                           |
| [**D3D10\_FILTER\_TYPE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_filter_type)                          | Types of texture-sampling filters.                                                                                                                  |
| [**D3D10\_FORMAT\_SUPPORT**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_format_support)                    | Which resources are supported for a given format and given device. See [**ID3D10Device::CheckFormatSupport**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-checkformatsupport). |
| [**D3D10\_INPUT\_CLASSIFICATION**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_input_classification)        | Types of input data.                                                                                                                                |
| [**D3D10\_MESSAGE\_CATEGORY**](/windows/desktop/api/d3d10sdklayers/ne-d3d10sdklayers-d3d10_message_category)                | Categories of debug messages.                                                                                                                       |
| [**D3D10\_MESSAGE\_ID**](/windows/desktop/api/d3d10sdklayers/ne-d3d10sdklayers-d3d10_message_id)                            | A debug message's unique ID.                                                                                                                        |
| [**D3D10\_MESSAGE\_SEVERITY**](/windows/desktop/api/d3d10sdklayers/ne-d3d10sdklayers-d3d10_message_severity)                | Severity of a debug message.                                                                                                                        |
| [**D3D10\_PRIMITIVE\_TOPOLOGY**](/previous-versions/windows/desktop/legacy/bb205334(v=vs.85))            | Types of primitive topology or the way a primitive's data is arranged.                                                                              |
| [**D3D10\_QUERY**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_query)                                       | Types of queries.                                                                                                                                   |
| [**D3D10\_QUERY\_MISC\_FLAG**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_query_misc_flag)                 | Flags that describe miscellaneous query behavior.                                                                                                   |
| [**D3D10\_RAISE\_FLAG**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_raise_flag)                            | Flags that indicate how to handle internal driver errors.                                                                                           |
| [**D3D10\_REGISTER\_COMPONENT\_TYPE**](/windows/win32/api/d3dcommon/ne-d3dcommon-d3d_register_component_type) | The register component types, usually used in [**D3D10\_SIGNATURE\_PARAMETER\_DESC**](/windows/desktop/api/D3D10Shader/ns-d3d10shader-d3d10_signature_parameter_desc).                          |
| [**D3D10\_RESOURCE\_RETURN\_TYPE**](/windows/win32/api/d3dcommon/ne-d3dcommon-d3d_resource_return_type)       | The return type of a resource. See [**D3D10\_SHADER\_INPUT\_BIND\_DESC**](/windows/desktop/api/D3D10Shader/ns-d3d10shader-d3d10_shader_input_bind_desc).                                        |
| [**D3D10\_STENCIL\_OP**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_stencil_op)                            | Stencil operations.                                                                                                                                 |
| [**D3D10\_TEXTURE\_ADDRESS\_MODE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_texture_address_mode)       | Actions to perform when a texture coordinate is outside of the boundaries of a texture.                                                             |
| [**D3D10\_TEXTURECUBE\_FACE**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_texturecube_face)                | The different faces of a cube texture.                                                                                                              |



 

## Related topics

<dl> <dt>

[Core Reference](d3d10-graphics-reference-d3d10-core.md)
</dt> </dl>

 

 
