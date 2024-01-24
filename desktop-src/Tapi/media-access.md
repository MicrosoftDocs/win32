---
description: Media features are different with TAPI 2.2 (TAPI/C) as opposed to TAPI 3 (COM), largely because the COM API has access to media service providers (MSPs).
ms.assetid: 73042eb1-b2d6-4dcb-b40e-f8f3933dcdb0
title: Media Access
ms.topic: article
ms.date: 05/31/2018
---

# Media Access

Media features are different with TAPI 2.2 (TAPI/C) as opposed to TAPI 3 (COM), largely because the COM API has access to media service providers (MSPs). For more information about MSPs, see [About The Media Service Provider (MSP)](./about-the-media-service-provider-msp-.md). For more information about media stream operations, see [Media Control](./device-control.md).

The two most important concepts for an application are the media type (or mode) and the stream. The type is the form in which data is transmitted. For more information and a list of TAPI-defined types, see [LINEMEDIAMODE\_ Constants](linemediamode--constants.md). The media stream is the actual stream of data. An MSP can provide direct access to the stream. TAPI 2.2 applications have some access, but primarily reference other APIs to implement such controls.

These APIs include the Waveform API, the Comm API, and the Media Control Interface (MCI). The Waveform API is used for multimedia programming, the Comm API is the set of communications functions provided by the Platform Software Development Kit (SDK), and the MCI provides a high-level generalized interface for controlling media devices.

For example, for line devices, an application can use TAPI 2.2 to establish a connection to another station. Once the connection is established, the application can then use the Waveform API (or the MCI Waveaudio API) on the associated device to play back (send) and record (receive) audio data over the connection. Similarly, if the connection media stream is from a modem, an application would use the modem configuration extensions of the Communications API to control the media stream.

To provide TAPI 2.2 with media-stream access to either a phone or a call on a line device, the service provider must implement both the Telephony SPI and the appropriate media stream SPI or device-driver interface (DDI). The service provider can support lines and phones simultaneously.

Because these device classes and media stream operations function independently of one another, coordination of their usage must occur at the application level. Multiple applications that share calls and media streams will likely require coordination of their activities at the application level to prevent conflicting usage of TAPI and the media stream API.

TAPI reports changes in the type of media stream (voice, fax, data modem, and so on) to participating applications. This process is sometimes referred to as [*call classification*](c-tapgloss.md). The mechanism used to determine the type of media stream is specific to the service provider. For example, a service provider may filter the media stream for energy or tones that characterize the media type, or it may use distinctive ringing, data exchanged in messages over the network, or knowledge about the caller or called ID to make this determination.

-   [Call Monitoring](call-monitoring.md)
-   [Media Control](/previous-versions/windows/desktop/legacy/ms736578(v=vs.85))
-   [Digit Gathering](digit-gathering.md)
-   [Generating Inband Digits and Tones](generating-inband-digits-and-tones.md)

 

 
