---
Description: 'The Microsoft RSA/Schannel Cryptographic Provider supports hashing, data signing, and signature verification.'
ms.assetid: '34ede85a-579f-400f-a53e-e40711fcaaf3'
title: 'Microsoft RSA/Schannel Cryptographic Provider'
---

# Microsoft RSA/Schannel Cryptographic Provider

The Microsoft [*RSA*](security.r_gly#-security-rsa-gly)/[*Schannel*](security.s_gly#-security-schannel-gly) Cryptographic Provider supports hashing, data signing, and signature verification. The algorithm identifier CALG\_SSL3\_SHAMD5 is used for SSL 3.0 and TLS 1.0 client authentication. This CSP supports key derivation for the SSL2, PCT1, SSL3, and TLS1 protocols. The [*hash*](security.h_gly#-security-hash-gly) consists of a concatenation of a MD5 hash with a SHA hash and signed with a RSA [*private key*](security.p_gly#-security-private-key-gly). It can be exported to other countries/regions.



|                |                                  |
|----------------|----------------------------------|
| Provider type: | **PROV\_RSA\_SCHANNEL**          |
| Provider name: | **MS\_DEF\_RSA\_SCHANNEL\_PROV** |



 

For more information about RSA/Schannel providers, see [CSP Functions](cryptography-functions.md#csp-functions).

 

 



