---
title: Choosing Security QOS Options
description: The security QOS options are passed as part of the SecurityQOS parameter given to the RpcBindingSetAuthInfoEx function. Use the following best practices.
ms.assetid: 43befe3d-079a-4389-a1ff-6bda90935769
ms.topic: article
ms.date: 05/31/2018
---

# Choosing Security QOS Options

The security QOS options are passed as part of the *SecurityQOS* parameter given to the [**RpcBindingSetAuthInfoEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) function. Use the following best practices.

## Use Mutual Authentication

True mutual authentication is available only for certain security providers: Negotiate (when it negotiates Kerberos), Kerberos, and Schannel. NTLM does not support mutual authentication. Using mutual authentication requires that a well formed server principal name be provided. Many developers use the following faulty security practice: The server is called to ask for its principal name ([**RpcMgmtInqServerPrincName**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtinqserverprincname)), and then they blindly ask for mutual authentication using that principal name. This approach breaks the whole idea of mutual authentication; the idea of mutual authentication is that only certain servers are called because they are trusted to parse and handle your data. Using the faulty security practice just described, developers give their data to anyone smart enough to return their name.

As an example, if the client software should call only a server running under Joe, Pete, or Alice's accounts, the [**RpcMgmtInqServerPrincName**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtinqserverprincname) function should be called, and the name sent back should be checked. If it is Joe, Pete or Alice, mutual authentication should be requested using their server principal name. This ensures both halves of the conversation go to the same principal.

If client software should call a service running under Joe's account only, directly compose Joe's server principal name and make the call. If the server is not Joe, the call will simply fail.

Many times, services run as Windows system services, which means they run under the machine account. Mutual authentication and creation of a server principal name is still recommended.

## Use the Lowest ImpersonationType that Allows the Call to Go Through

This Best Practice is fairly self explanatory. Even if mutual authentication is used, do not give the server more rights than necessary; a legitimate server may have been compromised, and even though the data you send falls into the wrong hands in such cases, at least the server will not be able to access other data on the network on your behalf. Some servers will reject a call that does not have sufficient information to determine, and possibly impersonate, the caller. Also, be aware that some protocol sequences support transport level security ([**ncacn\_np**](/windows/desktop/Midl/ncacn-np) and [**ncalrpc**](/windows/desktop/Midl/ncalrpc)). In such cases, the server can always impersonate you if you specify a sufficiently high impersonation level through the *NetworkOptions* parameter when you create the binding handle.

Finally, some security providers or transports may transparently bump ImpersonationType to a higher level than that specified. When developing a program, make sure you try to make calls with the intended ImpersonationType and check whether you are getting higher ImpersonationType on the server.

 

 