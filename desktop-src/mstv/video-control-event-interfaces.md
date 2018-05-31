---
title: Video Control Event Interfaces
description: Video Control Event Interfaces
ms.assetid: 939de48a-2816-46c8-bfda-b47d074a5939
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Video Control Event Interfaces

> [!Note]  
> This topic applies to Windows XP or later.

 

The following table lists the outgoing event interfaces that an application must implement in order to receive events from various objects associated with the Video Control.



| Interface                                                                | Description                                                                                                        |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**\_IMSVidCtlEvents**](/previous-versions/windows/desktop/api/msvidctl/)                            | Implement this interface to receive events from the Video Control.                                                 |
| [**IMSVidAnalogTunerEvent**](/windows/desktop/api/segment/)                 | Implement this interface to receive events from an analog tuner device.                                            |
| [**IMSVidAudioRendererEvent**](/windows/desktop/api/segment/)             | Implement this interface to receive events from an audio renderer.                                                 |
| [**IMSVidDeviceEvent**](/windows/desktop/api/segment/nn-segment-imsviddeviceevent)                           | Base interface for device events.                                                                                  |
| [**IMSVidEVREvent Interface**](/windows/desktop/api/segment/nn-segment-imsvidevrevent)                       | Implement this interface to receive events from the Enhanced Video Renderer (EVR) filter.                          |
| [**IMSVidFeatureEvent**](/windows/desktop/api/segment/)                         | Base interface for events from Video Control feature objects.                                                      |
| [**IMSVidFilePlaybackEvent**](/windows/desktop/api/segment/)               | Implement this interface to receive events from the file playback object.                                          |
| [**IMSVidInputDeviceEvent**](/windows/desktop/api/segment/)                 | Base interface for input device events.                                                                            |
| [**IMSVidOutputDeviceEvent**](/windows/desktop/api/segment/)               | Base interface for output device events.                                                                           |
| [**IMSVidPlaybackEvent**](/windows/desktop/api/segment/nn-segment-imsvidplaybackevent)                       | Implement this interface to receive events from a playback device.                                                 |
| [**IMSVidStreamBufferSinkEvent**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersinkevent)       | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent2**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersinkevent2)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent3**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersinkevent3)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent4**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersinkevent4)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSourceEvent**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersourceevent)   | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidStreamBufferSourceEvent2**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersourceevent2) | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidStreamBufferSourceEvent3**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersourceevent3) | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidTunerEvent**](/windows/desktop/api/segment/nn-segment-imsvidtunerevent)                             | Implement this interface to receive events from a tuner device.                                                    |
| [**IMSVidVideoRendererEvent**](/windows/desktop/api/segment/nn-segment-imsvidvideorendererevent)             | Implement this interface to receive events from a video renderer.                                                  |
| [**IMSVidXDSEvent**](/windows/desktop/api/segment/nn-segment-imsvidxdsevent)                                 | Implement this interface to receive events from the [MSVidXDS](msvidxds.md) object.                               |



 

## Related topics

<dl> <dt>

[**Receiving Video Control Events in C++**](receiving-video-control-events-in-c.md)
</dt> <dt>

[**Receiving Video Control Events in ATL**](receiving-video-control-events-in-atl.md)
</dt> <dt>

[**Video Control Reference**](video-control-reference.md)
</dt> </dl>

 

 




