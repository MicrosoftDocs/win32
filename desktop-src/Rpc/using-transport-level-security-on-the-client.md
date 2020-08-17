---
title: Using Transport-Level Security on the Client
description: The client specifies how the server impersonates the client when the client establishes the string binding.
ms.assetid: 0d02b7f2-4dcb-41e8-829c-6942dfdcd4c6
keywords:
- Remote Procedure Call RPC , tasks, using transport-level security on the client
ms.topic: article
ms.date: 05/31/2018
---

# Using Transport-Level Security on the Client

The client specifies how the server impersonates the client when the client establishes the string binding. This QOS information is provided as an endpoint option in the string binding. The client can specify the level of impersonation, dynamic or static tracking, and the effective-only flag.

**To supply quality-of-service information for the server**

1.  The client calls [**RpcStringBindingCompose**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringbindingcompose) to create the component strings, including endpoint options, in the correct string-binding context.
2.  The client calls [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) to obtain a new binding handle and to apply the quality-of-service information for the client.
3.  The client makes remote procedure calls using the handle.

Microsoft RPC supports Windows security features only on [**ncacn\_np**](/windows/desktop/Midl/ncacn-np) and [**ncalrpc**](/windows/desktop/Midl/ncalrpc). Security options for other transports are ignored.

The client can associate the following security parameters to the binding for the named-pipe transport [**ncacn\_np**](/windows/desktop/Midl/ncacn-np) or [**ncalrpc**](/windows/desktop/Midl/ncalrpc):

-   Identification, Impersonation, or Anonymous. Specifies the type of security used. The default is Impersonation.
-   Dynamic or Static. Determines whether security information associated with a thread is a copy of the security information created at the time the remote procedure call is made (static) or a pointer to the security information (dynamic).

    Static security information does not change. The dynamic setting reflects the current security settings, including changes made after the remote procedure call is made. For [**ncacn\_np**](/windows/desktop/Midl/ncacn-np), the default for remote named pipe connections is static, for local named pipe connections the default is dynamic.

-   **TRUE** or **FALSE**. Specifies the value of the effective-only flag. A value of **TRUE** indicates that only token privileges set to on at the time of the call are effective. A value of **FALSE** indicates that all privileges are available and that the application can modify them.

Any combination of these settings can be assigned to the binding, as shown in the following example:

``` syntax
"Security=Identification Dynamic True"
"Security=Anonymous Static True"
"Security=Impersonation Static False"
```

Default security-parameter settings vary according to the transport protocol.

For additional information about the syntax of the endpoint options, see [endpoint](/windows/desktop/Midl/endpoint).

 

 