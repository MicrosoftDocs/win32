---
description: The Microsoft RSA/Schannel Cryptographic Provider supports hashing, data signing, and signature verification.
ms.assetid: 34ede85a-579f-400f-a53e-e40711fcaaf3
title: Microsoft RSA/Schannel Cryptographic Provider
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft RSA/Schannel Cryptographic Provider

The Microsoft [*RSA*](../secgloss/r-gly.md)/[*Schannel*](../secgloss/s-gly.md) Cryptographic Provider supports hashing, data signing, and signature verification. The algorithm identifier CALG\_SSL3\_SHAMD5 is used for SSL 3.0 and TLS 1.0 client authentication. This CSP supports key derivation for the SSL2, PCT1, SSL3, and TLS1 protocols. The [*hash*](../secgloss/h-gly.md) consists of a concatenation of a MD5 hash with a SHA hash and signed with a RSA [*private key*](../secgloss/p-gly.md). It can be exported to other countries/regions.



|                   | Value                         |
|-------------------|-------------------------------|
| **Provider type** | PROV\_RSA\_SCHANNEL           |
| **Provider name** | MS\_DEF\_RSA\_SCHANNEL\_PROV  |



 

For more information about RSA/Schannel providers, see [CSP Functions](cryptography-functions.md).

 

 
