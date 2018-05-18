---
title: Using WSAIoctl(SIO\_SET\_QOS) During RSVP Sessions
description: The use of WSAIoctl(SIO\_SET\_QOS) is often unnecessary; the use of connection-oriented Windows Sockets function calls (such as the WSAConnect function) is generally sufficient for providing the RSVP SP (and therefore RSVP) with requisite QOS parameters.
ms.assetid: '696543b1-cf25-4a6e-8c26-5f68c65bc36a'
keywords: ["Quality of Service QOS , tasks, using WSAIoctl"]
---

# Using WSAIoctl(SIO\_SET\_QOS) During RSVP Sessions

The use of WSAIoctl(SIO\_SET\_QOS) is often unnecessary; the use of connection-oriented Windows Sockets function calls (such as the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function) is generally sufficient for providing the RSVP SP (and therefore RSVP) with requisite QOS parameters.

One exception is when a UDP application receives from multiple senders, in which case the **WSAIoctl**(SIO\_SET\_QOS) function/opcode pair must be used to specify QOS parameters to avoid limiting the socket to receive traffic from a single sender (as the use of a connection-oriented function call such as [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) would do). This is a limitation of Windows Sockets 2.

Another exception is when a UDP transmit uses the [**sendto**](https://msdn.microsoft.com/library/windows/desktop/ms740148) function to transmit data to one or more receivers through an unconnected socket (Microsoft NetMeeting version 2.1 is an example of such an application). In this circumstance, the sending application must do the following in order to invoke QOS provisioning:

-   Supply the RSVP SP with one or more appropriate SendingFlowspec(s) by issuing one or more SIO\_SET\_QOS IOCTLs.
-   Provide the RSVP SP with the destination address by issuing a [**QOS\_DESTADDR**](qos-destaddr.md) object in the [ProviderSpecific](the-providerspecific-buffer.md) buffer.

The **WSAIoctl**(SIO\_SET\_QOS) function/opcode pair is also useful for modifying QOS parameters subsequent to the establishment of the connection with a connection-oriented function call. This functionality also enables an application to separate the specification of QOS parameters from the determination of local and peer addresses implicit in making a connection-oriented function call.

 

 




