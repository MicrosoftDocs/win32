---
description: A TAPI 3 media service provider (MSP) allows an application considerable control over the media for a particular transport mechanism.
ms.assetid: 2dd1268f-b31a-443b-a36b-05c1570e7a8a
title: About the Media Service Provider (MSP)
ms.topic: article
ms.date: 05/31/2018
---

# About the Media Service Provider (MSP)

A TAPI 3 media service provider (MSP) allows an application considerable control over the media for a particular transport mechanism. An MSP always exists paired with a Telephony Service Provider (TSP). Just as a TSP is an abstraction layer for call control, the MSP controls media without need for device-specific coding. For an example of MSP/TSP communication, see [TAPI Service Provider Overview](./tapi-service-provider-overview.md).

An MSP enables media control through the use of special terminal, stream, and substream interfaces defined by TAPI. The diagram in [About Call and Media Controls](about-call-and-media-controls.md) illustrates how these interfaces appear to a TAPI 3 application.

In addition, an MSP may implement private [provider-specific interfaces](provider-specific-interfaces.md), which TAPI will aggregate onto the standard objects exposed to an application. For example, the Microsoft IPConf MSP, which is installed with Microsoft Windows 2000, implements the [**ITParticipant**](itparticipant.md) interface, which provides controls for individual members of a conference.

The following topic briefly describes the MSPs that may be installed with a Microsoft operating system. For details on configuration and usage, see the resource kit for the target platform.

Additional third-party media service providers can be written for particular protocols or for physical devices. The [Media Service Provider Interface (MSPI)](media-service-provider-interface-mspi-.md) describes the interfaces that must be implemented to allow an MSP to interact with the components of Microsoft Telephony.

 

 
