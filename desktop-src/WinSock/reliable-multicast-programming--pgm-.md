---
description: This section describes the Pragmatic General Multicast (PGM) multicast protocol implementation in Windows, often referred to as reliable multicast. Reliable multicast is implemented through Windows Sockets in Windows Server 2003 and later.
ms.assetid: 81c203ed-739f-4a06-99a1-9a99c6164edc
title: Reliable Multicast Programming (PGM)
ms.topic: article
ms.date: 05/31/2018
---

# Reliable Multicast Programming (PGM)

This section describes the Pragmatic General Multicast (PGM) multicast protocol implementation in Windows, often referred to as reliable multicast. Reliable multicast is implemented through Windows Sockets in Windows Server 2003 and later.

**Windows XP:** PGM is only supported when Microsoft Message Queuing (MSMQ) 3.0 is installed.

PGM is a reliable and scalable multicast protocol that enables receivers to detect loss, request retransmission of lost data, or notify an application of unrecoverable loss. PGM is a receiver-reliable protocol, which means the receiver is responsible for ensuring all data is received, absolving the sender of reception responsibility.

PGM is appropriate for applications that require duplicate-free multicast data delivery from multiple sources to multiple receivers. PGM does not support acknowledged delivery, nor does it guarantee ordering of packets from multiple senders.

For more information about PGM, refer to RFC 3208 available at [www.ietf.org](https://www.ietf.org/).

This section describes how to use reliable multicast on Windows. The following topics explain the various aspects of creating a reliable multicast application using Windows Sockets:

-   [PGM Senders and Receivers](pgm-senders-and-receivers.md)
-   [PGM Sender Options](pgm-sender-options.md)
-   [Sending and Receiving PGM Data](sending-and-receiving-pgm-data.md)
-   [Multihoming and PGM](multihoming-and-pgm.md)
-   [PGM Socket Options](pgm-socket-options.md)

 

 



