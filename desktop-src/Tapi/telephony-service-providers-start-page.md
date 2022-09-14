---
description: A telephony service provider (TSP) is a dynamic-link library (DLL) that supports communications device control through a set of exported service functions.
ms.assetid: 276c27ac-b6ee-42a7-8327-33dfd87e69bd
title: Telephony Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Telephony Service Providers

## Purpose

A telephony service provider (TSP) is a dynamic-link library (DLL) that supports communications device control through a set of exported service functions. A TAPI application uses standardized commands, TAPI passes information to the telephony service provider, and the TSP handles the specific commands that must be exchanged with the device.

A TSP must conform to the Telephony Service Provider Interface (TSPI) to function as a service provider within the Microsoft Telephony environment. TSPI defines the external functions exposed by a telephony service provider supplied with communications equipment.

## Developer audience

You can write TAPI-enabled applications in many languages, including Java, Visual Basic, and C/C++. Previous development experience with telecommunications or other telephony applications is helpful but not necessary.

## Run-time requirements

TSPI enables development of TSPs for all versions of Windows.

## In this section



| Topic                                                                | Description                                                              |
|----------------------------------------------------------------------|--------------------------------------------------------------------------|
| [Overview](about-the-telephony-service-provider-tsp-.md)<br/> | General information about TSPI's architecture and components.<br/> |
| [Reference](tspi-reference.md)<br/>                           | Documentation for the TSPI interfaces.<br/>                        |



 

## Related topics

<dl> <dt>

[Microsoft Telephony Overview](./microsoft-telephony-overview.md)
</dt> <dt>

[Media Service Providers](./media-service-providers-start-page.md)
</dt> <dt>

[TAPI 2.2](./tapi-2-2-start-page.md)
</dt> <dt>

[TAPI 3.1](./tapi-3-1-start-page.md)
</dt> </dl>

 

