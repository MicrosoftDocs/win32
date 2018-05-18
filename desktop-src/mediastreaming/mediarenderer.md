---
title: MediaRenderer class
description: Implements the IMediaRenderer interface that represents a DLNA Digital Media Renderer (DMR) device.
ms.assetid: 'FBA5BF5A-FA5A-4E25-8F2B-9D1C0A9BCACB'
keywords: ["MediaRenderer class Media Streaming API", "MediaRenderer class Media Streaming API , described"]
topic_type:
- apiref
api_name:
- MediaRenderer
api_type:
- COM
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
| [**add\_RenderingParametersUpdate**](mediarenderer-add-renderingparametersupdate.md)        | Registers an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                       |
| [**add\_TransportParametersUpdate**](mediarenderer-add-transportparametersupdate.md)        | Registers an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                       |
| [**GetMuteAsync**](mediarenderer-getmuteasync.md)                                           | Queries the DMR asynchronously to determine if audio is currently muted or unmuted.<br/>                                                                                                                                                                                                                                                                            |
| [**GetPositionInformationAsync**](mediarenderer-getpositioninformationasync.md)             | Queries the DMR asynchronously to retrieve position information.<br/>                                                                                                                                                                                                                                                                                               |
| [**GetTransportInformationAsync**](mediarenderer-gettransportinformationasync.md)           | Queries the DMR asynchronously to retrieve transport information.<br/>                                                                                                                                                                                                                                                                                              |
| [**GetVolumeAsync**](mediarenderer-getvolumeasync.md)                                       | Queries the DMR asynchronously for its current audio volume level.<br/>                                                                                                                                                                                                                                                                                             |
| [**PauseAsync**](mediarenderer-pauseasync.md)                                               | Instructs the DMR asynchronously to pause playing the current content.<br/>                                                                                                                                                                                                                                                                                         |
| [**PlayAsync**](mediarenderer-playasync.md)                                                 | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](mediarenderer-setsourcefromuriasync.md), [**SetSourceFromStreamAsync**](mediarenderer-setsourcefromstreamasync.md), or [**SetSourceFromMediaSourceAsync**](mediarenderer-setsourcefrommediasourceasync.md) method.<br/>                       |
| [**PlayAtSpeedAsync**](mediarenderer-playatspeedasync.md)                                   | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](mediarenderer-setsourcefromuriasync.md), [**SetSourceFromStreamAsync**](mediarenderer-setsourcefromstreamasync.md), or [**SetSourceFromMediaSourceAsync**](mediarenderer-setsourcefrommediasourceasync.md) method at the specified rate.<br/> |
| [**remove\_RenderingParametersUpdate**](mediarenderer-remove-renderingparametersupdate.md)  | Unregisters an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                     |
| [**remove\_TransportParametersUpdate**](mediarenderer-remove-transportparametersupdate.md)  | Unregisters an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                     |
| [**SeekAsync**](mediarenderer-seekasync.md)                                                 | Instructs the DMR asynchronously to seek to a particular time offset.<br/>                                                                                                                                                                                                                                                                                          |
| [**SetMuteAsync**](mediarenderer-setmuteasync.md)                                           | Instructs the DMR asynchronously to either mute or unmute the audio.<br/>                                                                                                                                                                                                                                                                                           |
| [**SetNextSourceFromMediaSourceAsync**](mediarenderer-setnextsourcefrommediasourceasync.md) | Instructs the DMR asynchronously to prepare the specified content for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                   |
| [**SetNextSourceFromStreamAsync**](mediarenderer-setnextsourcefromstreamasync.md)           | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                              |
| [**SetNextSourceFromUriAsync**](mediarenderer-setnextsourcefromuriasync.md)                 | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing once the current content has finished playing.<br/>                                                                                                                                                                                                             |
| [**SetSourceFromMediaSourceAsync**](mediarenderer-setsourcefrommediasourceasync.md)         | Instructs the DMR asynchronously to prepare the specified content for playing.<br/>                                                                                                                                                                                                                                                                                 |
| [**SetSourceFromStreamAsync**](mediarenderer-setsourcefromstreamasync.md)                   | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                              |
| [**SetSourceFromUriAsync**](mediarenderer-setsourcefromuriasync.md)                         | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing.<br/>                                                                                                                                                                                                                                                           |
| [**SetVolumeAsync**](mediarenderer-setvolumeasync.md)                                       | Sets the audio volume level on the DMR asynchronously to the specified value.<br/>                                                                                                                                                                                                                                                                                  |
| [**StopAsync**](mediarenderer-stopasync.md)                                                 | Instructs the DMR asynchronously to stop playing the current content.<br/>                                                                                                                                                                                                                                                                                          |



 

### Properties

The **MediaRenderer** class has these properties.



| Property                                                                | Access type          | Description                                                                                 |
|:------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------|
| [**ActionInformation**](mediarenderer-actioninformation.md)<br/> | Read-only<br/> | Gets information about which methods can currently be invoked on the DMR.<br/>        |
| [**IsAudioSupported**](mediarenderer-isaudiosupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of playing audio content.<br/> |
| [**IsImageSupported**](mediarenderer-isimagesupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of displaying images.<br/>     |
| [**IsVideoSupported**](mediarenderer-isvideosupported.md)<br/>   | Read-only<br/> | Gets a value that indicates whether the DMR is capable of playing video content.<br/> |



 

 

 





