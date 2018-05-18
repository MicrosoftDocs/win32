---
title: UDP Multicast Receivers
description: UDP multicast receivers.
ms.assetid: '894e36cd-89ee-4c86-835c-a8d85ca78231'
---

# UDP Multicast Receivers

UDP multicast receivers are expected to do the following:

-   Create UDP sockets using the [**WSASocket**](https://msdn.microsoft.com/library/windows/desktop/ms742212) function.
-   Indicate that they are multicast receivers in the accompanying ([**WSASocket**](https://msdn.microsoft.com/library/windows/desktop/ms742212)) flags.
-   Call the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function to indicate the multicast session they want to join.

UDP multicast receivers can indicate QOS parameters either through their call to the WSAJoinLeaf function, or through the use of the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair.

The RSVP SP does not send RESV messages for UDP multicast receivers until a multicast session address is unambiguously specified through the use of a [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function call. The RSVP SP does not use parameters with which the socket is bound; since no peer is specified, the RSVP service sends a WF style RESV message only when it has a PATH state from at least one sender.

A UDP unicast receiver may call both the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair and the [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) function in any order. In either case, the RSVP service begins sending RESV messages as soon as there is a sender in the multicast session. However, with multicast receivers the matching PATH state will only be found if a multicast socket has been created with a matching multicast session address.

### Joining Multiple Multicast Groups on a Single Socket

When a UDP multicast receiver joins multiple multicast groups on a single socket, the RSVP SP sends RESV messages for all groups for which there is a matching PATH state. QOS parameters are obtained separately from the ReceivingFlowspec included in individual WSAJoinLeaf function calls made for each multicast group. However, if the **WSAIoctl**(SIO\_SET\_QOS) function/IOCTL pair is called, its specified QOS parameters are applied to all presently joined multicast groups.

 

 




