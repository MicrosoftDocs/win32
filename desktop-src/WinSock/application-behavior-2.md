---
description: Another aspect of application development to consider is the difference in behavior between local, or intracomputer operations, and behavior when operations take place between two networked computers.
ms.assetid: e6f48446-948c-458c-8ecf-04ffb249c8a4
title: Application Behavior
ms.topic: article
ms.date: 05/31/2018
---

# Application Behavior

Another aspect of application development to consider is the difference in behavior between local, or intracomputer operations, and behavior when operations take place between two networked computers. There are application behaviors that may work acceptably well on a local computer, but when run across a network, cause significant performance degradation and resource consumption. The following application behaviors should be avoided when developing Windows Sockets applications.

## Behaviors to Avoid

-   Chatty Applications.

    Some applications perform many small transactions. When combined with the network overhead associated with each such transaction, the effect is multiplied. In networking, small transactions can consume as many resources and as much time as large transactions. A better approach is to combine many small transactions into a single large transaction.

-   Serialized Transactions.

    Unnecessary serialization of transactions can result in poor performance, and affect scalability. For example, 1000 serialized transactions take at least 1000 \* RTT to complete. A better approach is to run unrelated transactions in parallel. When serialized applications are combined with chatty applications, responsiveness can be seriously hampered.

    > [!Note]  
    > Properly deserializing an application can be difficult. If changing from serialized to parallel proves too difficult, consider combining multiple transactions into fewer large transactions.

     

-   Fat Transactions.

    Applications that send unnecessary bytes on the network are considered fat applications. Applications that send unnecessary bytes on the network increase network overhead, and performance is hampered. This situation often comes from inefficient data structures or inefficient data streaming. To remedy this, optimize data structures, or consider using compression.

The following sections address aspects of application development to consider.

-   [TCP/IP-specific Issues](tcp-ip-specific-issues-2.md)
-   [Recognizing Slow Applications](recognizing-slow-applications-2.md)
-   [Calculating Overhead with Netstat](calculating-overhead-with-netstat-2.md)

## Related topics

<dl> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> </dl>

 

 



