---
title: Video Control Event Interfaces
description: Video Control Event Interfaces
ms.assetid: 939de48a-2816-46c8-bfda-b47d074a5939
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Control Event Interfaces

> [!Note]  
> This topic applies to Windows XP or later.

 

The following table lists the outgoing event interfaces that an application must implement in order to receive events from various objects associated with the Video Control.



| Interface                                                                | Description                                                                                                        |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**\_IMSVidCtlEvents**](/windows/previous-versions/msvidctl/?branch=master)                            | Implement this interface to receive events from the Video Control.                                                 |
| [**IMSVidAnalogTunerEvent**](/windows/win32/segment/?branch=master)                 | Implement this interface to receive events from an analog tuner device.                                            |
| [**IMSVidAudioRendererEvent**](/windows/win32/segment/?branch=master)             | Implement this interface to receive events from an audio renderer.                                                 |
| [**IMSVidDeviceEvent**](/windows/win32/segment/nn-segment-imsviddeviceevent?branch=master)                           | Base interface for device events.                                                                                  |
| [**IMSVidEVREvent Interface**](/windows/win32/segment/nn-segment-imsvidevrevent?branch=master)                       | Implement this interface to receive events from the Enhanced Video Renderer (EVR) filter.                          |
| [**IMSVidFeatureEvent**](/windows/win32/segment/?branch=master)                         | Base interface for events from Video Control feature objects.                                                      |
| [**IMSVidFilePlaybackEvent**](/windows/win32/segment/?branch=master)               | Implement this interface to receive events from the file playback object.                                          |
| [**IMSVidInputDeviceEvent**](/windows/win32/segment/?branch=master)                 | Base interface for input device events.                                                                            |
| [**IMSVidOutputDeviceEvent**](/windows/win32/segment/?branch=master)               | Base interface for output device events.                                                                           |
| [**IMSVidPlaybackEvent**](/windows/win32/segment/nn-segment-imsvidplaybackevent?branch=master)                       | Implement this interface to receive events from a playback device.                                                 |
| [**IMSVidStreamBufferSinkEvent**](/windows/win32/segment/nn-segment-imsvidstreambuffersinkevent?branch=master)       | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent2**](/windows/win32/segment/nn-segment-imsvidstreambuffersinkevent2?branch=master)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent3**](/windows/win32/segment/nn-segment-imsvidstreambuffersinkevent3?branch=master)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent4**](/windows/win32/segment/nn-segment-imsvidstreambuffersinkevent4?branch=master)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSourceEvent**](/windows/win32/segment/nn-segment-imsvidstreambuffersourceevent?branch=master)   | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidStreamBufferSourceEvent2**](/windows/win32/segment/nn-segment-imsvidstreambuffersourceevent2?branch=master) | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidStreamBufferSourceEvent3**](/windows/win32/segment/nn-segment-imsvidstreambuffersourceevent3?branch=master) | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidTunerEvent**](/windows/win32/segment/nn-segment-imsvidtunerevent?branch=master)                             | Implement this interface to receive events from a tuner device.                                                    |
| [**IMSVidVideoRendererEvent**](/windows/win32/segment/nn-segment-imsvidvideorendererevent?branch=master)             | Implement this interface to receive events from a video renderer.                                                  |
| [**IMSVidXDSEvent**](/windows/win32/segment/nn-segment-imsvidxdsevent?branch=master)                                 | Implement this interface to receive events from the [MSVidXDS](msvidxds.md) object.                               |



 

## Related topics

<dl> <dt>

[**Receiving Video Control Events in C++**](receiving-video-control-events-in-c.md)
</dt> <dt>

[**Receiving Video Control Events in ATL**](receiving-video-control-events-in-atl.md)
</dt> <dt>

[**Video Control Reference**](video-control-reference.md)
</dt> </dl>

 

 




