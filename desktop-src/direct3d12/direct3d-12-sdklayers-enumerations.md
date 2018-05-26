---
title: Debug Layer Enumerations
description: The following enumerations are declared in d3d12sdklayers.h.
ms.assetid: 6E76C857-128E-4F0E-9711-72C4CF6C835C
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Debug Layer Enumerations

The following enumerations are declared in d3d12sdklayers.h.

## In this section



| Topic                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D12\_DEBUG\_COMMAND\_LIST\_PARAMETER\_TYPE**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_debug_command_list_parameter_type?branch=master)<br/>                                 | Indicates the debug parameter type used by [**ID3D12DebugCommandList1::SetDebugParameter**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12debugcommandlist1-setdebugparameter?branch=master) and [**ID3D12DebugCommandList1::GetDebugParameter**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12debugcommandlist1-getdebugparameter?branch=master).<br/>                                                                                                                                                                                                      |
| [**D3D12\_DEBUG\_DEVICE\_PARAMETER\_TYPE**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_debug_device_parameter_type?branch=master)<br/>                                              | Specifies the data type of the memory pointed to by the *pData* parameter of [**ID3D12DebugDevice1::SetDebugParameter**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12debugdevice1-setdebugparameter?branch=master) and [**ID3D12DebugDevice1::GetDebugParameter**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12debugdevice1-getdebugparameter?branch=master).<br/>                                                                                                                                                                                        |
| [**D3D12\_DEBUG\_FEATURE**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_debug_feature?branch=master)<br/>                                                                            | Flags for optional D3D12 Debug Layer features.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**D3D12\_GPU\_BASED\_VALIDATION\_FLAGS**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_gpu_based_validation_flags?branch=master)<br/>                                                | Describes the level of GPU-based validation to perform at runtime.<br/>                                                                                                                                                                                                                                                                                                                                                                                   |
| [**D3D12\_GPU\_BASED\_VALIDATION\_PIPELINE\_STATE\_CREATE\_FLAGS**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_gpu_based_validation_pipeline_state_create_flags?branch=master)<br/> | Specifies how GPU-Based Validation handles patched pipeline states during [**ID3D12Device::CreateGraphicsPipelineState**](/windows/win32/D3D12/nf-d3d12-id3d12device-creategraphicspipelinestate?branch=master) and [**ID3D12Device::CreateComputePipelineState**](/windows/win32/D3D12/nf-d3d12-id3d12device-createcomputepipelinestate?branch=master).<br/>                                                                                                                                                                             |
| [**D3D12\_GPU\_BASED\_VALIDATION\_SHADER\_PATCH\_MODE**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_gpu_based_validation_shader_patch_mode?branch=master)<br/>                      | Specifies the type of shader patching used by GPU-Based Validation at either the device or command list level.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**D3D12\_MESSAGE\_CATEGORY**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_message_category?branch=master)<br/>                                                                      | Specifies categories of debug messages. This will identify the category of a message when retrieving a message with [**ID3D12InfoQueue::GetMessage**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12infoqueue-getmessage?branch=master) and when adding a message with [**ID3D12InfoQueue::AddMessage**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12infoqueue-addmessage?branch=master). When creating an info queue filter, these values can be used to allow or deny any categories of messages to pass through the storage and retrieval filters. <br/> |
| [**D3D12\_MESSAGE\_ID**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_message_id?branch=master)<br/>                                                                                  | Specifies debug message IDs for setting up an info-queue filter (see [**D3D12\_INFO\_QUEUE\_FILTER**](/windows/win32/d3d12sdklayers/ns-d3d12sdklayers-d3d12_info_queue_filter?branch=master)); use these messages to allow or deny message categories to pass through the storage and retrieval filters. These IDs are used by methods such as [**ID3D12InfoQueue::GetMessage**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12infoqueue-getmessage?branch=master) or [**ID3D12InfoQueue::AddMessage**](/windows/win32/d3d12sdklayers/nf-d3d12sdklayers-id3d12infoqueue-addmessage?branch=master). <br/>                        |
| [**D3D12\_MESSAGE\_SEVERITY**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_message_severity?branch=master)<br/>                                                                      | Debug message severity levels for an information queue.<br/>                                                                                                                                                                                                                                                                                                                                                                                              |
| [**D3D12\_RLDO\_FLAGS**](/windows/win32/d3d12sdklayers/ne-d3d12sdklayers-d3d12_rldo_flags?branch=master)<br/>                                                                                  | Specifies options for the amount of information to report about a live device object's lifetime. <br/>                                                                                                                                                                                                                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Environment Setup](directx-12-programming-environment-set-up.md)
</dt> <dt>

[Debug Layer Reference](direct3d-12-sdklayers-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





