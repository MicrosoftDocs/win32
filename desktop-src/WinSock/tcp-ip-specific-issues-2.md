---
description: Certain programming techniques run into performance issues that are linked to the implementation of TCP/IP.
ms.assetid: 2a63e85e-06fd-4b6f-8351-9866099b9d54
title: TCP/IP-specific Issues
ms.topic: article
ms.date: 05/31/2018
---

# TCP/IP-specific Issues

Certain programming techniques run into performance issues that are linked to the implementation of TCP/IP. Such performance issues do not suggest that TCP/IP is inefficient or a performance bottleneck; rather, these issues are seen when TCP/IP operations are not understood.

The following issues identify common scenarios in which the combination of TCP/IP operation and network application development choices result in poor performance.

-   Connect-heavy Applications.

    Some applications instantiate a new TCP connection for each transaction. TCP connection establishment takes time, contributes extra RTTs, and is subject to slow-start. In addition, the closed connections are subject to TIME-WAIT, which consumes system resources.

    Connect-heavy applications are common largely because they are easy to create; testing and error handling is very simple. Detecting faults on a persistent connection can take considerable code and effort, and therefore is sometimes not completed.

    Remedy this situation by reusing the TCP connection. This may cause serialization over the TCP connection unless the transactions are multiplexed over multiple connections. If this approach is taken, the number of connections should be limited to two, and application-layer framing and advanced error handling are required.

-   Zero-length Send Buffers and Blocking Sends.

    Turning off buffering by using the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function to set the send buffer (SO\_SNDBUF) to zero is similar to turning off disk caching. When setting the send buffer to zero and issuing blocking sends, an application has a fifty percent chance of hitting a 200-millisecond delayed acknowledgment.

    Do not turn off send buffering unless you have considered the impact in all network environments. One exception: streaming data using overlapped I/O should set the send buffer to zero.

-   Send-Send-Receive programming model.

    Structuring an application to perform send-send-receives increases your chances of encountering the Nagle Algorithm, which causes a delay of RTT+200 ms. The Nagle Algorithm may be encountered if the last send is less than the TCP Maximum Segment Size (MSS, the maximum data in a single datagram). MSS can be a very large value (64K in IPv4, and even larger in IPv6), so do not count on a typically small MSS. A better option is to combine the two sends into a single send using the [**WSASend**](/windows/desktop/api/Winsock2/nf-winsock2-wsasend) or **memcpy** function.

-   Large Number of Simultaneous Connections.

    Concurrent connections should not exceed two, except in special purpose applications. Exceeding two concurrent connections results in wasted resources. A good rule is to have up to four short lived connections, or two persistent connections per destination.

## Related topics

<dl> <dt>

[Application Behavior](application-behavior-2.md)
</dt> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> <dt>

[Nagle Algorithm](https://msdn.microsoft.com/library/ms817942.aspx)
</dt> </dl>

 

 



