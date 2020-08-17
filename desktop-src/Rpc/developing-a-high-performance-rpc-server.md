---
title: Developing a High Performance RPC Server
description: The information in this section applies to remote protocol sequences ncacn\_ip\_tcp, ncacn\_http, ncacn\_np, and to Windows 2000 and Windows XP.
ms.assetid: 7b4239af-951b-4d1b-8ac3-224279f6929e
keywords:
- Remote Procedure Call RPC , best practices, developing a high performance server
ms.topic: article
ms.date: 05/31/2018
---

# Developing a High Performance RPC Server

The information in this section applies to remote protocol sequences: [**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp), [**ncacn\_http**](/windows/desktop/Midl/ncacn-http), [**ncacn\_np**](/windows/desktop/Midl/ncacn-np), and to Windows 2000 and Windows XP.

This section addresses three primary aspects of RPC server performance:

-   [Network Latency and Throughput](network-latency-and-throughput.md)
-   [Scalability](scalability.md)
-   [Miscellaneous RPC Performance Tips](miscellaneous-rpc-performance-tips.md)

Code path length is another primary performance consideration for RPC. Code path length is generally well understood, and since literature and tools are widely available on that topic, this article does not address it.

An important and established general performance rule to remember while considering RPC performance is this: find the bottleneck in the system, and work to resolve that. The gating bottleneck may not be the RPC programming, and if that is the case, performance tuning in RPC will not result in enhanced performance until that bottleneck is addressed. For example, a system plagued by resource contention does not need to make more efficient use of the network.

If your system is deployed in various environments, it is a good idea to make sure all aspects of it are well tuned, as different environments can produce varied performance bottlenecks.

 

 