---
title: Using the ProviderSpecific Buffer
description: Most application developers will find that the RSVP SP and its functions provide all the necessary programmatic access to QOS parameters and settings.
ms.assetid: 4282401e-f7a1-4e3f-a532-7d7c36f8d443
keywords:
- Quality of Service QOS , described, ProviderSpecific buffer
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the ProviderSpecific Buffer

Most application developers will find that the RSVP SP and its functions provide all the necessary programmatic access to QOS parameters and settings. However, some applications may find it necessary to provide information or parameters that are not available through the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure. The ProviderSpecific buffer enables application developers to provide special QOS information, such as RSVP style, Resv confirmation request, or traffic control parameters and settings.

The ProviderSpecific buffer is a member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure, and is of type [**WSABUF**](https://msdn.microsoft.com/library/windows/desktop/ms741542).

 

 




