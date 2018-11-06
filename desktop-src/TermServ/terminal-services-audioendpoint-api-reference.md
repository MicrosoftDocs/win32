---
title: Remote Desktop Services AudioEndpoint API reference
description: Supports interfaces for audio endpoint registration and data transport.
ms.assetid: 0e3ea0e7-8c61-400e-b8ef-8a0403aedafa
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , AudioEndpoint API reference
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services AudioEndpoint API reference

An *audio endpoint* represents an audio device, audio API, or any other audio source or sink, and is used to send data to or consume data from the audio engine. An audio endpoint must be connected to the audio engine through a *connection*, and each connection can have only one endpoint connected to it. After an endpoint is registered, the audio engine attaches the endpoint to the connection.

Each endpoint object must implement the following interfaces:

-   [**IAudioEndpoint**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudioendpoint) to enable the audio engine to get information about the endpoint.
-   [**IAudioEndpointRT**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudioendpointrt) to get information about the data buffer before performing a processing pass and notifying the endpoint when the pass is complete.
-   Either the [**IAudioInputEndpointRT**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudioinputendpointrt) or [**IAudioOutputEndpointRT**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudiooutputendpointrt) interface, depending on whether the endpoint object is capturing or rendering audio.
-   [**IAudioDeviceEndpoint**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudiodeviceendpoint)
-   [**IAudioEndpointControl**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudioendpointcontrol)

The audio engine uses these interfaces to get information about the endpoints that are attached to the engine. The endpoint implementation must provide the mechanism to deliver data to or consume data from the engine as specified by these interfaces.

The Remote Desktop Services AudioEndpoint API supports enumeration types, interfaces, and structures.

## In this section

-   [Remote Desktop Services AudioEndpoint Enumeration Types](terminal-services-audioendpoint-enumeration-types.md)
-   [Remote Desktop Services AudioEndpoint Functions](remote-desktop-services-audioendpoint-functions.md)
-   [Remote Desktop Services AudioEndpoint Interfaces](terminal-services-audioendpoint-interfaces.md)
-   [Remote Desktop Services AudioEndpoint Structures](terminal-services-audioendpoint-structures.md)

## Remarks

The Remote Desktop Services AudioEndpoint API is for use in Remote Desktop scenarios; it is not for client applications.

 

 




