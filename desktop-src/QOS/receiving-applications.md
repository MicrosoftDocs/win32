---
title: Receiving Applications
description: Information that the receiving application must provide for the RSVP SP to invoke RSVP processing and signaling.
ms.assetid: 'd3b8c225-8b2d-46a1-9f5e-f4c15bb27a83'
---

# Receiving Applications

For the RSVP SP to invoke RSVP processing and signaling, the receiving application is required to provide the following information:

-   QOS parameters, through the use of the ReceivingFlowspec member of the [**QOS**](qos.md) structure. Receiving applications generally provide such QOS parameters in a call to the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) or [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628) functions, or in a call to the WSAIoctl(SIO\_SET\_QOS) function/opcode pair.

For receiving applications, the RSVP SP must create a session object, and in certain cases must create a filterspec object (filterspec selects a subset of the senders by specifying their address) for placement into its RESV messages. These objects are generally matched to the PATH state (which itself is derived from corresponding PATH messages). In order to limit matching of the PATH state, the RSVP SP needs the following information:

-   Peer address or addresses (the source address). This enables RSVP to limit RSVP sessions for which RESV messages are sent.
-   Local address. The RSVP SP uses the local address to match received PATH messages and to select the interface on which to send out the RESV message.

Transmission of RESV messages begins as soon as the RSVP service has sufficient information.

Details of each of these receiver types are outlined individually in the following reference pages:

-   [UDP unicast receivers](udp-unicast-receivers.md)
-   [UDP multicast receivers](udp-multicast-receivers.md)
-   [TCP unicast receivers](tcp-unicast-receivers.md)

 

 




