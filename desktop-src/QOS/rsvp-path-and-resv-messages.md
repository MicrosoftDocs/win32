---
title: RSVP PATH and RESV Messages
description: RSVP establishes QOS-enabled connections through the use of PATH and RESV messages.
ms.assetid: dbee8a22-26d1-47e0-b6bb-7a35930e05fc
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RSVP PATH and RESV Messages

RSVP establishes QOS-enabled connections through the use of PATH and RESV messages. A short explanation of each, and how they pertain to Windows 2000 QOS and the RSVP SP is merited. For a thorough explanation and discussion of RSVP PATH and RESV messages, consult IETF RFC 2205.

When a QOS-enabled connection is established and RSVP signaling is triggered (see [Invoking RSVP](invoking-rsvp.md)), the sender and receiver(s) play specific roles in the establishment of an RSVP session:

-   The sender emits PATH messages toward the receiver (or receivers).
-   The receiver waits until the PATH message corresponding to the flow arrives, then issues an RESV message.

The information contained in the PATH and RESV messages is derived from the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structures associated with the **SendingFlowspec** and **ReceivingFlowspec** members of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure.

## Transmission of RSVP PATH and RESV Messages

When a PATH message is received, the RSVP SP creates an RSVP session and associates a PATH state (based on the PATH message) with the RSVP session. The RSVP SP sends RESV messages once it determines that the PATH state exists for a session that matches a socket for which receiving QOS is indicated. In the absence of a received PATH message, the RSVP SP creates an RSVP session using QOS parameters (and thereby, QOS is invoked) on a receive socket. In this latter case, PATH state is not associated with the session until a matching PATH message is received.

The transmission of RESV messages, therefore, may be triggered by the following circumstances:

-   Upon receipt of a PATH message that matches the session associated with a preexisting socket.
-   Upon creation of a socket that matches the session associated with a preexisting PATH state.

## RSVP PATH Message Parameters

RSVP PATH messages derive their RSVP sender Tspec from the SendingFlowspec member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure (the SendingFlowspec member of **QOS** is itself a [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure).

The following table outlines the information required to begin transmission of RSVP PATH messages, and how the information is derived from the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure or other information provided by the sender. The RSVP PATH parameters discussed serve the following purposes:

-   [SenderTspec](tspec-flowspec-and-adspec.md) contains QOS parameters for sent traffic.
-   SenderTemplate contains the sender's address.
-   Session contains the destination of the sent traffic.



| RSVP PATH parameter | Equivalent receiver–based parameters                                                               |
|---------------------|----------------------------------------------------------------------------------------------------|
| SenderTspec         | **SendingFlowspec** member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure.                                    |
| SenderTemplate      | Source IP address/port to which sending socket is bound.                                           |
| Session             | Destination IP address/port and protocol identifier to which the socket is sending (sockaddr\_in). |



 

Note that the RSVP session parameter includes specification of the protocol identifier can be UDP or TCP. The type of socket on which the QOS-enabled connection is being invoked determines the protocol identifier.

## RSVP RESV Message Parameters

RSVP RESV messages derive their RSVP [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) parameters from the ReceivingFlowspec member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure (the **ReceivingFlowspec** member of **QOS** is itself a [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure).

The following table outlines the information required to begin transmission of RSVP RESV messages, and how the information is derived from the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure or other information provided by the receiver. The RSVP RESV parameters discussed serve the following purposes:

-   Flowspec contains desired QOS parameters for traffic to be received.
-   Filterspec contains the source or sources from which QOS-enabled traffic will be received.
-   Session contains the destination of the sent traffic.



| RSVP RESV parameter                                             | Derived from the following Winsock parameter                                                                                                         |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| flowspec                                                        | **ReceivingFlowspec** member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure or the ProviderSpecific buffer.                                                     |
| Filterspec (source(s) from which QOS traffic will be received)1 | Address(es) of peer(s) from which the socket is receiving.                                                                                           |
| Session (destination of sent traffic).                          | Local IP address and port to which the receiving socket is bound (unicast), or multicast session address to which the socket has joined (multicast). |



 

RESV messages can be generated without knowledge of the sender's address. These type of RESV messages are said to be WF style, meaning that they apply to all senders in the session.

The WF reservation style RESV messages do not have any filterspecs, so receivers do not need to supply the sender with an IP address.

 

 




