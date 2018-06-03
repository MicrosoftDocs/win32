---
title: Using the RSVP\_RESERVE\_INFO Object
description: The RSVP\_RESERVE\_INFO object enables application developers to specify granular QOS parameters directly to RSVP, providing a mechanism for fine-tuning RSVP reservations.
ms.assetid: 9aa492ec-eec3-4dd6-bac2-5b1da9e95605
keywords:
- Quality of Service QOS , tasks, using the RSVP_RESERVE_INFO object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the RSVP\_RESERVE\_INFO Object

The [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) object enables application developers to specify granular QOS parameters directly to RSVP, providing a mechanism for fine-tuning RSVP reservations. To implement the object, you must pass a filled **RSVP\_RESERVE\_INFO** object to the RSVP SP using the [ProviderSpecific](the-providerspecific-buffer.md) buffer. The following members can be fine-tuned with the **RSVP\_RESERVE\_INFO** object:

-   RSVP Filter Style
-   RESV Confirmation Request
-   Policy Objects
-   List of flow descriptors

 

 




