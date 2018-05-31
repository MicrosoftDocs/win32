---
title: Video Control Interfaces
description: Video Control Interfaces
ms.assetid: bf6c3ce9-1e56-4109-93f1-5b313e6ca19b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Video Control Interfaces

This topic applies to Windows XP or later.

The following table lists the interfaces implemented by the Video Control and its related objects.



| Interface                                                                        | Description                                                                                                   |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**IBroadcastEventEx**](ibroadcasteventex.md)                                   | Extended version of **IBroadcastEvent**.                                                                      |
| [**IBroadcastEvent**](ibroadcastevent.md)                                       | Enables an object to receive events from another object without setting up a direct connection point.         |
| [**IMSVidAnalogTuner**](/windows/desktop/api/segment/nn-segment-imsvidanalogtuner)                                   | Represents an analog-only tuner card that does not support the Broadcast Driver Architecture (BDA).           |
| [**IMSVidAnalogTuner2**](/windows/desktop/api/segment/nn-segment-imsvidanalogtuner2)                                 | Represents an analog-only tuner card that does not support the Broadcast Driver Architecture (BDA).           |
| [**IMSVidAudioRendererDevices**](/windows/desktop/api/segment/nn-segment-imsvidaudiorendererdevices)                 | Represents a collection of audio renderers.                                                                   |
| [**IMSVidAudioRenderer**](/windows/desktop/api/segment/nn-segment-imsvidaudiorenderer)                               | Represents an audio renderer device.                                                                          |
| [**IMSVidClosedCaptioning**](/windows/desktop/api/segment/nn-segment-imsvidclosedcaptioning)                         | Enables or disables closed captioning.                                                                        |
| [**IMSVidClosedCaptioning2**](/windows/desktop/api/segment/nn-segment-imsvidclosedcaptioning2)                       | Sets the closed captioning service.                                                                           |
| [**IMSVidClosedCaptioning3**](/windows/desktop/api/segment/nn-segment-imsvidclosedcaptioning3)                       | Retrieves the teletext filter.                                                                                |
| [**IMSVidCtl**](imsvidctl.md)                                                   | Provides the primary interface for the Video Control.                                                         |
| [**IMSVidDataServices**](/windows/desktop/api/segment/)                                 | Represents the data services feature.                                                                         |
| [**IMSVidDevice**](/windows/desktop/api/segment/nn-segment-imsviddevice)                                             | Provides the base interface for all the devices and features that the Video Control supports.                 |
| [**IMSVidDevice2**](/windows/desktop/api/segment/nn-segment-imsviddevice2)                                           | Extends the [**IMSVidDevice**](/windows/desktop/api/segment/nn-segment-imsviddevice) interface.                                                   |
| [**IMSVidEncoder**](/windows/desktop/api/segment/nn-segment-imsvidencoder)                                           | Represents the [MSVidEncoder](msvidencoder.md) feature.                                                      |
| [**IMSVidEVR**](/windows/desktop/api/segment/nn-segment-imsvidevr)                                                   | Represents the Enhanced Video Renderer (EVR) filter within the Video Control filter graph.                    |
| [**IMSVidFeature**](/windows/desktop/api/segment/)                                           | Represents a feature that is available through the Video Control, such as data services or closed captioning. |
| [**IMSVidFeatures**](/windows/desktop/api/segment/nn-segment-imsvidfeatures)                                         | Represents a collection of Video Control features.                                                            |
| [**IMSVidFilePlayback**](/windows/desktop/api/segment/nn-segment-imsvidfileplayback)                                 | Enables the client to specify a local file for playback.                                                      |
| [**IMSVidFilePlayback2**](/windows/desktop/api/segment/nn-segment-imsvidfileplayback2)                               | Extends the [**IMSVidFilePlayback**](/windows/desktop/api/segment/nn-segment-imsvidfileplayback) interface.                                       |
| [**IMSVidGenericSink**](/windows/desktop/api/segment/nn-segment-imsvidgenericsink)                                   | Represents a generic output device.                                                                           |
| [**IMSVidGenericSink2**](/windows/desktop/api/segment/nn-segment-imsvidgenericsink2)                                 | Extends the [**IMSVidGenericSink**](/windows/desktop/api/segment/nn-segment-imsvidgenericsink) interface.                                         |
| [**IMSVidGraphSegmentContainer**](/windows/desktop/api/segment/nn-segment-imsvidgraphsegmentcontainer)               | Obtains a pointer to the Filter Graph Manager.                                                                |
| [**IMSVidInputDevice**](/windows/desktop/api/segment/nn-segment-imsvidinputdevice)                                   | Represents any input device that is recognized by the Video Control, such as a television tuner card.         |
| [**IMSVidInputDevices**](/windows/desktop/api/segment/nn-segment-imsvidinputdevices)                                 | Represents a collection of input devices.                                                                     |
| [**IMSVidOutputDevice**](/windows/desktop/api/segment/)                                 | Represents an output device.                                                                                  |
| [**IMSVidOutputDevices**](/windows/desktop/api/segment/nn-segment-imsvidoutputdevices)                               | Represents a collection of output devices.                                                                    |
| [**IMSVidPlayback**](/windows/desktop/api/segment/nn-segment-imsvidplayback)                                         | Controls a playback device.                                                                                   |
| [**IMSVidRect**](/windows/desktop/api/segment/nn-segment-imsvidrect)                                                 | Represents a rectangle with an associated window handle.                                                      |
| [**IMSVidStreamBufferRecordingControl**](/windows/desktop/api/segment/nn-segment-imsvidstreambufferrecordingcontrol) | Enables an application to manage a stream buffer recording object through the Video Control.                  |
| [**IMSVidStreamBufferSink**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersink)                         | Represents the Stream Buffer Sink filter within the Video Control.                                            |
| [**IMSVidStreamBufferSink2**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersink2)                       | Extends the [**IMSVidStreamBufferSink**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersink) interface.                               |
| [**IMSVidStreamBufferSink3**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersink3)                       | Extends the [**IMSVidStreamBufferSink2**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersink2) interface.                             |
| [**IMSVidStreamBufferSource**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersource)                     | Represents the Stream Buffer Source filter within the Video Control.                                          |
| [**IMSVidStreamBufferSource2**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersource2)                   | Extends the [**IMSVidStreamBufferSource**](/windows/desktop/api/segment/nn-segment-imsvidstreambuffersource) interface.                           |
| [**IMSVidTuner**](/windows/desktop/api/segment/nn-segment-imsvidtuner)                                               | Manages tuning devices.                                                                                       |
| [**IMSVidVideoInputDevice**](/windows/desktop/api/segment/)                         | Represents a video input device.                                                                              |
| [**IMSVidVideoRenderer**](/windows/desktop/api/segment/nn-segment-imsvidvideorenderer)                               | Represents a video renderer device.                                                                           |
| [**IMSVidVideoRenderer2**](/windows/desktop/api/segment/nn-segment-imsvidvideorenderer2)                             | Represents a video renderer device.                                                                           |
| [**IMSVidVideoRendererDevices**](/windows/desktop/api/segment/nn-segment-imsvidvideorendererdevices)                 | Represents a collection of video renderers.                                                                   |
| [**IMSVidVMR9**](/windows/desktop/api/segment/nn-segment-imsvidvmr9)                                                 | Represents the Video Mixing Renderer Filter 9 (VMR-9) within the Video Control filter graph.                  |
| [**IMSVidXDS**](/windows/desktop/api/segment/nn-segment-imsvidxds)                                                   | Represents the extended data services feature.                                                                |



 

 

 




