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
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location: 
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
| [**add\_RenderingParametersUpdate**](https://msdn.microsoft.com/en-us/library/Hh828928(v=VS.85).aspx)        | Registers an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                          |
| [**add\_TransportParametersUpdate**](https://msdn.microsoft.com/en-us/library/Hh828929(v=VS.85).aspx)        | Registers an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                          |
| [**GetMuteAsync**](https://msdn.microsoft.com/en-us/library/Hh828930(v=VS.85).aspx)                                           | Queries the DMR asynchronously to determine if audio is currently muted or unmuted.<br/>                                                                                                                                                                                                                                                                               |
| [**GetPositionInformationAsync**](https://msdn.microsoft.com/en-us/library/Hh828931(v=VS.85).aspx)             | Queries the DMR asynchronously to retrieve position information.<br/>                                                                                                                                                                                                                                                                                                  |
| [**GetTransportInformationAsync**](https://msdn.microsoft.com/en-us/library/Hh828932(v=VS.85).aspx)           | Queries the DMR asynchronously to retrieve transport information.<br/>                                                                                                                                                                                                                                                                                                 |
| [**GetVolumeAsync**](https://msdn.microsoft.com/en-us/library/Hh828933(v=VS.85).aspx)                                       | Queries the DMR asynchronously for its current audio volume level.<br/>                                                                                                                                                                                                                                                                                                |
| [**IsAudioSupported**](imediarenderer-isaudiosupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of playing audio content.<br/>                                                                                                                                                                                                                                                                             |
| [**IsImageSupported**](imediarenderer-isimagesupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of displaying images.<br/>                                                                                                                                                                                                                                                                                 |
| [**IsVideoSupported**](imediarenderer-isvideosupported.md)                                   | Retrieves a value that indicates whether the DMR is capable of playing video content.<br/>                                                                                                                                                                                                                                                                             |
| [**PauseAsync**](imediarenderer-pauseasync.md)                                               | Instructs the DMR asynchronously to pause playing the current content.<br/>                                                                                                                                                                                                                                                                                            |
| [**PlayAsync**](https://msdn.microsoft.com/en-us/library/Hh828938(v=VS.85).aspx)                                                 | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](https://msdn.microsoft.com/en-us/library/Hh828949(v=VS.85).aspx), [**SetSourceFromStreamAsync**](https://msdn.microsoft.com/en-us/library/Hh828948(v=VS.85).aspx), or [**SetSourceFromMediaSourceAsync**](https://msdn.microsoft.com/en-us/library/Hh828947(v=VS.85).aspx) method.<br/>                       |
| [**PlayAtSpeedAsync**](https://msdn.microsoft.com/en-us/library/Hh828939(v=VS.85).aspx)                                   | Instructs the DMR asynchronously to play the content that was specified by calling the [**SetSourceFromUriAsync**](https://msdn.microsoft.com/en-us/library/Hh828949(v=VS.85).aspx), [**SetSourceFromStreamAsync**](https://msdn.microsoft.com/en-us/library/Hh828948(v=VS.85).aspx), or [**SetSourceFromMediaSourceAsync**](https://msdn.microsoft.com/en-us/library/Hh828947(v=VS.85).aspx) method at the specified rate.<br/> |
| [**remove\_RenderingParametersUpdate**](https://msdn.microsoft.com/en-us/library/Hh828940(v=VS.85).aspx)  | Unregisters an event handler for the [**RenderingParametersUpdate**](renderingparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                        |
| [**remove\_TransportParametersUpdate**](https://msdn.microsoft.com/en-us/library/Hh828941(v=VS.85).aspx)  | Unregisters an event handler for the [**TransportParametersUpdate**](transportparametersupdate.md) event.<br/>                                                                                                                                                                                                                                                        |
| [**SeekAsync**](https://msdn.microsoft.com/en-us/library/Hh828942(v=VS.85).aspx)                                                 | Instructs the DMR asynchronously to seek to a particular time offset.<br/>                                                                                                                                                                                                                                                                                             |
| [**SetMuteAsync**](https://msdn.microsoft.com/en-us/library/Hh828943(v=VS.85).aspx)                                           | Instructs the DMR asynchronously to either mute or unmute the audio. <br/>                                                                                                                                                                                                                                                                                             |
| [**SetNextSourceFromMediaSourceAsync**](https://msdn.microsoft.com/en-us/library/Hh828944(v=VS.85).aspx) | Instructs the DMR asynchronously to prepare the specified content for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                      |
| [**SetNextSourceFromStreamAsync**](https://msdn.microsoft.com/en-us/library/Hh828945(v=VS.85).aspx)           | Instructs the DMR asynchronously to prepare the specified media stream for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                                 |
| [**SetNextSourceFromUriAsync**](https://msdn.microsoft.com/en-us/library/Hh828946(v=VS.85).aspx)                 | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing once the current content has finished playing.<br/>                                                                                                                                                                                                                |
| [**SetSourceFromMediaSourceAsync**](https://msdn.microsoft.com/en-us/library/Hh828947(v=VS.85).aspx)         | Instructs the DMR asynchronously to prepare the specified content for playing.<br/>                                                                                                                                                                                                                                                                                    |
| [**SetSourceFromStreamAsync**](https://msdn.microsoft.com/en-us/library/Hh828948(v=VS.85).aspx)                   | Instructs the DMR asynchronously to prepare the specified media stream for playing.<br/>                                                                                                                                                                                                                                                                               |
| [**SetSourceFromUriAsync**](https://msdn.microsoft.com/en-us/library/Hh828949(v=VS.85).aspx)                         | Instructs the DMR asynchronously to prepare the content identified by the specified URI for playing.<br/>                                                                                                                                                                                                                                                              |
| [**SetVolumeAsync**](https://msdn.microsoft.com/en-us/library/Hh828950(v=VS.85).aspx)                                       | Sets the audio volume level on the DMR asynchronously to the specified value.<br/>                                                                                                                                                                                                                                                                                     |
| [**StopAsync**](imediarenderer-stopasync.md)                                                 | Instructs the DMR asynchronously to stop playing the current content.<br/>                                                                                                                                                                                                                                                                                             |



 

## See also

<dl> <dt>

[**IBasicDevice**](ibasicdevice.md)
</dt> </dl>

 

 





