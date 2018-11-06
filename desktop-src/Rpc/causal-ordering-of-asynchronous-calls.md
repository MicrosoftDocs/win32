---
title: Causal Ordering of Asynchronous Calls
description: In an asynchronous RPC application, it is possible for a client thread to make a second asynchronous call on a binding handle before an earlier call made on that handle has completed.
ms.assetid: 69beb3a4-39ae-4e3f-bb7d-31519278334d
ms.topic: article
ms.date: 05/31/2018
---

# Causal Ordering of Asynchronous Calls

In an asynchronous RPC application, it is possible for a client thread to make a second asynchronous call on a binding handle before an earlier call made on that handle has completed. The RPC run-time library handles this situation as follows:

-   The asynchronous RPC mechanism guarantees that asynchronous calls made on the same binding handle, on the same thread, at the same security level, are dispatched in the order they were made. Actual execution of the calls may occur out of order.
-   As with synchronous calls, asynchronous remote procedure calls from different client threads execute simultaneously.
-   If an asynchronous call from a client application is followed by one or more synchronous calls, the asynchronous call can execute while the synchronous calls are executing. Regardless of the status of the asynchronous call, the synchronous calls are executed in the order in which they are received by the server.
-   If a client application selects noncausal ordering for a particular binding handle, it disables serialization for that handle. Applications enable noncausal ordering by calling [**RpcBindingSetOption**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetoption) with the *Option* parameter set to RPC\_C\_OPT\_BINDING\_NONCAUSAL and the *OptionValue* parameter set to **TRUE**. For details, see [Binding Option Constants](binding-option-constants.md).

 

 




