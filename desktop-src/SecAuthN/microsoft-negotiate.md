---
description: Microsoft Negotiate is a security support provider that acts as an application layer between Security Support Provider Interface and the other SSPs.
ms.assetid: 3aa7e979-8b55-416d-bed1-28296055d38e
title: Microsoft Negotiate
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Negotiate

Microsoft Negotiate is a [*security support provider*](../secgloss/s-gly.md) (SSP) that acts as an application layer between [*Security Support Provider Interface*](../secgloss/s-gly.md) ([SSPI](sspi.md)) and the other SSPs. When an application calls into SSPI to log on to a network, it can specify an SSP to process the request. If the application specifies Negotiate, Negotiate analyzes the request and picks the best SSP to handle the request based on customer-configured security policy.

Currently, the Negotiate security package selects between [Kerberos](microsoft-kerberos.md) and [NTLM](microsoft-ntlm.md). Negotiate selects Kerberos unless it cannot be used by one of the systems involved in the authentication or the calling application did not provide sufficient information to use Kerberos.

To allow Negotiate to select the [Kerberos](microsoft-kerberos.md) security provider, the client application must provide a [*service principal name*](../secgloss/s-gly.md) (SPN), a user principal name (UPN), or a NetBIOS account name as the target name. Otherwise, Negotiate always selects the [NTLM](microsoft-ntlm.md) security provider.

A server that uses the Negotiate package is able to respond to client applications that specifically select either the [Kerberos](microsoft-kerberos.md) or [NTLM](microsoft-ntlm.md) security provider. However, a client application must know that a server supports the Negotiate package to request authentication using Negotiate. A server that does not support Negotiate cannot always respond to requests from clients that specify Negotiate as the SSP.

## Reasons to Use the Negotiate Package

-   Allows the system to use the strongest (most secure) available protocol.
-   Ensures forward compatibility for your application.
-   Ensures that your application exhibits behavior that is in accordance with the security policy set by the customer.

 

 
