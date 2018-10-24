---
Description: The Microsoft RSA/Schannel Cryptographic Provider supports hashing, data signing, and signature verification.
ms.assetid: 34ede85a-579f-400f-a53e-e40711fcaaf3
title: Microsoft RSA/Schannel Cryptographic Provider
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft RSA/Schannel Cryptographic Provider

The Microsoft [*RSA*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx)/[*Schannel*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) Cryptographic Provider supports hashing, data signing, and signature verification. The algorithm identifier CALG\_SSL3\_SHAMD5 is used for SSL 3.0 and TLS 1.0 client authentication. This CSP supports key derivation for the SSL2, PCT1, SSL3, and TLS1 protocols. The [*hash*](https://msdn.microsoft.com/en-us/library/ms721586(v=VS.85).aspx) consists of a concatenation of a MD5 hash with a SHA hash and signed with a RSA [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx). It can be exported to other countries/regions.



|                |                                  |
|----------------|----------------------------------|
| Provider type: | **PROV\_RSA\_SCHANNEL**          |
| Provider name: | **MS\_DEF\_RSA\_SCHANNEL\_PROV** |



 

For more information about RSA/Schannel providers, see [CSP Functions](cryptography-functions.md).

 

 



