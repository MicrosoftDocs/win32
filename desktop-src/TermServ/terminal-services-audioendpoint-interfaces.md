---
title: Remote Desktop Services AudioEndpoint Interfaces
description: The following interfaces are used with the AudioEndpoint API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 615c2d03-c2fb-46f8-aa78-064f8e7b6064
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Services AudioEndpoint Interfaces

The following interfaces are used with the AudioEndpoint API.

## In this section

<dl> <dt>

[**IAudioDeviceEndpoint**](/windows/win32/Audioengineendpoint/nn-audioengineendpoint-iaudiodeviceendpoint?branch=master)
</dt> <dd>

Initializes a device endpoint object and gets the capabilities of the device that it represents.

</dd> <dt>

[**IAudioEndpoint**](/windows/win32/Audioengineendpoint/nn-audioengineendpoint-iaudioendpoint?branch=master)
</dt> <dd>

Provides information to the audio engine about an audio endpoint. This interface is implemented by an audio endpoint.

</dd> <dt>

[**IAudioEndpointControl**](/windows/win32/Audioengineendpoint/nn-audioengineendpoint-iaudioendpointcontrol?branch=master)
</dt> <dd>

Controls the stream state of an endpoint.

</dd> <dt>

[**IAudioEndpointRT**](/windows/win32/Audioengineendpoint/nn-audioengineendpoint-iaudioendpointrt?branch=master)
</dt> <dd>

Gets the difference between the current read and write positions in the endpoint buffer.

</dd> <dt>

[**IAudioInputEndpointRT**](/windows/win32/Audioengineendpoint/nn-audioengineendpoint-iaudioinputendpointrt?branch=master)
</dt> <dd>

Gets the input buffer for each processing pass.

</dd> <dt>

[**IAudioOutputEndpointRT**](/windows/win32/Audioengineendpoint/nn-audioengineendpoint-iaudiooutputendpointrt?branch=master)
</dt> <dd>

Gets the output buffer for each processing pass.

</dd> </dl>

## Remarks

The Remote Desktop Services AudioEndpoint API is for use in Remote Desktop scenarios; it is not for client applications.

 

 




