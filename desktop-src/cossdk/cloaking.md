---
description: There are two ingredients in determining the behavior of impersonation the authority the client explicitly grants the server through an impersonation level and the servers ability to mask its own identity when making calls on the clients behalf.
ms.assetid: b34264ff-eb6a-4b99-8c0e-ab6b969a7fb1
title: Cloaking (Component Services)
ms.topic: article
ms.date: 05/31/2018
---

# Cloaking (Component Services)

There are two ingredients in determining the behavior of impersonation: the authority the client explicitly grants the server through an impersonation level and the server's ability to mask its own identity when making calls on the client's behalf. This latter capability is known as *cloaking*. Cloaking has to do with the security identity under which the server makes calls.

When the server impersonates the client, it has direct access to the client's security credentials. In a very local sense, the server thread takes on the identity of the client. But when the server makes calls outside of its process, the client identity will not necessarily be projected as the identity under which the call is made.

When cloaking is enabled, calls made by the server impersonating the client can be made under the client's identity. When cloaking is disabled, calls by the server will be made under the server's identity.

Moreover, there are two forms of cloaking, *static cloaking* and *dynamic cloaking*, which can be described as follows:

-   Impersonation with static cloaking. The original client identity (realized as the server thread token) can be presented once to a downstream server on a call using [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket), setting the original client identity once on the proxy, and that thread token will be used on subsequent method calls.
-   Impersonation with dynamic cloaking. The original client identity is discovered as the server thread token on each method call to the downstream server. In effect, the identity that is presented can be determined dynamically. The overhead required to do this can be considerably more expensive.

For COM+ applications, the default configuration is for dynamic cloaking capability. This can be changed programmatically and administratively. While dynamic cloaking can have performance overhead, it provides the flexibility that is usually required by circumstances that necessitate using impersonation in the first place.

For more detail regarding cloaking and precise descriptions of possible behaviors, see [Cloaking](/windows/desktop/com/cloaking) in the COM documentation.

## Related topics

<dl> <dt>

[Client Impersonation and Delegation](client-impersonation-and-delegation.md)
</dt> <dt>

[Client-Side Requirements for Impersonation](client-side-requirements-for-impersonation.md)
</dt> <dt>

[Server-Side Requirements for Impersonation](server-side-requirements-for-impersonation.md)
</dt> </dl>

 

 
