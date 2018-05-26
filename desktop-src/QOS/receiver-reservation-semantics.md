---
title: Receiver Reservation Semantics
description: The process of joining RSVP sessions includes making appropriate function calls particular to the type of RSVP session an application wants to join.
ms.assetid: 4ce61799-c32b-4ac5-b1c9-468786d16eb9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Receiver Reservation Semantics

The process of joining RSVP sessions includes making appropriate function calls particular to the type of RSVP session an application wants to join. Due to their inherent differences, and the difference in the way each handles sockets, unicast (both TCP and UDP) and multicast sessions are best discussed individually. To generalize:

-   Unicast sessions typically include use of the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function.
-   Multicast sessions generally use the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function (and [**sendto**](https://msdn.microsoft.com/library/windows/desktop/ms740148) for multicast senders).
-   Both unicast and multicast can use the **WSAIoctl**(SIO\_SET\_QOS) function/opcode pair.

Each of these common methods for joining RSVP sessions is discussed individually.

 

 




