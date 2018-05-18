---
title: Invoking the RSVP SP
description: QOS-enabled connections are unidirectional.
ms.assetid: '1f74359c-1f07-4355-9e1d-9860780a09a5'
---

# Invoking the RSVP SP

QOS-enabled connections are unidirectional. To enable a connection with service guarantees for both sending and receiving from a host, two individual QOS-enabled flows are required. Whether the QOS-enabled flow is for sending or receiving, the initial process of invoking the RSVP SP usually includes the use of one of the following Windows Sockets 2 APIs:

-   [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559)
-   [**WSAJoinLeaf**](https://msdn.microsoft.com/library/windows/desktop/ms741628)
-   [**WSAAccept**](https://msdn.microsoft.com/library/windows/desktop/ms741513)
-   [**WSAIoctl(SIO\_SET\_QOS)**](https://msdn.microsoft.com/library/windows/desktop/ms741621)

Each of these functions invokes the RSVP SP on the application's behalf, and begins the process of establishing Quality of Service between the receiver and sender. Each of these functions includes a parameter that provides the application with the capability of providing QOS-specific parameters. These QOS-specific parameters are provided through the [**QOS**](qos.md) structure, which is included as a parameter of each of the three preceding functions (WSAAccept generally implements the **QOS** structure through the callback function provided in its lpfnCondition parameter).

Whenever an application calls the WSAConnect function, the WSAJoinLeaf function, or the WSAAccept callback function with a non-NULL pointer to the [**QOS**](qos.md) structure, QOS functionality is implicitly invoked. This invocation includes enlistment of any other QOS components' services (such as traffic control or RSVP signaling) by the RSVP SP on behalf of the application.

QOS technology and parameters are unidirectional, enabling different transmission parameters for sender and receiver. Additionally, RSVP semantics are receiver-centric, in that resources are not reserved until the receiver sends out a RESV message. Due to this unidirectional approach, differences exist in the behavior of the receiver and the sender. These differences are outlined in the [Receiving QOS-Enabled Data](receiving-qos-enabled-data.md) and [Sending QOS-Enabled Data](sending-qos-enabled-data.md) sections.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




