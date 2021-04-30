---
description: In morphing the Life cell update code, several guidelines for writing high performance network applications have been uncovered.
ms.assetid: 2c5d0610-88b5-437e-acde-214553121380
title: Best Practices for Interactive Applications
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices for Interactive Applications

In morphing the Life cell update code, several guidelines for writing high performance network applications have been uncovered. Some general strategies to apply when writing these types of applications are:

-   Make the data stream as much as possible, rather than going in chunks.
-   Use a few large transactions rather than many small ones. Large transactions can also be efficiently streamed.
-   Recognize that the network is a slow, unreliable resource and develop each application to minimize its reliance on the network.
-   Use a well-architected representation of the data on the network. The data representation should be computer-architecture agnostic, contain no fat, and possibly be compressed.
-   During initialization and shutdown, do not make the user wait for the network to start up or shut down. Network related initialization could take a relatively long time. Separate the noncritical network code.
-   Handle errors as appropriate to their impact. Not all errors are critical. Implement recovery mechanisms and provide nonintrusive user feedback.
-   Use remote procedure calls (RPC) only when appropriate. RPC is synchronous on Windows Me/98 and always results in chatty, fat protocols when used to send small amounts of data.
-   Measure your network overhead using Netstat; you may be surprised at what your measurements reveal.
-   Test the application on a variety of networks, especially slow or loss-prone networks. Wireless LAN networks, modems, and virtual private networks (VPN) over the Internet are good networks for testing.

## Related topics

<dl> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> </dl>

 

 



