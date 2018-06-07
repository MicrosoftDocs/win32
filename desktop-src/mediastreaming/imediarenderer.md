---
title: IMediaRenderer interface
description: Encapsulates the methods and events needed to represent a DLNA Digital Media Renderer (DMR) device.
ms.assetid: FBA5BF5A-FA5A-4E25-8F2B-9D1C0A9BCACB
keywords:
- IMediaRenderer interface Media Streaming API
- IMediaRenderer interface Media Streaming API , described
topic_type:
- apiref
api_name:
- IMediaRenderer
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
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
| [**add\_RenderingParametersUpdate**](https://www.bing.com/search?q=**add\_RenderingParametersUpdate**)        | Registers an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                          |
| [**add\_TransportParametersUpdate**](https://www.bing.com/search?q=**add\_TransportParametersUpdate**)        | Registers an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                          |
| [**GetMuteAsync**](https://www.bing.com/search?q=**GetMuteAsync**)                                           | Queries the DMR asynchronously to determine if audio is currently muted or unmuted.<br/>                                                                                                                                                                                                                                                                               |
| [**GetPositionInformationAsync**](https://www.bing.com/search?q=**GetPositionInformationAsync**)             | Queries the DMR asynchronously to retrieve position information.<br/>                                                                                                                                                                                                                                                                                                  |
| [**GetTransportInformationAsync**](https://www.bing.com/search?q=**GetTransportInformationAsync**)           | Queries the DMR asynchronously to retrieve transport information.<br/>                                                                                                                                                                                                                                                                                                 |
| [**GetVolumeAsync**](https://www.bing.com/search?q=**GetVolumeAsync**)                                       | Queries the DMR asynchronously for its current audio volume level.<br/>                                                                                                                                                                                                                                                                                                |
| [**IsAudioSupported**](imediarenderer-isaudiosupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of playing audio content.<br/>                                                                                                                                                                                                                                                                             |
| [**IsImageSupported**](imediarenderer-isimagesupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of displaying images.<br/>                                                                                                                                                                                                                                                                                 |
| [**IsVideoSupported**](imediarenderer-isvideosupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of playing video content.<br/>                                                                                                                                                                                                                                                                             |
| [**PauseAsync**](imediarenderer-pauseasync.md)                                               | Instructs the DMR asynchronously to pause playing the current content.<br/>                                                                                                                                                                                                                                                                                            |
| [**PlayAsync**](https://www.bing.com/search?q=**PlayAsync**)                                                 | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](https://www.bing.com/search?q=**SetSourceFromUriAsync**), [**SetSourceFromStreamAsync**](https://www.bing.com/search?q=**SetSourceFromStreamAsync**), or [**SetSourceFromMediaSourceAsync**](https://www.bing.com/search?q=**SetSourceFromMediaSourceAsync**) method.<br/>                       |
| [**PlayAtSpeedAsync**](https://www.bing.com/search?q=**PlayAtSpeedAsync**)                                   | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](https://www.bing.com/search?q=**SetSourceFromUriAsync**), [**SetSourceFromStreamAsync**](https://www.bing.com/search?q=**SetSourceFromStreamAsync**), or [**SetSourceFromMediaSourceAsync**](https://www.bing.com/search?q=**SetSourceFromMediaSourceAsync**) method at the specified rate.<br/> |
| [**remove\_RenderingParametersUpdate**](https://www.bing.com/search?q=**remove\_RenderingParametersUpdate**)  | Unregisters an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                        |
| [**remove\_TransportParametersUpdate**](https://www.bing.com/search?q=**remove\_TransportParametersUpdate**)  | Unregisters an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                        |
| [**SeekAsync**](https://www.bing.com/search?q=**SeekAsync**)                                                 | Instructs the DMR asynchronously to seek to a particular time offset.<br/>                                                                                                                                                                                                                                                                                             |
| [**SetMuteAsync**](https://www.bing.com/search?q=**SetMuteAsync**)                                           | Instructs the DMR asynchronously to either mute or unmute the audio. <br/>                                                                                                                                                                                                                                                                                             |
| [**SetNextSourceFromMediaSourceAsync**](https://www.bing.com/search?q=**SetNextSourceFromMediaSourceAsync**) | Instructs the DMR asynchronously to prepare the specified content for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                      |
| [**SetNextSourceFromStreamAsync**](https://www.bing.com/search?q=**SetNextSourceFromStreamAsync**)           | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                 |
| [**SetNextSourceFromUriAsync**](https://www.bing.com/search?q=**SetNextSourceFromUriAsync**)                 | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                |
| [**SetSourceFromMediaSourceAsync**](https://www.bing.com/search?q=**SetSourceFromMediaSourceAsync**)         | Instructs the DMR asynchronously to prepare the specified content for playing.<br/>                                                                                                                                                                                                                                                                                    |
| [**SetSourceFromStreamAsync**](https://www.bing.com/search?q=**SetSourceFromStreamAsync**)                   | Instructs the DMR asynchronously to prepare the specified media stream for playing.<br/>                                                                                                                                                                                                                                                                               |
| [**SetSourceFromUriAsync**](https://www.bing.com/search?q=**SetSourceFromUriAsync**)                         | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing.<br/>                                                                                                                                                                                                                                                              |
| [**SetVolumeAsync**](https://www.bing.com/search?q=**SetVolumeAsync**)                                       | Sets the audio volume level on the DMR asynchronously to the specified value.<br/>                                                                                                                                                                                                                                                                                     |
| [**StopAsync**](imediarenderer-stopasync.md)                                                 | Instructs the DMR asynchronously to stop playing the current content.<br/>                                                                                                                                                                                                                                                                                             |



 

## See also

<dl> <dt>

[**IBasicDevice**](ibasicdevice.md)
</dt> </dl>

 

 





