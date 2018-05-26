---
Description: This section contains information about the following core enumerations
ms.assetid: 3d1541bf-75d8-459d-a912-4068e9a0a9e4
title: Core Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Core Enumerations

This section contains information about the following core enumerations:



| Enumeration                                                               | Description                                                                                                                                         |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D10\_ASYNC\_GETDATA\_FLAG**](/windows/win32/D3D10/ne-d3d10-d3d10_async_getdata_flag?branch=master)           | Optional flags that control what happens when data is retrieved by calling [**ID3D10Asynchronous::GetData**](/windows/win32/D3D10/nf-d3d10-id3d10asynchronous-getdata?branch=master).       |
| [**D3D10\_BLEND**](/windows/win32/D3D10/ne-d3d10-d3d10_blend?branch=master)                                       | Blend options.                                                                                                                                      |
| [**D3D10\_BLEND\_OP**](/windows/win32/D3D10/ne-d3d10-d3d10_blend_op?branch=master)                                | Blending operations between source and destination pixels.                                                                                          |
| [**D3D10\_CLEAR\_FLAG**](/windows/win32/D3D10/ne-d3d10-d3d10_clear_flag?branch=master)                            | Specifies which parts of the depth stencil to clear.                                                                                                |
| [**D3D10\_COLOR\_WRITE\_ENABLE**](/windows/win32/D3D10/ne-d3d10-d3d10_color_write_enable?branch=master)           | Color writing masks.                                                                                                                                |
| [**D3D10\_COMPARISON\_FUNC**](/windows/win32/D3D10/ne-d3d10-d3d10_comparison_func?branch=master)                  | Comparison functions.                                                                                                                               |
| [**D3D10\_COUNTER**](/windows/win32/D3D10/ne-d3d10-d3d10_counter?branch=master)                                   | Types of performance counters.                                                                                                                      |
| [**D3D10\_COUNTER\_TYPE**](/windows/win32/D3D10/ne-d3d10-d3d10_counter_type?branch=master)                        | Data type of a counter.                                                                                                                             |
| [**D3D10\_CREATE\_DEVICE\_FLAG**](/windows/win32/D3D10/ne-d3d10-d3d10_create_device_flag?branch=master)           | Device creation flags.                                                                                                                              |
| [**D3D10\_CULL\_MODE**](/windows/win32/D3D10/ne-d3d10-d3d10_cull_mode?branch=master)                              | Rasterizer cull modes.                                                                                                                              |
| [**D3D10\_DEPTH\_WRITE\_MASK**](/windows/win32/D3D10/ne-d3d10-d3d10_depth_write_mask?branch=master)               | Determines which portion of the depth stencil is writable.                                                                                          |
| [**D3D10\_DEVICE\_STATE\_TYPES**](/windows/win32/D3D10Effect/ne-d3d10effect-_d3d10_device_state_types?branch=master)           | Used in [**ID3D10StateBlock Interface**](/windows/win32/d3d10effect/nn-d3d10effect-id3d10stateblock?branch=master) function calls.                                                                      |
| [**D3D10\_DRIVER\_TYPE**](/windows/win32/D3D10misc/ne-d3d10misc-d3d10_driver_type?branch=master)                          | Type of device driver.                                                                                                                              |
| [**D3D10\_FEATURE\_LEVEL1**](/windows/win32/D3D10_1/ne-d3d10_1-d3d10_feature_level1?branch=master)                    | The version of hardware acceleration.                                                                                                               |
| [**D3D10\_FILL\_MODE**](/windows/win32/D3D10/ne-d3d10-d3d10_fill_mode?branch=master)                              | Rasterizer fill modes.                                                                                                                              |
| [**D3D10\_FILTER**](/windows/win32/D3D10/ne-d3d10-d3d10_filter?branch=master)                                     | Types of sampler filters.                                                                                                                           |
| [**D3D10\_FILTER\_TYPE**](/windows/win32/D3D10/ne-d3d10-d3d10_filter_type?branch=master)                          | Types of texture-sampling filters.                                                                                                                  |
| [**D3D10\_FORMAT\_SUPPORT**](/windows/win32/D3D10/ne-d3d10-d3d10_format_support?branch=master)                    | Which resources are supported for a given format and given device. See [**ID3D10Device::CheckFormatSupport**](/windows/win32/D3D10/nf-d3d10-id3d10device-checkformatsupport?branch=master). |
| [**D3D10\_INPUT\_CLASSIFICATION**](/windows/win32/D3D10/ne-d3d10-d3d10_input_classification?branch=master)        | Types of input data.                                                                                                                                |
| [**D3D10\_MESSAGE\_CATEGORY**](/windows/win32/d3d10sdklayers/ne-d3d10sdklayers-d3d10_message_category?branch=master)                | Categories of debug messages.                                                                                                                       |
| [**D3D10\_MESSAGE\_ID**](/windows/win32/d3d10sdklayers/ne-d3d10sdklayers-d3d10_message_id?branch=master)                            | A debug message's unique ID.                                                                                                                        |
| [**D3D10\_MESSAGE\_SEVERITY**](/windows/win32/d3d10sdklayers/ne-d3d10sdklayers-d3d10_message_severity?branch=master)                | Severity of a debug message.                                                                                                                        |
| [**D3D10\_PRIMITIVE\_TOPOLOGY**](/windows/win32/D3D10/?branch=master)            | Types of primitive topology or the way a primitive's data is arranged.                                                                              |
| [**D3D10\_QUERY**](/windows/win32/D3D10/ne-d3d10-d3d10_query?branch=master)                                       | Types of queries.                                                                                                                                   |
| [**D3D10\_QUERY\_MISC\_FLAG**](/windows/win32/D3D10/ne-d3d10-d3d10_query_misc_flag?branch=master)                 | Flags that describe miscellaneous query behavior.                                                                                                   |
| [**D3D10\_RAISE\_FLAG**](/windows/win32/D3D10/ne-d3d10-d3d10_raise_flag?branch=master)                            | Flags that indicate how to handle internal driver errors.                                                                                           |
| [**D3D10\_REGISTER\_COMPONENT\_TYPE**](/windows/win32/D3D10shader/?branch=master) | The register component types, usually used in [**D3D10\_SIGNATURE\_PARAMETER\_DESC**](/windows/win32/D3D10Shader/ns-d3d10shader-_d3d10_signature_parameter_desc?branch=master).                          |
| [**D3D10\_RESOURCE\_RETURN\_TYPE**](/windows/win32/D3D10shader/?branch=master)       | The return type of a resource. See [**D3D10\_SHADER\_INPUT\_BIND\_DESC**](/windows/win32/D3D10Shader/ns-d3d10shader-_d3d10_shader_input_bind_desc?branch=master).                                        |
| [**D3D10\_STENCIL\_OP**](/windows/win32/D3D10/ne-d3d10-d3d10_stencil_op?branch=master)                            | Stencil operations.                                                                                                                                 |
| [**D3D10\_TEXTURE\_ADDRESS\_MODE**](/windows/win32/D3D10/ne-d3d10-d3d10_texture_address_mode?branch=master)       | Actions to perform when a texture coordinate is outside of the boundaries of a texture.                                                             |
| [**D3D10\_TEXTURECUBE\_FACE**](/windows/win32/D3D10/ne-d3d10-d3d10_texturecube_face?branch=master)                | The different faces of a cube texture.                                                                                                              |



 

## Related topics

<dl> <dt>

[Core Reference](d3d10-graphics-reference-d3d10-core.md)
</dt> </dl>

 

 



