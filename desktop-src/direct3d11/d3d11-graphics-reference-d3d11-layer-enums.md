---
title: Layer Enumerations
description: This section contains information about the layer enumerations.
ms.assetid: 0fd0456b-2638-4b4c-8a34-a3e104a1a034
keywords:
- enumerations, Direct3D 11 Layer
ms.topic: article
ms.date: 05/31/2018
---

# Layer Enumerations

This section contains information about the layer enumerations.


## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**D3D11\_MESSAGE\_CATEGORY**](/windows/desktop/api/D3D11SDKLayers/ne-d3d11sdklayers-d3d11_message_category)<br/>                             | Categories of debug messages. This will identify the category of a message when retrieving a message with [**ID3D11InfoQueue::GetMessage**](/windows/desktop/api/D3D11SDKLayers/nf-d3d11sdklayers-id3d11infoqueue-getmessage) and when adding a message with [**ID3D11InfoQueue::AddMessage**](/windows/desktop/api/D3D11SDKLayers/nf-d3d11sdklayers-id3d11infoqueue-addmessage). When creating an [**info queue filter**](/windows/desktop/api/D3D11SDKLayers/ns-d3d11sdklayers-d3d11_info_queue_filter), these values can be used to allow or deny any categories of messages to pass through the storage and retrieval filters.<br/> |
| [**D3D11\_MESSAGE\_ID**](/windows/desktop/api/D3D11SDKLayers/ne-d3d11sdklayers-d3d11_message_id)<br/>                                         | Debug messages for setting up an info-queue filter (see [**D3D11\_INFO\_QUEUE\_FILTER**](/windows/desktop/api/D3D11SDKLayers/ns-d3d11sdklayers-d3d11_info_queue_filter)); use these messages to allow or deny message categories to pass through the storage and retrieval filters. These IDs are used by methods such as [**ID3D11InfoQueue::GetMessage**](/windows/desktop/api/D3D11SDKLayers/nf-d3d11sdklayers-id3d11infoqueue-getmessage) or [**ID3D11InfoQueue::AddMessage**](/windows/desktop/api/D3D11SDKLayers/nf-d3d11sdklayers-id3d11infoqueue-addmessage). <br/>                                                             |
| [**D3D11\_MESSAGE\_SEVERITY**](/windows/desktop/api/D3D11SDKLayers/ne-d3d11sdklayers-d3d11_message_severity)<br/>                             | Debug message severity levels for an information queue.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**D3D11\_RLDO\_FLAGS**](/windows/desktop/api/D3D11SDKLayers/ne-d3d11sdklayers-d3d11_rldo_flags)<br/>                                         | Options for the amount of information to report about a device object's lifetime.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| [**D3D11\_SHADER\_TRACKING\_OPTIONS**](/windows/win32/api/d3d11sdklayers/ne-d3d11sdklayers-d3d11_shader_tracking_options)<br/>              | Options that specify how to perform shader debug tracking.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**D3D11\_SHADER\_TRACKING\_RESOURCE\_TYPE**](/windows/desktop/api/D3D11SDKLayers/ne-d3d11sdklayers-d3d11_shader_tracking_resource_type)<br/> | Indicates which resource types to track.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[Layer Reference](d3d11-graphics-reference-d3d11-layer.md)
</dt> </dl>

 

 





