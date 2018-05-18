---
title: Video Control Event Interfaces
description: Video Control Event Interfaces
ms.assetid: '939de48a-2816-46c8-bfda-b47d074a5939'
---

# Video Control Event Interfaces

> [!Note]  
> This topic applies to Windows XP or later.

 

The following table lists the outgoing event interfaces that an application must implement in order to receive events from various objects associated with the Video Control.



| Interface                                                                | Description                                                                                                        |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**\_IMSVidCtlEvents**](-imsvidctlevents.md)                            | Implement this interface to receive events from the Video Control.                                                 |
| [**IMSVidAnalogTunerEvent**](imsvidanalogtunerevent.md)                 | Implement this interface to receive events from an analog tuner device.                                            |
| [**IMSVidAudioRendererEvent**](imsvidaudiorendererevent.md)             | Implement this interface to receive events from an audio renderer.                                                 |
| [**IMSVidDeviceEvent**](imsviddeviceevent.md)                           | Base interface for device events.                                                                                  |
| [**IMSVidEVREvent Interface**](imsvidevrevent.md)                       | Implement this interface to receive events from the Enhanced Video Renderer (EVR) filter.                          |
| [**IMSVidFeatureEvent**](imsvidfeatureevent.md)                         | Base interface for events from Video Control feature objects.                                                      |
| [**IMSVidFilePlaybackEvent**](imsvidfileplaybackevent.md)               | Implement this interface to receive events from the file playback object.                                          |
| [**IMSVidInputDeviceEvent**](imsvidinputdeviceevent.md)                 | Base interface for input device events.                                                                            |
| [**IMSVidOutputDeviceEvent**](imsvidoutputdeviceevent.md)               | Base interface for output device events.                                                                           |
| [**IMSVidPlaybackEvent**](imsvidplaybackevent.md)                       | Implement this interface to receive events from a playback device.                                                 |
| [**IMSVidStreamBufferSinkEvent**](imsvidstreambuffersinkevent.md)       | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent2**](imsvidstreambuffersinkevent2.md)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent3**](imsvidstreambuffersinkevent3.md)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSinkEvent4**](imsvidstreambuffersinkevent4.md)     | Implement this interface to receive events from the [MSVidStreamBufferSink](msvidstreambuffersink.md) object.     |
| [**IMSVidStreamBufferSourceEvent**](imsvidstreambuffersourceevent.md)   | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidStreamBufferSourceEvent2**](imsvidstreambuffersourceevent2.md) | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidStreamBufferSourceEvent3**](imsvidstreambuffersourceevent3.md) | Implement this interface to receive events from the [MSVidStreamBufferSource](msvidstreambuffersource.md) object. |
| [**IMSVidTunerEvent**](imsvidtunerevent.md)                             | Implement this interface to receive events from a tuner device.                                                    |
| [**IMSVidVideoRendererEvent**](imsvidvideorendererevent.md)             | Implement this interface to receive events from a video renderer.                                                  |
| [**IMSVidXDSEvent**](imsvidxdsevent.md)                                 | Implement this interface to receive events from the [MSVidXDS](msvidxds.md) object.                               |



 

## Related topics

<dl> <dt>

[**Receiving Video Control Events in C++**](receiving-video-control-events-in-c.md)
</dt> <dt>

[**Receiving Video Control Events in ATL**](receiving-video-control-events-in-atl.md)
</dt> <dt>

[**Video Control Reference**](video-control-reference.md)
</dt> </dl>

 

 




