---
title: Service Types
description: Service types enable an application to specify service quality requirements for a QOS-enabled connection.
ms.assetid: 895efcac-1b59-4f4c-a180-df26222ad212
keywords:
- Quality of Service QOS ,described,service types
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service Types

Service types enable an application to specify service quality requirements for a QOS-enabled connection. The availability of different service types enables the RSVP SP to categorize the quality of service required by the application, and thereby decide the type of requests it (the RSVP SP) should make to complementary components on behalf of the requesting application.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

There are four primary service types included in the RSVP SP. Applications must choose which service type is most appropriate for their transmission requirements, based on traffic characteristics, performance requirements, user preferences, or any other criterion that influences how data should be transmitted. Also note that when an application invokes the RSVP SP to initiate quality of service for a given connection, the ServiceType member of the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure (where the service type is specified) for both the SendingFlowspec and ReceivingFlowspec members of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure must be specified.

Specifying either [CONTROLLED LOAD](controlled-load.md) or [GUARANTEED](guaranteed.md) for the ServiceType parameter implicitly invokes QOS service for the corresponding direction of the QOS-enabled connection.

In addition to the primary service types, the RSVP SP provides secondary service types that enable application programmers and the RSVP SP to monitor or modify service provisions under certain circumstances, and on an ongoing basis.

 

 




