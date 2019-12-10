---
title: MediaRenderer class
description: Implements the IMediaRenderer interface that represents a DLNA Digital Media Renderer (DMR) device.
ms.assetid: 'bac7898f-1334-4e28-92c7-6de464884eaf'
keywords:
- MediaRenderer class Media Streaming API
- MediaRenderer class Media Streaming API , described
topic_type:
- apiref
api_name:
- MediaRenderer
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MediaRenderer class

Implements the [**IMediaRenderer**](imediarenderer.md) interface that represents a DLNA Digital Media Renderer (DMR) device.

**MediaRenderer** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MediaRenderer** class has these methods.



| Method                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                               |
|:---------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**add\_RenderingParametersUpdate**](https://msdn.microsoft.com/library/Hh828962(v=VS.85).aspx)        | Registers an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                       |
| [**add\_TransportParametersUpdate**](https://msdn.microsoft.com/library/Hh828963(v=VS.85).aspx)        | Registers an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                       |
| [**GetMuteAsync**](https://msdn.microsoft.com/library/Hh828964(v=VS.85).aspx)                                           | Queries the DMR asynchronously to determine if audio is currently muted or unmuted.<br/>                                                                                                                                                                                                                                                                            |
| [**GetPositionInformationAsync**](https://msdn.microsoft.com/library/Hh828965(v=VS.85).aspx)             | Queries the DMR asynchronously to retrieve position information.<br/>                                                                                                                                                                                                                                                                                               |
| [**GetTransportInformationAsync**](https://msdn.microsoft.com/library/Hh828966(v=VS.85).aspx)           | Queries the DMR asynchronously to retrieve transport information.<br/>                                                                                                                                                                                                                                                                                              |
| [**GetVolumeAsync**](https://msdn.microsoft.com/library/Hh828967(v=VS.85).aspx)                                       | Queries the DMR asynchronously for its current audio volume level.<br/>                                                                                                                                                                                                                                                                                             |
| [**PauseAsync**](mediarenderer-pauseasync.md)                                               | Instructs the DMR asynchronously to pause playing the current content.<br/>                                                                                                                                                                                                                                                                                         |
| [**PlayAsync**](https://msdn.microsoft.com/library/Hh828972(v=VS.85).aspx)                                                 | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](https://msdn.microsoft.com/library/Hh828983(v=VS.85).aspx), [**SetSourceFromStreamAsync**](https://msdn.microsoft.com/library/Hh828982(v=VS.85).aspx), or [**SetSourceFromMediaSourceAsync**](https://msdn.microsoft.com/library/Hh828981(v=VS.85).aspx) method.<br/>                       |
| [**PlayAtSpeedAsync**](https://msdn.microsoft.com/library/Hh828973(v=VS.85).aspx)                                   | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](https://msdn.microsoft.com/library/Hh828983(v=VS.85).aspx), [**SetSourceFromStreamAsync**](https://msdn.microsoft.com/library/Hh828982(v=VS.85).aspx), or [**SetSourceFromMediaSourceAsync**](https://msdn.microsoft.com/library/Hh828981(v=VS.85).aspx) method at the specified rate.<br/> |
| [**remove\_RenderingParametersUpdate**](https://msdn.microsoft.com/library/Hh828974(v=VS.85).aspx)  | Unregisters an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                     |
| [**remove\_TransportParametersUpdate**](https://msdn.microsoft.com/library/Hh828975(v=VS.85).aspx)  | Unregisters an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                     |
| [**SeekAsync**](https://msdn.microsoft.com/library/Hh828976(v=VS.85).aspx)                                                 | Instructs the DMR asynchronously to seek to a particular time offset.<br/>                                                                                                                                                                                                                                                                                          |
| [**SetMuteAsync**](https://msdn.microsoft.com/library/Hh828977(v=VS.85).aspx)                                           | Instructs the DMR asynchronously to either mute or unmute the audio.<br/>                                                                                                                                                                                                                                                                                           |
| [**SetNextSourceFromMediaSourceAsync**](https://msdn.microsoft.com/library/Hh828978(v=VS.85).aspx) | Instructs the DMR asynchronously to prepare the specified content for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                   |
| [**SetNextSourceFromStreamAsync**](https://msdn.microsoft.com/library/Hh828979(v=VS.85).aspx)           | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                              |
| [**SetNextSourceFromUriAsync**](https://msdn.microsoft.com/library/Hh828980(v=VS.85).aspx)                 | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing once the current content has finished playing.<br/>                                                                                                                                                                                                             |
| [**SetSourceFromMediaSourceAsync**](https://msdn.microsoft.com/library/Hh828981(v=VS.85).aspx)         | Instructs the DMR asynchronously to prepare the specified content for playing.<br/>                                                                                                                                                                                                                                                                                 |
| [**SetSourceFromStreamAsync**](https://msdn.microsoft.com/library/Hh828982(v=VS.85).aspx)                   | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                              |
| [**SetSourceFromUriAsync**](https://msdn.microsoft.com/library/Hh828983(v=VS.85).aspx)                         | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing.<br/>                                                                                                                                                                                                                                                           |
| [**SetVolumeAsync**](https://msdn.microsoft.com/library/Hh828984(v=VS.85).aspx)                                       | Sets the audio volume level on the DMR asynchronously to the specified value.<br/>                                                                                                                                                                                                                                                                                  |
| [**StopAsync**](mediarenderer-stopasync.md)                                                 | Instructs the DMR asynchronously to stop playing the current content.<br/>                                                                                                                                                                                                                                                                                          |



 

### Properties

The **MediaRenderer** class has these properties.



| Property                                                                | Access type          | Description                                                                                 |
|:------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------|
| [**ActionInformation**](mediarenderer-actioninformation.md)<br/> | Read-only<br/> | Gets information about which methods can currently be invoked on the DMR.<br/>        |
| [**IsAudioSupported**](mediarenderer-isaudiosupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of playing audio content.<br/> |
| [**IsImageSupported**](mediarenderer-isimagesupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of displaying images.<br/>     |
| [**IsVideoSupported**](mediarenderer-isvideosupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of playing video content.<br/> |



 

 

 





