---
title: Video Control Objects (C++)
description: Video Control Objects (C++)
ms.assetid: ea8be9a1-b672-49f0-b563-df58f2184321
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Control Objects (C++)

This topic applies to Windows XP or later.

The following tables list the Video Control objects, grouped by functionality.

**Video Control**

The Video Control (MSVidCtl) is the primary object that a television application uses to display television, tune to channels, and so forth.



| Object                   | Description                   |
|--------------------------|-------------------------------|
| [MSVidCtl](msvidctl.md) | Represents the Video Control. |



 

**Devices**

Devices represent components that the Video Control uses to display television. Devices include *input devices*, such as tuners, and *output devices*, such as audio renderers and video renderers.



| Object                                                 | Description                                            |
|--------------------------------------------------------|--------------------------------------------------------|
| [MSVidAnalogTunerDevice](msvidanalogtunerdevice.md)   | Represents a non-BDA analog TV tuner.                  |
| [MSVidAudioRenderer](msvidaudiorenderer.md)           | Represents the audio renderer.                         |
| [MSVidBDATunerDevice](msvidbdatunerdevice.md)         | Represents a BDA-compatible TV tuner.                  |
| [MSVidEVR](msvidevr.md)                               | Represents the Enhanced Video Renderer (EVR) filter.   |
| [MSVidFilePlaybackDevice](msvidfileplaybackdevice.md) | Represents a file-playback filter.                     |
| [MSVidGenericSink](msvidgenericsink.md)               | Represents a generic output device.                    |
| [MSVidStreamBufferSink](msvidstreambuffersink.md)     | Represents a stream buffer output device.              |
| [MSVidStreamBufferSource](msvidstreambuffersource.md) | Represents a stream buffer source device.              |
| [MSVidVideoRenderer](msvidvideorenderer.md)           | Represents the video renderer.                         |
| [MSVidVMR9](msvidvmr9.md)                             | Represents the Video Mixing Renderer Filter 9 (VMR-9). |



 

**Features**

Features represent additional functionality that an application can activate, such as closed captioning and IP data services.



| Object                                             | Description                                    |
|----------------------------------------------------|------------------------------------------------|
| [MSVidClosedCaptioning](msvidclosedcaptioning.md) | Represents the closed captioning feature.      |
| [MSVidDataServices](msviddataservices.md)         | Represents the data services feature.          |
| [MSVidEncoder](msvidencoder.md)                   | Represents the encoder feature.                |
| [MSVidXDS](msvidxds.md)                           | Represents the extended data services feature. |



 

**Collections**

Collection objects manage collections of other objects.



| Object                                                     | Description                                 |
|------------------------------------------------------------|---------------------------------------------|
| [MSVidAudioRendererDevices](msvidaudiorendererdevices.md) | Represents a collection of audio renderers. |
| [MSVidFeatures](msvidfeatures.md)                         | Represents a collection of features.        |
| [MSVidInputDevices](msvidinputdevices.md)                 | Represents a collection of input devices.   |
| [MSVidOutputDevices](msvidoutputdevices.md)               | Represents a collection of output devices.  |
| [MSVidVideoRendererDevices](msvidvideorendererdevices.md) | Represents a collection of video renderers. |



 

**Helper Objects**

The following helper objects are used by other Video Control objects.



| Object                                           | Description                                            |
|--------------------------------------------------|--------------------------------------------------------|
| [Broadcast Event Service](broadcast-service.md) | Handles broadcast events for the Filter Graph Manager. |
| [MSVidRect](msvidrect.md)                       | Represents a rectangle with an associated window.      |



 

**Abstract Classes**

The following objects represent abstract classes. They are never directly instantiated, and exist only to support polymorphism.



| Object                                             | Description                                          |
|----------------------------------------------------|------------------------------------------------------|
| [MSVidInputDevice](msvidinputdevice.md)           | Represents an input device.                          |
| [MSVidOutputDevice](msvidoutputdevice.md)         | Represents an output device.                         |
| [MSVidVideoInputDevice](msvidvideoinputdevice.md) | Represents a video input device.                     |
| [MSVidFeature](msvidfeature.md)                   | Represents a feature supported by the Video Control. |



 

 

 




