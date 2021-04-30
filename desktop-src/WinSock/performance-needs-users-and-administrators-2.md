---
description: Performance needs of users and administrators with Windows Sockets (Winsock) applications.
ms.assetid: 6c4365c6-a406-497b-a313-1faeb3e3b7f5
title: 'Performance Needs: Users and Administrators'
ms.topic: article
ms.date: 05/31/2018
---

# Performance Needs: Users and Administrators

Users judge application performance by their experience:

-   Is the application quick to respond?
-   Is an hourglass icon displayed while background operations are carried out?
-   Does the application launch and close quickly?
-   Are errors handled in an understandable way?

To summarize, users want applications to be fast and predictable.

In contrast, administrators often judge an application's performance on how efficiently it uses network resources. Administrators may ask:

-   Does the application have low overhead and efficient network usage?
-   Are the minimum number of connections used, so my server can service as many users at once as possible?
-   Am I constantly calling helpdesk?

In short, administrators want applications to scale.

## Best Practices for Performance Needs

When developing a Windows Sockets application, these performance requirements translate into useful rules.

-   Have network applications initialize quickly.

    The user interface should not have to wait for network responses. Some tasks can be performed before the network is available, or without the network. If the network is not responding, the user may need the user interface for simple operations, such as closing the application.

-   Do not wait for the network for shutdown.

    Properly written client-server applications handle abortive disconnects gracefully. Do not initiate a potentially lengthy operation, such as synchronizing files or folders with a server, that cannot be interrupted on shutdown. Networks are not consistently responsive, so even small operations could prove time consuming. Provide positive feedback for users, including indications of progress and estimated completion times.

-   Ensure a responsive user interface.

    Application responsiveness helps eliminate unnecessary helpdesk calls. A good guideline for interactive response is 500 milliseconds. Users perceive pauses longer than 500 milliseconds as a lag in performance. Applications should be responsive enough to provide the user with confidence about the application.

-   Scrutinize network errors.

    Not all network errors are critical. For example, an application that has received or posted all of its data can likely ignore errors when closing the connection. Do not assume the network or the user is available; either handle errors without user intervention, or ignore them if errors are noncritical.

-   An application should define its own reasonable time outs.

    For example, a Windows Sockets connect() request may block under some conditions for as much as 21 seconds. Applications may need to introduce their own time outs as appropriate for their users.

-   Minimize protocol overhead.

    Conserving network bandwidth is partially about minimizing the protocol overhead incurred by your application. It is also about eliminating unnecessary network traffic. Protocols with a lower header overhead can be used to transfer application data. For example, when sending smaller amounts of noncritical or repeatable data, use UDP as opposed to TCP to reduce the overhead associated with connection establishment and maintenance. If the same data must be sent to multiple recipients, consider multicast. Be aware that UDP applications are not flow-controlled—pushing beyond the available bandwidth can cause catastrophic network failure. The Netstat utility can be used with its **-e** and **-s** options to display statistics for various protocols.

-   Conserve system resources.

    System resources can be consumed quickly if proper restraint is not used. For example, sockets and TCP connections consume resources. Do not use several TCP connections per client where one will serve the application's purpose.

For transactional applications, good user experience and low network utilization are not conflicting goals. The network is a bottleneck. Network-intensive applications spend more time waiting, and well written network applications are designed to minimize unnecessary wait time, both for the user interface and for network transmissions.

## Related topics

<dl> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> <dt>

[Performance Dimensions](performance-dimensions-2.md)
</dt> </dl>

 

 



