---
description: The event (notification) interfaces allow a TAPI 3 application to respond to asynchronous events.
ms.assetid: 27fd91e8-b628-49ee-af4e-9aec0afa5449
title: Event Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Event Interfaces

The event (notification) interfaces allow a TAPI 3 application to respond to asynchronous events.

You must call the [**ITTAPI::put\_EventFilter**](/windows/win32/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter) method and set an event filter mask to enable reception of request events. If you do not call **ITTAPI::put\_EventFilter**, your application will not receive any events.

Please see the [Events](./asynchronous-spontaneous-events.md) overview for a description of how an application ensures reception of notifications. See the individual interfaces listed in the following table for more information about setting a filter mask for individual event types.



| Interface                                                           | Description                                                                                                                                 |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITAddressEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itaddressevent)                   | Retrieves the description of address events.                                                                                                |
| [**ITASRTerminalEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itasrterminalevent)           | Retrieves the description of Automatic Speech Recognition terminal events.                                                                  |
| [**ITCallHubEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itcallhubevent)                   | Retrieves the description of CallHub events.                                                                                                |
| [**ITCallInfoChangeEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itcallinfochangeevent)     | Retrieves the description of call information change events.                                                                                |
| [**ITCallMediaEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itcallmediaevent)               | Retrieves the description of call media events.                                                                                             |
| [**ITCallNotificationEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itcallnotificationevent) | Retrieves the description of call notification events.                                                                                      |
| [**ITCallStateEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itcallstateevent)               | Retrieves the description of call state events.                                                                                             |
| [**ITDigitDetectionEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itdigitdetectionevent)     | Retrieves information about DTMF digit events during a call.                                                                                |
| [**ITDigitGenerationEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itdigitgenerationevent)   | Retrieves information about calls that require the generation of DTMF digits.                                                               |
| [**ITDigitsGatheredEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itdigitsgatheredevent)     | Retrieves data related to an application's digit-gathering request.                                                                         |
| [**ITFileTerminalEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itfileterminalevent)         | Retrieves the description of file terminal events.                                                                                          |
| [**ITParticipantEvent**](./itparticipantevent.md)           | Retrieves the description of conference participant events.                                                                                 |
| [**ITPhoneEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itphoneevent)                       | Retrieves the description of phone events.                                                                                                  |
| [**ITQOSEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itqosevent)                           | Retrieves the description of quality of service (QOS) events.                                                                               |
| [**ITQueueEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itqueueevent)                       | Retrieves the description of Automatic Call Distribution (ACD) queue events.                                                                |
| [**ITRequestEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itrequestevent)                   | Retrieves the description of [Assisted Telephony](./assisted-telephony-overview.md) request events.                                 |
| [**ITTAPIObjectEvent**](/windows/win32/api/tapi3if/nn-tapi3if-ittapiobjectevent)             | Retrieves the description of TAPI object events.                                                                                            |
| [**ITTAPIObjectEvent2**](/windows/win32/api/tapi3if/nn-tapi3if-ittapiobjectevent2)           | Extends [**ITTAPIObjectEvent**](/windows/win32/api/tapi3if/nn-tapi3if-ittapiobjectevent); retrieves a pointer to the phone object that caused the TAPI object event. |
| [**ITToneDetectionEvent**](/windows/win32/api/tapi3if/nn-tapi3if-ittonedetectionevent)       | Retrieves information about a tone detection event.                                                                                         |
| [**ITToneTerminalEvent**](/windows/win32/api/tapi3if/nn-tapi3if-ittoneterminalevent)         | Retrieves the description of tone terminal events.                                                                                          |
| [**ITTTSTerminalEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itttsterminalevent)           | Retrieves the description of text-to-speech (TTS) terminal events.                                                                          |



 



| Interface                                                                                             | Description                                                                                      |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**ITPluggableTerminalEventSink**](/windows/win32/api/tapi3/nn-tapi3-itpluggableterminaleventsink)                         | Notifies client applications about changes in a pluggable terminal.                              |
| [**ITPluggableTerminalEventSinkRegistration**](/windows/win32/api/tapi3/nn-tapi3-itpluggableterminaleventsinkregistration) | Registers and unregisters a client application for notification about pluggable terminal events. |



 

 

 
