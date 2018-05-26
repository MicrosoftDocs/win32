---
title: Video Control Interfaces
description: Video Control Interfaces
ms.assetid: bf6c3ce9-1e56-4109-93f1-5b313e6ca19b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Control Interfaces

This topic applies to Windows XP or later.

The following table lists the interfaces implemented by the Video Control and its related objects.



| Interface                                                                        | Description                                                                                                   |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**IBroadcastEventEx**](/windows/previous-versions/tuner/nn-tuner-ibroadcasteventex?branch=master)                                   | Extended version of **IBroadcastEvent**.                                                                      |
| [**IBroadcastEvent**](/windows/previous-versions/tuner/nn-tuner-ibroadcastevent?branch=master)                                       | Enables an object to receive events from another object without setting up a direct connection point.         |
| [**IMSVidAnalogTuner**](/windows/win32/segment/nn-segment-imsvidanalogtuner?branch=master)                                   | Represents an analog-only tuner card that does not support the Broadcast Driver Architecture (BDA).           |
| [**IMSVidAnalogTuner2**](/windows/win32/segment/nn-segment-imsvidanalogtuner2?branch=master)                                 | Represents an analog-only tuner card that does not support the Broadcast Driver Architecture (BDA).           |
| [**IMSVidAudioRendererDevices**](/windows/win32/segment/nn-segment-imsvidaudiorendererdevices?branch=master)                 | Represents a collection of audio renderers.                                                                   |
| [**IMSVidAudioRenderer**](/windows/win32/segment/nn-segment-imsvidaudiorenderer?branch=master)                               | Represents an audio renderer device.                                                                          |
| [**IMSVidClosedCaptioning**](/windows/win32/segment/nn-segment-imsvidclosedcaptioning?branch=master)                         | Enables or disables closed captioning.                                                                        |
| [**IMSVidClosedCaptioning2**](/windows/win32/segment/nn-segment-imsvidclosedcaptioning2?branch=master)                       | Sets the closed captioning service.                                                                           |
| [**IMSVidClosedCaptioning3**](/windows/win32/segment/nn-segment-imsvidclosedcaptioning3?branch=master)                       | Retrieves the teletext filter.                                                                                |
| [**IMSVidCtl**](/windows/previous-versions/msvidctl/nn-msvidctl-imsvidctl?branch=master)                                                   | Provides the primary interface for the Video Control.                                                         |
| [**IMSVidDataServices**](/windows/win32/segment/?branch=master)                                 | Represents the data services feature.                                                                         |
| [**IMSVidDevice**](/windows/win32/segment/nn-segment-imsviddevice?branch=master)                                             | Provides the base interface for all the devices and features that the Video Control supports.                 |
| [**IMSVidDevice2**](/windows/win32/segment/nn-segment-imsviddevice2?branch=master)                                           | Extends the [**IMSVidDevice**](/windows/win32/segment/nn-segment-imsviddevice?branch=master) interface.                                                   |
| [**IMSVidEncoder**](/windows/win32/segment/nn-segment-imsvidencoder?branch=master)                                           | Represents the [MSVidEncoder](msvidencoder.md) feature.                                                      |
| [**IMSVidEVR**](/windows/win32/segment/nn-segment-imsvidevr?branch=master)                                                   | Represents the Enhanced Video Renderer (EVR) filter within the Video Control filter graph.                    |
| [**IMSVidFeature**](/windows/win32/segment/?branch=master)                                           | Represents a feature that is available through the Video Control, such as data services or closed captioning. |
| [**IMSVidFeatures**](/windows/win32/segment/nn-segment-imsvidfeatures?branch=master)                                         | Represents a collection of Video Control features.                                                            |
| [**IMSVidFilePlayback**](/windows/win32/segment/nn-segment-imsvidfileplayback?branch=master)                                 | Enables the client to specify a local file for playback.                                                      |
| [**IMSVidFilePlayback2**](/windows/win32/segment/nn-segment-imsvidfileplayback2?branch=master)                               | Extends the [**IMSVidFilePlayback**](/windows/win32/segment/nn-segment-imsvidfileplayback?branch=master) interface.                                       |
| [**IMSVidGenericSink**](/windows/win32/segment/nn-segment-imsvidgenericsink?branch=master)                                   | Represents a generic output device.                                                                           |
| [**IMSVidGenericSink2**](/windows/win32/segment/nn-segment-imsvidgenericsink2?branch=master)                                 | Extends the [**IMSVidGenericSink**](/windows/win32/segment/nn-segment-imsvidgenericsink?branch=master) interface.                                         |
| [**IMSVidGraphSegmentContainer**](/windows/win32/segment/nn-segment-imsvidgraphsegmentcontainer?branch=master)               | Obtains a pointer to the Filter Graph Manager.                                                                |
| [**IMSVidInputDevice**](/windows/win32/segment/nn-segment-imsvidinputdevice?branch=master)                                   | Represents any input device that is recognized by the Video Control, such as a television tuner card.         |
| [**IMSVidInputDevices**](/windows/win32/segment/nn-segment-imsvidinputdevices?branch=master)                                 | Represents a collection of input devices.                                                                     |
| [**IMSVidOutputDevice**](/windows/win32/segment/?branch=master)                                 | Represents an output device.                                                                                  |
| [**IMSVidOutputDevices**](/windows/win32/segment/nn-segment-imsvidoutputdevices?branch=master)                               | Represents a collection of output devices.                                                                    |
| [**IMSVidPlayback**](/windows/win32/segment/nn-segment-imsvidplayback?branch=master)                                         | Controls a playback device.                                                                                   |
| [**IMSVidRect**](/windows/win32/segment/nn-segment-imsvidrect?branch=master)                                                 | Represents a rectangle with an associated window handle.                                                      |
| [**IMSVidStreamBufferRecordingControl**](/windows/win32/segment/nn-segment-imsvidstreambufferrecordingcontrol?branch=master) | Enables an application to manage a stream buffer recording object through the Video Control.                  |
| [**IMSVidStreamBufferSink**](/windows/win32/segment/nn-segment-imsvidstreambuffersink?branch=master)                         | Represents the Stream Buffer Sink filter within the Video Control.                                            |
| [**IMSVidStreamBufferSink2**](/windows/win32/segment/nn-segment-imsvidstreambuffersink2?branch=master)                       | Extends the [**IMSVidStreamBufferSink**](/windows/win32/segment/nn-segment-imsvidstreambuffersink?branch=master) interface.                               |
| [**IMSVidStreamBufferSink3**](/windows/win32/segment/nn-segment-imsvidstreambuffersink3?branch=master)                       | Extends the [**IMSVidStreamBufferSink2**](/windows/win32/segment/nn-segment-imsvidstreambuffersink2?branch=master) interface.                             |
| [**IMSVidStreamBufferSource**](/windows/win32/segment/nn-segment-imsvidstreambuffersource?branch=master)                     | Represents the Stream Buffer Source filter within the Video Control.                                          |
| [**IMSVidStreamBufferSource2**](/windows/win32/segment/nn-segment-imsvidstreambuffersource2?branch=master)                   | Extends the [**IMSVidStreamBufferSource**](/windows/win32/segment/nn-segment-imsvidstreambuffersource?branch=master) interface.                           |
| [**IMSVidTuner**](/windows/win32/segment/nn-segment-imsvidtuner?branch=master)                                               | Manages tuning devices.                                                                                       |
| [**IMSVidVideoInputDevice**](/windows/win32/segment/?branch=master)                         | Represents a video input device.                                                                              |
| [**IMSVidVideoRenderer**](/windows/win32/segment/nn-segment-imsvidvideorenderer?branch=master)                               | Represents a video renderer device.                                                                           |
| [**IMSVidVideoRenderer2**](/windows/win32/segment/nn-segment-imsvidvideorenderer2?branch=master)                             | Represents a video renderer device.                                                                           |
| [**IMSVidVideoRendererDevices**](/windows/win32/segment/nn-segment-imsvidvideorendererdevices?branch=master)                 | Represents a collection of video renderers.                                                                   |
| [**IMSVidVMR9**](/windows/win32/segment/nn-segment-imsvidvmr9?branch=master)                                                 | Represents the Video Mixing Renderer Filter 9 (VMR-9) within the Video Control filter graph.                  |
| [**IMSVidXDS**](/windows/win32/segment/nn-segment-imsvidxds?branch=master)                                                   | Represents the extended data services feature.                                                                |



 

 

 




