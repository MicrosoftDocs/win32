---
title: Kerberos v5 Protocol
description: Kerberos v5 Protocol
ms.assetid: a53a1edf-f374-4cbf-8050-7cde45284157
ms.topic: article
ms.date: 05/31/2018
---

# Kerberos v5 Protocol

The Kerberos v5 authentication protocol has an authentication service identifier of RPC\_C\_AUTHN\_GSS\_KERBEROS. The Kerberos protocol defines how clients interact with a network authentication service and was standardized by the Internet Engineering Task Force (IETF) in September 1993, in document [RFC 1510](https://www.ietf.org/rfc/rfc1510.txt). Clients obtain tickets from the Kerberos Key Distribution Center (KDC), and they present these tickets to servers when connections are established. Kerberos tickets represent the client's network credentials.

Like NTLM, the Kerberos protocol uses the domain name, user name, and password to represent the client's identity. The initial Kerberos ticket obtained from the KDC when the user logs on is based on an encrypted hash of the user's password. This initial ticket is cached. When the user tries to connect to a server, the Kerberos protocol checks the ticket cache for a valid ticket for that server. If one is not available, the initial ticket for the user is sent to the KDC along with a request for a ticket for the specified server. That session ticket is added to the cache, and it can be used to connect to the same server until the ticket expires.

When a server calls [**CoQueryClientBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryclientblanket) using the Kerberos protocol, the client's domain name and user name are returned. When a server calls [**CoImpersonateClient**](/windows/desktop/api/combaseapi/nf-combaseapi-coimpersonateclient), the client's token is returned. These behaviors are the same as when using NTLM.

The Kerberos protocol works across computer boundaries. The client and server computers must both be in domains, and those domains must have a trust relationship.

The Kerberos protocol requires mutual authentication and supports it remotely. The client must specify the principal name of the server, and the server's identity must match that principal name exactly. If the client specifies **NULL** for the server's principal name or if the principal name doesn't match the server, the call will fail.

With the Kerberos protocol, the impersonation levels identify, impersonate, and delegate can be used. When a server calls [**CoImpersonateClient**](/windows/desktop/api/combaseapi/nf-combaseapi-coimpersonateclient), the token returned is valid off the computer for some time period between 5 minutes and 8 hours. After this time, it can be used on the server computer only. If a server is "run as activator" and the activation is done with the Kerberos protocol, the server's token will expire between 5 minutes and 8 hours after activation.

The Kerberos v5 authentication protocol implemented by WindowsÂ supports [cloaking](cloaking.md).

## Related topics

<dl> <dt>

[COM and Security Packages](com-and-security-packages.md)
</dt> </dl>

 

 




