---
title: TCP Unicast Receivers
description: TCP receivers are generally the active peer in a TCP connection.
ms.assetid: 'f5f0c195-bbc0-4414-b92d-08125d9c445e'
---

# TCP Unicast Receivers

TCP receivers are generally the active peer in a TCP connection. TCP unicast receivers are therefore expected to initiate a QOS-enabled connection by providing QOS parameters to the RSVP SP using one of the following methods:

-   A call to the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function.
-   A call using the **WSAIoctl**(SIO\_SET\_QOS) function/opcode pair.

The RSVP SP uses the address specified in the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function call to specify the peer sender's address, which enables RSVP to compose its filterspec for Fixed Filter (FF) style RESV messages. The RSVP SP begins RSVP processing.

RSVP will start signaling as soon as the RSVP SP knows the receiving QOS parameters, and those parameters match a PATH state; PATH state only matches if the associated socket's session address matches the bound address and its SenderTemplate matches the peer address.

If the receiving socket is bound using INADDR\_ANY, the bound address cannot be determined until the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function is called. Under this circumstance, RESV messages are delayed until, following connection establishment, the RSVP SP automatically calls the getsockname function to determine local address.

 

 




