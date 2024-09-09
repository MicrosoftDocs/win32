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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MediaRenderer class

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Implements the [**IMediaRenderer**](imediarenderer.md) interface that represents a DLNA Digital Media Renderer (DMR) device.

**MediaRenderer** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MediaRenderer** class has these methods.



| Method                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                               |
|:---------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**add\_RenderingParametersUpdate**](/previous-versions/windows/desktop/legacy/hh828962(v=vs.85))        | Registers an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                       |
| [**add\_TransportParametersUpdate**](/previous-versions/windows/desktop/legacy/hh828963(v=vs.85))        | Registers an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                       |
| [**GetMuteAsync**](/previous-versions/windows/desktop/legacy/hh828964(v=vs.85))                                           | Queries the DMR asynchronously to determine if audio is currently muted or unmuted.<br/>                                                                                                                                                                                                                                                                            |
| [**GetPositionInformationAsync**](/previous-versions/windows/desktop/legacy/hh828965(v=vs.85))             | Queries the DMR asynchronously to retrieve position information.<br/>                                                                                                                                                                                                                                                                                               |
| [**GetTransportInformationAsync**](/previous-versions/windows/desktop/legacy/hh828966(v=vs.85))           | Queries the DMR asynchronously to retrieve transport information.<br/>                                                                                                                                                                                                                                                                                              |
| [**GetVolumeAsync**](/previous-versions/windows/desktop/legacy/hh828967(v=vs.85))                                       | Queries the DMR asynchronously for its current audio volume level.<br/>                                                                                                                                                                                                                                                                                             |
| [**PauseAsync**](mediarenderer-pauseasync.md)                                               | Instructs the DMR asynchronously to pause playing the current content.<br/>                                                                                                                                                                                                                                                                                         |
| [**PlayAsync**](/previous-versions/windows/desktop/legacy/hh828972(v=vs.85))                                                 | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](/previous-versions/windows/desktop/legacy/hh828983(v=vs.85)), [**SetSourceFromStreamAsync**](/previous-versions/windows/desktop/legacy/hh828982(v=vs.85)), or [**SetSourceFromMediaSourceAsync**](/previous-versions/windows/desktop/legacy/hh828981(v=vs.85)) method.<br/>                       |
| [**PlayAtSpeedAsync**](/previous-versions/windows/desktop/legacy/hh828973(v=vs.85))                                   | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](/previous-versions/windows/desktop/legacy/hh828983(v=vs.85)), [**SetSourceFromStreamAsync**](/previous-versions/windows/desktop/legacy/hh828982(v=vs.85)), or [**SetSourceFromMediaSourceAsync**](/previous-versions/windows/desktop/legacy/hh828981(v=vs.85)) method at the specified rate.<br/> |
| [**remove\_RenderingParametersUpdate**](/previous-versions/windows/desktop/legacy/hh828974(v=vs.85))  | Unregisters an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                     |
| [**remove\_TransportParametersUpdate**](/previous-versions/windows/desktop/legacy/hh828975(v=vs.85))  | Unregisters an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                     |
| [**SeekAsync**](/previous-versions/windows/desktop/legacy/hh828976(v=vs.85))                                                 | Instructs the DMR asynchronously to seek to a particular time offset.<br/>                                                                                                                                                                                                                                                                                          |
| [**SetMuteAsync**](/previous-versions/windows/desktop/legacy/hh828977(v=vs.85))                                           | Instructs the DMR asynchronously to either mute or unmute the audio.<br/>                                                                                                                                                                                                                                                                                           |
| [**SetNextSourceFromMediaSourceAsync**](/previous-versions/windows/desktop/legacy/hh828978(v=vs.85)) | Instructs the DMR asynchronously to prepare the specified content for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                   |
| [**SetNextSourceFromStreamAsync**](/previous-versions/windows/desktop/legacy/hh828979(v=vs.85))           | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                              |
| [**SetNextSourceFromUriAsync**](/previous-versions/windows/desktop/legacy/hh828980(v=vs.85))                 | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing once the current content has finished playing.<br/>                                                                                                                                                                                                             |
| [**SetSourceFromMediaSourceAsync**](/previous-versions/windows/desktop/legacy/hh828981(v=vs.85))         | Instructs the DMR asynchronously to prepare the specified content for playing.<br/>                                                                                                                                                                                                                                                                                 |
| [**SetSourceFromStreamAsync**](/previous-versions/windows/desktop/legacy/hh828982(v=vs.85))                   | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                              |
| [**SetSourceFromUriAsync**](/previous-versions/windows/desktop/legacy/hh828983(v=vs.85))                         | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing.<br/>                                                                                                                                                                                                                                                           |
| [**SetVolumeAsync**](/previous-versions/windows/desktop/legacy/hh828984(v=vs.85))                                       | Sets the audio volume level on the DMR asynchronously to the specified value.<br/>                                                                                                                                                                                                                                                                                  |
| [**StopAsync**](mediarenderer-stopasync.md)                                                 | Instructs the DMR asynchronously to stop playing the current content.<br/>                                                                                                                                                                                                                                                                                          |



 

### Properties

The **MediaRenderer** class has these properties.



| Property                                                                | Access type          | Description                                                                                 |
|:------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------|
| [**ActionInformation**](mediarenderer-actioninformation.md)<br/> | Read-only<br/> | Gets information about which methods can currently be invoked on the DMR.<br/>        |
| [**IsAudioSupported**](mediarenderer-isaudiosupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of playing audio content.<br/> |
| [**IsImageSupported**](mediarenderer-isimagesupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of displaying images.<br/>     |
| [**IsVideoSupported**](mediarenderer-isvideosupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of playing video content.<br/> |



 

 

