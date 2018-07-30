---
Description: The event (notification) interfaces allow a TAPI 3 application to respond to asynchronous events.
ms.assetid: 27fd91e8-b628-49ee-af4e-9aec0afa5449
title: Event Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Event Interfaces

The event (notification) interfaces allow a TAPI 3 application to respond to asynchronous events.

You must call the [**ITTAPI::put\_EventFilter**](https://msdn.microsoft.com/en-us/library/ms732553(v=VS.85).aspx) method and set an event filter mask to enable reception of request events. If you do not call **ITTAPI::put\_EventFilter**, your application will not receive any events.

Please see the [Events](https://msdn.microsoft.com/en-us/library/ms726212(v=VS.85).aspx) overview for a description of how an application ensures reception of notifications. See the individual interfaces listed in the following table for more information about setting a filter mask for individual event types.



| Interface                                                           | Description                                                                                                                                 |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITAddressEvent**](https://msdn.microsoft.com/en-us/library/ms728210(v=VS.85).aspx)                   | Retrieves the description of address events.                                                                                                |
| [**ITASRTerminalEvent**](https://msdn.microsoft.com/en-us/library/Aa382353(v=VS.85).aspx)           | Retrieves the description of Automatic Speech Recognition terminal events.                                                                  |
| [**ITCallHubEvent**](https://msdn.microsoft.com/en-us/library/ms729263(v=VS.85).aspx)                   | Retrieves the description of CallHub events.                                                                                                |
| [**ITCallInfoChangeEvent**](https://msdn.microsoft.com/en-us/library/ms729287(v=VS.85).aspx)     | Retrieves the description of call information change events.                                                                                |
| [**ITCallMediaEvent**](https://msdn.microsoft.com/en-us/library/ms729332(v=VS.85).aspx)               | Retrieves the description of call media events.                                                                                             |
| [**ITCallNotificationEvent**](https://msdn.microsoft.com/en-us/library/ms729340(v=VS.85).aspx) | Retrieves the description of call notification events.                                                                                      |
| [**ITCallStateEvent**](https://msdn.microsoft.com/en-us/library/ms729348(v=VS.85).aspx)               | Retrieves the description of call state events.                                                                                             |
| [**ITDigitDetectionEvent**](https://msdn.microsoft.com/en-us/library/ms729517(v=VS.85).aspx)     | Retrieves information about DTMF digit events during a call.                                                                                |
| [**ITDigitGenerationEvent**](https://msdn.microsoft.com/en-us/library/ms729523(v=VS.85).aspx)   | Retrieves information about calls that require the generation of DTMF digits.                                                               |
| [**ITDigitsGatheredEvent**](https://msdn.microsoft.com/en-us/library/ms729528(v=VS.85).aspx)     | Retrieves data related to an application's digit-gathering request.                                                                         |
| [**ITFileTerminalEvent**](https://msdn.microsoft.com/en-us/library/ms730039(v=VS.85).aspx)         | Retrieves the description of file terminal events.                                                                                          |
| [**ITParticipantEvent**](https://msdn.microsoft.com/en-us/library/ms730763(v=VS.85).aspx)           | Retrieves the description of conference participant events.                                                                                 |
| [**ITPhoneEvent**](https://msdn.microsoft.com/en-us/library/ms730844(v=VS.85).aspx)                       | Retrieves the description of phone events.                                                                                                  |
| [**ITQOSEvent**](https://msdn.microsoft.com/en-us/library/ms731442(v=VS.85).aspx)                           | Retrieves the description of quality of service (QOS) events.                                                                               |
| [**ITQueueEvent**](https://msdn.microsoft.com/en-us/library/ms731451(v=VS.85).aspx)                       | Retrieves the description of Automatic Call Distribution (ACD) queue events.                                                                |
| [**ITRequestEvent**](https://msdn.microsoft.com/en-us/library/ms731494(v=VS.85).aspx)                   | Retrieves the description of [Assisted Telephony](https://msdn.microsoft.com/en-us/library/ms726209(v=VS.85).aspx) request events.                                 |
| [**ITTAPIObjectEvent**](https://msdn.microsoft.com/en-us/library/ms732512(v=VS.85).aspx)             | Retrieves the description of TAPI object events.                                                                                            |
| [**ITTAPIObjectEvent2**](https://msdn.microsoft.com/en-us/library/ms732515(v=VS.85).aspx)           | Extends [**ITTAPIObjectEvent**](https://msdn.microsoft.com/en-us/library/ms732512(v=VS.85).aspx); retrieves a pointer to the phone object that caused the TAPI object event. |
| [**ITToneDetectionEvent**](https://msdn.microsoft.com/en-us/library/ms733243(v=VS.85).aspx)       | Retrieves information about a tone detection event.                                                                                         |
| [**ITToneTerminalEvent**](https://msdn.microsoft.com/en-us/library/ms733263(v=VS.85).aspx)         | Retrieves the description of tone terminal events.                                                                                          |
| [**ITTTSTerminalEvent**](https://msdn.microsoft.com/en-us/library/ms733276(v=VS.85).aspx)           | Retrieves the description of text-to-speech (TTS) terminal events.                                                                          |



 



| Interface                                                                                             | Description                                                                                      |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**ITPluggableTerminalEventSink**](https://msdn.microsoft.com/en-us/library/ms731414(v=VS.85).aspx)                         | Notifies client applications about changes in a pluggable terminal.                              |
| [**ITPluggableTerminalEventSinkRegistration**](https://msdn.microsoft.com/en-us/library/ms731415(v=VS.85).aspx) | Registers and unregisters a client application for notification about pluggable terminal events. |



 

 

 



