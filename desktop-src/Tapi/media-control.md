---
Description: The media of a communications session is the form in which the data is transmitted. Media controls allow an application to recognize a variety of media types and adjust aspects of the media stream, such as the volume of voice transmission.
ms.assetid: b32503fe-d494-44ea-b144-e38b8ab9b3d4
title: Media Control
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Media Control

The media of a communications session is the form in which the data is transmitted. Media controls allow an application to recognize a variety of media types and adjust aspects of the media stream, such as the volume of voice transmission.

The availability of media control and information varies widely with the type of TAPI application, service provider support, and the local communications environment. The following material provides a general description of media control. TAPI supplies a flexible framework for the implementation of controls, so the most interesting capabilities will often be specific to a given service provider.

Under classic telephony, an application had very little control over the media stream once a communications path had been set up. TAPI 2 applications have access to some functions that allow them to recognize and react to digits or tones during a call, and they may be able to use the Wave API to exercise additional control over media during a communications session, but otherwise they do not have media stream access. See the TAPI 2.2 [Media Access](https://msdn.microsoft.com/en-us/library/ms736575(v=VS.85).aspx) overview or the TSPI [Media Access](https://msdn.microsoft.com/library/ms725240) overview for a review of these functions.

TAPI 3 introduces the [Media Service Providers](about-the-media-service-provider-msp-.md), which steeply increases both information about and control over the media or a communication session. A TAPI 3 application can directly access the media [stream](stream-objects.md) of a session. A separate stream is created for each media type involved in the session, such as voice or video. Some MSPs may implement substream controls, which can divide streams further, such as by participant in the case of the IPConf MSP.



| TAPI 2.x functions                                          | Description                                                                                                                |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**lineGatherDigits**](https://msdn.microsoft.com/en-us/library/ms735655(v=VS.85).aspx)       | Initiates the buffered gathering of digits on the specified call.                                                          |
| [**lineGenerateDigits**](https://msdn.microsoft.com/en-us/library/ms735659(v=VS.85).aspx)   | Initiates the generation of the specified digits on the specified call as inband tones using the specified signaling mode. |
| [**lineGenerateTone**](https://msdn.microsoft.com/en-us/library/ms735668(v=VS.85).aspx)       | Generates the specified inband tone over the specified call.                                                               |
| [**lineMonitorDigits**](https://msdn.microsoft.com/en-us/library/ms735996(v=VS.85).aspx)     | Enables and disables the unbuffered detection of digits received on the call.                                              |
| [**lineMonitorMedia**](https://msdn.microsoft.com/en-us/library/ms735997(v=VS.85).aspx)       | Enables and disables the detection of media types on the specified call.                                                   |
| [**lineMonitorTones**](https://msdn.microsoft.com/en-us/library/ms735998(v=VS.85).aspx)       | Enables and disables the detection of inband tones on the call.                                                            |
| [**lineSetMediaControl**](https://msdn.microsoft.com/en-us/library/ms736100(v=VS.85).aspx) | Enables and disables control actions on the media stream associated with the specified line, address, or call.             |



 



| TAPI 3.x interfaces or methods                               | Description                                                                                                                                                                                            |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITLegacyCallMediaControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itlegacycallmediacontrol) | Supports legacy applications that must communicate directly with a device.                                                                                                                             |
| [**ITLegacyWaveSupport**](/windows/desktop/api/tapi3if/nn-tapi3if-itlegacywavesupport)           | Allows an application to discover whether a terminal created by a legacy TSP (pre-TAPI 3) can be controlled using the Wave API.                                                                        |
| [**ITStream**](https://msdn.microsoft.com/en-us/library/ms732390(v=VS.85).aspx)                                 | Allows an application to retrieve information on a stream; to start, pause, or stop the stream; to select or unselect terminals on a stream; and to obtain a list of terminals selected on the stream. |
| [**ITStreamControl**](https://msdn.microsoft.com/en-us/library/ms732393(v=VS.85).aspx)                   | Allows an application to enumerate, create, or remove media streams.                                                                                                                                   |



 

 

 



