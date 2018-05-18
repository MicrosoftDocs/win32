---
title: Remote Desktop Services AudioEndpoint Interfaces
description: The following interfaces are used with the AudioEndpoint API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '615c2d03-c2fb-46f8-aa78-064f8e7b6064'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Remote Desktop Services AudioEndpoint Interfaces

The following interfaces are used with the AudioEndpoint API.

## In this section

<dl> <dt>

[**IAudioDeviceEndpoint**](iaudiodeviceendpoint.md)
</dt> <dd>

Initializes a device endpoint object and gets the capabilities of the device that it represents.

</dd> <dt>

[**IAudioEndpoint**](iaudioendpoint.md)
</dt> <dd>

Provides information to the audio engine about an audio endpoint. This interface is implemented by an audio endpoint.

</dd> <dt>

[**IAudioEndpointControl**](iaudioendpointcontrol.md)
</dt> <dd>

Controls the stream state of an endpoint.

</dd> <dt>

[**IAudioEndpointRT**](iaudioendpointrt.md)
</dt> <dd>

Gets the difference between the current read and write positions in the endpoint buffer.

</dd> <dt>

[**IAudioInputEndpointRT**](iaudioinputendpointrt.md)
</dt> <dd>

Gets the input buffer for each processing pass.

</dd> <dt>

[**IAudioOutputEndpointRT**](iaudiooutputendpointrt.md)
</dt> <dd>

Gets the output buffer for each processing pass.

</dd> </dl>

## Remarks

The Remote Desktop Services AudioEndpoint API is for use in Remote Desktop scenarios; it is not for client applications.

 

 




