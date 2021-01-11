---
description: TCP/IP has characteristics that enable the protocol to operate as its standardized implementation requirements dictate.
ms.assetid: 6e9b3878-85f0-4572-9c00-a2e7647286ff
title: TCP/IP Characteristics
ms.topic: article
ms.date: 05/31/2018
---

# TCP/IP Characteristics

TCP/IP has characteristics that enable the protocol to operate as its standardized implementation requirements dictate. These characteristics can combine with development choices that result in poor performance. The impact these TCP/IP characteristics have on an application depend on whether the application is transactional or streaming.

Transactional applications are affected by the overhead required for connection establishment and termination. For example, each time a connection is established on an Ethernet network, three packets of approximately 60 bytes each must be sent, and approximately one RTT is required for the exchange. When termination of a connection occurs, four packets are exchanged. This is for each connection; an application that opens and closes connections often incurs this overhead on each occurrence.

Another aspect of TCP/IP is *slow-start*, which takes place whenever a connection is established. Slow-start is an artificial limit on the number of data segments that can be sent before acknowledgment of those segments is received. Slow-start is designed to limit network congestion. When a connection over Ethernet is established, regardless of the receiver's window size, a 4 KB transmission can take up to 3-4 RTT due to slow-start.

A TCP/IP optimization called the Nagle Algorithm can also limit data transfer speed on a connection. The Nagle Algorithm is designed to reduce protocol overhead for applications that send small amounts of data, such as Telnet, which sends a single character at a time. Rather than immediately send a packet with lots of header and little data, the stack waits for more data from the application, or an acknowledgment, before proceeding.

Delayed acknowledgments, commonly referred to as *delayed ACK*, are also designed into TCP/IP to enable more efficient piggybacking of acknowledgments when return data is forthcoming from the receiving side application. Unfortunately, if this data is not forthcoming and the sending side is waiting for an acknowledgment, delays of approximately 200 milliseconds per send can occur.

When a TCP connection is closed, connection resources at the node that initiated the close are put into a wait state, called TIME-WAIT, to guard against data corruption if duplicate packets linger in the network. This ensures both ends are finished with the connection. This can cause depletion of resources required per-connection, such as RAM and ports, when applications open and close connections frequently.

Besides being affected by delayed ACK and other congestion avoidance schemes, streaming applications can also be affected by a too-small default receive window size on the receiving end.

## Related topics

<dl> <dt>

[Application Behavior](application-behavior-2.md)
</dt> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> <dt>

[Nagle Algorithm](https://msdn.microsoft.com/library/ms817942.aspx)
</dt> </dl>

 

 



