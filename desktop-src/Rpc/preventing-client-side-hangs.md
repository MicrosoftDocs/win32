---
title: Preventing Client-side Hangs
description: There are two ways your client can hang network connectivity can cause server requests to become lost, or the server itself can crash. With default options, RPC will never time out a call, and your client thread will wait forever for a response.
ms.assetid: 2c201e29-9d9c-48e6-b0b5-68e4b25c3fb7
keywords:
- Remote Procedure Call RPC , best practices, preventing client hangs
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Client-side Hangs

There are two ways your client can hang: network connectivity can cause server requests to become lost, or the server itself can crash. With default options, RPC will never time out a call, and your client thread will wait forever for a response.

There are two methods to prevent this: keep alives and time outs.

## TCP Keep Alives

The client can be set up to periodically ping the server to ensure the server is alive and running. The pings are TCP keep-alives for the [**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp) and [**ncacn\_http**](/windows/desktop/Midl/ncacn-http) protocol sequences, and as such, they are efficient in CPU utilization and network bandwidth. To enable keep alives on a given remote procedure call, use the [**RpcMgmtSetComTimeout**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtsetcomtimeout) function before the call is initiated. This function takes a binding handle and a time out as arguments. Every remote procedure call on this binding handle after **RpcMgmtSetComTimeout** uses the supplied time out.

The Timeout parameter for the [**RpcMgmtSetComTimeout**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtsetcomtimeout) function specifies how long the RPC run time waits before it turns on keep alives. The time out is a value between 0 and 10, where 0 is the minimal time out, and 10 is infinite time out (no time out). The time out itself is not in seconds; the translation from the time-out value supplied to the **RpcMgmtSetComTimeout** function to seconds is done by the RPC run time, and is implementation specific.

The following table provides the translation to seconds for Windows 2000 and Windows XP. Future versions of Windows may change the mapping between the Timeout parameter and the time-out value in seconds:

| Timeout parameter                       | Actual time out in seconds |
|-----------------------------------------|----------------------------|
| 0 (RPC\_C\_BINDING\_MIN\_TIMEOUT)       | 120                        |
| 1                                       | 240                        |
| 2                                       | 360                        |
| 3                                       | 480                        |
| 4                                       | 600                        |
| 5 (RPC\_C\_BINDING\_DEFAULT\_TIMEOUT)   | 720                        |
| 6                                       | 840                        |
| 7                                       | 960                        |
| 8                                       | 1080                       |
| 9 (RPC\_C\_BINDING\_MAX\_TIMEOUT)       | 1200                       |
| 10 (RPC\_C\_BINDING\_INFINITE\_TIMEOUT) | Infinite time out          |



 

Once the keep alives are turned on, the client sends one keep alive packet every second. If there is no acknowledgment from the server for three or more keep alives, the client declares the connection dead and fails the remote procedure call. If the server sends a response within the specified time out, keep alives will not be turned on. If the server responds to keep alives, but does not respond to the remote procedure call, the client continues sending keep alives. Once the server responds to the RPC call, the keep alives are turned off. For Windows 2000, keep alives are turned on only for synchronous RPC calls. For Windows XP, keep alives are turned on for asynchronous RPC calls as well.

It is tempting to set keep alives to the lowest value to ensure the client application responds to network problems in a timely fashion. Careful consideration should be given to such temptation, and scrutiny applied to whether an aggressive value is warranted. A server that temporarily loses connectivity may find itself flooded with keep alives from numerous clients once connectivity is restored. In addition, long computational tasks can take more than two minutes, and the server may find itself spending more CPU time answering keep alives than performing useful work. Therefore, keep alives should be used with moderation. If the client cannot tolerate its thread being tied up for long periods, asynchronous RPC should be considered.

Other protocol sequences may implement different mechanisms for detecting unresponsive servers, depending on which transport is used. The [**ncalrpc**](/windows/desktop/Midl/ncalrpc) transport does not use keep alives. Since all communications in **ncalrpc** are local, if the server becomes unresponsive while a call is in progress, the RPC run time on the client immediately fails the call.

## Call Time Outs

TCP keep alives are fine if network connectivity is lost, or if the server crashes. But if the server deadlocks in user mode, TCP keep alives return successfully but the call will never return. To deal with this scenario, a new run-time option was added for Windows XP: RPC\_C\_OPT\_CALL\_TIMEOUT. This option instructs the RPC run time to set up a timer each time it sends a request to the server. If the timer expires, the call is automatically canceled and completes with RPC\_S\_CALL\_CANCELLED. As long as the server responds within the specified time limit, the client will not cancel the call. This means a multifragment call may take more than the time-out period to complete, as each response from the server is received within the time-out period, even though the time period for all responses to arrive was more than the time-out period.

Also, when a call is canceled the server is not notified of the cancellation. The server, therefore, will likely execute the call at some point, and the client will simply ignore the response from the server.

The most dangerous pitfall with call time outs is establishing a short time out and retrying the call on the same server. The following scenario illustrates the dangers of this approach:

Imagine a server that operates near capacity. It has a number of clients with very short time outs, such as five seconds. A temporary loss of network connectivity or congestion at a router causes a lapse in server replies for a few seconds. On Ethernet networks, this situation can easily be caused by a burst of activity on a link that the server shares with another machine. The server does not manage to send all replies before the five-second time out. The clients get their calls canceled, and immediately retry. The server is not aware the calls are retries, and executes them as well. Thus, instead of executing its normal workload of calls, it executes 30-50% more calls, depending on how many clients timed out. If this exceeds its capacity, and the server cannot respond to all clients within five seconds, another round of calls are sent to the server. The clients keep reissuing the same calls, and since the server is overloaded processing previous calls, it is unable to respond within the time out. Once it responds, the clients have hit the time out, issued a new call, and discarded the answer. In a worst case scenario, the server will not recover until reboot, and depending on client access pattern, may not recover until a sufficient number of clients are stopped.

> [!Note]  
> Call time outs work only on the [**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp) and [**ncacn\_http**](/windows/desktop/Midl/ncacn-http) protocol sequences.

 

 

 