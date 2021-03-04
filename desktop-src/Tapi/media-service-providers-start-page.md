---
description: A media service provider (MSP) enables an application to control media for a particular transport mechanism.
ms.assetid: f886380f-d970-4511-bf71-fb1eb767e4f4
title: Media Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Media Service Providers

## Purpose

A media service provider (MSP) enables an application to control media for a particular transport mechanism. An MSP is always paired with a Telephony Service Provider (TSP).

The Media Service Provider Interface (MSPI) is a set of interfaces and methods implemented by an MSP to allow an application control over media transport during a communications session. An MSP handles the device-specific and protocol-specific mechanisms required to enact these controls, and communicates with its paired TSP or an application through use of the methods provided in the MSPI.

## Developer audience

Familiarity with COM is required. Development experience with telecommunications or other telephony applications is helpful, but not necessary.

## Run-time requirements

MSPI enables development of media service providers for particular protocols or devices running on Windows Server 2003 operating systems, Windows XP, and Windows 2000.

## In this section



| Topic                                                                       | Description                                                           |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [Overview](about-the-media-service-provider-msp-.md)<br/>            | General information about MSP architecture and components.<br/> |
| [Reference](media-service-provider-interface-mspi-reference.md)<br/> | Documentation for the MSPI interfaces.<br/>                     |



 

## Related topics

<dl> <dt>

[Microsoft Telephony Overview](microsoft-telephony-overview.md)
</dt> <dt>

[TAPI 3.1](tapi-3-1-start-page.md)
</dt> <dt>

[Telephony Service Providers](./telephony-service-providers-start-page.md)
</dt> </dl>

 

