---
title: Dealing with Loss of Connectivity
description: Dealing with Loss of Connectivity
ms.assetid: a90fcb5a-773e-4c21-bf6c-c3519ec13a09
ms.topic: article
ms.date: 05/31/2018
---

# Dealing with Loss of Connectivity

After an RPC call completes the connection is not closed; it is marked as free. As such, the server can go down or network connectivity can be lost during or between calls, while a connection is sitting in the pool. As a matter of policy, the RPC run time re-attempts those calls only if the following two conditions are met:

-   The server cannot possibly execute the call, or the call is idempotent.
-   The client can implement retries in a performance-efficient manner.

The following paragraphs expand and clarify the two conditions.

An idempotent call is a call that can be executed more than once on the server without undesirable side effects. For example, having an RPC call that queries the balance in the bank for a given account is idempotent. If this call is executed twice due to loss of connectivity, no harm is done. Another example of an idempotent call is changing the address of a customer in a database. Executing twice is fine, since the second execution simply replaces the already-current address with the same address. An operation like "subtract fifty dollars from account xyz" is not idempotent. Loss of network connectivity should not result in multiple executions of such a call.

To be safe, the RPC run time treats all calls as non-idempotent. The \[idempotent\] attribute is not supported for [**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp), and is ignored. As such, the first condition in the preceding list is reduced to *the server that cannot possibly execute the call*.

In many cases the RPC run time is unable to conclusively determine the call was not already executed on the server. In such cases, the client will not retry executing the call.

The following examples illustrate when the RPC run time does or does not retry a call:

-   A server is rebooted.

    A simple, no-security RPC call is made on an interface on which no previous call has been made after the reboot. Since no calls were made on this interface, the RPC run time first attempts to negotiate use of the interface. It sends a packet using a connection in the pool. Since the server was rebooted, and the connection is no longer valid, it returns an error. Since the client side RPC run time has not yet started sending the data for the actual call, the client determines that the server could not possibly have executed on those data. Therefore, it closes the connection and looks for another connection in the pool. If it cannot find a connection, it opens a new connection and tries to negotiate use of the interface again. If this succeeds, the call is made (that is, a retry is made, because the failure was detected before the call was started).

-   An RPC call with privacy-level security (encryption) is made on a connection with an already-negotiated security context.

    To ensure efficient performance, the RPC run time encrypts the marshaled packet inline (over the clear text data). If the attempt to send the data fails, the RPC run time cannot retry the call, since the clear text data have been overwritten with the encrypted data, and it cannot re-encrypt the data with a new security context. Therefore, no retry is made.

-   The sending of a non-first fragment fails.

    Retry is not made, since the RPC run time may choose to discard the contents of the first fragment once it is complete, and has no way to retry sending the first fragment.

-   The RPC request is sent.

    The server aborts the connection. No retry is attempted, since RPC cannot discern whether the server received the call and started executing it.

If the server uses a dynamic endpoint, RPC will not re-resolve the endpoint during retries. This means that if a server is brought down and comes back up, it may reside on a different endpoint, and RPC will not transparently re-resolve the endpoint when a call is retried. To force re-resolving of the endpoint, the RPC client should calling [**RpcBindingReset**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingreset) before it retries a call.

In many of these cases, if an RPC client can determine whether a call is idempotent, or if it keeps data that RPC discards, it may choose to build a retry mechanism on top of RPC.

> [!Note]  
> If the server is a cluster, and the different nodes of the cluster run different versions of the server software, an RPC retry may land the call on a different node of the cluster in the case of failover, and potentially on a different version of the server. In such deployment scenarios, make sure the client does not rely on a particular version of the server software to execute a given call. If it does, the client should build a mechanism on top of RPC that detects and handles such conditions.

 

 

 