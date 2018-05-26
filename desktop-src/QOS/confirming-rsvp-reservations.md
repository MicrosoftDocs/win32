---
title: Confirming RSVP Reservations
description: The RSVP\_RESERVE\_INFO object enables a receiving application to be notified of the outcome of an RSVP reservation request.
ms.assetid: dbc6a918-cfdf-40b5-83a4-0695014a90e3
keywords:
- Quality of Service QOS , tasks, confirming reservations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Confirming RSVP Reservations

The [**RSVP\_RESERVE\_INFO**](/windows/previous-versions/Qossp/ns-qossp-_rsvp_reserve_info?branch=master) object enables a receiving application to be notified of the outcome of an RSVP reservation request. RSVP reservation confirmation is achieved by setting the **ConfirmRequest** member of the [**RSVP\_RESERVE\_INFO**](/windows/previous-versions/Qossp/ns-qossp-_rsvp_reserve_info?branch=master) object to a nonzero value. This setting is necessary because RSVP network nodes are not required to automatically generate RSVP CONFIRMATION messages, per the RSVP specification.

Until the presence of a reservation is discerned (senders learn about the presence of a reservation by listening for a WSA\_QOS\_RECEIVERS event), data for the connection will be treated as BEST\_EFFORT traffic, which provides a compelling reason for network programmers to enable RSVP confirmation immediately after a [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559), [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function call, or use of the SIO\_SET\_QOS IOCTL.

Senders can query whether their application is allowed to send by using SIO\_CHK\_QOS. If the binary result of ALLOWED\_TO\_SEND is false (indicating that the application is not allowed to send) and the application chooses to send anyway, the traffic is treated as BEST\_EFFORT. Once the RESV message arrives at the sender (triggering the RSVP confirmation), the RSVP SP on the sending host modifies traffic control service to match the service type in the RESV message, and the traffic is treated as per the service type.

RSVP confirmation requests are only useful for receiving applications.

**Note**  RSVP signaling is not supported on Windows XP, Windows Server 2003, or later versions of Windows.

 

 




