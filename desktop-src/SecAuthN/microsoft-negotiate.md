---
description: Microsoft Negotiate is a security support provider that acts as an application layer between Security Support Provider Interface and the other SSPs.
ms.assetid: 3aa7e979-8b55-416d-bed1-28296055d38e
title: Microsoft Negotiate
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Negotiate

Microsoft Negotiate is a [*security support provider*](../secgloss/s-gly.md) (SSP) that acts as an application layer between [*Security Support Provider Interface*](../secgloss/s-gly.md) ([SSPI](sspi.md)) and the other SSPs. When an app calls into SSPI to sign-in a network, it can specify an SSP to process the request. If the app specifies Negotiate, Negotiate analyzes the request and picks the best SSP to handle the request based on customer-configured security policy.

Currently, the Negotiate security package selects between [Kerberos](microsoft-kerberos.md) and [NTLM](microsoft-ntlm.md). Negotiate selects Kerberos unless one of the following conditions applies:

* It can't be used by one of the systems involved in the authentication.
* The calling app didn't provide sufficient information to use Kerberos.

To allow Negotiate to select the [Kerberos](microsoft-kerberos.md) security provider, the client app must provide one of the following:

* A [*service principal name*](../secgloss/s-gly.md) (SPN).
* A user principal name (UPN).
* A NetBIOS account name as the target name.

Otherwise, Negotiate always selects the [NTLM](microsoft-ntlm.md) security provider.

A server that uses the Negotiate package is able to respond to client apps that specifically select either the [Kerberos](microsoft-kerberos.md) or [NTLM](microsoft-ntlm.md) security provider. However, a client app must know that a server supports the Negotiate package to request authentication using Negotiate. A server that doesn't support Negotiate can't always respond to requests from clients that specify Negotiate as the SSP.

## Reasons to Use the Negotiate Package

- Allows the system to use the most secure available protocol.
- Ensures forward compatibility for the app.
- Ensures that the app exhibits behavior that is in accordance with the security policy set by the customer.
