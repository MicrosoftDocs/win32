---
title: UDP Unicast Receivers
description: UDP unicast receivers can initiate a QOS-enabled connection by providing QOS parameters to the RSVP SP.
ms.assetid: 60a43a6a-0b22-480a-9b32-a8bb8d4bf34d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UDP Unicast Receivers

UDP unicast receivers can initiate a QOS-enabled connection by providing QOS parameters to the RSVP SP using either of the following methods:

-   A call to the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function
-   A call using the **WSAIoctl**(SIO\_SET\_QOS) function/opcode pair.

## Using WSAConnect

A UDP unicast receiver should use the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function only if it wants to receive from a single sender; using **WSAConnect** causes traffic received from other senders to be discarded. In order to receive traffic from multiple senders using the **WSAConnect** function, a separate socket must be created for each sender. By using the **WSAConnect** function as a UDP unicast receiver, the application provides a peer address and, in doing so, selects a specific sender.

When a UDP unicast receiver uses the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function, the RSVP SP sends RESV messages only when the PATH state exists for the specified sender, and uses the included peer address to compose Fixed Filter style (FF) RESV messages.

Note that using the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function may cause the RSVP SP to cease sending RESV messages that were triggered in a previous call to the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair; this is because PATH state, though it may have existed for some sender, may not have existed for the sender specified in the **WSAConnect** function call.

## Using WSAIoctl(SIO\_SET\_QOS)

A UDP unicast receiver can use the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair to indicate receiving QOS parameters, after which the RSVP SP begins transmitting RESV messages for any matching PATH state. Since the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair does not associate a peer address with the socket (unless the ProviderSpecific buffer is used to specify a particular sender), the socket will match PATH state of any sender in this RSVP session.

When the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair is used by a UDP unicast receiver, the RSVP SP transmits Wildcard Filter (WF) style RESV messages. Note that WF RESV messages are used for unconnected UDP sockets only; connected UDP sockets result in Fixed Filter (FF) style reservations.

## Combining WSAConnect and WSAIoctl(SIO\_SET\_QOS)

A UDP unicast receiver may call both the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair and the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function in any order. In either case, the RSVP service begins sending RESV messages as soon as the indicated QOS parameters match a PATH state.

If the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair is called before the WSAConnect function, the RSVP SP initially sends Wildcard Filter (WF) RESV messages, presuming a matching PATH state. Subsequently (upon calling of the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function, its specified peer, and a matching PATH state) the RSVP SP sends a RESVTEAR message for the WF style reservation followed by Fixed Filter (FF) style RESV messages.

Calling the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair subsequent to a call to the WSAConnect function does not negate the selection of a specific sender. Therefore, while the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair is a useful method of altering RESV messages (such as altering QOS parameters, or terminating RESV messages altogether by indicating BEST\_EFFORT), its use does not cause the RSVP SP to send Wildcard Filter (WF) style RESV messages.

 

 




