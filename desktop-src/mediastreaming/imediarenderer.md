---
title: IMediaRenderer interface
description: Encapsulates the methods and events needed to represent a DLNA Digital Media Renderer (DMR) device.
ms.assetid: 'FBA5BF5A-FA5A-4E25-8F2B-9D1C0A9BCACB'
keywords: ["IMediaRenderer interface Media Streaming API", "IMediaRenderer interface Media Streaming API , described"]
topic_type:
- apiref
api_name:
- IMediaRenderer
api_type:
- COM
---

# IMediaRenderer interface

Encapsulates the methods and events needed to represent a DLNA Digital Media Renderer (DMR) device.

## Members

The **IMediaRenderer** interface inherits from [**IBasicDevice**](ibasicdevice.md). **IMediaRenderer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMediaRenderer** interface has these methods.



| Method                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                  |
|:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActionInformation**](imediarenderer-actioninformation.md)                                 | Retrieves information about which methods can currently be invoked on the DMR.<br/>                                                                                                                                                                                                                                                                                    |
| [**add\_RenderingParametersUpdate**](imediarenderer-add-renderingparametersupdate.md)        | Registers an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                          |
| [**add\_TransportParametersUpdate**](imediarenderer-add-transportparametersupdate.md)        | Registers an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                          |
| [**GetMuteAsync**](imediarenderer-getmuteasync.md)                                           | Queries the DMR asynchronously to determine if audio is currently muted or unmuted.<br/>                                                                                                                                                                                                                                                                               |
| [**GetPositionInformationAsync**](imediarenderer-getpositioninformationasync.md)             | Queries the DMR asynchronously to retrieve position information.<br/>                                                                                                                                                                                                                                                                                                  |
| [**GetTransportInformationAsync**](imediarenderer-gettransportinformationasync.md)           | Queries the DMR asynchronously to retrieve transport information.<br/>                                                                                                                                                                                                                                                                                                 |
| [**GetVolumeAsync**](imediarenderer-getvolumeasync.md)                                       | Queries the DMR asynchronously for its current audio volume level.<br/>                                                                                                                                                                                                                                                                                                |
| [**IsAudioSupported**](imediarenderer-isaudiosupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of playing audio content.<br/>                                                                                                                                                                                                                                                                             |
| [**IsImageSupported**](imediarenderer-isimagesupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of displaying images.<br/>                                                                                                                                                                                                                                                                                 |
| [**IsVideoSupported**](imediarenderer-isvideosupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of playing video content.<br/>                                                                                                                                                                                                                                                                             |
| [**PauseAsync**](imediarenderer-pauseasync.md)                                               | Instructs the DMR asynchronously to pause playing the current content.<br/>                                                                                                                                                                                                                                                                                            |
| [**PlayAsync**](imediarenderer-playasync.md)                                                 | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](imediarenderer-setsourcefromuriasync.md), [**SetSourceFromStreamAsync**](imediarenderer-setsourcefromstreamasync.md), or [**SetSourceFromMediaSourceAsync**](imediarenderer-setsourcefrommediasourceasync.md) method.<br/>                       |
| [**PlayAtSpeedAsync**](imediarenderer-playatspeedasync.md)                                   | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](imediarenderer-setsourcefromuriasync.md), [**SetSourceFromStreamAsync**](imediarenderer-setsourcefromstreamasync.md), or [**SetSourceFromMediaSourceAsync**](imediarenderer-setsourcefrommediasourceasync.md) method at the specified rate.<br/> |
| [**remove\_RenderingParametersUpdate**](imediarenderer-remove-renderingparametersupdate.md)  | Unregisters an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                        |
| [**remove\_TransportParametersUpdate**](imediarenderer-remove-transportparametersupdate.md)  | Unregisters an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                        |
| [**SeekAsync**](imediarenderer-seekasync.md)                                                 | Instructs the DMR asynchronously to seek to a particular time offset.<br/>                                                                                                                                                                                                                                                                                             |
| [**SetMuteAsync**](imediarenderer-setmuteasync.md)                                           | Instructs the DMR asynchronously to either mute or unmute the audio. <br/>                                                                                                                                                                                                                                                                                             |
| [**SetNextSourceFromMediaSourceAsync**](imediarenderer-setnextsourcefrommediasourceasync.md) | Instructs the DMR asynchronously to prepare the specified content for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                      |
| [**SetNextSourceFromStreamAsync**](imediarenderer-setnextsourcefromstreamasync.md)           | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                 |
| [**SetNextSourceFromUriAsync**](imediarenderer-setnextsourcefromuriasync.md)                 | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                |
| [**SetSourceFromMediaSourceAsync**](imediarenderer-setsourcefrommediasourceasync.md)         | Instructs the DMR asynchronously to prepare the specified content for playing.<br/>                                                                                                                                                                                                                                                                                    |
| [**SetSourceFromStreamAsync**](imediarenderer-setsourcefromstreamasync.md)                   | Instructs the DMR asynchronously to prepare the specified media stream for playing.<br/>                                                                                                                                                                                                                                                                               |
| [**SetSourceFromUriAsync**](imediarenderer-setsourcefromuriasync.md)                         | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing.<br/>                                                                                                                                                                                                                                                              |
| [**SetVolumeAsync**](imediarenderer-setvolumeasync.md)                                       | Sets the audio volume level on the DMR asynchronously to the specified value.<br/>                                                                                                                                                                                                                                                                                     |
| [**StopAsync**](imediarenderer-stopasync.md)                                                 | Instructs the DMR asynchronously to stop playing the current content.<br/>                                                                                                                                                                                                                                                                                             |



 

## See also

<dl> <dt>

[**IBasicDevice**](ibasicdevice.md)
</dt> </dl>

 

 





