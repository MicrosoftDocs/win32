---
title: Events (Media Streaming API)
description: The Media Streaming API generates the following events.
ms.assetid: 8954B079-5CCB-4D0C-9F48-A8DEA101C3FA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Events (Media Streaming API)

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [Media Streaming API](media-streaming-api-portal.md) generates the following events.

## In this section



| Topic                                                                           | Description                                                                                                                                              |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConnectionStatusChanged Event**](connectionstatuschanged.md)<br/>     | Occurs when the device s network connection status changes.<br/>                                                                                   |
| [**DeviceArrival Event**](devicearrival.md)<br/>                         | Occurs when a new device is added to the list of devices returned by the [**CachedDevices**](idevicecontroller-cacheddevices.md) method.<br/>     |
| [**DeviceDeparture Event**](devicedeparture.md)<br/>                     | Occurs when a new device is removed from the list of devices returned by the [**CachedDevices**](idevicecontroller-cacheddevices.md) method.<br/> |
| [**RenderingParametersUpdate Event**](renderingparametersupdate.md)<br/> | Occurs whenever any of a set of rendering control parameters are updated on the DMR.<br/>                                                          |
| [**TransportParametersUpdate Event**](transportparametersupdate.md)<br/> | Occurs whenever any of a set of transport parameters are updated on the DMR.<br/>                                                                  |



 

 

 





