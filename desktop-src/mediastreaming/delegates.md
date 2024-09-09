---
title: Delegates
description: The Media Streaming API provides the following event handler functions.
ms.assetid: CDE7B829-D0D1-479D-9B35-4445E711AF58
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Delegates

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [Media Streaming API](media-streaming-api-portal.md) provides the following event handler functions.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConnectionStatusHandler**](/previous-versions/windows/desktop/legacy/hh828836(v=vs.85))<br/>                   | Represents the function that will handle the [**ConnectionStatusChanged**](connectionstatuschanged.md) event which notifies the client of changes in the device s network connection status.<br/>               |
| [**DeviceControllerFinderHandler**](/previous-versions/windows/desktop/legacy/hh828843(v=vs.85))<br/>       | Represents the function that will handle the [**DeviceArrival**](devicearrival.md) and [**DeviceDeparture**](devicedeparture.md) events which notify the client of changes in the list of cached devices.<br/> |
| [**RenderingParametersUpdateHandler**](/previous-versions/windows/desktop/legacy/hh828994(v=vs.85))<br/> | Represents the function that will handle the [**RenderingParametersUpdate**](renderingparametersupdate.md) event which notifies the client of an update to any of the DMR s rendering control parameters.<br/>  |
| [**TransportParametersUpdateHandler**](/previous-versions/windows/desktop/legacy/hh829007(v=vs.85))<br/> | Represents the function that will handle the [**TransportParametersUpdate**](transportparametersupdate.md) event which notifies the client of an update to any of the DMR s transport parameters.<br/>          |



 

 

