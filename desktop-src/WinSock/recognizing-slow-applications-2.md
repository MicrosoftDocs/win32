---
description: This guide identifies a slow application as a Microsoft Windows application with impaired performance.
ms.assetid: cacf55d8-ab64-47a4-a55b-59a3c4e3877b
title: Recognizing Slow Applications
ms.topic: article
ms.date: 05/31/2018
---

# Recognizing Slow Applications

This guide identifies a *slow* application as a Microsoft Windows application with impaired performance. A slow application exhibits one or more of the following symptoms:

-   CPU and network utilization are low.

    The computer appears to be waiting on something. Often, the application is waiting on the network.

-   Turning off the Nagle Algorithm through the TCP\_NODELAY socket option increases performance.

    This indicates other problems, and should not be considered a solution. Turning off the Nagle algorithm increases the protocol overhead. Do not use this method as a fix for the broken applications—only as an indication the application needs other work to fix performance issues.

-   The application exhibits high overhead.

    To calculate your applications overhead, determine how much data you intended to transfer in each direction. Then use Netstat and add (for Ethernet) 60 bytes for each packet and 500 bytes for each connection. The best overhead that can be expected for streaming over Ethernet is approximately 6%. For a modem connection, the best overhead is approximately 2%, due to the fact that a PPP link uses header compression. See [Calculating Overhead with Netstat](calculating-overhead-with-netstat-2.md) for more information.

-   Application response slows when the connection has a large RTT.

    Assuming the application is not approaching the link's bandwidth, a large RTT should have little or no effect. A dramatic slowdown with a large RTT is a clear sign of serialized processing and many small transactions.

Every application should be tested in an environment with a large RTT. Doing so reveals most applications that suffer from poor development choices. This testing can be performed in several environments, including a wireless LAN network, a link-delay simulator, or a satellite network.

## Related topics

<dl> <dt>

[Application Behavior](application-behavior-2.md)
</dt> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> <dt>

[Nagle Algorithm](https://msdn.microsoft.com/library/ms817942.aspx)
</dt> </dl>

 

 



