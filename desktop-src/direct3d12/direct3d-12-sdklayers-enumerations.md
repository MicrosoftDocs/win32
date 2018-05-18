---
title: Debug Layer Enumerations
description: The following enumerations are declared in d3d12sdklayers.h.
ms.assetid: '6E76C857-128E-4F0E-9711-72C4CF6C835C'
---

# Debug Layer Enumerations

The following enumerations are declared in d3d12sdklayers.h.

## In this section



| Topic                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D12\_DEBUG\_COMMAND\_LIST\_PARAMETER\_TYPE**](d3d12-debug-command-list-parameter-type.md)<br/>                                 | Indicates the debug parameter type used by [**ID3D12DebugCommandList1::SetDebugParameter**](id3d12debugcommandlist1-setdebugparameter.md) and [**ID3D12DebugCommandList1::GetDebugParameter**](id3d12debugcommandlist1-getdebugparameter.md).<br/>                                                                                                                                                                                                      |
| [**D3D12\_DEBUG\_DEVICE\_PARAMETER\_TYPE**](d3d12-debug-device-parameter-type.md)<br/>                                              | Specifies the data type of the memory pointed to by the *pData* parameter of [**ID3D12DebugDevice1::SetDebugParameter**](id3d12debugdevice1-setdebugparameter.md) and [**ID3D12DebugDevice1::GetDebugParameter**](id3d12debugdevice1-getdebugparameter.md).<br/>                                                                                                                                                                                        |
| [**D3D12\_DEBUG\_FEATURE**](d3d12-debug-feature.md)<br/>                                                                            | Flags for optional D3D12 Debug Layer features.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**D3D12\_GPU\_BASED\_VALIDATION\_FLAGS**](d3d12-gpu-based-validation-flags.md)<br/>                                                | Describes the level of GPU-based validation to perform at runtime.<br/>                                                                                                                                                                                                                                                                                                                                                                                   |
| [**D3D12\_GPU\_BASED\_VALIDATION\_PIPELINE\_STATE\_CREATE\_FLAGS**](d3d12-gpu-based-validation-pipeline-state-create-flags.md)<br/> | Specifies how GPU-Based Validation handles patched pipeline states during [**ID3D12Device::CreateGraphicsPipelineState**](id3d12device-creategraphicspipelinestate.md) and [**ID3D12Device::CreateComputePipelineState**](id3d12device-createcomputepipelinestate.md).<br/>                                                                                                                                                                             |
| [**D3D12\_GPU\_BASED\_VALIDATION\_SHADER\_PATCH\_MODE**](d3d12-gpu-based-validation-shader-patch-mode.md)<br/>                      | Specifies the type of shader patching used by GPU-Based Validation at either the device or command list level.<br/>                                                                                                                                                                                                                                                                                                                                       |
| [**D3D12\_MESSAGE\_CATEGORY**](d3d12-message-category.md)<br/>                                                                      | Specifies categories of debug messages. This will identify the category of a message when retrieving a message with [**ID3D12InfoQueue::GetMessage**](id3d12infoqueue-getmessage.md) and when adding a message with [**ID3D12InfoQueue::AddMessage**](id3d12infoqueue-addmessage.md). When creating an info queue filter, these values can be used to allow or deny any categories of messages to pass through the storage and retrieval filters. <br/> |
| [**D3D12\_MESSAGE\_ID**](d3d12-message-id.md)<br/>                                                                                  | Specifies debug message IDs for setting up an info-queue filter (see [**D3D12\_INFO\_QUEUE\_FILTER**](d3d12-info-queue-filter.md)); use these messages to allow or deny message categories to pass through the storage and retrieval filters. These IDs are used by methods such as [**ID3D12InfoQueue::GetMessage**](id3d12infoqueue-getmessage.md) or [**ID3D12InfoQueue::AddMessage**](id3d12infoqueue-addmessage.md). <br/>                        |
| [**D3D12\_MESSAGE\_SEVERITY**](d3d12-message-severity.md)<br/>                                                                      | Debug message severity levels for an information queue.<br/>                                                                                                                                                                                                                                                                                                                                                                                              |
| [**D3D12\_RLDO\_FLAGS**](d3d12-rldo-flags.md)<br/>                                                                                  | Specifies options for the amount of information to report about a live device object's lifetime. <br/>                                                                                                                                                                                                                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Environment Setup](directx-12-programming-environment-set-up.md)
</dt> <dt>

[Debug Layer Reference](direct3d-12-sdklayers-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





