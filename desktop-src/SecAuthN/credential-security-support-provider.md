---
description: The Credential Security Support Provider protocol (CredSSP) is a Security Support Provider that is implemented by using the Security Support Provider Interface (SSPI).
ms.assetid: b3006b89-d9fc-4444-a3c8-ad2698de501c
title: Credential Security Support Provider
ms.topic: article
ms.date: 05/31/2018
---

# Credential Security Support Provider

The Credential Security Support Provider protocol (CredSSP) is a Security Support Provider that is implemented by using the Security Support Provider Interface ([SSPI](sspi.md)). CredSSP lets an application delegate the user's credentials from the client to the target server for remote authentication. CredSSP provides an encrypted [Transport Layer Security Protocol](transport-layer-security-protocol.md) channel. The client is authenticated over the encrypted channel by using the Simple and Protected Negotiate (SPNEGO) protocol with either [Microsoft Kerberos](microsoft-kerberos.md) or [Microsoft NTLM](microsoft-ntlm.md).

> [!Caution]  
> This is not constrained delegation. CredSSP passes the user's full credentials to the server without any constraint.

 

For information about SPNEGO, see [Microsoft Negotiate](microsoft-negotiate.md).

After the client and server are authenticated, the client passes the user's credentials to the server. The credentials are doubly encrypted under the SPNEGO and TLS session keys. CredSSP supports password-based logon as well as smart card logon based on both [*X.509*](/windows/desktop/SecGloss/x-gly) and PKINIT.

> [!IMPORTANT]
> CredSSP does not support Wow64 clients.

 

For more information about CredSSP, see the following topics.



| Topic                                                                         | Description                                                                                       |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [CredSSP Group Policy Settings](credssp-group-policy-settings.md)<br/> | Delegation of credentials by CredSSP can be controlled by using group policy settings.<br/> |



 

 

