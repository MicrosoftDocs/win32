---
title: Using Methods
description: When a client registers with the routing table manager, it can export a set of methods. These methods are used by other clients to obtain client-specific information. Methods enable private communication between clients of the routing table manager.
ms.assetid: 6d984a02-d005-43ad-81c4-968ae9c1a105
ms.topic: reference
ms.date: 05/31/2018
---

# Using Methods

When a client registers with the routing table manager, it can export a set of methods. These methods are used by other clients to obtain client-specific information. Methods enable private communication between clients of the routing table manager.

A client can obtain the list of methods exported by another client. The client calls the [**RtmGetEntityMethods**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetentitymethods) function, supplying the target client's handle.

Each method exported by a client is uniquely identified by its method identifier. Each client can export up to 32 methods. Each method corresponds to a bit set in the **MethodType** member of the [**RTM\_ENTITY\_EXPORT\_METHOD**](/windows/win32/api/rtmv2/nc-rtmv2-_entity_method) structure. To invoke multiple methods, the client should perform a logical OR of the identifiers for those methods. The syntax and semantics of input and output structures for each protocol must be specified when the protocol is implemented.

> [!Note]  
> Method identifier values that correspond to a bit set in the lower half of the **MethodType** member (the lower 16 bits) are reserved by Microsoft.

 

To invoke a second client's method, a client calls the [**RtmInvokeMethod**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtminvokemethod) function. The routing table manager arbitrates all requests to invoke a client's methods. The routing table manager performs two functions when it arbitrates between clients:

-   Preventing the second client from invoking a method for a client that is unregistering.
-   Holding an "invoke" request when methods are blocked, and allowing the request to continue when the methods are unblocked.

If a client must prevent other clients from executing its methods, the client can call [**RtmBlockMethods**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmblockmethods). The routing table manager will not allow a call to [**RtmInvokeMethod**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtminvokemethod) to be processed until the client unblocks its methods again.

Clients typically block methods when making changes to the private data that is exchanged between clients. Blocking methods is an optional action. A client can also use internal locks to prevent other clients from invoking methods.

For sample code that shows how to use these functions, see [Obtain and Call the Exported Methods for a Client](obtain-and-call-the-exported-methods-for-a-client.md).

 

 




